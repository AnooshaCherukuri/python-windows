import os
import sys

#This will give directories list subdirectories list and then files list 
for dirName, subdirList, fileList in os.walk(file_path_on_server):
  print dirName
  print subdirList
  print fileList
  
  #If you want to get all the the files in the path
    for fname in fileList:
      print fname
