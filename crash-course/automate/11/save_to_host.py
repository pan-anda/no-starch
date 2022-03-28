import requests
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt.utf8')
res.raise_for_status()
playFile = open('romeo.txt', 'wb')   #'wb'调用open()以写二进制方式打开新文件
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()







