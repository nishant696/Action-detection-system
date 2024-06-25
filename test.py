import streamlit as st
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

st.title("Webcam Live Feed")
run = st.checkbox('Run')

# Create a placeholder to display the live feed
FRAME_WINDOW = st.image([])

while run:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to get frame from the webcam. Please check your camera settings.")
        break
    # Convert the color space from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Display the resulting frame
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')

# When everything is done, release the capture
cap.release()