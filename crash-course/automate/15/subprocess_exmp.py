import subprocess
subprocess.Popen('/usr/bin/gnome-calendar')

cld = subprocess.Popen('/usr/bin/gnome-calendar')
print(cld.poll() == None)  # True : 程序仍运行

print(cld.wait())    
print(cld.poll())     # wait(), poll() 返回0 ：该进程终止且无误

















