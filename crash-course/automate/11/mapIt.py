#! python3
# mapIt.py -  Launches a map in the browser using an address from command or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:  # 提供了命令行参数（即不只有文件名）
    address = ' '.join(sys.argv[1:])   #命令行参数通常用空格
else:
    address = pyperclip.paste()

webbrowser.open('https://map.baidu.com/search/' + address)


















