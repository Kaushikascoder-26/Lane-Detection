import cv2
import numpy as np 


image = cv2.imread('test files\\male_face.png',1)

black = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

print(black.shape)

point1 = (0 , image.shape[0])
middlepoint = (image.shape[1] / 2 , image.shape[0] / 2)
lastpoint = (image.shape[1] , image.shape[0])

r = [
     
     (0 , image.shape[0]) , 
     (image.shape[1] / 2 , image.shape[0] / 2) , 
     (image.shape[1] , image.shape[0])
]

arr = np.array([r] , np.int32)

complete_black = np.zeros_like(black) 

white_portion = cv2.fillPoly(complete_black , arr , 255)
print(white_portion.shape)


g = cv2.bitwise_and(white_portion , black)

cv2.imshow('image' , black)

cv2.imshow('black' , white_portion)

cv2.imshow('bitwiseand' , g)



cv2.waitKey()

cv2.destroyAllWindows()