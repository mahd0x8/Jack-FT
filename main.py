import numpy as np
from sklearn.linear_model import LogisticRegression as lg
import csv
import pandas as pd
from matplotlib import pyplot as plt
import cv2 as cv
import mediapipe as mp
import time
from math import sqrt, acos
from tkinter import *
from tkinter import messagebox
import os

def CameraAndPoseDetection(choice):
    '''
    CameraAndPoseDetection:
        Arguements: 
        ______________________________________
            choice (Yoga Model to check)
                choice = 1: for chair.
                choice = 2: for cobra.
                choice = 3: for downdog.
                choice = 4: for goddess.
                choice = 5: for tree.
                choice = 6: for warrior.
        Returns: 
        ______________________________________
        Boolean 1 and 0 for Exercise angles Satisfactory or wrong  
    
    '''
    # Activating Camera and Pose detection
    mpDraw = mp.solutions.drawing_utils
    myPose = mp.solutions.pose
    pose = myPose.Pose() # creating object of pose detection class
    cam = cv.VideoCapture(0) # initializing camera
    pTime = 0



    # Calculating angles from coordinates
    def getAngle(a, b, c):# a = [x,y,z] , b = [x,y,z] , c = [x,y,z]
        ba = [aa - bb for aa, bb in zip(a, b)]
        bc = [cc - bb for cc, bb in zip(c, b)]

        nba = sqrt(sum((x ** 2.0 for x in ba)))
        ba = [x / nba for x in ba]

        nbc = sqrt(sum((x ** 2.0 for x in bc)))
        bc = [x / nbc for x in bc]

        scalar = sum((aa * bb for aa, bb in zip(ba, bc)))

        angle = acos(scalar)
        return angle * (180 / 3.146) # returning angles in degree




    # initializing lists for further use in loop
    cor = list()
    corSetRight = list()
    corSetRightShoulder = list()
    corSetLeftShoulder = list()
    cor1 = list()
    corSetRight1 = list()
    corSetRightShoulder1 = list()
    result = list()
    RuntimeData = list()
    # Pausing program for 5 sec
    time.sleep(5)



    while True:

        success, img = cam.read() # cv function which return image npArray and success in bool telling if is detecting image or not
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB) # converting image in RGB colours
        results = pose.process(imgRGB) # result is the object of pose detection class


        if results.pose_landmarks: # if landmarks available

            mpDraw.draw_landmarks(img, results.pose_landmarks, myPose.POSE_CONNECTIONS) # to draw landmarks on image

            for id, lm in enumerate(results.pose_landmarks.landmark): # id is joint number and lm is coordinate dictionary

                h, w, c = img.shape
                coordinates = [lm.x, lm.y, lm.z] # coordinate list
                # angle calculation according with the exercise choice
                if choice == 0:
  
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
  
                if choice == 1 or choice == 2:
  
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
  
                    if id == 14 or id == 12 or id == 24:
                        corSetLeftShoulder.append(coordinates)
                        if len(corSetLeftShoulder) == 3:
                            result.append(getAngle(corSetLeftShoulder[0], corSetLeftShoulder[1], corSetLeftShoulder[2]))
                            corSetLeftShoulder = []
  
                if choice == 3 or choice == 4 or choice == 5:
  
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
                            result.append(
                                getAngle(corSetRightShoulder[0], corSetRightShoulder[1], corSetRightShoulder[2]))
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
                cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED) # showing dots on image
  
  
        # result has the the list of all desired angles
        RuntimeData.append(result)
        if len(RuntimeData) == 50:# only reads the angle 50 times (2-sec)
            break
  
        result = []
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime# calculating fps

        cv.putText(img, str(int(fps)), (10, 50), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)# showing fps on display
        cv.imshow("image", img) # show image
        cv.waitKey(1)# main loop of cv


    # Data collected and now applying Machine learning
    # logistic regression algorithm
    if choice == 0:
        data = pd.read_csv("Data/Chair.csv")
        x_feature = ["Angle24", "Angle26", "Angle28"]

    elif choice == 1:
        data = pd.read_csv("Data/Cobra.csv")
        x_feature = ["Angle 12","Angle 24", "Angle 26", "Angle 28"]

    elif choice == 2:
        data = pd.read_csv("Data/Downdog.csv")
        x_feature = ["Angle 12","Angle 24", "Angle 26", "Angle 28"]

    elif choice == 3:
        data = pd.read_csv("Data/Godess.csv")
        x_feature = ["Angle 23", "Angle 24", "Angle 25","Angle 26", "Angle 27", "Angle 28"]

    elif choice == 4:
        data = pd.read_csv("Data/Tree.csv")
        x_feature = ["Angle 23", "Angle 24", "Angle 25","Angle 26", "Angle 27", "Angle 28"]

    elif choice == 5:
        data = pd.read_csv("Data/Warrior.csv")
        x_feature = ["Angle 23", "Angle 24", "Angle 25","Angle 26", "Angle 27", "Angle 28"]

    Lg = lg() # Initializing object of logistic regression

    try: # exception handling for not recognizing the person in frame

        x = data[x_feature] # initializing independent variable
        y = data["label"] # initializing dependent variable
        Lg.fit(x, y) # Training our model
        y_pred = Lg.predict(RuntimeData) # getting prediction on collected angles data

        if 0 in y_pred: # predicted data is boolean array .. 0 means not correct angle
            messagebox.showinfo("showinfo", "Angles Not Correct, Please Try again!")
            return 0
        else: # 1 means correct angle
            print("Satisfactory!")
            return 1

    except: # dialog box on error
        messagebox.showinfo("showinfo", "Not being able to recognize you!")
