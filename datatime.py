#coding=utf-8
from datetime import datetime

now=datetime.now()
current_year=now.year
current_month= now.month
current_day=now.day
current_hour=now.hour
current_minutes=now.minute
current_second=now.second
current_date="今天是" + str(current_year) + "年" + str(current_month) +"月" +str(current_day) + "日"
current_time="现在时间:"+str(current_hour)+"点"+str(current_minutes)+"分"+str(current_second)+"秒"

print current_date
print current_time

