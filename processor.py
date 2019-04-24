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
