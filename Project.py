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
print("4.Press \"R\" key to filter red;\n Press \"B\" key to filter blue;\n Press \"P\" key to filter purple;\n Press \"Y\" key to filter yellow;\n")
print("5.Press \"esc\" key to exit the program")

#function areas
#function that shows the resultant image
def showResult(img):
    cv2.imshow("result",img)
    k = cv2.waitKey(0)
    print("Press any key to exit")

#function that stores the resultant image
def storeResult(img):
    cv2.imwrite("result.jpg",img)

#get properties from image
img_gray = cv2.imread(user_input,0)
row,col = img_gray.shape


# tracking user input (in forms of Key_press)
key = cv2.waitKey(0)
    #turn the image to hsv mode
if key == ord("h"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    showResult(hsv)
    storeResult(hsv)

    #basic info of image
elif key == ord("i"):
    cv2.destroyAllWindows()
    row,col,color = img.shape
    print("The size of the is {0} x {1} big".format(row,col))
    showResult(img)


    #rotation of image
elif key == ord("l"):
    cv2.destroyAllWindows()
    M = cv2.getRotationMatrix2D((row/2,col/2),90,1)
    result = cv2.warpAffine(img,M,(row,col))
    showResult(result)
    storeResult(result)


    #filter blue color in the image
elif key == ord("b"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    showResult(mask)
    storeResult(mask)

    #filter red color in the image
elif key == ord("r"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red = np.array([-10,50,50])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    showResult(mask)
    storeResult(mask)

    #filter yellow color in the image
elif key == ord("y"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20,50,50])
    upper_yellow = np.array([40,255,255])
    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    showResult(mask)
    storeResult(mask)

    #filter green color in the image
elif key == ord("g"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])
    mask = cv2.inRange(hsv,lower_green,upper_green)
    showResult(mask)
    storeResult(mask)

    #filter purple color in the image
elif key == ord("p"):
    cv2.destroyAllWindows()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_purple = np.array([140,50,50])
    upper_purple = np.array([160,255,255])
    mask = cv2.inRange(hsv,lower_purple,upper_purple)
    showResult(mask)
    storeResult(mask)

    #thanks for using
print("Thank you for using this software!")
