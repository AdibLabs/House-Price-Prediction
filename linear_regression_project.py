import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression

# CSV Load
df = pd.read_csv("house_data.csv")

# Features (X)
X = df[["Area_sqft", "Bedrooms"]]

# Target (y)
y = df["Price_Lakh"]

# Model Create
model = LinearRegression()

# Model Training
model.fit(X, y)

# Prediction
pre = model.predict([[2500, 5]])

print("Predicted House Price:", pre[0], "Lakh")