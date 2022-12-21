import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
    print('Unable to open the camera')
    exit()

# Read frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame is not read correctly, break the loop
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # If the 'q' key is pressed, break the loop
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()