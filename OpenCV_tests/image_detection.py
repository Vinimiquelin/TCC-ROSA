import cv2
import Utils

# Frontal Face Classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Eye Classifier
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Full Body Classifier
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Read the input image
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

Utils.draw_rectangle_with_label(img, faces, "Face")
Utils.draw_rectangle_with_label(img, eyes, "Eye")
Utils.draw_rectangle_with_label(img, bodies, "Body")

# Display the output
cv2.imshow("img", img)
cv2.waitKey()