from .processor import imageProcessor
from . import commandLine
from .dataExporter import exportAsCSV
import glob
import sys

#get list of files in the specified directory
#extensions - list of all extensions
#directory - searched directory
#returns: file list
def getFileList(extensions, directory):
    files = []
    for extension in extensions:
        files.extend(glob.glob(directory + "/*." + extension))

    return files

userInput = commandLine.parse()

processor = imageProcessor()

#if user entered directory instead of data then use glob to find all images in the directory
if userInput['inputIsFile'] == False:
    images = getFileList(["jpg", "png", "gif", "bmp"], userInput['dataInputPath'])
    print(str(len(images)) + " images detected in '" + userInput['dataInputPath'] + "'")

    #if they are no images availale in the directory then exit
    if len(images) == 0:
        print("No images in the directory!")
        sys.exit(0)

    #process all images in the direcotry
    for imageFile in images:
        print("Loading file " + imageFile + " ...")
        processor.loadImage(imageFile)

else:#just load single image
    print("Loading file " + userInput['dataInputPath'] + " ...")
    processor.loadImage(userInput['dataInputPath'])


#process all images
results, processImages = processor.process()

#export results to csv
if not(userInput['outputFilePath'] is None):
    exportAsCSV(results, userInput['outputFilePath'])
