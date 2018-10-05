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
    if cv2.imread(user_input) is not None and user_input != "Exit":
        isValid = True
    elif user_input == "Exit":
        exit()
    else:
        print("Invalid input. Try again or enter 'Exit' to exit the program'")
#showing the original image
img = cv2.imread(user_input)
cv2.imshow("processing window",img)

#showing user guide
print("User Mannual\n")
print("=====================================================================================")
print("1.Press \"H\" key to switch the image to hsv mode\n")
print("2.Press \"I\" key to print basic image info \n")
print("3.Press \"L\" key key to rotate 90 degrees to left\n")
print("4.Press \"R\" key to filter red;\n Press \"B\" key to filter blue;\n Press")

# tracking user input (in forms of Key_press)
key = cv2.waitKey(0)
    #turn the image to hsv mode
if key == ord("h"):
    im
    #basic info of image
elif key == ord("i"):
    img_gray = cv2.imread(user_input,0)
    row,col = img_gray.shape
    row,col,color = img.shape
    print("The size of the is {0} x {1} big".format(row,col))


#function that shows the resultant image
def showResult(img):
    cv2.imshow("result",img)
    k = cv2.waitKey(0)
    print("Press esc to exit")
