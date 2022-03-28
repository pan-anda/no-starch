import requests
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt.utf8')
print(type(res))
print(res.status_code == requests.codes.ok)   #对网页请求是否成功
print(len(res.text))
print(res.text[:250])   #显示前250字元

res.raise_for_status()   #下载是否成功（成功不显示，失败会有traceback & 程序停止)

# 下载失败影响不大
res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1113.txt.utf8')
try:
    res.raise_for_status()  
except Exception as exc:
    print('There was a problem: %s' %(exc))








