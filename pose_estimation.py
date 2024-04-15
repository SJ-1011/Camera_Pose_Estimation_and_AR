import cv2
import numpy as np

# Load camera matrix and distortion coefficients obtained from camera calibration
camera_matrix = np.load('camera_matrix.npy')
dist_coeffs = np.load('dist_coeffs.npy')

# Load video file
video_file = './video.mp4'
cap = cv2.VideoCapture(video_file)

# Define AR object (in this case, a red circle)
ar_object_radius = 25
ar_object_color = (0, 0, 255)  # Red color
ar_object_thickness = 2

# Offset to move the circle to the right (in pixels)
offset1 = 130
offset2 = 90

# Output video settings
output_file = 'output_video.mp4'
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Undistort the frame using camera matrix and distortion coefficients
    undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)
    
    # Draw AR object (red circle) at the center of the frame
    h, w, _ = undistorted_frame.shape
    center_x = w // 2 + offset1  # Adjusted x-coordinate
    center_y = h // 2 + offset2
    cv2.circle(undistorted_frame, (center_x, center_y), ar_object_radius, ar_object_color, ar_object_thickness)
    
    # Write frame to output video
    out.write(undistorted_frame)
    
    # Display the output frame
    cv2.imshow('AR Visualization', undistorted_frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
