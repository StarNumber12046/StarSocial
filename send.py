from os import system as s

import platform

print(str(platform.system()).lower())
if str(platform.system()).lower() == "linux":
    s('pip3 install pymongo')
    s('pip3 install termcolor')
    s('pip3 install dnspython')
else:
    s('pip install pymongo')
    s('pip install termcolor')
    s('pip install dnspython')

import pymongo
from termcolor import colored

from datetime import datetime

s('git pull origin main')

url = 'mongodb+srv://NoOne:Something@cluster0.dhplg.mongodb.net/Cluster0?retryWrites=true&w=majority'

date = datetime.now().strftime('%x')

cluster = pymongo.MongoClient(
    'mongodb+srv://NoOne:Something@cluster0.dhplg.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = cluster['socialmedia']['messaging']
all = db.find()

time = datetime.now().strftime('%X')
for messages in all:
    try:
        if date != messages['date']:
            print(f"""{messages['date']}""", 'red')
        else:
            print(colored("From: ", "yellow"), messages['id'])
            print(colored("Message: ", 'blue'), messages['message'])
            print('--------------------------------------------')
    except:
        pass

person = input('Insert nickname: ')
message = input('Insert your message: ')

msg = {"id": person, "message": message, "date": date, "time": time}
db.insert_one(msg)
