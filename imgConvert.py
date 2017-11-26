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
        else:
            self.file_list = []
            for file in listdir(self.folder):
                if file.endswith(self.ext_old):
                    self.file_list.append(path.join(self.folder, file))
                    print(file)
            if(len(self.file_list) == 0):
                print('Path ' + self.folder + ': No file here')
            else:
                print('Path ' + self.folder + ': ' + str(len(self.file_list)) + " files detected")
        print('-----------------------------------------')

    def imageConvert(self):
        try:
            for file_name in self.file_list:
                ext_len = len(self.ext_old) * -1;
                file_new_name = file_name[:ext_len] + self.ext_new
                print("Converting " + file_name + ' to ' + file_new_name)
                system('convert ' + file_name + ' ' + file_new_name)
                if self.is_del == 1:
                    print('Image deleted: ' + file_name)
                    system('rm ' + file_name)
        except:
            print('Error: no file to convert')
        print('-----------------------------------------')