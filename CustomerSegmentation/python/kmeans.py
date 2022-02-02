import pandas as pd
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from validate import *
import sys

server = '(localdb)\\MSSQLLocalDB'
database = 'CustomerSegmentationDB'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute("SELECT Age,Gender,AnnualIncome,SpendingScore,CustomerID FROM Customer") 
row = cursor.fetchone()
id = []
age = []
gender = []
annualincome = []
spendingscore = []
while row: 
    age.append(row[0])
    gender.append(row[1])
    annualincome.append(row[2])
    spendingscore.append(row[3])
    id.append(row[4])
    row = cursor.fetchone()

df = pd.DataFrame(list(zip(age,gender,annualincome,spendingscore)),index = id, columns=['Age','Gender','AnnualIncome','SpendingScore'])
df['Gender'] = pd.factorize(df['Gender'])[0]

#Scale data
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFrame(df_scaled, columns=['Age','Gender','AnnualIncome','SpendingScore'])

#Assign data to x and y
x = df_scaled.drop('SpendingScore', axis=1)
y = df_scaled[['SpendingScore']]

#Split data
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=0)

#Train the algorithm
model = KMeans(n_clusters=4, random_state=0)
y_pred = model.fit_predict(X_train)

#Prints a plot and shows the appropriate amount of clusters based on our data, using the elbow method
#show_cl(X_train)

#Find on which cluster known data belongs, input order: Age, gender, annualincome, spendingscore
#testingpoints(model.fit(df_scaled), scaler, 44, 1 , 73 , 7)

#Print a 3d plot of how well data is distrubuted into the clusters
#show_accuracy(model,X_train)

scaler = MinMaxScaler()
scaler.fit(df.drop('SpendingScore', axis=1).to_numpy())

#Finalized version of the algorithm and ready for predictions
def predict(a,g,i):
    if g.lower() == "male":
        g = 0
    else:
        g = 1

    arr = np.array([[a,g,i]])
    arr = pd.DataFrame(arr, columns=['Age','Gender','AnnualIncome'])
    dscaled = scaler.transform(arr)

    result = model.predict(dscaled)
    if result == 3 or result == 0:
        return "Customer is most likely to have a low spending score"
    if result == 1 or result == 2:
        return "Customer is most likely to have an average or high spending score"

inp = sys.argv[1]
inp = inp.split(",")
result = (predict(inp[0],inp[1],inp[2]))
print(result)