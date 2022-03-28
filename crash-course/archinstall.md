# 区域设置
#### 生成
/etc/locale.gen &#8195; 取消注释 en_US...UTF-8 / zh_CN...UTF-8  
#locale-gen &#8195; 生成  
#locale -a &#8195; 列所有启用的区域设置   
#locale &#8195; 列正在使用的locale和相关环变  
#localedef --list-archive &#8195;查看已生成  
#### 系统区域设置
/etc/locale.conf 中写入LANG变量  
e.g. LANG=zh_CN.UTF-8  
# 选择镜像
/etc/pacman.d/mirrorlist 中加一行在开头：  
Server = https://mirrors.nju.edu.cn/archlinux/ （ 南京大学）
# 分区
#### 用gdisk工具
①显示分区： # gdisk -l /dev/sda  
② # gdisk /dev/sda  
&#8195; → 0( 字母 ) &#8195; 建新分区表  
&#8195; → n &#8195;  &#8195;  &#8195;  &#8195; 建新分区  
&#8195; → Enter  
&#8195; → 选择gdisk 类型 （默认 Linux filesystem)  
&#8195; → L &#8195; &#8195; &#8195; 显gdisk内部编码列表  
&#8195; → w &#8195; &#8195; &#8195; 写入
#### 格式化
#mkfs.ext4 /dev/sda1
#### 挂载
#mount /dev/sda1 /mnt  
列出挂载系统： # findmnt  
#### 卸载文件系统
#unmount /dev/sda1  
or &#8195; # unmount /mnt ( 挂载点 )
# enable disk encryption ( optional )
# set hostnam
/etc/hostname 加一行 panpanda  
# set root password
#passwd
# 安装必需软件包
#pacstrap /mnt base linux linux-firmware （虚拟机可不装linux-firmware)
# 安装引导程序( grub )
安装相关软件包:  
#pacman -S grub efibootmgr  
#grub-install --target=i386-pc /dev/sda
#grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=ArchLinux  
使用 grub-mkconfig 生成 grub 配置文件:   
#grub-mkconfig -o /boot/grub/grub.cfg











