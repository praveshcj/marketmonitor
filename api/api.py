import time
from flask import Flask
import requests
import pandas as pd
import http3
import json
# from flask import Flask
from flask_script import Manager, Server
from flask_mongoengine import MongoEngine


client = pymongo.MongoClient("mongodb+srv://root_user:rootuser@3108@cluster0.ud5re.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test


print("Sending Request");
main_list = {}


for i in range (1, 177):
    response = requests.get('https://api.bseindia.com/BseIndiaAPI/api/GetStkCurrMain/w?flag=Equity&ddlVal1=Index&ddlVal2=All&m=0&pgN='+i)
    print(response.json());



# for name in named_list:
#     response = requests.get('https://www.alphavantage.co/query?function=SMA&symbol='+name+'&interval=daily&time_period=9&series_type=close&apikey='+api_key+"outputsize=compact");
#     print("Getting data for "+ name);
#     if(bool(response.json())):
#         try:
#             data= response.json()['Technical Analysis: SMA'];
#             try:
#                 main_list[name] = data['2020-08-14']
#                 print(data['2020-08-14'])
#             except KeyError as e:
#                 print("Date not found")
#         except KeyError as e:
#             print(response.json())
#             print("Company Not Found")
#         # print(data['2020-08-14']);
# print(main_list)
# def generate_url(function, symbol



