#! /usr/bin/python3

from tkinter import *
from tkinter import filedialog
from imgConvert import imgConverter
import sys

class IORedirector(object):
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    def write(self,message):
        self.text_area.config(state = "normal")
        self.text_area.insert("insert", message)
        self.text_area.config(state = "disabled")

EXT = ['jpg', 'png', 'bmp']

win = Tk()
win.title('Image Batch Converter')

old_ext = StringVar()
new_ext = StringVar()
dirr = StringVar()
del_old = IntVar()

old_ext.set(EXT[0])
new_ext.set(EXT[0])

Label(win, text='Dir').grid(row=1, column=1, sticky=W)
Label(win, text='From').grid(row=2, column=1, sticky=W)
Label(win, text='To').grid(row=3, column=1, sticky=W)

Entry(win, textvariable=dirr).grid(row=1, column=2, sticky=W)

def folderSearch():
    folder = filedialog.askdirectory(initialdir='~/')
    dirr.set(folder)

Button(win, text='Browse', command=folderSearch).grid(row=1, column=3, sticky=W)

OptionMenu(win, old_ext, *EXT).grid(row=2, column=2, sticky=(W, E))
OptionMenu(win, new_ext, *EXT).grid(row=3, column=2, sticky=(W, E))

def startConvert():
    print('SCANNING...')
    converter = imgConverter(dirr.get(), old_ext.get(), new_ext.get(), del_old.get())
    converter.checkFolder()
    print('CONVERTING...')
    converter.imageConvert()
    

def startScan():
    print('SCANNING...')
    converter = imgConverter(dirr.get(), old_ext.get(), new_ext.get(), del_old.get())
    converter.checkFolder()

Button(win, text='SCAN', command=startScan).grid(row=4, column=1, columnspan=3, sticky=(W, E))
Button(win, text='CONVERT', command=startConvert).grid(row=5, column=1, columnspan=3, sticky=(W, E))
Checkbutton(win, text='Delete old file?', variable=del_old).grid(row=2, column=3, sticky=W)

inform_box = Text(win, wrap='word', height = 11, width=60)
inform_box.grid(row=6, column=1, columnspan=3, sticky=(W, E, S, N))
sys.stdout = StdoutRedirector(inform_box)

for child in win.winfo_children():
    child.grid_configure(padx=10, pady=10)

win.mainloop()