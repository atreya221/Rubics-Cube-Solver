import cv2
import sys
import numpy as np
from scipy import stats
from datetime import datetime

import scan_face

def cw_rotate(face):
    result = np.zeros_like(face)
    result[0, 0] = face[0, 6]
    result[0, 1] = face[0, 3]
    result[0, 2] = face[0, 0]
    result[0, 3] = face[0, 7]
    result[0, 4] = face[0, 4]
    result[0, 5] = face[0, 1]
    result[0, 6] = face[0, 8]
    result[0, 7] = face[0, 5]
    result[0, 8] = face[0, 2]
    return result


def acw_rotate(face):
	result = np.zeros_like(face)
	result[0, 0] = face[0, 2]
	result[0, 1] = face[0, 5]
	result[0, 2] = face[0, 8]
	result[0, 3] = face[0, 1]
	result[0, 4] = face[0, 4]
	result[0, 5] = face[0, 7]
	result[0, 6] = face[0, 0]
	result[0, 7] = face[0, 3]
	result[0, 8] = face[0, 6]
	return result


def cw_right(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: R Clockwise")
    temp = FF

    FF[0, 2] = DF[0, 2]
    FF[0, 5] = DF[0, 5]
    FF[0, 8] = DF[0, 8]

    DF[0, 2] = BF[0, 6]
    DF[0, 5] = BF[0, 3]
    DF[0, 8] = BF[0, 0]

    BF[0, 0] = UF[0, 8]
    BF[0, 3] = UF[0, 5]
    BF[0, 6] = UF[0, 2]

    UF[0, 2] = temp[0, 2]
    UF[0, 5] = temp[0, 5]
    UF[0, 8] = temp[0, 8]

    RF = cw_rotate(RF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[8]
                    b_center2 = specs[2]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def acw_right(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: R Anticlockwise")
    temp = FF

    FF[0, 8] = UF[0, 8]
    FF[0, 5] = UF[0, 5]
    FF[0, 2] = UF[0, 2]

    UF[0, 8] = BF[0, 0]
    UF[0, 5] = BF[0, 3]
    UF[0, 2] = BF[0, 6]

    BF[0, 6] = DF[0, 2]
    BF[0, 3] = DF[0, 5]
    BF[0, 0] = DF[0, 8]

    DF[0, 8] = temp[0, 8]
    DF[0, 5] = temp[0, 5]
    DF[0, 2] = temp[0, 2]
    
    RF = acw_rotate(RF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[8]
                    b_center2 = specs[2]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p2, p1, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def cw_left(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: L Clockwise")
    temp = FF
    FF[0, 0] = UF[0, 0]
    FF[0, 3] = UF[0, 3]
    FF[0, 6] = UF[0, 6]
    UF[0, 0] = BF[0, 8]
    UF[0, 3] = BF[0, 5]
    UF[0, 6] = BF[0, 2]
    BF[0, 2] = DF[0, 6]
    BF[0, 5] = DF[0, 3]
    BF[0, 8] = DF[0, 0]
    DF[0, 0] = temp[0, 0]
    DF[0, 3] = temp[0, 3]
    DF[0, 6] = temp[0, 6]
    LF = cw_rotate(LF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[6]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def acw_left(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: L AntiClockwise")
    temp = (FF)

    FF[0, 6] = DF[0, 6]
    FF[0, 3] = DF[0, 3]
    FF[0, 0] = DF[0, 0]
    
    DF[0, 6] = BF[0, 2]
    DF[0, 3] = BF[0, 5]
    DF[0, 0] = BF[0, 8]
    
    BF[0, 8] = UF[0, 0]
    BF[0, 5] = UF[0, 3]
    BF[0, 2] = UF[0, 6]
    
    UF[0, 6] = temp[0, 6]
    UF[0, 3] = temp[0, 3]
    UF[0, 0] = temp[0, 0]
    
    LF = acw_rotate(LF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[6]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p2, p1, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def cw_up(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: U Clockwise")
    temp = FF

    FF[0, 2] = RF[0, 2]
    FF[0, 1] = RF[0, 1]
    FF[0, 0] = RF[0, 0]
    
    RF[0, 2] = BF[0, 2]
    RF[0, 1] = BF[0, 1]
    RF[0, 0] = BF[0, 0]
    
    BF[0, 2] = LF[0, 2]
    BF[0, 1] = LF[0, 1]
    BF[0, 0] = LF[0, 0]
    
    LF[0, 2] = temp[0, 2]
    LF[0, 1] = temp[0, 1]
    LF[0, 0] = temp[0, 0]
    
    UF = cw_rotate(UF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[2]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p2, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def acw_up(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: U AntiClockwise")
    temp = FF
    FF[0, 0] = LF[0, 0]
    FF[0, 1] = LF[0, 1]
    FF[0, 2] = LF[0, 2]
    LF[0, 0] = BF[0, 0]
    LF[0, 1] = BF[0, 1]
    LF[0, 2] = BF[0, 2]
    BF[0, 0] = RF[0, 0]
    BF[0, 1] = RF[0, 1]
    BF[0, 2] = RF[0, 2]
    RF[0, 0] = temp[0, 0]
    RF[0, 1] = temp[0, 1]
    RF[0, 2] = temp[0, 2]
    UF = acw_rotate(UF)
    #FF = temp


    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[6]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def cw_down(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: D Clockwise")
    temp = FF
    FF[0, 6] = LF[0, 6]
    FF[0, 7] = LF[0, 7]
    FF[0, 8] = LF[0, 8]
    LF[0, 6] = BF[0, 6]
    LF[0, 7] = BF[0, 7]
    LF[0, 8] = BF[0, 8]
    BF[0, 6] = RF[0, 6]
    BF[0, 7] = RF[0, 7]
    BF[0, 8] = RF[0, 8]
    RF[0, 6] = temp[0, 6]
    RF[0, 7] = temp[0, 7]
    RF[0, 8] = temp[0, 8]
    DF = cw_rotate(DF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[6]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def acw_down(output,outputWriter,UF,RF,FF,DF,LF,BF):

    print("Next Move: D AntiClockwise")
    temp = FF
    FF[0, 6] = RF[0, 6]
    FF[0, 7] = RF[0, 7]
    FF[0, 8] = RF[0, 8]
    RF[0, 6] = BF[0, 6]
    RF[0, 7] = BF[0, 7]
    RF[0, 8] = BF[0, 8]
    BF[0, 6] = LF[0, 6]
    BF[0, 7] = LF[0, 7]
    BF[0, 8] = LF[0, 8]
    LF[0, 6] = temp[0, 6]
    LF[0, 7] = temp[0, 7]
    LF[0, 8] = temp[0, 8]
    DF = acw_rotate(DF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[0]
                    b_center2 = specs[6]
                    p1 = (b_center1[5]+(b_center1[7]/2), b_center1[6]+(b_center1[8]/2))
                    p2 = (b_center2[5]+(b_center2[7]/2), b_center2[6]+(b_center2[8]/2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (255, 0, 255), 4, tipLength=0.3)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def right_turn(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: Show Right Face")
    temp = FF
    FF = RF
    RF = BF
    BF = LF
    LF = temp
    UF = cw_rotate(UF)
    DF = acw_rotate(DF)
    #FF = temp
    
    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 10:
                faces = np.array(faces)
                # print('INNNNN')
                # face = np.transpose(face)
                face_scanned = stats.mode(face)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[8]
                    b_center2 = specs[6]
                    b_center3 = specs[5]
                    b_center4 = specs[3]
                    b_center5 = specs[2]
                    b_center6 = specs[0]
                    p1 = (b_center1[5] + (b_center1[7] / 2), b_center1[6] + (b_center1[7] / 2))
                    p2 = (b_center2[5] + (b_center2[8] / 2), b_center2[6] + (b_center2[8] / 2))
                    p3 = (b_center3[5] + (b_center3[7] / 2), b_center3[6] + (b_center3[7] / 2))
                    p4 = (b_center4[5] + (b_center4[8] / 2), b_center4[6] + (b_center4[8] / 2))
                    p5 = (b_center5[5] + (b_center5[7] / 2), b_center5[6] + (b_center5[7] / 2))
                    p6 = (b_center6[5] + (b_center6[8] / 2), b_center6[6] + (b_center6[8] / 2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p3, p4, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p5, p6, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p3, p4, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p5, p6, (0, 0, 255), 4, tipLength=0.2)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def left_turn(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: Show Front Face")
    temp = FF
    FF = LF
    LF = BF
    BF = RF
    RF = temp
    UF = acw_rotate(UF)
    DF = cw_rotate(DF)
    #FF = temp
    
    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 10:
                faces = np.array(faces)
                # print('INNNNN')
                # face = np.transpose(face)
                face_scanned = stats.mode(face)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp) == True:
                    b_center1 = specs[6]
                    b_center2 = specs[8]
                    b_center3 = specs[3]
                    b_center4 = specs[5]
                    b_center5 = specs[0]
                    b_center6 = specs[2]
                    p1 = (b_center1[5] + (b_center1[7] / 2), b_center1[6] + (b_center1[7] / 2))
                    p2 = (b_center2[5] + (b_center2[8] / 2), b_center2[6] + (b_center2[8] / 2))
                    p3 = (b_center3[5] + (b_center3[7] / 2), b_center3[6] + (b_center3[7] / 2))
                    p4 = (b_center4[5] + (b_center4[8] / 2), b_center4[6] + (b_center4[8] / 2))
                    p5 = (b_center5[5] + (b_center5[7] / 2), b_center5[6] + (b_center5[7] / 2))
                    p6 = (b_center6[5] + (b_center6[8] / 2), b_center6[6] + (b_center6[8] / 2))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p3, p4, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p5, p6, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p3, p4, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p5, p6, (0, 0, 255), 4, tipLength=0.2)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break
        

def cw_front(output,outputWriter,UF,RF,FF,DF,LF,BF):


    print(FF)
    print("Next Move: F Clockwise")
    temp1 = FF
    temp = UF
    temp2 = cw_rotate(FF)
    #temp2 = FF
    if np.array_equal(temp2, temp1) == True:
        [UF, RF, FF, DF, LF, BF] = right_turn(output, outputWriter, UF, RF, FF, DF, LF, BF)
        [UF, RF, FF, DF, LF, BF] = cw_left(output, outputWriter, UF, RF, FF, DF, LF, BF)
        [UF, RF, FF, DF, LF, BF] = left_turn(output, outputWriter, UF, RF, FF, DF, LF, BF)
        return UF, RF, FF, DF, LF, BF
    UF[0, 8] = LF[0, 2]
    UF[0, 7] = LF[0, 5]
    UF[0, 6] = LF[0, 8]
    LF[0, 2] = DF[0, 0]
    LF[0, 5] = DF[0, 1]
    LF[0, 8] = DF[0, 2]
    DF[0, 2] = RF[0, 0]
    DF[0, 1] = RF[0, 3]
    DF[0, 0] = RF[0, 6]
    RF[0, 0] = temp[0, 6]
    RF[0, 3] = temp[0, 7]
    RF[0, 6] = temp[0, 8]

    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp1) == True:
                    b_center1 = specs[8]
                    b_center2 = specs[6]
                    b_center3 = specs[0]
                    b_center4 = specs[2]
                    p1 = (b_center1[5] + (b_center1[7] / 4), b_center1[6] + (b_center1[7] / 2))
                    p2 = (b_center2[5] + (3 * b_center2[8] / 4), b_center2[6] + (b_center2[8] / 2))
                    p3 = (b_center2[5] + (b_center2[7] / 2), b_center2[6] + (b_center2[7] / 4))
                    p4 = (b_center3[5] + (b_center3[8] / 2), b_center3[6] + (3 * b_center3[8] / 4))
                    p5 = (b_center3[5] + (3 * b_center3[8] / 4), b_center3[6] + (b_center3[8] / 2))
                    p6 = (b_center4[5] + (b_center4[8] / 4), b_center4[6] + (b_center4[8] / 2))
                    p7 = (b_center4[5] + (b_center4[8] / 2), b_center4[6] + (3 * b_center4[8] / 4))
                    p8 = (b_center1[5] + (b_center1[8] / 2), b_center1[6] + (b_center1[8] / 4))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p3, p4, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p5, p6, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p7, p8, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p3, p4, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p5, p6, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p7, p8, (0, 0, 255), 4, tipLength=0.2)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def ccw_front(output,outputWriter,UF,RF,FF,DF,LF,BF):

    print("Next Move: F AntiClockwise")
    temp = UF
    temp1 = FF
    FF = acw_rotate(FF)
    temp2 = FF
    if np.array_equal(temp2,temp1) == True:
        [UF, RF, FF, DF, LF, BF] = right_turn(output, outputWriter, UF, RF, FF, DF, LF, BF)
        [UF, RF, FF, DF, LF, BF] = acw_left(output, outputWriter, UF, RF, FF, DF, LF, BF)
        [UF, RF, FF, DF, LF, BF] = left_turn(output, outputWriter, UF, RF, FF, DF, LF, BF)
        return UF,RF,FF,DF,LF,BF
    UF[0, 6] = RF[0, 0]
    UF[0, 7] = RF[0, 3]
    UF[0, 8] = RF[0, 6]
    RF[0, 0] = DF[0, 2]
    RF[0, 3] = DF[0, 1]
    RF[0, 6] = DF[0, 0]
    DF[0, 0] = LF[0, 2]
    DF[0, 1] = LF[0, 5]
    DF[0, 2] = LF[0, 8]
    LF[0, 8] = temp[0, 6]
    LF[0, 5] = temp[0, 7]
    LF[0, 2] = temp[0, 8]

    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
                elif np.array_equal(face_scanned,temp1) == True:
                    b_center1 = specs[2]
                    b_center2 = specs[0]
                    b_center3 = specs[6]
                    b_center4 = specs[8]
                    p1 = (b_center1[5] + (b_center1[7] / 4), b_center1[6] + (b_center1[7] / 2))
                    p2 = (b_center2[5] + (3 * b_center2[8]/4), b_center2[6] + (b_center2[8] / 2))
                    p3 = (b_center2[5] + (b_center2[7] / 2), b_center2[6] + (3 * b_center2[7] / 4))
                    p4 = (b_center3[5] + (b_center3[8] / 2), b_center3[6] + (b_center3[8] / 4))
                    p5 = (b_center3[5] + (3 * b_center3[8] / 4), b_center3[6] + (b_center3[8] / 2))
                    p6 = (b_center4[5] + (b_center4[8] / 4), b_center4[6] + (b_center4[8] / 2))
                    p7 = (b_center4[5] + (b_center4[8] / 2), b_center4[6] + (b_center4[8] / 4))
                    p8 = (b_center1[5] + (b_center1[8] / 2), b_center1[6] + (3 * b_center1[8] / 4))
                    #cv2.arrowedLine(frame, p1, p2, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p3, p4, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p5, p6, (0, 0, 0), 7, tipLength = 0.2)
                    #cv2.arrowedLine(frame, p7, p8, (0, 0, 0), 7, tipLength = 0.2)
                    cv2.arrowedLine(frame, p1, p2, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p3, p4, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p5, p6, (0, 0, 255), 4, tipLength=0.2)
                    cv2.arrowedLine(frame, p7, p8, (0, 0, 255), 4, tipLength=0.2)
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def cw_back(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: B Clockwise")
    temp = np.copy(UF)
    UF[0, 0] = RF[0, 2]
    UF[0, 1] = RF[0, 5]
    UF[0, 2] = RF[0, 8]
    RF[0, 8] = DF[0, 6]
    RF[0, 5] = DF[0, 7]
    RF[0, 2] = DF[0, 8]
    DF[0, 6] = LF[0, 0]
    DF[0, 7] = LF[0, 3]
    DF[0, 8] = LF[0, 6]
    LF[0, 0] = temp[0, 2]
    LF[0, 3] = temp[0, 1]
    LF[0, 6] = temp[0, 0]
    BF = cw_rotate(BF)
    #FF = temp

    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


def acw_back(output,outputWriter,UF,RF,FF,DF,LF,BF):
    print("Next Move: B CounterClockwise")
    temp = UF
    UF[0, 2] = LF[0, 0]
    UF[0, 1] = LF[0, 3]
    UF[0, 0] = LF[0, 6]
    LF[0, 0] = DF[0, 6]
    LF[0, 3] = DF[0, 7]
    LF[0, 6] = DF[0, 8]
    DF[0, 6] = RF[0, 8]
    DF[0, 7] = RF[0, 5]
    DF[0, 8] = RF[0, 2]
    RF[0, 2] = temp[0, 0]
    RF[0, 5] = temp[0, 1]
    RF[0, 8] = temp[0, 2]
    BF = acw_rotate(BF)
    #FF = temp

    
    print(FF)
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()

        face, specs = scan_face(frame)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                face_scanned = stats.mode(faces)[0]
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #face_scanned = np.asarray(face_scanned)
                faces = []
                if np.array_equal(face_scanned, FF) == True:
                    print("MOVE MADE")
                    return UF,RF,FF,DF,LF,BF
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break


