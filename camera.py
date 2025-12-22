import cv2
import numpy as np
import time
import math
from collections import deque

# ----------------- USER TUNABLES -----------------
CAMERA_INDEX = 0
USE_VIDEO = False
VIDEO_PATH = "video.mp4"

# Optional crop to the beam region: (y1, y2, x1, x2) or None
ROI = None  # e.g., ROI = (200, 360, 80, 560)

# Preprocess
BLUR_KSIZE = 5           # Gaussian blur kernel size (odd)

# "Semi-white" thresholds (tune to your lighting)
# HSV: low saturation (nearly gray/white), high value (bright)
S_MAX = 80               # 0..255 (lower -> stricter "white-ish")
V_MIN = 150              # 0..255 (higher -> brighter)
# LAB: Brightness gate (optional, helps with uneven light)
L_MIN = 160              # 0..255 (lower if too strict)

# Shape constraints
MIN_AREA = 120           # px^2
MAX_AREA = 90000
MIN_CIRCULARITY = 0.65   # 0..1 (1 is perfect circle)

# Motion logic
EMA_ALPHA = 0.4
SPEED_DEADZONE_PX_S = 40.0
MIN_FRAMES_STABLE = 3
# -------------------------------------------------

def semiwhite_mask(bgr):
    """Return a mask for 'semi-white' pixels using HSV (primary) + LAB (optional)."""
    # Smooth to reduce salt-and-pepper
    bgr_blur = cv2.GaussianBlur(bgr, (BLUR_KSIZE, BLUR_KSIZE), 0)

    # HSV gate: S small (desaturated), V large (bright)
    hsv = cv2.cvtColor(bgr_blur, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)
    mask_hsv = cv2.inRange(hsv, (0, 0, V_MIN), (179, S_MAX, 255))

    # LAB gate: L (lightness) high
    lab = cv2.cvtColor(bgr_blur, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)
    mask_lab = cv2.inRange(L, L_MIN, 255)

    # Combine (AND) to be stricter, then clean up
    mask = cv2.bitwise_and(mask_hsv, mask_lab)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    return mask

def circularity(contour):
    area = cv2.contourArea(contour)
    if area <= 0:
        return 0.0, area
    perim = cv2.arcLength(contour, True)
    if perim <= 0:
        return 0.0, area
    return (4.0 * math.pi * area) / (perim * perim), area

def find_ball_by_shape_and_color(bgr):
    """
    1) Build semi-white mask (color).
    2) Find contours, filter by area and circularity (shape).
    3) Return center, contour, circularity if found.
    """
    mask = semiwhite_mask(bgr)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    best = None
    best_score = -1.0

    for c in contours:
        circ, area = circularity(c)
        if area < MIN_AREA or area > MAX_AREA:
            continue
        if circ < MIN_CIRCULARITY:
            continue
        # Prefer more circular; if tie, pick larger area
        score = circ * 1.0 + min(area, MAX_AREA) / (MAX_AREA * 10.0)
        if score > best_score:
            best_score = score
            best = c

    if best is None:
        return None, None, None, mask

    M = cv2.moments(best)
    if M["m00"] == 0:
        return None, None, None, mask

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    circ, _ = circularity(best)
    return (cx, cy), best, circ, mask

def main():
    cap = cv2.VideoCapture(VIDEO_PATH if USE_VIDEO else CAMERA_INDEX)
    if not cap.isOpened():
        print("Could not open camera/video.")
        return

    prev_time = time.time()
    ema_x = None
    label = "STOP"
    recent = deque(maxlen=MIN_FRAMES_STABLE)

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        view = frame
        if ROI is not None:
            y1, y2, x1, x2 = ROI
            view = frame[y1:y2, x1:x2]

        center, contour, circ, mask = find_ball_by_shape_and_color(view)

        # Time delta
        now = time.time()
        dt = max(now - prev_time, 1e-6)
        prev_time = now

        if center is not None:
            cx, cy = center

            # Overlays
            cv2.circle(view, (cx, cy), 10, (0, 255, 0), 2)
            cv2.drawContours(view, [contour], -1, (0, 255, 255), 2)

            (enc_c, enc_r) = cv2.minEnclosingCircle(contour)
            cv2.circle(view, (int(enc_c[0]), int(enc_c[1])), int(enc_r), (255, 0, 0), 2)

            if ema_x is None:
                ema_x = float(cx)
                speed_x = 0.0
            else:
                prev_ema = ema_x
                ema_x = EMA_ALPHA * cx + (1 - EMA_ALPHA) * ema_x
                speed_x = (ema_x - prev_ema) / dt  # px/s

            if abs(speed_x) < SPEED_DEADZONE_PX_S:
                cand = "STOP"
            else:
                cand = "RIGHT" if speed_x > 0 else "LEFT"

            recent.append(cand)
            if len(recent) == recent.maxlen and len(set(recent)) == 1:
                label = recent[-1]

            cv2.putText(
                view, f"x={cx}  vx={speed_x:6.1f} px/s  circ={circ:.2f}",
                (10, 26), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (220, 220, 220), 2, cv2.LINE_AA
            )
        else:
            recent.append("STOP")
            if len(recent) == recent.maxlen and len(set(recent)) == 1:
                label = "STOP"

        cv2.putText(
            view, label, (10, 66),
            cv2.FONT_HERSHEY_SIMPLEX, 1.8,
            (0, 0, 255) if label == "STOP" else (0, 255, 0), 5, cv2.LINE_AA
        )

        # Compose output
        if ROI is not None:
            out = frame.copy()
            y1, y2, x1, x2 = ROI
            out[y1:y2, x1:x2] = view
        else:
            out = view

        cv2.imshow("Ball by Shape + Semi-White Color (LEFT/RIGHT/STOP)", out)
        # Optional: show mask in a small window for tuning
        cv2.imshow("Semi-white mask (tune S_MAX, V_MIN, L_MIN)", mask)

        key = cv2.waitKey(1) & 0xFF
        if key in (27, ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
