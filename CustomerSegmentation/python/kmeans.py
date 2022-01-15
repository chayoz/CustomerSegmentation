import pandas as pd
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix
from validate import *

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

scaler = StandardScaler()

df = pd.DataFrame(list(zip(age,annualincome,spendingscore)),index = id, columns=['Age','AnnualIncome','SpendingScore'])


df_scaled = scaler.fit_transform(df.to_numpy())

splited = np.vsplit(df_scaled,4)
#print(splited[3].size)
#print(splited[3])

X_test = pd.DataFrame(splited[3], columns=['Age','AnnualIncome','SpendingScore'])
df_scaled = pd.DataFrame(df_scaled, columns=['Age','AnnualIncome','SpendingScore'])

#print(df_scaled)

x = df_scaled.drop('SpendingScore', axis=1)
y = df_scaled['SpendingScore']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2)

# Sum_of_squared_distances = []
# K = range(1,10)
# for num_clusters in K :
#  kmeans = KMeans(n_clusters=num_clusters)
#  kmeans.fit(X_train)
#  Sum_of_squared_distances.append(kmeans.inertia_)
# plt.plot(K,Sum_of_squared_distances,'bx-')
# plt.xlabel('Values of K') 
# plt.ylabel('Sum of squared distances/Inertia') 
# plt.title('Elbow Method For Optimal k')
# plt.show()

kmeans = KMeans(n_clusters=3, random_state=2)
clrs = kmeans.fit(X_train)

cl_pred = clrs.predict(X_train)

def predict(a,b):
    return(clrs.predict([[a,b]]))


#print_score(clrs, X_test, y_test)