import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

#read the car price dataset
df=pd.read_csv('car_data_v2 (1).csv')

df

#separating features and target variable
X = df[['vehicle_age', 'km_driven', 'mileage','max_power']]  # features
y = df[['selling_price']] 

#train test split
from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest=train_test_split(X,y, test_size=0.2, random_state=42)



from sklearn.ensemble import RandomForestRegressor

model=RandomForestRegressor()
model.fit(Xtrain,ytrain)

#Save the model
joblib.dump(model,'car_price.pkl')
print("The model has been saved successfully")
