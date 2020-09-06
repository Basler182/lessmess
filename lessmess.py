from watchdog.observers import Observer
import time, os, shutil, json
from watchdog.events import FileSystemEventHandler

#Checks if the input is blank  
def is_not_blank(s):
    return bool(s and s.strip())

#Used as default directory
path = r'D:\shared\mess'  
print("Would be kind of smart to not mess up the input, since it could fuck up your system and result in a even bigger mess")
eingabe = input("Where to clean the mess? No input for default path: " + path)
if is_not_blank(eingabe):
    path = eingabe

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
