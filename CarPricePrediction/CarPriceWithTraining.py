import numpy as np
import pandas as pd
import pickle #pip install pickle-mixin
dataset = pd.read_csv('Data_Train1.csv')
x = dataset.iloc[:,1:11].values
y = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
x[:,0]=lb.fit_transform(x[:,0])
x[:,3]=lb.fit_transform(x[:,3])
x[:,4]=lb.fit_transform(x[:,4])
x[:,5]=lb.fit_transform(x[:,5])
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',strategy='mean',axis=0)
imputer = imputer.fit(x[:,])
x[:, ] = imputer.transform(x[:,])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.10,random_state = 0)
#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

with open('check.pkl', 'wb') as f:
    pickle.dump(regressor, f)




#predict the test set results
y_pred = regressor.predict([[float(city), float(year), float(km), float(fuel), float(transmission), float(ownertype), float(mileage), float(engine), float(power), float(seats)]])


redirectURL = "http://localhost/Animesh/final.py?data={:.2f}".format(y_pred[0])
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')