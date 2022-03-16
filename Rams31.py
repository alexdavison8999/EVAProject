# Here we integrated both the capture of images and text recognition programs.
from cgitb import text
import cv2
import os
import numpy as np
import pytesseract
from pytesseract import Output
import psycopg2
from fuzzywuzzy import process, fuzz
from dateutil import parser
import re

# Establishes connection to database.
conn = psycopg2.connect(
    host="localhost",
    database="EVA",
    user="postgres",
    password="alex"
)

cur = conn.cursor()
# cur.execute("select count from pillbottlecount")
pillBottleCount = 0
isCaptureImages = True
# pillBottleCount = cur.fetchone()[0] #Keeps track of no of pill bottles captured.
folderPath = 'C:/EVA/pillbottles'  # folder path to create a folder and save captured images.

for base, dirs, files in os.walk(folderPath):
    for directories in dirs:
        pillBottleCount += 1


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def captureImages():
    isCaptureImages = True
    pillBottleCount = 0
    while isCaptureImages:
        beginOCR = False  # Decides when to start OCR.
        medicineFolderPath = ""  # temp variable that holds path to the medicine.
        mainImagePath = ""  # Path of image with medicine name.
        extractedTexts = []
        img_counter = 0  # count of no of images captured.

        # Code below is to capture images.
        font = cv2.FONT_HERSHEY_SIMPLEX
        displayedText = "Position the bottle in the box and take pictures covering entire label."

        # folder creation for each pill bottle.
        pillBottleCount += 1
        folderName = 'pillbottle' + str(pillBottleCount)
        IMG_DIR = os.path.join(folderPath, folderName)
        medicineFolderPath = IMG_DIR
        cam = cv2.VideoCapture(0)  # opens the camera.

        width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

        while True:
            ret, frame = cam.read()
            cv2.putText(frame, displayedText, (round(width * 0.08), round(height * 0.1)), font, 0.5, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.rectangle(frame, (round(width * 0.3), round(height * 0.2)), (round(width * 0.7), round(height * 0.9)),
                          (255, 255, 255), 2)
            cv2.imshow('test', frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                break
            elif k % 256 == 32:
                img_counter += 1
                imageName = "Image" + str(img_counter) + ".png"
                try:
                    if not os.path.isdir(IMG_DIR):
                        os.mkdir(IMG_DIR)
                    ret1, frame1 = cam.read()
                    cv2.imwrite(os.path.join(IMG_DIR, imageName), frame1)
                    print("{} written".format(imageName))
                except OSError as error:
                    print("Error creating or saving a image to the folder\n", error)
        cam.release()
        cv2.destroyAllWindows()

        beginOCR = True  # Starting character recognition for each image.

        if beginOCR:
            print("Starting Tesseract OCR..!")  # Beginning text extraction using Tesseract OCR.
            medicineNames = ["ROSUVASTATIN", "Tamsulosin HCL 0.4 MG cap sunp", "Cyclobenzaprine 5 MG",
                             "docusate sodium 100 MG capsule", "Ibuprofen Tablet 800 MG", "ATORVASTATIN"]

            # Pill table attributes intialization.
            medicineName = None
            dateFilled = 9 / 9 / 99
            quantity = 99
            refillsLeft = 9
            frontImagePath = None
            # imageFolderPath variable will be initialized when capturing the images itself.

            percentage = 0
            medicineName = ""
            matchedtext = ""  # Matched extracted text.

            print('\n-----------------------------------------')
            print('TESSERACT OUTPUT --> Original Image')
            print('-----------------------------------------')

            extractedTexts = []  # Variable to store extracted texts.
            for image_name in os.listdir(IMG_DIR):  # Iterates over each image of the pill bottle and extracts texts.
                tempTexts = []

                image = cv2.imread(os.path.join(IMG_DIR, image_name))

                # preprocess image
                gray = get_grayscale(image)
                thresh = thresholding(gray)

                # Get OCR output using Pytesseract
                custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-:" " --oem 3'

                print("{} output".format(image_name))

                print(pytesseract.image_to_string(thresh, config=custom_config))

                extractedTexts.extend(pytesseract.image_to_string(thresh, config=custom_config).splitlines())
                extractedTexts.extend(pytesseract.image_to_string(image, config=custom_config).splitlines())

                if len(extractedTexts) > 0:
                    for i in range(0, len(medicineNames)):
                        matches = process.extract(medicineNames[i], extractedTexts, scorer=fuzz.ratio)
                        print("Percentages:\n", matches[0][1])
                        if matches[0][1] > percentage and percentage > 30:
                            percentage = matches[0][1]
                            medicineName = medicineNames[i]
                            matchedtext = matches[0][0]
                            frontImagePath = os.path.join(IMG_DIR, image_name)

            if len(extractedTexts) > 0:
                # Extracting datefilled texts
                dateFilledTexts = ["datefilled", "filled", "date filled", "df", "DF"]
                similarTexts = []
                for i in range(0, len(dateFilledTexts)):
                    matches = process.extract(dateFilledTexts[i], extractedTexts, scorer=fuzz.ratio)
                    if matches[0][1] > 60:
                        print(matches[0][1], matches[0][0])
                        similarTexts.append(matches[0][0])
                print("Similar texts..!\n", similarTexts)
                noDateExtracted = True
                for i in range(0, len(similarTexts)):
                    try:
                        dateFilled = parser.parse(similarTexts[i], fuzzy=True)
                        noDateExtracted = False
                        break
                    except:
                        print("except block")
                        continue
                if noDateExtracted:
                    print("date not extracted..!")
                    dateFilled = "not found..!"  # NULL/None can be used for database

                print("Date filled is {}\n".format(dateFilled))

                # Extracting quantity
                quantityTexts = ["QTY", "qty"]
                percentage = 0
                quantityText = ""
                for i in range(0, len(quantityTexts)):
                    matches = process.extract(quantityTexts[i], extractedTexts, scorer=fuzz.ratio)
                    for i in range(0, len(matches)):
                        if re.search(r'\d', matches[i][0]):
                            if matches[i][1] > percentage:
                                quantityText = matches[i][0]

                if quantityText == "":
                    print("Quantity not extracted..!")
                else:
                    print("Quantity extracted text..!", quantityText)
                    temp = re.findall(r'\d+', quantityText)
                    quantity = temp[0]

            # store the data in DB.
            sql_stmt = """insert into medicine1(medname,datefilled,quantity,refillsleft,imagepath,folderpath) values(%s,%s,%s,%s,%s,%s)"""
            data = (medicineName, dateFilled, quantity, refillsLeft, frontImagePath, medicineFolderPath)
            cur.execute(sql_stmt, data)
            conn.commit()

        img_counter = 0

        conn.commit()

        print("Do you want to capture images of another pill bottle[y/n]?")
        userInput = str(input())
        print(userInput)
        if (userInput == 'n'):
            print("No further capturing..!")
            isCaptureImages = False
            return



captureImages()
conn.commit()
# Commiting the data to the DB and closing the connection.
cur.close()
conn.close()