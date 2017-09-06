#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

# 获取当前datetime:
now = datetime.now()
now1 = datetime.now()
print('now =', now)
print('now =', now1)

print('type(now) =', type(now)) # 注意是datetime模块中都datetime类

# 用指定日期时间创建datetime:
dt = datetime(2015, 2, 28, 12, 20)
print('dt =', dt)

# 把datetime转换为timestamp:
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# 从str读取datetime:
cday = datetime.strptime('2015-2-28 18:19:59', '%Y-%m-%d %H:%M:%S')
print('str->time: strptime:', cday)

# 把datetime格式化输出:
print('time->str: strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days (2days 12hours) =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)


# 练习

# 输入日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，编写一个函数将其转换为timestamp：

# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_info = re.findall(r'(\d+):(\d+)', tz_str)
    if tz_str.upper().find('UTC+') >=0:
        cday = cday - timedelta(hours=int(tz_info[0][0]), minutes=int(tz_info[0][1]))
    else:
        cday = cday + timedelta(hours=int(tz_info[0][0]), minutes=int(tz_info[0][1]))
    # 注意cday现在是按系统时区算的, 转化为timestamp需要先replace到utc
    cday = cday.replace(tzinfo=timezone.utc)
    return cday.timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')