import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

cred = credentials.Certificate("accountkey.json")
app = firebase_admin.initialize_app(cred)

root = db.reference(url= "https://pictup-ade2d-default-rtdb.asia-southeast1.firebasedatabase.app")
uref = root.child('test')
udata = uref.get()
udata = dict(udata)
print(udata)
dataframe = pd.read_csv("new.csv")
print(dataframe)
for i in range(len(list(udata.keys()))):
    name = dataframe['name'].iloc[i]
    cluster = dataframe['cluster'].iloc[i]
    udata[name]['cluster'] = int(cluster)
print(udata)
l =[]
for i in udata.keys():
    key = udata[i]['name']
    value = udata[i]
    dicti = {key:value}
    l.append(dicti)
testref = root.child('test')
for i in l:
    testref.update(i)