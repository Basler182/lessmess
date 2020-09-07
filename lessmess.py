import json
import os
import shutil
import time
from tkinter import *
from tkinter import filedialog

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


#Dialog to choose folder which gets sorted
root = Tk()
root.withdraw()
path = filedialog.askdirectory()

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #Iterates through all files in the path 
        for file_ in os.listdir(path): 
            name, ext = os.path.splitext(file_) 
            # Save extension type
            ext = ext[1:] 
            if ext == '': 
                continue
            print(name)
            # Moves all pictures into same folder
            if ext == 'jpg' or  ext == 'gif' or  ext == 'png' or  ext == 'tif' or  ext == 'bmp': 
                if os.path.exists(path+'/'+'pictures'):
                    shutil.move(path+'/'+file_, path+'/'+'pictures'+'/'+file_)
                    continue
                else:
                    os.makedirs(path+'/'+'pictures') 
                    shutil.move(path+'/'+file_, path+'/'+'pictures'+'/'+file_) 
                    continue
            # If folder already exists it will move the file to the corresponding folder 
            if os.path.exists(path+'/'+ext): 
                shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
            # Otherwise it will create the folder and move as well
            else: 
                os.makedirs(path+'/'+ext) 
                shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 

event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(13)
except KeyboardInterrupt:
        observer.stop()
observer.join
