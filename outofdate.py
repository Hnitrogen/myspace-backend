# A daily script to free up space 
# python3 manage.py shell < outofdate.py 

# Installation: 

# 1 apt-get install cron 
# 2 crontab -e
# 3 0 10 * * * /path/to/command 每天十点执行脚本

from django.core.mail import EmailMessage
from myspace.models.paste import Paste
import datetime # now 和 数据库里面的createtime都是datetime类，可以直接减hhh
import pytz

now = datetime.datetime.now() 
tz = pytz.timezone('Asia/Shanghai')  
now = tz.localize(now)  #   把now转换成带时区的datetime类型

before = Paste.objects.count() 
items = Paste.objects.all() 
for item in items: 
    delta = now - item.createtime 
    id = item.id 
    if delta.days > 1 : 
        obj = Paste.objects.get(id=id) 
        obj.delete() 
        print("Delete Data: id=%d" %id)
    

after = Paste.objects.count() 

print("Active")
print("--------- Finished ---------" + '\n') 

# print("--------- Finished ---------")
# print("free up : DataBase: {} -> {}" .format(before,after))

# SMTP 反馈
msg = "--------- Finished ---------" + '\n' + "free up : DataBase: " + str(before) + " -> " + str(after) 
# print(msg) 

email = EmailMessage(
    'PasteBin垃圾回收',     # Title
    msg,       # Main
    '1791422575@qq.com',    # poster
    ['2978632316@qq.com'])      # receiver 

email.send()