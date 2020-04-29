import cv2

def face_detection_preset():
    # Loading classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Loading custom classifier to recognize
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    # Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
    video_capture = cv2.VideoCapture(0)

    return faceCascade, clf, video_capture
            
# Method to recognize the person
def recognize(img, clf, classifier, scaleFactor, minNeighbors):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    username = ""
    
    for (x, y, w, h) in features:
        # Predicting the id of the user
        id, _ = clf.predict(gray_img[y:y+h, x:x+w])
        
        if (id == 1):
            username = "Vini"
        elif (id == 2):
            username = "Natty"
        elif (id == 3):
            username = "Bru"
        elif (id == 4):
            username = "Fabio"
        else:
           raise Exception("Não existe um usuário com o ID ", id)

    return username

def video_read(video):
    _, img = video.read()
    return img

def video_release(video):
    # releasing web-cam
    video.release()