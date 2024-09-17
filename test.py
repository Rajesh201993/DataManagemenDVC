import pandas as pd

Data = [
    {'name':'sunny','age':28,'city':"bhopal"},
    {'name':'Sudhanshu','age':30,'city':"Delhi"},
    {'name':'Krish','age':35,'city':"Bengalore"},
    {'name':'Vikas','age':29,'city':"Pune"}
]

Data=pd.DataFrame(Data)

Data.to_csv('data/data.csv',index =True)