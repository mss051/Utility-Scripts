"""
    Utility Script to automatically organize every file in your directory
    in neat folders.
    -----------------------------------------------------------
    Made by Massimo Sabba
"""

from os.path import isdir, exists
from os import listdir, mkdir, rename
from shutil import move

files = listdir()
extentions = []
grouped = {}
filtered_files = []

def file_sorter():
    # Filter out folders and this program from the list of files
    for file in files:
        if file.endswith(".py"):
            pass
        elif not isdir(file):
            filtered_files.append(file)
        
    # Get the extentions of the files for creating the folders
    for file in filtered_files:
        extention = file.split(".")[-1]
        if extention not in extentions:
            extentions.append(extention)

    # Organize files based on their extentions
    for extention in extentions:
        grouped[extention] = []
        for file in filtered_files:
            if file.endswith(extention):
                grouped[extention].append(file)

    # Create the folders of the extentions
    for extention in extentions:
        if not isdir(extention):
            mkdir(extention)
    
    # Moves the files into the newly created folders
    for extention in grouped:
        count = 0
        for file in grouped[extention]:
            try:
                move(file, extention)
            except:
                while True:
                    count += 1
                    split_name = file.split(".")
                    split_name.insert(-1, str(count))
                    new_name = "-".join(split_name[0:-1]) + "." + split_name[-1]
                    if not exists(f"{extention}/{new_name}"):
                        break
                    else:
                        continue
                print(f"The file {file} already exists! Renaming it to: {new_name}")
                rename(file, new_name)
                file = new_name
                move(file, extention)

if __name__ == '__main__':
    file_sorter()
