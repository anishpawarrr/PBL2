import firebase_admin
from firebase_admin import credentials, db
from pandas import json_normalize
import pandas as pd

cred = credentials.Certificate("accountkey.json")
app = firebase_admin.initialize_app(cred)

root = db.reference(url= "https://pictup-ade2d-default-rtdb.asia-southeast1.firebasedatabase.app")
uref = root.child('test')
udata = uref.get()
l=[]
print(udata)
udata = dict(udata)
for i in udata.keys():
    df = pd.json_normalize(udata[i])
    l.append(df)
df = pd.concat(l,ignore_index=True)
print(df)
# df.to_csv('userdb.csv',index=False,header=True,encoding='utf-8')