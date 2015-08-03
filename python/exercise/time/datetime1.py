from datetime import datetime, date, time, timedelta, timezone
import re

"""datetime module exercise
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
"""


def to_timestamp(dt_str, tz_str):
    dt1 = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    m = re.match(r'^UTC([+-]\d+):00$', tz_str) # re来找出时区字符串
    tz_n = int(m.group(1))
    print(tz_n)
    tz_utc_this = timezone(timedelta(hours=tz_n))
    tz_res = dt1.replace(tzinfo=tz_utc_this) # 把时间的时区用传入的时区替换
    return tz_res.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')