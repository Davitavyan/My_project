import pandas as pd
import requests
url='https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
c=pd.read_csv(url)
print(c.head())
print(c.tail())
print("----"*10)
url2='https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv'
f=pd.read_csv(url2)
print(f.describe())
k=f.describe()
bp=k.boxplot("BMI")

