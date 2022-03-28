#! /usr/bin/python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'jjiijijijijijjjij',
             'blog': 'hkhkhhkhkhkhkh',
             'twitter': 'kkooppl'}

import sys, pyperclip
# 执行时输入py pw.py未加blog,显示用法信息，即Usage--- 
if len(sys.argv) < 2:   # 命令行参数(即执行时的输入)会存在变量sys.argv中(sys.argv[0]为pw.py / sys.argv[1]为命令行参数)
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('no account named ' + account)


