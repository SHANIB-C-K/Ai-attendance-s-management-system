import cv2
import numpy as np
import os
import pickle

video = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_data = []

name = input("Enter your name: ")

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to capture video")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50))
        face_data.append(resized_img)  # Append the resized image to face_data

        cv2.putText(frame, str(len(face_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)

    cv2.imshow("Attendance Management System", frame)

    k = cv2.waitKey(1)
    if len(face_data) == 50: 
        break

video.release()
cv2.destroyAllWindows()

face_data = np.array(face_data)
face_data = face_data.reshape(100, -1) 

if not os.path.exists('data'):
    os.makedirs('data')  # Create data directory if it doesn't exist

if 'name.pkl' not in os.listdir('data/'):
    names = [name] * 100
    with open('data/name.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/name.pkl', 'rb') as f:
        names = pickle.load(f)
    names += [name] * 100  # Append new names

    with open('data/name.pkl', 'wb') as f:
        pickle.dump(names, f)

if 'face_data.pkl' not in os.listdir('data/'):
    with open('data/face_data.pkl', 'wb') as f:
        pickle.dump(face_data, f)
else:
    with open('data/face_data.pkl', 'rb') as f:
        existing_face_data = pickle.load(f)

    faces = np.append(existing_face_data, face_data, axis=0)  # Append new face data

    with open('data/face_data.pkl', 'wb') as f:
        pickle.dump(faces, f)
