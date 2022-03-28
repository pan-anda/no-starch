import os
#1
print("\nexample1:")
print(os.path.join('usr', 'bin', 'spam'))

#2
print("\nexample2:")
myfiles = ['accounts.txt', 'details.scv', 'invite.doxc']
for filename in myfiles:
    print(os.path.join('~/ufo', filename))

#3
print("\nexample3:")
print(os.getcwd())
os.chdir('/home/panda/ufo')    #一定要加''
print(os.getcwd())

#4
#os.makedirs('/home/panda/ufo/test')
#os.chdir('/home/panda/ufo/test')
#print(os.getcwd())

#5
print("\nexample5:")
print(os.path.abspath('.'))
print(os.path.isabs('.'))



