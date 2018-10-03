# October 2018
# Qintu Tao
# Opencv_Image_Processing_Software

# Import Libraries
import cv2
import sys
import numpy as np
#introduction
print("Hello. Welcome to use the image processing software")
print("Please enter the image you want to use[must in the same folder]")

#get user input, and check if the input is a valid (OR available) image
isValid = False
while isValid == False:
    user_input = input()
    if cv2.imread(user_input) == None:
        print("Invalid input. Try again or enter 'Exit' to exit the program'")
    elif user_input = "Exit":
        exit()
    else:
        isValid = True

#showing the original image
img = cv2.imread(user_input)
cv2.imshow("processing window",img)
