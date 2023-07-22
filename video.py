import cv2
import numpy as np 

def final(frames , add):

    im = np.zeros((frames.shape[0] , frames.shape[1] , 3) , np.uint8)

    for i in add:
        for x1 , y1 , x2, y2 in i:
            cv2.line(im , (x1,y1) , (x2,y2) , (0,255,255) , 2)
    
    final_sol = cv2.addWeighted(frames , 0.9 , im , 1 , 0)

    return final_sol


def interested_area(edge , values):
    complete_black = np.zeros_like(edge) 
    white_portion = cv2.fillPoly(complete_black , values , 255)
    g = cv2.bitwise_and(white_portion , edge)
    return g



def edge_indi(frame):
    
    black_white = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)  # reducing time complexity I am coverting BGR frame to Gray 
    edge = cv2.Canny(black_white, 100 , 120)

    area_required = [
     
     (0 , frame.shape[0]) , 
     (frame.shape[1] / 2 , frame.shape[0] * 0.65) , 
     (frame.shape[1] , frame.shape[0])
            ] 

    half = interested_area(edge , np.array([area_required] , np.int32))

    add = cv2.HoughLinesP(half , rho=2 , theta=np.pi / 180 , threshold=50 , lines=np.array([]))

    last = final(frame , add)




    return last




video = cv2.VideoCapture('C:\Data Science\Proj_ByKamalSir\Lane Detection By Kamal Sir\lane_detection_video.mp4',1)

#print(video.read())  # 2 outcomes : 1 outcome is whether information is available or not in the video 
# second outcome : each frame pixel values:

# Accessing each frame in the video using while loop
while video.read():
    res , frame = video.read()
    if res == True:
        result = edge_indi(frame)

        cv2.imshow('frames' , result)

        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()