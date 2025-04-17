# src/train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


df = pd.read_csv('../data/cardio_train.csv', sep=';')



df = df.drop_duplicates()
df = df.dropna()
df = df[(df.height > 100) & (df.height < 250)]
df = df[(df.weight > 30) & (df.weight < 200)]
df = df[(df.ap_hi > 50) & (df.ap_hi < 250)]
df = df[(df.ap_lo > 30) & (df.ap_lo < 200)]


features = ["age", "height", "weight", "ap_hi", "ap_lo", "cholesterol", "gluc", "smoke", "alco", "active"]
X = df[features]
y = df["cardio"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
model.fit(X_train, y_train)


accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model Accuracy: {accuracy:.4f}")


joblib.dump(model, "src/model.pkl")
