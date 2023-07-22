import cv2

image = cv2.imread('test files\\male_face.png',1)

canny = cv2.Canny(image , 100 , 120)

cv2.imshow('image' , image)
cv2.imshow('image1' , canny)

cv2.waitKey()

cv2.destroyAllWindows()