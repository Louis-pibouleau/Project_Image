import cv2

# Charge the classifier Haar for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#open la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossibleto get to the webcam.")
    exit()

print("press 'q' to quit.")

while True:
    #lire une image de la webcam
    ret, frame = cap.read()
    if not ret:
        print("Error :impossible reading of video.")
        break

    #convert image on gray for detection
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detect faces in the image
    faces =face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    #draw rectangle around theface
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x, y), (x+ w, y + h), (255,0,0), 2)

    #image with detection of the face
    cv2.imshow('Détection de visage', frame)

    #exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# free
cap.release()
cv2.destroyAllWindows()
