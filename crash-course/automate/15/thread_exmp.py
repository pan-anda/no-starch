import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)    #暂停5秒
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)   #新线程中调用takeANap()函数
threadObj.start()   #新线程中执行目标函数

print('End of program.')
print('')  

# 向目标函数传递参数
print('Cats', 'Dogs', 'Frogs', sep=' & ')

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})
threadObj.start()   







