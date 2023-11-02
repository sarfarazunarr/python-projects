import cv2

video_cap = cv2.VideoCapture(0)
face_cap = cv2.CascadeClassifier('C:/Users/hp/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
while True : 
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col, 
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags= cv2.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x,y), (x+w, y+h), (0,255,0),2)
    cv2.imshow('video_live', video_data)
    if cv2.waitKey(10) == ord('x'):
        break 
video_cap.release()

# I am also working on it and will add more things soon....
# If Camera once started you can stop it by clicking on 'x' on keyboard.
