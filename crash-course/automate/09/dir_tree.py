import os

for folderName, subfolders, filenames in os.walk('/home/panda/vim-prac'):
    print('the current foleder: ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')   #隔空行



















