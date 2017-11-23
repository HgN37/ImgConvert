#! /usr/bin/python3

from os import system
from os import path
from os import listdir
import sys
import getopt

EXT_OLD = 'jpg'
EXT_NEW = '.png'

class imgConverter:

    def __init__(self, folder, old, new, delete):
        self.ext_old = '.' + old
        self.ext_new = '.' + new
        self.folder = folder
        self.is_del = delete

    def checkFolder(self):
        if not path.isdir(self.folder):
            print('Path ' + self.folder + 'not valid')
            return False
        else:
            self.file_list = []
            for file in listdir(self.folder):
                if file.endswith(self.ext_old):
                    self.file_list.append(path.join(self.folder, file))
            if(len(self.file_list) == 0):
                print('Path ' + self.folder + ': No file here')
            else:
                print('Path ' + self.folder + ': ' + str(len(self.file_list)) + " files detected")
            return True

    def imageConvert(self):
        for file_name in self.file_list:
            print("Converting " + file_name)
            ext_len = len(self.ext_old) * -1;
            file_new_name = file_name[:ext_len] + self.ext_new
            system('convert ' + file_name + ' ' + file_new_name)
            if self.is_del is True:
                print('   Image deleted:    ' + file_name)
                system('rm ' + file_name)


def main(argv):
    # Get args
    try:
        opts, args = getopt.getopt(argv, "d:i:o:rh")
    except getopt.GetoptError:
        sys.exit(2)
    # Variable
    remove_old_file = False
    IMG_DIR = './'
    OLD_EXT = ''
    NEW_EXT = ''
    # Parse args
    for opt, arg in opts:
        if opt == '-h':
            print('Convert all images in folder from jpg to png')
            print('Usage: jpg2png.py -d <path to folder> -i <input extension> -o <output extension> [-r]')
            print('Add -r to remove old file')
            sys.exit()
        elif opt == '-d':
            IMG_DIR = arg
        elif opt == '-i':
            OLD_EXT = arg
        elif opt == '-o':
            NEW_EXT = arg
        elif opt == '-r':
            remove_old_file = True
    converter = imgConverter(IMG_DIR, OLD_EXT, NEW_EXT, remove_old_file)
    converter.checkFolder()
    converter.imageConvert()

if __name__ == "__main__":
    main(sys.argv[1:])
