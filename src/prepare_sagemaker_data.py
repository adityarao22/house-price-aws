import pandas as pd
from sklearn.model_selection import train_test_split

# Load processed dataset
df = pd.read_csv("data/housing.csv")

# Convert yes/no columns
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

# Put target column FIRST
X = df.drop("price", axis=1)
y = df["price"]

df_final = pd.concat([y, X], axis=1)

# Split data
train, validation = train_test_split(
    df_final,
    test_size=0.2,
    random_state=42
)

# Save without header
train.to_csv(
    "data/train.csv",
    index=False,
    header=False
)

validation.to_csv(
    "data/validation.csv",
    index=False,
    header=False
)

print("Training file created:", train.shape)
print("Validation file created:", validation.shape)
print("\nFirst training row:")
print(train.iloc[0])