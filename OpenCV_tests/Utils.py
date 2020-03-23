import cv2

def build_classifier(classifier):
    return cv2.CascadeClassifier(classifier)

def detect_multi_scale(feature_cascade, scale):
    return feature_cascade.detectMultiScale(scale, 1.1, 4)

def draw_rectangle_with_label(img, feature, label):
    for (x, y, w, h) in feature:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText(img, label, (x, y-4), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 2, cv2.LINE_AA)