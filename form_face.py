import cv2
import sys
import numpy as np
from scipy import stats
from datetime import datetime
import scan_face

def form_face(output,outputWriter,UF,RF,FF,DF,LF,BF,caption = ""):
    faces = []
    while True:
        ok, frame = output.read()

        if not ok:
            print("Cannot read output source")
            sys.exit()


        face, specs = scan_face.scan_face(frame)
        frame = cv2.putText(frame, caption, (40, 40), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 4)
        # print(len(face))
        if len(face) == 9:
            faces.append(face)
            if len(faces) == 5:
                faces = np.array(faces)
                # print('INNNNN')
                # faces = np.transpose(faces)
                scanned_face = stats.mode(faces)[0]
                # print(final_face)
                #UF = np.asarray(UF)
                #FF = np.asarray(FF)
                #scanned_face = np.asarray(scanned_face)
                #print(np.array_equal(scanned_face, tf))
                #print(np.array_equal(scanned_face, FF))
                faces = []
                if not np.array_equal(scanned_face, UF) and not np.array_equal(scanned_face, FF) and not np.array_equal(scanned_face, BF) and not np.array_equal(scanned_face, DF) and not np.array_equal(scanned_face, LF) and not np.array_equal(scanned_face, RF):
                    return scanned_face
        outputWriter.write(frame)
        cv2.imshow("Video Output", frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == 27 or key_pressed == ord('q'):
            break
