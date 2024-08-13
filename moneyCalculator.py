
#++++++++ money calculator according to the widths of the images of them ++++++++#

import cv2 as cv

image = cv.imread("materials\\money.png", cv.IMREAD_COLOR)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255,1)

#finds contours
contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of Contours found = " + str(len(contours)))

#draws contour
cv.drawContours(image, contours,-1, (0,255,0), 3)
totalMoney = 0

for  i in range(len(contours)):
   width=cv.boundingRect(contours[i])[2];
   if(width ==87):
       totalMoney= 0.5+totalMoney
   if(width == 130):
       totalMoney= 1+totalMoney
print("total money is: ",totalMoney)

cv.imshow("image", image)
cv.waitKey(0)