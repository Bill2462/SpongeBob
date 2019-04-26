import cv2
import sys

this = sys.modules[__name__] 

#images buffer
this.rawImages = []

#load image to the memory
def loadImage(filename):
    image = {
        'image': cv2.imread(filename),
        'filename': filename
        }
    this.rawImages.append(image)

#empty data processor buffers
def empty():
    this.rawImages = []

#calculate avarage brightness of the image
def calcAvgBrightness(image):
    avarageBrightness = 0
    for col in range(0, image.shape[0]):
        for row in range(0, image.shape[1]):
            avarageBrightness += image[col,row]

    return int(avarageBrightness/(image.shape[0]*image.shape[1]))

#count brigth and black pixels
def countPixels(image):
    darkPixels = 0
    brigthPixels = 0
    for col in range(0, image.shape[0]):
        for row in range(0, image.shape[1]):
            if image[col,row] == 255:
                brigthPixels += 1
            else:
                darkPixels += 1
    return darkPixels, brigthPixels, image.shape[0]*image.shape[1]

#process single image
#returns: preprocessed image
def processImage(image):
    image = image['image']
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#convert to greyscale
    image = cv2.threshold(image, calcAvgBrightness(image), 255, cv2.THRESH_BINARY)
    return image[1]

#process data
#returns the array of results
def processData():
    results = []
    for image in rawImages:
        print("Processing image '" + image['filename'] + "' ...")
        imageData = processImage(image)
        darkPixels, brigthPixels, pixelTotalCount = countPixels(imageData)
        porosity = (darkPixels/pixelTotalCount)*100
        print("Porosity: " + str(porosity) + "%")
        
        result = {
            'filename': image['filename'],
            'porosity': porosity
        }
        results.append(result)
            
    return results
