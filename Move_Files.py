import os
import shutil
import sys
import time
import random
import logging
from watchdog.observers import Observer
 from watchdog.events import FileSystemEventHandler
# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/"

list_of_files = os.listdir(from_dir)
print(list_of_files)

# Move All Image files from Downloads Folder to Another Folder
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path1 = from_dir + '/' + file_name                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Document_Files"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name   # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

class FileEventHandler(FileSystemEventHandler):
  def on_created(self, event):
    print(f"oi, {event.src_path} is a thing now, you created it.")

  def on_deleted(self, event):
    print(f"oi, {event.src_path} is gone, you deleted it.")

  def on_moved(self, event):
    print(f"oi, {event.src_path} isnt here anymore, you moved it.")

  def on_modified(self, event):
    print(f"oi, {event.src_path} isnt the same, you modified it.")

event_handler = FileEventHandler()
observer = Observer()
observer.start()
try:
  while true:
    time.sleep(2)
    print("running")
except KeyboardInterupt:print("stop")
observer.stop()