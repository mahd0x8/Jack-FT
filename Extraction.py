import csv
import cv2 as cv
import mediapipe as mp
from math import sqrt, acos
import os

# This is the code we used to get and create the datasets from images.
# Data set consists of coordinates of different joints according to the type of exercise.
def getAngle(a, b, c):
    ba = [aa - bb for aa, bb in zip(a, b)]
    bc = [cc - bb for cc, bb in zip(c, b)]

    nba = sqrt(sum((x ** 2.0 for x in ba)))
    ba = [x / nba for x in ba]

    nbc = sqrt(sum((x ** 2.0 for x in bc)))
    bc = [x / nbc for x in bc]

    scalar = sum((aa * bb for aa, bb in zip(ba, bc)))

    angle = acos(scalar)
    return angle * (180 / 3.14)

path = 'Yoga_combined - removed some/testCobra'

files = os.listdir(path)



mpDraw = mp.solutions.drawing_utils
myPose = mp.solutions.pose
pose = myPose.Pose()

for f in files:
    image = cv.imread("Yoga_combined - removed some/testCobra/"+f)
    imageRgb = cv.cvtColor(image,cv.COLOR_BGR2RGB)
    results = pose.process(imageRgb)

    cor = list()
    corSetRight = list()
    corSetRightShoulder = list()
    corSetLeftShoulder = list()
    cor1 = list()
    corSetRight1 = list()
    corSetRightShoulder1 = list()
    corSetLeftShoulder1 = list()
    result = list()
    RuntimeData = list()

    if results.pose_landmarks:
        mpDraw.draw_landmarks(image, results.pose_landmarks, myPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = image.shape
            coordinates = [lm.x, lm.y, lm.z]
            if id == 12 or id == 24 or id == 26:
                cor.append(coordinates)

                if len(cor) == 3:
                    result.append(getAngle(cor[0], cor[1], cor[2]))
                    cor = []
            if id == 24 or id == 26 or id == 28:
                corSetRight.append(coordinates)
                if len(corSetRight) == 3:
                    result.append(getAngle(corSetRight[0], corSetRight[1], corSetRight[2]))
                    corSetRight = []
            if id == 26 or id == 28 or id == 32:
                corSetRightShoulder.append(coordinates)
                if len(corSetRightShoulder) == 3:
                    result.append(getAngle(corSetRightShoulder[0], corSetRightShoulder[1], corSetRightShoulder[2]))
                    corSetRightShoulder = []

            if id == 11 or id == 23 or id == 25:
                cor1.append(coordinates)
                if len(cor1) == 3:
                    result.append(getAngle(cor1[0], cor1[1], cor1[2]))
                    cor1 = []
            if id == 23 or id == 25 or id == 27:
                corSetRight1.append(coordinates)
                if len(corSetRight1) == 3:
                    result.append(getAngle(corSetRight1[0], corSetRight1[1], corSetRight1[2]))
                    corSetRight1 = []
            if id == 25 or id == 27 or id == 31:
                corSetRightShoulder1.append(coordinates)
                if len(corSetRightShoulder1) == 3:
                    result.append(getAngle(corSetRightShoulder1[0], corSetRightShoulder1[1], corSetRightShoulder1[2]))
                    corSetRightShoulder1 = []

            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(image, (cx, cy), 5, (255, 0, 0), cv.FILLED)


    print(result)

    cv.waitKey(1)


    with open("data.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(result)
    result = []