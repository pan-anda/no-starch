#1 time.time()
import time
print(time.time())
print('')

#2 查看运算时间
"""
cProfile.run()函数，亦可剖析代码运行时间，更详细(参见https://docs.python.org/3/library/profile.html)
"""
def calcProd():
    # caculate the product of the first 100,000 nubmbers.
    product = 1
    for i in range (1, 100000):
        product = product * i
    return product     #结果存入变量product(不return,结果不会被保存)

startTime = time.time()
prod = calcProd()   #执行运算过程
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
print('')

#3 time.sleep()
for i in range(5):   #5遍tick tock
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
time.sleep(3)    #停顿3秒
print('')

#4 round()
now = time.time()
print(round(now, 2))
print(round(now))








