import cv2

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

#just create new image processor
def imageProcessor():
    return imageProcessor()

class imageProcessor:
    rawImages = []

    def __init__(self):
        pass

    #load image to the memory
    def loadImage(self, filename):
        image = {
            'image': cv2.imread(filename),
            'filename': filename
            }
        self.rawImages.append(image)

    #empty data processor buffers
    def empty():
        self.rawImages = []

    #process data
    #returns the array of results
    def process(self):
        results = []
        for image in self.rawImages:
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

        return results, imageData
