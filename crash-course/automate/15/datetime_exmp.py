import datetime, time
dt = datetime.datetime.now()
print(dt)
print('')
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print('')

# fromtimestamp
dt = datetime.datetime.fromtimestamp(10000)   #1970后10000秒
print(dt)
print('')
dt = datetime.datetime.fromtimestamp(time.time())   # 同datetime.datetime.now()
print(dt)
print('')

# 比较
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
print(halloween2015 > newyear2016)    #后面 > 前面
print('')

# timedelta 表一段时间
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds, delta.total_seconds())
print(str(delta))
print('')

# 运算
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)
print('')  

aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(dt - aboutThirtyYears)    #从现在往回数30年
print(dt - (2 * aboutThirtyYears))   #往回数60年
print('')  

# 暂停至特定日期
"""
halloween2024 = datetime.datetime(2024, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2024:
    time.sleep(1)    #每秒检查一次，直到2024，继续执行后面程序
"""
# strftime() 将datetime显示为字符串（ 反向用strptime() )
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
















