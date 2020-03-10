import cv2
import Utils

# Classifiers vector
classifiers = ["haarcascade_frontalface_default.xml", "haarcascade_eye.xml"]

# Feature_cascade
feature_cascade =[]

# Labels
labels = ["Face", "Eye"]

for x in range(len(classifiers)):
    feature_cascade.append(Utils.build_classifier(classifiers[x]))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Features
    features = []

    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for x in range(len(classifiers)):
        features.append(Utils.detect_multi_scale(feature_cascade[x], gray))
        Utils.draw_rectangle_with_label(img, features[x], labels[x])

    # Display the output
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()