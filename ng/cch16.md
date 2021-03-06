#### 程式 & 程序
- 程式 program ( binary file )   e.g.  /bin/bash 是程式
- 程序 progress 
- 子程序 & 父程序 
> -  最处杂点： 程序间呼叫fork-and-exec (先复制再执行)
- job : 当前 bash 子程序(tty1 无法管理tty2 bash)


#### job control
- tar -zpcf /tmp/etec.tar.gz /etc &  (& ： 丢到背景执行。不怕ctrl-c)
- tar -zpcvf /tmp/etc.tar.gz /etc > /tmp/log.txt 2>&1 &  (输出资料重导向)
    
ctrl-z : 当前job丢背景执行    

jobs     
- -l  列所有
- -r  running
- -s  stop

fg 拿到前景处理    
- fg %jobnumber
- fg - 取用减号job

bg 背景下变running    
- ba %jobnumber

kill
- -1 reload 重读参数设定档
- -2 同ctrl-c
- -9 强删（不正常工作）
- -15 以正常程序终止工作
- e.g. kill -9 %2 (预设PID)

#### 16.2.3 离线管理
- 背景（bash 非系统） → 远端方式离线后，工作不会继续
- 改用at / nohup (nohangup) 放系统背景
> - nohup 放前景执行
> - nohup & 放背景执行   
例：
![这是图片](/home/panda/no-starch/ng/jpg/16-1.jpg "nohup")





#### 程序观察
ps   
- ps -l(自己bash程序)
- ps aux(所有系统程序)

top   
- top -d 2   每2s更新（预设5s）
- top -b -n 2 > ~/abc.txt  (top进行2次，结果传入abc.txt)
- echo $$ (查看自己bash PID) → top -d 2 -p 2602

pstree  程序树 （-p 显示PID）   
- 所有程序在systmd底下，PID为1，因为是核心呼叫第一个程式。






#### 16.3.3 程序执行顺序













#### 系统资源观察
free(查看记忆体使用情况)   
- free -m (单位Mbytes)
- 系统会将记忆体用光（加速存取效能）
- swap最好不被使用（实体记忆体不足才会用swap）

uname -a 查看系统&核心资讯   

uptime 系统启动时间&工件负载   
- load average : 1min 5min 15min 平均负载

netstat 查看网路连线&socket file   
- RefCnt : 连接到此socket 的程序数
- Type(存取类型) : STREAM（确认连线）； DGRAM(不需确认)
- netstat -tulnp 哪些程序启动哪些port
- socket file(程序可接收不同程序发来的资讯，e.g. XWindow 以socket进行视窗介面的连线沟通) 


dmesg 核心开机时资讯   
- dmesg | more
- dmesd | grep -i vda 硬盘相关

vmstat 查看系统资源变化   
- vmstat 1 3   统计CPU状态，1s 1次，共3次
- vmstat -d    磁碟读写状态 

























#### SELinux (Security Enhanced)
- 核心模组
- 防止员工资源误用
> - DAC (自主式存取控制) ：rwx 对 root 无效
> - MAC (委任式        ) ：是否能读档案资源
- 运作模式















#### 16.5.3 三种模式
- enforcing
- permissive 放行，但没通过的会记入log
- disable

![这是图片](/home/panda/no-starch/ng/jpg/16-2.jpg "selinux")
<center><font color=red>(不是所有程序都受限)</font></center>

- #getenforce 查看当前模式
- #sestatus 查看policy
- #ps -eZ | grep -E 'cron | bash'查看cron bash是否受限(<font color=red>type项：unconfined_t为不受限</font>)
![这是图片](/home/panda/no-starch/ng/jpg/16-3.jpg "bash")

- 模式切换
> - enforcing & permissive 互换 disable 改设定档/etc/selinux/config,需重启（整合到核心）
> - enforcing 互换 permissive:   
> 1.#setenforce 0 变permissive    
> 2.#setenforce 1 变enforcing   

#### 16.5.4 规则管理
- 查看规则启动与否（布林值)
> #getsebool -a 列所有
- 查看规则内限制
> - seinfo
> - sesearch
- 改布林值
> #setsebool -P 规则 0/1 (0: off / 1: on)

#### 16.5.5 改安全文本
- chcon 改type
- restorecon type恢复成预设
- semanage 预设 type 查询 & 修改






