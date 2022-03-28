import zipfile, os

#1 新建zip
os.chdir('/home/panda/vim-prac/equations')
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('eqt_1.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

#2 解压缩
os.chdir('/home/panda/tmp')
makeZip = zipfile.ZipFile('new.zip')
makeZip.extractall()
makeZip.close()

#3 读取
os.chdir('/home/panda/tmp')
showZip = zipfile.ZipFile('new.zip')
print(showZip.namelist())
eqtInfo = showZip.getinfo('eqt_1.py')
print(eqtInfo.file_size)
print(eqtInfo.compress_size)
message = 'Compressed file is %sx smaller.' % (round(eqtInfo.file_size / eqtInfo.compress_size, 2))
print(message)
showZip.close()

















