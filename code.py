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

    while True:
        ok, frame = output.read()
        if not ok:
            break
        while True:
            #print("Show Front Face")
            FF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Front Face")
            midfront = FF[0,4]
            print(FF)
            print(midfront)
            #print("Show Up Face")
            #time.sleep(2)
            UF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Top Face")
            begin_time = datetime.now()
            while True:
                if (datetime.now() - begin_time).total_seconds() > 5:
                    break
                else:
                    ok, frame = output.read()
                    if not ok:
                        flag = 1
                        break
                    frame = cv2.putText(frame, "Show Front Face", (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
                    outputWriter.write(frame)
                    cv2.imshow("Video Output", frame)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        flag = 1
                        break
                    
            if flag == 1:
                sys.exit()
                
            midup = UF[0, 4]
            print(UF)
            print(midup)
            #print("Show Down Face")
            #time.sleep(2)
            DF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Down Face")
            begin_time = datetime.now()
            while True:
                if (datetime.now() - begin_time).total_seconds() > 5:
                    break
                else:
                    ok, frame = output.read()
                    if not ok:
                        flag = 1
                        break
                    frame = cv2.putText(frame, "Show Top Face", (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
                    outputWriter.write(frame)
                    cv2.imshow("Video Output", frame)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        flag = 1
                        break
            if flag == 1:
                sys.exit()
            middown = DF[0, 4]
            print(DF)
            print(middown)
            #print("Show Right Face")
            #time.sleep(2)
            RF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Right Face")
            begin_time = datetime.now()
            while True:
                if (datetime.now() - begin_time).total_seconds() > 5:
                    break
                else:
                    ok, frame = output.read()
                    if not ok:
                        flag = 1
                        break
                    frame = cv2.putText(frame,"Show Down Face", (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
                    outputWriter.write(frame)
                    cv2.imshow("Video Output", frame)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        flag = 1
                        break
            if flag == 1:
                sys.exit()
            midright = RF[0, 4]
            print(RF)
            print(midright)
            #print("Show Left Face")
            #time.sleep(2)
            LF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Left Face")
            begin_time = datetime.now()
            while True:
                if (datetime.now() - begin_time).total_seconds() > 5:
                    break
                else:
                    ok, frame = output.read()
                    if not ok:
                        flag = 1
                        break
                    frame = cv2.putText(frame, "Show Right Face", (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
                    outputWriter.write(frame)
                    cv2.imshow("Video Output", frame)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        flag = 1
                        break
            if flag == 1:
                sys.exit()
            midleft = LF[0, 4]
            print(LF)
            print(midleft)
            #print("Show Back Face")
            #time.sleep(2)
            BF = form_face.form_face(output, outputWriter, UF, RF, FF, DF, LF, BF, caption="Show Back Face")
            begin_time = datetime.now()
            while True:
                if (datetime.now() - begin_time).total_seconds() > 5:
                    break
                else:
                    ok, frame = output.read()
                    if not ok:
                        flag = 1
                        break
                    frame = cv2.putText(frame, "Show Left Face", (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
                    outputWriter.write(frame)
                    cv2.imshow("Video Output", frame)
                    key_pressed = cv2.waitKey(1) & 0xFF
                    if key_pressed == 27 or key_pressed == ord('q'):
                        flag = 1
                        break
            if flag == 1:
                sys.exit()
            midback = BF[0, 4]
            print(BF)
            #time.sleep(2)
            print(midback)

            unsolved_cube = concat(UF,RF,FF,DF,LF,BF)

if __name__ == "__main__":
    main()