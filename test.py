import cv2

# Load video file
video_file = './video.mp4'
cap = cv2.VideoCapture(video_file)

# Define AR object (in this case, a red circle)
ar_object_radius = 50
ar_object_color = (0, 0, 255)  # Red color
ar_object_thickness = 2

# Offset to move the circle to the right (in pixels)
offset = 20

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Draw AR object (red circle) at the adjusted position
    h, w, _ = frame.shape
    center_x = w // 2 + offset  # Adjusted x-coordinate
    center_y = h // 2
    cv2.circle(frame, (center_x, center_y), ar_object_radius, ar_object_color, ar_object_thickness)
    
    # Display the output frame
    cv2.imshow('AR Visualization', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and clos
