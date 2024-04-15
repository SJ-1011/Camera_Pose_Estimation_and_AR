import cv2
import numpy as np

# 새로운 내부 파라미터와 왜곡 계수
camera_matrix = np.array([[3.91517404e+02, 0.00000000e+00, 1.88267484e+03],
                          [0.00000000e+00, 3.91899672e+02, 1.55514330e+03],
                          [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist_coeffs = np.array([[ 3.64094175e-02, -2.29205097e-03, -3.99212931e-02, 3.34740586e-03, 5.31703144e-05]])

# AR 물체 로드
ar_object = cv2.imread('./hello.png')

# Capture video from the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Undistort the frame
    undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)
    
    # Resize AR object to match frame size
    h, w, _ = undistorted_frame.shape
    ar_object_resized = cv2.resize(ar_object, (w, h))
    
    # Overlay the AR object at the center of the frame
    overlay = np.zeros((h, w, 3), dtype=np.uint8)
    x_offset = (w - ar_object_resized.shape[1]) // 2
    y_offset = (h - ar_object_resized.shape[0]) // 2
    overlay[y_offset:y_offset+ar_object_resized.shape[0], x_offset:x_offset+ar_object_resized.shape[1]] = ar_object_resized
    
    # Overlay the AR object onto the frame
    output_frame = cv2.addWeighted(undistorted_frame, 1, overlay, 0.5, 0)
    
    # Display the output frame
    cv2.imshow('AR Visualization', output_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()