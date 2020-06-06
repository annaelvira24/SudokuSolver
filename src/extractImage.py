# Refrence from https://github.com/KleinSamuel/sudoku-solver with some modifictions

import cv2.cv2 as cv2
import imutils
import pytesseract
import sys

# CHANGE THIS TO YOUR TESSERACT LOCATION!
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\acer\AppData\Local\Tesseract-OCR\tesseract.exe'

# Extract image to sudoku matrix
def extractImage(img):
    # read the image img
    image = cv2.imread(img)

    # check if sudoku image is not fullscreen
    tempImage = imutils.resize(image, height=500)
    gray = cv2.cvtColor(tempImage, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # find largest rectangle in image
    highest = 0
    boundingRect = None
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        rectSize = w*h
        if rectSize < 250000 and rectSize > 100000 and rectSize > highest:
            highest = rectSize
            boundingRect = cv2.boundingRect(cnt)

    # if highest rectangle is found crop image
    if not highest == 0:
        x,y,w,h = boundingRect
        image = tempImage[y:y+h, x:x+w]

    # resize image to 500x500
    image = imutils.resize(image, height=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # compute size of single field of 9x9 array of image
    innerRectWidth = int(500/9)

    # initialized empty sudoku matrix
    sudoku = [['#' for i in range(9)] for j in range(9)]

    # iterate detected numbers
    for cnt in contours:

        # get parameters of bounding rectangle of detected part of image
        x,y,w,h = cv2.boundingRect(cnt)

        # compute size of detected part
        rectSize = w*h

        # check if detected part of image is of appropriate size
        if rectSize <= 2000 and rectSize > 400:

            # compute coordinates of center of rectangle
            xMiddle = int(x+(w/2))
            yMiddle = int(y+(h/2))

            # compute coordinates of rectangle
            xCoord = int(xMiddle/innerRectWidth)
            yCoord = int(yMiddle/innerRectWidth)

            # crop image part where a digit is detected
            tempImage = image[y-2:y+h+2, x-2:x+w+2]
            gray = cv2.cvtColor(tempImage, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # use tesseract to detect digits from cropped image parts
            config = ("--oem 2 --psm 10")
            detectedDigit = pytesseract.image_to_string(blurred, lang="eng", config=config)

            # store detected digit into sudoku matrix
            sudoku[yCoord][xCoord] = str(detectedDigit)[0]

    return sudoku


