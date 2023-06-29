import cv2
import time
import autopy
import numpy as np
import tracking_module as tm

width, height = 640, 480
frameR = 100
smoothening = 5

wScr, hScr = autopy.screen.size()
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, -1)
cap.set(4, -1)

obj = tm.HandTracking()

prev_time = 0
left_click_state = False
right_click_state = False
frame_skip = 0
frame_interval = 5  # Process every 5th frame

while True:
    test, img = cap.read()

    if frame_skip % frame_interval == 0:
        img = obj.hand_tracker(img)
        pos_list, bound_box = obj.finger_tracker(img, box=True, show=False)

        if len(pos_list) != 0:
            x1, y1 = pos_list[8][1:]
            x2, y2 = pos_list[12][1:]

            fingers = obj.decision()
            cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)

            if fingers[1] == 1 and fingers[2] == 0:
                x3 = np.interp(x1, (frameR, width - frameR), (0, wScr))
                y3 = np.interp(y1, (frameR, height - frameR), (0, hScr))

                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            if fingers[1] == 1 and fingers[2] == 1:
                # Perform left click when index and middle fingers are raised
                length, img, lineInfo = obj.distance(8, 12,img)
            
        
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()


            if fingers[1] == 1 and fingers[4] == 1:
                # Perform right click when index and pinky fingers are raised
                if not right_click_state:
                    autopy.mouse.toggle(autopy.mouse.Button.RIGHT, True)
                    right_click_state = True
            elif fingers[1] == 1 and fingers[4] == 0 and right_click_state:
                # End right click when pinky finger is lowered while index finger is raised
                autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
                right_click_state = False

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(img, str(int(fps)), (10, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Virtual Mouse", img)
        cv2.waitKey(33)

    frame_skip += 1

    frame_skip = not frame_skip
