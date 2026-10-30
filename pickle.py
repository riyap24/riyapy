import pickle

Riya={'key':'Riya','Age':21,'job':'None'}
Shivam={'key':'Shivam','Age':21,'job':'None'}

db ={}
db['Riya']= Riya
db['Shivam']=Shivam

b=pickle.dumps(db)

myEntry = pickle.loads(b)

print=(myEntry)