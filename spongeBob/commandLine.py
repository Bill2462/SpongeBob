import argparse
import os
import sys

#parse command options
def parse():
    #define arguments taken by the program
    parser = argparse.ArgumentParser(description='Calculate porosity based on microscopic images')
    parser.add_argument('dataInput', type=str, help='Path to an image file or directory containing raw images')
    parser.add_argument('--output-file', type=str, help='Path to the file that will contain results')

    args = parser.parse_args()

    #check whether the seldction exists
    if not(os.path.isfile(args.dataInput) or os.path.isdir(args.dataInput)):
        print(args.dataInput + " does not exists!")
        sys.exit(1)

    #check whether the selected dataInput is a file or directory
    isFile = os.path.isfile(args.dataInput)

    output = {
    'dataInputPath': args.dataInput,
    'inputIsFile': isFile,
    'outputFilePath': args.output_file
    }

    return output
