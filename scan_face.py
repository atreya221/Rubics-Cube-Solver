import cv2
import sys
import numpy as np
from scipy import stats
from datetime import datetime

def scan_face(frame):

    BW_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    patch = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    #BW_image = cv2.morphologyEx(BW_image, cv2.MORPH_OPEN, patch)
    #BW_image = cv2.morphologyEx(BW_image, cv2.MORPH_CLOSE, patch)

    BW_image = cv2.adaptiveThreshold(BW_image,20,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,0)
    #cv2.imwidthrite()
    try:
         image, contours, hierarchy = cv2.findContours(BW_image,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    except:
         contours, hierarchy = cv2.findContours(BW_image,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)


    i = 0
    contour_cnt = 0
    #print(len(contours))
    cnt = 0
    specs_list = []
    for contour in contours:
        Area = cv2.contourArea(contour)
        contour_cnt = contour_cnt + 1

        if Area < 3000 and Area > 1000: 
            perimeter = cv2.arcLength(contour, True)
            epsilon = 0.01 * perimeter
            approx = cv2.approxPolyDP(contour, epsilon, True)
            #hull = cv2.convexhull(contour)
            if (((perimeter / 4) * (perimeter / 4)) - Area) < 150:
                #if cv2.ma
                cnt = cnt + 1
                x, y, width, height = cv2.boundingRect(contour)
                #cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 255), 2)
                #cv2.imshowidth('cutted contour', frame[y:y + height, x:x + width])
                sorting_parameter = (50*y) + (10*x)
                specs = np.array(cv2.mean(frame[y:y+height,x:x+width])).astype(int)
                cv2.drawContours(frame,[contour],0,(255, 255, 0),2)
                cv2.drawContours(frame, [approx], 0, (255, 255, 0), 2)
                specs = np.append(specs, sorting_parameter)
                specs = np.append(specs, x)
                specs = np.append(specs, y)
                specs = np.append(specs, width)
                specs = np.append(specs, height)
                specs_list.append(specs)
    if len(specs_list) > 0:
        specs_list = np.asarray(specs_list)
        specs_list = specs_list[specs_list[:, 4].argsort()]
    face = np.array([0,0,0,0,0,0,0,0,0])
    if len(specs_list) == 9:
        #print(specs_list)
        for i in range(9):
            #print(specs_list[i]) 
            if specs_list[i][0] > 150 and specs_list[i][1] > 120 and specs_list[i][2] > 120: #WHITE
                specs_list[i][3] = 1
                face[i] = 1
            elif specs_list[i][0] < 150 and specs_list[i][1] > 180 and specs_list[i][2] > 120: #YELLOW
                specs_list[i][3] = 2
                face[i] = 2
            elif specs_list[i][0] < 140 and specs_list[i][0] < 100 and specs_list[i][2] > 200: #ORANGE
                specs_list[i][3] = 3
                face[i] = 3
            elif specs_list[i][0] > 120 and specs_list[i][1] < 120 and specs_list[i][2] < 120: #BLUE
                specs_list[i][3] = 4
                face[i] = 4
            elif specs_list[i][0] < 120 and specs_list[i][1] < 200 and specs_list[i][2] > 200: #RED
                specs_list[i][3] = 5
                face[i] = 5
            elif specs_list[i][0] < 120 and specs_list[i][1] > 120 and specs_list[i][2] < 120: #GREEN
                specs_list[i][3] = 6
                face[i] = 6
        #print(face)
        if np.count_nonzero(face) == 9:
            #print(face)
            #print (specs_list)
            return face, specs_list
        else:
            return [0,0], specs_list
    else:
        return [0,0,0], specs_list
        #break
