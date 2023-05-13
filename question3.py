# -*- coding: utf-8 -*-
"""Question3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Cc2EYT4sYoOC8w-XbjcnpuFfy_IxagV
"""




"""**Question 3**
Download a week of PM2.5 dataset from the OpenAQ website for Delhi. Fill in the missing data with appropriate methods. Use i) the sklearn Random Forest regressor; ii) sklearn Linear regression and iii) Gaussian process regressor to interpolate the PM2.5 values across the space. Use all the available features that you can get from the OpenAQ website or elsewhere (e.g., meteorological variables). Compare the results and prepare a table showing the metrics in K-Fold cross-validation setting.

"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load data from CSV file
df = pd.read_csv("/content/measurements_8118.csv")

# Check for missing data
missing = df.isna().sum()
print(f"Missing data:\n{missing}")

# Fill in missing data
# For example, to use linear interpolation:
df = df.interpolate()

# Define features and target variable
features = ["locationId",	"location" , "parameter" ,	"value"	,"dateUtc"	,"dateLocal",	"unit","latitude","longitude", "country" ,	"city", "isMobile" ,"isAnalysis",	"entity",	"sensorType"]
X = df[features]
y = df["value"]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
rf = RandomForestRegressor(n_estimators=100, random_state=42)
lr = LinearRegression()
kernel = RBF(1.0)
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=5, random_state=42)

# Define performance metrics
metrics = ["neg_mean_absolute_error", "neg_mean_squared_error", "neg_root_mean_squared_error"]

# Calculate scores using K-fold cross-validation
scores_rf = cross_validate(rf, X_train, y_train, cv=5, scoring=metrics)
scores_lr = cross_validate(lr, X_train, y_train, cv=5, scoring=metrics)
scores_gp = cross_validate(gp, X_train, y_train, cv=5, scoring=metrics)

# Calculate mean scores for each model
mean_scores_rf = {k: -np.mean(v) for k, v in scores_rf.items()}
mean_scores_lr = {k: -np.mean(v) for k, v in scores_lr.items()}
mean_scores_gp = {k: -np.mean(v) for k, v in scores_gp.items()}

# Print results
print("Random Forest:\n", mean_scores_rf)
print("Linear Regression:\n", mean_scores_lr)
print("Gaussian Process:\n", mean_scores_gp)
