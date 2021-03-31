import cv2
import sys
import time
import math
import numpy as np
import random as rng
from scipy import stats
import kociemba
from datetime import datetime

import scan_face
import form_face
import rotations

def concat(UF,RF,FF,DF,LF,BF):
    # unsolved_cube = [UF,RF,FF,DF,LF,BF]
    unsolved_cube = np.concatenate((UF, RF), axis=None)
    unsolved_cube = np.concatenate((unsolved_cube, FF), axis=None)
    unsolved_cube = np.concatenate((unsolved_cube, DF), axis=None)
    unsolved_cube = np.concatenate((unsolved_cube, LF), axis=None)
    unsolved_cube = np.concatenate((unsolved_cube, BF), axis=None)
    # print(unsolved_cube)
    return unsolved_cube

def main():
    UF = [0, 0]
    FF = [0, 0]
    LF = [0, 0]
    RF = [0, 0]
    DF = [0, 0]
    BF = [0, 0]
    output = cv2.VideoCapture(0)
    ok, frame = output.read()
    flag = 0
    

    if not ok:
        print("Can't detect output")
        sys.exit()

    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    faces = []
    
    try:
        video_ext = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        file_name = "OUTPUT.avi"
        frames_per_sec = 20.0
        outputWriter = cv2.VideoWriter(file_name, video_ext, frames_per_sec, (frame_width, frame_height))
    except:
        print("Output output can't be created: %s" % file_name)
        sys.exit()