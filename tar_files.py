import os
import tarfile

filename = input("Enter the file name: ")
filepath = input("Enter the files path: ")

os.chdir(filepath)

file_obj = tarfile.open(filename, "w")

for files in os.listdir():
    file_obj.add(files)

file_obj.close()

