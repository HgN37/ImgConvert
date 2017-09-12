from os import system
from os import path
from os import listdir
import sys
import getopt

EXT_OLD = '.jpg'
EXT_NEW = '.png'

def main(argv):
    # Get args
    try:
        opts, args = getopt.getopt(argv, "p:rh")
    except getopt.GetoptError:
        sys.exit(2)
    # Variable
    remove_old_file = False
    IMG_DIR = ''
    # Parse args
    for opt, arg in opts:
        if opt == '-h':
            print('Convert all images in folder from jpg to png')
            print('Usage: jpg2png.py -p <path to folder>')
            print('Add -r to remove old file')
            sys.exit()
        elif opt == '-p':
            IMG_DIR = arg
        elif opt == '-r':
            remove_old_file = True  
    # Check dir valid
    if not path.isdir(IMG_DIR):
        print('Path ' + IMG_DIR + 'not valid')
        sys.exit()
    # Scan all jpg file
    file_list = []
    for file in listdir(IMG_DIR):
        if file.endswith(EXT_OLD):
            file_list.append(path.join(IMG_DIR, file))
    # Check if there's file
    if len(file_list) == 0:
        print('There no image(s)')
        sys.exit()
    # Convert to png
    for file_name in file_list:
        print('+++Image converting: ' + file_name)
        file_new_name = file_name[:-4] + EXT_NEW
        print('   Image converted:  ' + file_new_name)
        system('convert ' + file_name + ' ' + file_new_name)
        if remove_old_file is True:
            print('   Image deleted:    ' + file_name)
            system('rm ' + file_name)
    print('\r\nCONVERT DONE!!!')

if __name__ == "__main__":
    main(sys.argv[1:])
