import cv2
import numpy as np 


image = cv2.imread('test files\\male_face.png',1)

image1 = cv2.imread('test files\\0.jpg',1)



size = cv2.resize(image , (256,256))
s = cv2.resize(image1 , (256,256))

add = cv2.addWeighted(size , 0.7 ,s , 0.3 , 1)


cv2.imshow('black' , size)

cv2.imshow('bitwiseand' , s)

cv2.imshow('add' , add)

cv2.waitKey()

cv2.destroyAllWindows()