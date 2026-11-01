# 🏠 House Price Project

I built this project to answer a simple question: **can we estimate what a house is worth just from its features?**

Using Python and a Linear Regression model, I went through the whole workflow: cleaning the raw data, exploring it, preparing the features, training the model and checking how well it actually performs.

---

## What this project does

- Cleans the raw housing data (missing values, duplicates, outliers)
- Explores the data with charts to see what really drives price
- Prepares features for modelling (encoding and scaling where needed)
- Trains a Linear Regression model
- Evaluates it with MAE, RMSE and R²
- Predicts the price of a new house from its features

---

## Tech stack

- **Python 3**
- **Pandas, NumPy** for data handling
- **Matplotlib, Seaborn** for visualization
- **Scikit-learn** for modelling and evaluation
- **Jupyter Notebook** for analysis

---

## Dataset

- **Source:** [add dataset name / link]
- **Size:** [rows] rows, [columns] columns
- **Target:** `price`
- **Main features:** [e.g. area, bedrooms, bathrooms, location]

---

## How I approached it

1. **Understand the data.** Looked at shape, data types, missing values and basic statistics.
2. **Clean it.** Handled missing values, removed duplicates and checked outliers that could distort the model.
3. **Explore it.** Used distributions, a correlation heatmap and feature-vs-price plots to find the strongest relationships.
4. **Prepare features.** Encoded categorical columns and scaled numeric ones where it made sense.
5. **Train and test.** Split the data 80/20 and trained a Linear Regression model.
6. **Evaluate.** Measured error with MAE and RMSE and explained variance with R².

---

## Results

| Metric | Score |
|---|---|
| MAE | [your value] |
| RMSE | [your value] |
| R² | [your value] |

**What I learned from the results:**
- [e.g. Area is the strongest predictor of price]
- [e.g. Extra bathrooms and parking add a clear premium]
- [e.g. Linear Regression works well as a baseline, but a few outliers pull predictions off]

---

## Getting started

```bash
git clone https://github.com/adib-toki/House_Price_Project.git
cd House_Price_Project
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
jupyter notebook
```

Then open the notebook and run the cells from top to bottom.

---

## Quick example

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("housing.csv")           # use your file name
df = pd.get_dummies(df, drop_first=True)  # encode categorical columns

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

print("MAE :", mean_absolute_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
print("R²  :", r2_score(y_test, pred))
```

---

## Limitations

Linear Regression assumes a straight-line relationship between features and price, so it can miss more complex patterns. Outliers and highly correlated features can also affect the results.

## What's next

- Try Ridge and Lasso regression
- Compare against Random Forest and XGBoost
- Add cross-validation and hyperparameter tuning
- Turn it into a small web app with Streamlit

---

## About me

I'm **Adib**, a Python data analyst who works on data cleaning, analysis, visualization and interactive dashboards.

If this project helped you, a ⭐ on the repo would mean a lot.