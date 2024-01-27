from glob import glob
from time import  sleep
from os import system as sy
from os import getcwd
import cv2


occupied = []
empty = []
now = []
order = []
click = ""
go = True
path_empty = "img\\vaz\\"
path_occupied = "img\\ocu\\"

def get_event(event, x, y, flags, param):
    global occupied
    global empty
    global now
    global click
    global go

    if event == cv2.EVENT_LBUTTONDOWN and go:
        print("L")
        print(now)
        click = "L"
        co = "mv {} {}".format(now[-1],path_empty);sy(co)
        empty.append(path_empty + now[-1])
        order.append(path_empty + now[-1])
        print(order)

    if event == cv2.EVENT_RBUTTONDOWN and go:
        print("R")
        print(now)
        click = "R"
        co = "mv {} {}".format(now[-1],path_occupied);sy(co)
        occupied.append(path_occupied + now[-1])
        order.append(path_occupied + now[-1])
        print(order)
    
    if event == cv2.EVENT_LBUTTONDOWN and not(go): click = "M"

imgs = glob("*.jpg")

cv2.namedWindow("Main")
cv2.setMouseCallback("Main", get_event)

for image in imgs:
    print('fui meno')
    if len(now) < 3:
        now.append(image)
    if len(now) == 3:
        now.pop(0)
        
    click = ""
    am = ''
    while True:
        frame = cv2.imread(image)

        scale = 300 / 100

        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dim = (width,height)

        frame = cv2.resize(frame,dim,interpolation = cv2.INTER_AREA)   

        cv2.imshow('Main',frame) 
        k = cv2.waitKey(1)

        if k == ord('z'):
            print("---------------------")
            co = "mv {} {}".format(order[-1],getcwd())
            sy(co)
            var = None
            if "vaz" in order[-1]:
                var = "ocu"
            if "ocu" in order[-1]:
                var = "vaz"
            name = order[-1][-15:]
            path = 'img\\{}\\{}'.format(var,name)
            co = "mv {} {}".format(name,path)
            sy(co)
            z = cv2.imread(path)
            cv2.imshow("Z",z)
            cv2.waitKey(800)
            cv2.destroyWindow("Z")

        if k == ord('q'):
            exit()

        if click != "" and go:
            break
            

cv2.namedWindow("Main")
cv2.setMouseCallback("Main", get_event)