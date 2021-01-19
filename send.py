s('pip install pymongo')
s('pip install termcolor')
s('pip install dnspython')
import pymongo
from termcolor import colored
from os import system as s
from datetime import datetime


url = 'mongodb+srv://NoOne:Something@cluster0.dhplg.mongodb.net/Cluster0?retryWrites=true&w=majority'

date = datetime.now().strftime('%x')

cluster = pymongo.MongoClient('mongodb+srv://NoOne:Something@cluster0.dhplg.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = cluster['socialmedia'] ['messaging']
all = db.find()
for messages in all:
    try:
        if date != messages['date']:
            print(f"""{messages['date']}""", 'red')
        else:
            print(colored("From: ", "green"), messages['id'])
            print(colored("Message: ", 'green'), messages['message'])
            print('--------------------------------------------')
    except:
        pass

time = datetime.now().strftime('%X')



person = input('Insert nickname: ')
message = input('Insert your message: ')

msg = {"id": person, "message": message, "date": date, "time": time}
db.insert_one(msg)
