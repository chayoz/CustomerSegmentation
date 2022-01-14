import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

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
df_scaled = pd.DataFrame(df_scaled, columns=['Age','AnnualIncome','SpendingScore'])

#print(df_scaled)

x = df.drop('SpendingScore', axis=1)
y = df['SpendingScore']


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=2)
#print("train: ",X_train)
#print("test: ",X_test)

kmeans = KMeans(n_clusters=3, random_state=2)
results = kmeans.fit(X_train, y_train)

y_pred = results.predict(X_test)
y_true = results.predict(X_test, y_test)
print(results.predict([[57,75]]))

print(confusion_matrix(y_true, y_pred))

def test():
    return 5;