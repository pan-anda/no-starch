import requests, bs4

#1 从网页获取
res = requests.get('https://blog.csdn.net/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)   #下载的网页会存入到res.text
print(type(noStarchSoup))

#2 从已有文件获取
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, features="html.parser")   # features="html.parser"后加的，否则报错
print(type(noStarchSoup))

#3 用select()方法找元素
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[1].getText())






























