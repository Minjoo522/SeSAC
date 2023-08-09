import os
import sys
import json
import requests
import cv2

def clova_face(filename):
    client_id = "23rMCvEBKJKQe73NXqcO"
    client_secret = open("secret.txt", "r").read()

    url = "https://openapi.naver.com/v1/vision/face"
    # url = "https://openapi.naver.com/v1/vision/celebrity"

    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    data = json.loads(response.text)
    return data

def my_opencv(filename):
    face_info = clova_face(filename)
    image = cv2.imread(filename)

    # ✨ 좌표값이 없는 경우도 있기 때문에 예외 처리 필요

    # 네모 그리기, 색상은 bgr
    # 얼굴 위치에 박스 그리기
    for face in face_info['faces']:
        roi = face['roi']
        x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']

        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

        gender = face['gender']['value']
        age = face['age']['value']
        emotion = face['emotion']['value']

        left_eye = face['landmark']['leftEye']
        eye_x, eye_y = left_eye['x'], left_eye['y']

        cv2.circle(image, (eye_x, eye_y), 30, (0, 0, 255), 2)

        # 텍스트 찍기
        cv2.putText(image, gender, (x, y+h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(image, f'age: {age}', (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(image, f'emotion: {emotion}', (x, y+h+60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('WindowName', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    filename = 'imgs/장원영.jpg'
    my_opencv(filename)