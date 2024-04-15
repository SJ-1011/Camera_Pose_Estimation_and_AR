import cv2
import numpy as np

# 카메라 보정 (카메라 행렬과 왜곡 계수가 이미 있다고 가정)
# 카메라 보정으로부터 얻은 카메라 행렬과 왜곡 계수를 불러옵니다.
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')

# AR 물체 시각화
# AR 물체의 3D 모델을 불러옵니다.
ar_object = cv2.imread('./hello.png')

# 카메라로부터 비디오 캡처
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