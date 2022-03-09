import cv2
import os
import mediapipe as mp
import imageio
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog
  
# initialize mediapipe pose solution
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

#create a dialog for getting the video location if required using tkinter

root = Tk()
root.withdraw()

#Opened windows will be active. above all windows despite of selection.
root.attributes('-topmost', True)
#returns opened path as str
open_file = filedialog.askopenfilename()

# take video input for pose detection
# you can put here video of your choice
cap = cv2.VideoCapture(open_file)
img_list = []

# take live camera  input for pose detection
# cap = cv2.VideoCapture(0)

# read each frame/image from capture object
i=1
while cap.isOpened():
    ret, img = cap.read()
    print(img)
    if (img) is None:
        break
    # resize image/frame so we can accommodate it on our screen
    img = cv2.resize(img,(500, 500))

    # do Pose detection
    results = pose.process(img)
    # draw the detected pose on original video/ live stream
    mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_draw.DrawingSpec((0, 0, 255), 2, 2),
                        mp_draw.DrawingSpec((0, 250, 0), 2, 2)
                        )
    # Display pose on original video/live stream
    # Extract and draw pose on plain white image
    h, w, c = img.shape   # get shape of original frame
    opImg = np.zeros([h, w, c])  # create blank image with original frame size
    opImg.fill(0)  # set white background. put 0 if you want to make it black
    # draw extracted pose on black white image
    mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_draw.DrawingSpec((0, 0, 255), 2, 2),
                        mp_draw.DrawingSpec((0, 250, 0), 2, 2)
                        )
    

    # display extracted pose on blank images
    cv2.imshow('Holistic', img)
    img_list.append(img)

    # print all landmarks
    print(results.pose_landmarks)
    keypoints = []
    for data_point in results.pose_landmarks.landmark:
        keypoints.append([
                            data_point.x,
                            data_point.y,
                            data_point.z,
                            data_point.visibility
                        ])
    df=pd.DataFrame(keypoints)
    df.to_csv('base'+str(i)+'.csv', index=False, header=False)
    i=i+1

    cv2.waitKey(1)
imageio.mimsave('output1.gif', img_list, fps = 20)