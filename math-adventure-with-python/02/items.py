a = [12,'apple', True, 0.25]
for thing in a:
    print(thing)
    print(thing, end=',')   #放一行以，隔开
print("\n")


name_list = ['abc', 'def', 'ghi', 'jkl']
score_list = [11, 12, 13, 14]
for i in range(4):
    print(name_list[i], score_list[i])
print("\n") 
for i, name in enumerate(name_list):
    print(name, "has index", i)
print("\n") 
# enumerate用法：
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
	print(i, element)
print("\n") 

# 知道内容不知道序号：
c = [1, 2, 3, 'hello']
print(c.index(1))








