# Import the required libaraies 
import numpy as np
from sklearn import datasets, linear_model

# Load in the datasets from SKlearn. We will be using the diabetes dataset. 
diabetes = datasets.load_diabetes()

# Use only one feature. To make the prediction simple. 
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# Examples to show. 
#print(diabetes_y_pred)

NewValue = 12
NewValuePrediction = regr.predict(NewValue)

print(NewValuePrediction)