#! /usr/bin/python3

import sys
import getopt
from imgConvert import imgConverter

def main(argv):
    # Get args
    try:
        opts, args = getopt.getopt(argv, "d:i:o:rh")
    except getopt.GetoptError:
        sys.exit(2)
    # Variable
    remove_old_file = 0
    IMG_DIR = './'
    OLD_EXT = ''
    NEW_EXT = ''
    # Parse args
    for opt, arg in opts:
        if opt == '-h':
            print('Convert all images in folder')
            print('Usage: imageBatchConverterCLI.py -d <path to folder> -i <input extension> -o <output extension> [-r]')
            sys.exit()
        elif opt == '-d':
            IMG_DIR = arg
        elif opt == '-i':
            OLD_EXT = arg
        elif opt == '-o':
            NEW_EXT = arg
        elif opt == '-r':
            remove_old_file = 1
    converter = imgConverter(IMG_DIR, OLD_EXT, NEW_EXT, remove_old_file)
    converter.checkFolder()
    converter.imageConvert()

if __name__ == "__main__":
    main(sys.argv[1:])