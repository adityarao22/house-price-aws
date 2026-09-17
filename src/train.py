import pandas as pd

# Load dataset
df = pd.read_csv("data/housing.csv")

print("Original Dataset:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert categorical columns into numbers
binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning"
]

for column in binary_columns:
    df[column] = df[column].map({
        "yes": 1,
        "no": 0
    })

# Convert furnishing status
df["furnishingstatus"] = df["furnishingstatus"].map({
    "unfurnished": 0,
    "semi-furnished": 1,
    "furnished": 2
})

print("\nAfter Encoding:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nFinal Shape:")
print(df.shape)

from sklearn.model_selection import train_test_split

# Features (X)
X = df.drop("price", axis=1)

# Target (y)
y = df["price"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Create XGBoost model
model = XGBRegressor(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    objective="reg:squarederror",
    random_state=42
)

# Train model
model.fit(X_train, y_train)

print("\nModel training completed!")

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE :", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
print("\nAccuracy  of the model is : ",r2*100, "%")
