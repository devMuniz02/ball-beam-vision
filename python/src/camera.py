import cv2

def initialize_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    return cap

def capture_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise Exception("Could not read frame")
    return frame

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()