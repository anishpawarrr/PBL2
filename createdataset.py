import numpy
import firebase_admin
from firebase_admin import credentials, db
from pandas import json_normalize
import pandas as pd

cred = credentials.Certificate("accountkey.json")
app = firebase_admin.initialize_app(cred)


root = db.reference(url= "https://pictup-ade2d-default-rtdb.asia-southeast1.firebasedatabase.app")

# for i in range(10):
#     print(numpy.random.randint(2))
l=[]
for i in range(101):
    name = f"{i}!com"
    dictio = {"AIML": numpy.random.randint(2),
              "Competitive programming": numpy.random.randint(2),
              "Webdev": numpy.random.randint(2),
              "Appdev": numpy.random.randint(2),
              "Books": numpy.random.randint(2),
              "Music": numpy.random.randint(2),
              "Gaming": numpy.random.randint(2),
              "Normal humour": numpy.random.randint(2),
              "Gen-z homour": numpy.random.randint(2),
              "cluster": 0,
              "name": name}
    dicti = {name : dictio}
    l.append(dicti)
testref = root.child('test')
for i in l:
    testref.update(i)
print("1")