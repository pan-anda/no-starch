def average(a,b):
    return(a+b)/2
aa=average(10,20)
print(aa)
print("\n") 

running_sum = 0
for i in range(10):
    running_sum +=3
    print(running_sum)
print("\n") 

#写mySum函数(1加到n)
def mySum(num):
    running_sum = 0
    for i in range(1,num+1):
        running_sum += i
    return running_sum
print(mySum(100))
print("\n") 

#写mySum2函数
def mySum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 + 1
    return running_sum
print(mySum2(20))
print("\n") 

#写average3函数
def average3(numList):
    return sum(numList) / len(numList)
print(average3([8, 11, 15]))



















