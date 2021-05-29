#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import argparse

import cv2 as cv
import numpy as np
import mediapipe as mp
import math as math
import os
import csv
from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt

from utils import CvFpsCalc

from tkinter import *
import os
from tkinter import filedialog

#User Interface

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("920x180")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")

    width= login_screen.winfo_screenwidth() 
    height= login_screen.winfo_screenheight()

    # Set window size
    #login_screen.geometry("%dx%d" % (width, height))
    login_screen.geometry('554x270')
    login_screen.configure(bg = '#fbc95c')
    Label(login_screen, text="Please enter details below to login", bg = '#fbc95c').pack()
    Label(login_screen, text="", bg = '#fbc95c').pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ", bg = '#fbc95c').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg = '#fbc95c').pack()
    Label(login_screen, text="Password * ", bg = '#fbc95c').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="", bg = '#fbc95c').pack()
    Button(login_screen, text="Login", width=10, height=1, bg = '#F9D179', command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("200x100")
    login_success_screen.configure(bg = '#fbc95c')
    Label(login_success_screen, text="Login Success", bg = '#fbc95c').pack()
    Button(login_success_screen, text="OK", bg = '#F9D179', command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    main_screen.destroy()
    browse_video_screen()
 
def delete_browse_success():
    browse_video_window.destroy() 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
# Designing Main(first) window 

def logo_screen():
    global logoScreen
    logoScreen = Tk()
    logoScreen.geometry('554x551')
    logoScreen.title("Welcome")
    bg = PhotoImage(file = "logo_METAL.png")
    label1 = Label(logoScreen, image = bg)
    label1.place(x = 0, y = 0)

    logoScreen.after(5000, lambda: logoScreen.destroy())
    logoScreen.mainloop()

def main_account_screen():
    global main_screen
    main_screen = Tk()

    #getting screen width and height of display
    width= main_screen.winfo_screenwidth() 
    height= main_screen.winfo_screenheight()

    # Set window size
    #main_screen.geometry("%dx%d" % (width, height))
    main_screen.geometry('554x270')
    main_screen.configure(bg = '#fbc95c')
    main_screen.title("METAL")
    Label(text="Select Your Choice", bg = '#fbc95c',width="3000", height="2", font=("Calibri", 13)).pack()
    Label(text="", bg = '#fbc95c').pack()
    Button(text="Login", height="2", bg = '#F9D179', width="15", command = login).pack()
    Label(text="", bg = '#fbc95c').pack()
    Button(text="Register", height="2", bg = '#F9D179', width="15", command=register).pack()
 
    main_screen.mainloop()
 
def browse_video_screen():

    # Function for opening the
    # file explorer window
    def browseFiles():
        global filename
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        print("From Browse Screen Filename: " + filename)


    global browse_video_window
    # Create the root window
    browse_video_window = Tk()

    #getting screen width and height of display 
    width = browse_video_window.winfo_screenwidth() 
    height = browse_video_window.winfo_screenheight()
    print(width)

    # Set window size
    browse_video_window.geometry("%dx%d" % (width, height))  

    # Set window title
    browse_video_window.title('File Explorer')

    #Set window background color
    browse_video_window.config(background = "white")
  
    # Create a File Explorer label
    label_file_explorer = Label(browse_video_window,text = "Select Video Files",width = 100, height = 4,fg = "blue").pack()    
    button_explore = Button(browse_video_window,text = "Browse Video",command = browseFiles).pack()
    button_process = Button(browse_video_window,text = "Start Process",command = delete_browse_success).pack()

    # Let the window wait for any events
    browse_video_window.mainloop()

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument('--upper_body_only', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='face mesh min_detection_confidence',
                        type=float,
                        default=0.5)
    parser.add_argument("--min_tracking_confidence",
                        help='face mesh min_tracking_confidence',
                        type=int,
                        default=0.5)

    parser.add_argument('--use_brect', action='store_true')

    args = parser.parse_args()

    return args


def main(filename):
    args = get_args()
    
    print("Filename in main is " + filename)

    cap_device = args.device
    cap_width = args.width
    cap_height = args.height

    upper_body_only = args.upper_body_only
    min_detection_confidence = args.min_detection_confidence
    min_tracking_confidence = args.min_tracking_confidence

    use_brect = args.use_brect

    cap = cv.VideoCapture(filename)   
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)
    length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    print(length)

    mp_holistic = mp.solutions.holistic
    holistic = mp_holistic.Holistic(
        upper_body_only=upper_body_only,
        min_detection_confidence=min_detection_confidence,
        min_tracking_confidence=min_tracking_confidence,
    )

    cvFpsCalc = CvFpsCalc(buffer_len=10)
    d = 0
    real_right_shoulder_hip = 0.57
    velocity_counter = 0
    velocity_15 = 0
    velocity_16 = 0
    velocity_27 = 0
    velocity_28 = 0
    array_counter = 0
    velocity_array_counter = 0
    frame_array = []
    angle_1_array = []
    angle_2_array = []
    angle_3_array = []
    angle_4_array = []
    angle_5_array = []
    angle_6_array = []
    angle_7_array = []
    angle_8_array = []
    velocity_array = []
    velocity_15_array = []
    velocity_16_array = []
    velocity_27_array = []
    velocity_28_array = []
    # to append angles of joint to array
    angle_1_array.append("Right Elbow")
    angle_2_array.append("Left Elbow")
    angle_3_array.append("Right Knee")
    angle_4_array.append("Left Knee")
    angle_5_array.append("Right Hip")
    angle_6_array.append("Left Hip")
    angle_7_array.append("Right Shoulder")
    angle_8_array.append("Left Shoulder")
    velocity_15_array.append("Left Wrist")
    velocity_16_array.append("Right Wrist")
    velocity_27_array.append("Left Ankle")
    velocity_28_array.append("Right Ankle")
    while True:
        velocity_counter+=1
        display_fps = cvFpsCalc.get()

        ret, image = cap.read()
        if not ret:
            break
        image = cv.flip(image, 1)  
        debug_image = copy.deepcopy(image)
        blank_image = np.zeros((cap_height,cap_width,3), np.uint8)

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        image.flags.writeable = False
        results = holistic.process(image)
        image.flags.writeable = True

        # Pose ###############################################################
        pose_landmarks = results.pose_landmarks
        if pose_landmarks is not None:
            brect = calc_bounding_rect(debug_image, pose_landmarks)
            
            debug_image, image_right_shoulder_hip, vel_xparsed_15, vel_yparsed_15, vel_xparsed_16, vel_yparsed_16, vel_xparsed_27, vel_yparsed_27, vel_xparsed_28, vel_yparsed_28, angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, angle_7, angle_8 = draw_pose_landmarks(debug_image, pose_landmarks,
                                              upper_body_only)
            debug_image = draw_bounding_rect(use_brect, debug_image, brect)
            #blank_image = draw_pose_landmarks(blank_image, pose_landmarks,
                                              #upper_body_only)

        # to append angles of joint to array
        angle_1_array.append(angle_1)
        angle_2_array.append(angle_2)
        angle_3_array.append(angle_3)
        angle_4_array.append(angle_4)
        angle_5_array.append(angle_5)
        angle_6_array.append(angle_6)
        angle_7_array.append(angle_7)
        angle_8_array.append(angle_8)

        # to calculate velocity of right wrist (no.16) and left wrist (no.15)
        if velocity_counter == 1:
            # set coordinate of joint no. 15 on 1st frame
            vel_x1_15, vel_y1_15 = vel_xparsed_15, vel_yparsed_15
            # set coordinate of joint no. 16 on 1st frame
            vel_x1_16, vel_y1_16 = vel_xparsed_16, vel_yparsed_16
            # set coordinate of joint no. 27 on 1st frame
            vel_x1_27, vel_y1_27 = vel_xparsed_27, vel_yparsed_27
            # set coordinate of joint no. 28 on 1st frame
            vel_x1_28, vel_y1_28 = vel_xparsed_28, vel_yparsed_28
        if velocity_counter == 60:
            # set coordinate of joint no. 15 on 60th frame
            vel_x60_15, vel_y60_15 = vel_xparsed_15, vel_yparsed_15
            # set coordinate of joint no. 16 on 60th frame
            vel_x60_16, vel_y60_16 = vel_xparsed_16, vel_yparsed_16
            # set coordinate of joint no. 27 on 60th frame
            vel_x60_27, vel_y60_27 = vel_xparsed_27, vel_yparsed_27
            # set coordinate of joint no. 28 on 60th frame
            vel_x60_28, vel_y60_28 = vel_xparsed_28, vel_yparsed_28
            # calculate the ratio between the real length and image length of shoulder to hip
            ratio_shoulder_hip = real_right_shoulder_hip / image_right_shoulder_hip
            # calculate the velocity of joint no. 15
            velocity_15 = math.sqrt(pow(vel_x1_15 - vel_x60_15,2) + pow(vel_y1_15 - vel_y60_15,2)) * ratio_shoulder_hip
            velocity_15_array.append(velocity_15)
            # calculate the velocity of joint no. 16
            velocity_16 = math.sqrt(pow(vel_x1_16 - vel_x60_16,2) + pow(vel_y1_16 - vel_y60_16,2)) * ratio_shoulder_hip
            velocity_16_array.append(velocity_16)
            # calculate the velocity of joint no. 27
            velocity_27 = math.sqrt(pow(vel_x1_27 - vel_x60_27,2) + pow(vel_y1_27 - vel_y60_27,2)) * ratio_shoulder_hip
            velocity_27_array.append(velocity_27)
            # calculate the velocity of joint no. 28
            velocity_28 = math.sqrt(pow(vel_x1_28 - vel_x60_28,2) + pow(vel_y1_28 - vel_y60_28,2)) * ratio_shoulder_hip
            velocity_28_array.append(velocity_28)
            cv.putText(debug_image, "V-[9] Right Wrist:" + "{:.2f}".format(velocity_16) + 'ms-1', (10, 330),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[10] Left Wrist:" + "{:.2f}".format(velocity_15) + 'ms-1', (10, 360),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[11] Right Ankle:" + "{:.2f}".format(velocity_28) + 'ms-1', (10, 390),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[12] Left Ankle:" + "{:.2f}".format(velocity_27) + 'ms-1', (10, 420),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            velocity_counter = 0
        if velocity_counter != 60:
            cv.putText(debug_image, "V-[9] Right Wrist:" + "{:.2f}".format(velocity_16) + 'ms-1', (10, 330),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[10] Left Wrist:" + "{:.2f}".format(velocity_15) + 'ms-1', (10, 360),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[11] Right Ankle:" + "{:.2f}".format(velocity_28) + 'ms-1', (10, 390),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            cv.putText(debug_image, "V-[12] Left Ankle:" + "{:.2f}".format(velocity_27) + 'ms-1', (10, 420),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
            

        #to calculate and display the frame processed
        processed_frame_percent = (d/length) * 100
        cv.putText(debug_image, "Processing Frame:" + "{:.2f}".format(processed_frame_percent) + '%', (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        filename = 'output/save_%06d.png'%d
        cv.imshow('MediaPipe Holistic Demo', debug_image)
        cv.imwrite(filename, debug_image)



        #to display the 2d output on blank canvas
        #cv.imshow('Blank image',blank_image)
        
        d+=1

    # to convert frame images into video format
    Video_Writer()
    for array_counter in range(length+1):
        frame_array.append(array_counter)

    with open('anglebyframe.csv', 'w', newline='') as angle_file:
        writer = csv.writer(angle_file)
        writer.writerow(frame_array)
        writer.writerow(angle_1_array)
        writer.writerow(angle_2_array)
        writer.writerow(angle_3_array)
        writer.writerow(angle_4_array)
        writer.writerow(angle_5_array)
        writer.writerow(angle_6_array)
        writer.writerow(angle_7_array)
        writer.writerow(angle_8_array)

    total_seconds = length // 60

    for velocity_array_counter in range(total_seconds + 1):
        velocity_array.append(velocity_array_counter)

    with open('velocitybyframe.csv', 'w', newline='') as velocity_file:
        writer = csv.writer(velocity_file)
        writer.writerow(velocity_array)
        writer.writerow(velocity_15_array)
        writer.writerow(velocity_16_array)
        writer.writerow(velocity_27_array)
        writer.writerow(velocity_28_array)

    folder = 'output'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    cap.release()
    cv.destroyAllWindows()

def Video_Writer():
    dir_path = 'output'
    ext = 'png'
    output = 'output.mp4'

    images = []
    for f in os.listdir(dir_path):
        if f.endswith(ext):
            images.append(f)

    # Determine the width and height from the first image
    image_path = os.path.join(dir_path, images[0])
    frame = cv.imread(image_path)
    cv.imshow('video',frame)
    height, width, channels = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv.VideoWriter(output, fourcc, 60.0, (width, height))

    for image in images:

        image_path = os.path.join(dir_path, image)
        frame = cv.imread(image_path)

        out.write(frame) # Write out frame to video

        cv.imshow('video',frame)
        if (cv.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
            break

    return print('Video is successfully saved in ' + dir_path + ' folder.')

def calc_bounding_rect(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_array = np.empty((0, 2), int)

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)

        landmark_point = [np.array((landmark_x, landmark_y))]

        landmark_array = np.append(landmark_array, landmark_point, axis=0)

    x, y, w, h = cv.boundingRect(landmark_array)

    return [x, y, x + w, y + h]


def draw_pose_landmarks(image, landmarks, upper_body_only, visibility_th=0.5):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []
    x11 = 0
    x12 = 0
    x13 = 0
    x14 = 0
    x15 = 0
    x16 = 0
    x23 = 0
    x24 = 0
    x25 = 0
    x26 = 0
    x27 = 0
    x28 = 0
    y11 = 0
    y12 = 0
    y13 = 0
    y14 = 0
    y15 = 0
    y16 = 0
    y23 = 0
    y24 = 0
    y25 = 0
    y26 = 0
    y27 = 0
    y28 = 0
    for index, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_z = landmark.z
        landmark_point.append([landmark.visibility, (landmark_x, landmark_y)])
        
        if landmark.visibility < visibility_th:
            continue

        if index == 11:  # left shoulder
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x11, y11 = landmark_x, landmark_y
        if index == 12:  # right shoulder
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x12, y12 = landmark_x, landmark_y
        if index == 13:  # left elbow
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x13, y13 = landmark_x, landmark_y
        if index == 14:  # right elbow
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x14, y14 = landmark_x, landmark_y
        if index == 15:  # left wrist
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x15, y15 = landmark_x, landmark_y
            cv.putText(image,'[10]',(x15,y15),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)
        if index == 16:  # right wrist
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x16, y16 = landmark_x, landmark_y
            cv.putText(image,'[9]',(x16,y16),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)
        if index == 23:  # left hip
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x23, y23 = landmark_x, landmark_y
        if index == 24:  # right hip
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x24, y24 = landmark_x, landmark_y
        if index == 25:  # left knee
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x25, y25 = landmark_x, landmark_y
        if index == 26:  # right knee
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x26, y26 = landmark_x, landmark_y
        if index == 27:  # left ankle
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x27, y27 = landmark_x, landmark_y
            cv.putText(image,'[12]',(x27,y27),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)
        if index == 28:  # right ankle
            cv.circle(image, (landmark_x, landmark_y), 5, (0, 255, 0), 2)
            x28, y28 = landmark_x, landmark_y
            cv.putText(image,'[11]',(x28,y28),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)

    if len(landmark_point) > 0:
        
        if landmark_point[11][0] > visibility_th and landmark_point[12][
                0] > visibility_th:
            cv.line(image, landmark_point[11][1], landmark_point[12][1],
                    (0, 255, 0), 2)

        
        if landmark_point[11][0] > visibility_th and landmark_point[13][
                0] > visibility_th:
            cv.line(image, landmark_point[11][1], landmark_point[13][1],
                    (0, 255, 0), 2)
        if landmark_point[13][0] > visibility_th and landmark_point[15][
                0] > visibility_th:
            cv.line(image, landmark_point[13][1], landmark_point[15][1],
                    (0, 255, 0), 2)

        
        if landmark_point[12][0] > visibility_th and landmark_point[14][
                0] > visibility_th:
            cv.line(image, landmark_point[12][1], landmark_point[14][1],
                    (0, 255, 0), 2)
        if landmark_point[14][0] > visibility_th and landmark_point[16][
                0] > visibility_th:
            cv.line(image, landmark_point[14][1], landmark_point[16][1],
                    (0, 255, 0), 2)

        
        if landmark_point[11][0] > visibility_th and landmark_point[23][
                0] > visibility_th:
            cv.line(image, landmark_point[11][1], landmark_point[23][1],
                    (0, 255, 0), 2)
        if landmark_point[12][0] > visibility_th and landmark_point[24][
                0] > visibility_th:
            cv.line(image, landmark_point[12][1], landmark_point[24][1],
                    (0, 255, 0), 2)
        if landmark_point[23][0] > visibility_th and landmark_point[24][
                0] > visibility_th:
            cv.line(image, landmark_point[23][1], landmark_point[24][1],
                    (0, 255, 0), 2)

        if len(landmark_point) > 25:
            # 右足
            if landmark_point[23][0] > visibility_th and landmark_point[25][
                    0] > visibility_th:
                cv.line(image, landmark_point[23][1], landmark_point[25][1],
                        (0, 255, 0), 2)
            if landmark_point[25][0] > visibility_th and landmark_point[27][
                    0] > visibility_th:
                cv.line(image, landmark_point[25][1], landmark_point[27][1],
                        (0, 255, 0), 2)

            
            if landmark_point[24][0] > visibility_th and landmark_point[26][
                    0] > visibility_th:
                cv.line(image, landmark_point[24][1], landmark_point[26][1],
                        (0, 255, 0), 2)
            if landmark_point[26][0] > visibility_th and landmark_point[28][
                    0] > visibility_th:
                cv.line(image, landmark_point[26][1], landmark_point[28][1],
                        (0, 255, 0), 2)

        # to calculate angle of right elbow no. 14
        if x12 != 0 and x14 != 0 and x16 != 0:
            angle_1 = calculate_Angle(image,'[1] ','Right Elbow: ',0,x14,y14,x12,y12,x16,y16)
        else:
            angle_1 = 0

        # to calculate angle of left elbow no. 13
        if x11 != 0 and x13 != 0 and x15 != 0:
            angle_2 = calculate_Angle(image,'[2] ','Left Elbow: ',30,x13,y13,x11,y11,x15,y15)
        else:
            angle_2 = 0

        # to calculate angle of right knee no. 26
        if x24 != 0 and x26 != 0 and x28 != 0:
            angle_3 = calculate_Angle(image,'[3] ','Right Knee: ',60,x26,y26,x24,y24,x28,y28)
        else:
            angle_3 = 0

        # to calculate angle of left knee no. 25
        if x23 != 0 and x25 != 0 and x27 != 0:
            angle_4 = calculate_Angle(image,'[4] ','Left Knee: ',90,x25,y25,x23,y23,x27,y27)
        else:
            angle_4 = 0

        # to calculate the angle of right hip no. 24
        if x12 != 0 and x24 != 0 and x26 != 0:
            angle_5 = calculate_Angle(image,'[5] ','Right Hip: ',120,x24,y24,x12,y12,x26,y26)
        else:
            angle_5 = 0

        # to calculate the angle of left hip no. 23
        if x11 != 0 and x23 != 0 and x25 != 0:
            angle_6 = calculate_Angle(image,'[6] ','Left Hip: ',150,x23,y23,x11,y11,x25,y25)
        else:
            angle_6 = 0

        # to calculate the angle of right shoulder no. 12
        if x14 != 0 and x12 != 0 and x24 != 0:
            angle_7 = calculate_Angle(image,'[7] ','Right Shoulder: ',180,x12,y12,x14,y14,x24,y24)
        else:
            angle_7 = 0

        # to calculate the angle of left shoulder no. 11
        if x13 != 0 and x11 != 0 and x23 != 0:
            angle_8 = calculate_Angle(image,'[8] ','Left Shoulder: ',210,x11,y11,x13,y13,x23,y23)
        else:
            angle_8 = 0

        # to calculate the distance between the right shoulder and right hip to be used as the pixel distance of the subject's body
        distance_rshoulder_rhip = math.sqrt(pow(x12 - x24,2) + pow(y12 - y24,2)) 
        
    return image, distance_rshoulder_rhip , x15, y15, x16, y16, x27, y27, x28, y28, angle_1, angle_2, angle_3, angle_4, angle_5, angle_6, angle_7, angle_8;


def draw_bounding_rect(use_brect, image, brect):
    if use_brect:
        
        cv.rectangle(image, (brect[0], brect[1]), (brect[2], brect[3]),
                     (0, 255, 0), 2)

    return image

def calculate_Angle(image,joint_number,joint_name,display_height,x1,y1,x2,y2,x3,y3):
#for point (x1,y1), it needs to be the point at which the angle of the joint to be calculated.
#(x2,y2) and (x3,y3) does not matter in terms of order

  distance_hypotenuse = math.sqrt(pow(x2 - x3,2) + pow(y2 - y3,2)) 
  distance_opposite = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
  distance_adjacent = math.sqrt(pow(x1 - x3,2) + pow(y1 - y3,2))

  numer_angle_interest = (pow(distance_hypotenuse,2) - pow(distance_opposite,2) - pow(distance_adjacent,2))
  denom_angle_interest = (-2 * distance_opposite * distance_adjacent)
  if denom_angle_interest == 0:
    denom_angle_interest = 0.00001
  value_interest = numer_angle_interest / denom_angle_interest
  angle_interest = math.acos(value_interest)
  angle_interest = (angle_interest * 180 ) / 3.142 

  cv.putText(image,'A-' + joint_number + joint_name + str(round(angle_interest, 3)),(10,60 + display_height),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)
  cv.putText(image,joint_number,(x1,y1),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,cv.LINE_AA)

  return angle_interest

if __name__ == '__main__':

    filename = ''
    logo_screen()
    main_account_screen()
    print("Filename from after main screen destroyed is: " + filename)
    main(filename)
