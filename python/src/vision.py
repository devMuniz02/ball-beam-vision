import cv2
import numpy as np

def detect_ball(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([20, 100, 100])  # Adjust these values for the ball color
    upper_color = np.array([30, 255, 255])  # Adjust these values for the ball color

    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)
        if radius > 10:  # Minimum radius to consider it a valid detection
            return int(x), int(y), int(radius)
    
    return None, None, None

def draw_ball(frame, x, y, radius):
    cv2.circle(frame, (x, y), radius, (0, 255, 0), 2)
    cv2.putText(frame, "Ball", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)