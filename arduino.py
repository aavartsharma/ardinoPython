import cv2 
import mediapipe as mp
import time
import serial

arduninoData = serial.Serial('com3',115200) #connecting with Serial port COM3 at 115200
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ctime = 0
ptime = 0
cmd = ""
while True:
    success , img = cap.read()
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgrgb)
    if result.multi_hand_landmarks:
        cmd="yes"  # if dectected a hand send yes to Serial port
        cmd += "\r"
        arduninoData.write(cmd.encode())
        for handlms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
    else:
        cmd="off"  # Send off if there is no hand on the frame
        cmd += "\r"
        arduninoData.write(cmd.encode())
    cv2.imshow("Image",img)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,str(int(fps)),(0,0),cv2.FONT_HERSHEY_TRIPLEX,3,(100,0,255),3)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press  button q  to exit
        break

cap.release()
cv2.destroyAllWindows()