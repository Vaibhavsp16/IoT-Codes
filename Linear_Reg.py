import pandas as pd
import matplotlib.pyplot as plt

# -------------------- LOAD DATA --------------------
df = pd.read_csv("file.csv", header=None)

# -------------------- SPLIT --------------------
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# -------------------- PREPROCESSING --------------------
X = pd.get_dummies(X)
X = X.fillna(X.mean())

# -------------------- TRAIN TEST SPLIT --------------------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -------------------- MODEL --------------------
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# -------------------- TRAIN --------------------
model.fit(X_train, y_train)

# -------------------- PREDICT --------------------
y_pred = model.predict(X_test)

# -------------------- METRICS --------------------
from sklearn.metrics import mean_squared_error, mean_absolute_error
print("MSE:", mean_squared_error(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# -------------------- VISUALIZATION --------------------
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Linear Regression")
plt.show()


# ===================== EXAM MODIFICATIONS =====================

# For text dataset:
# Linear Regression is NOT suitable for text classification

# For label encoding:
# Not usually required unless y is categorical (then use classification model instead)

# Scaling:
# NOT REQUIRED (do not add StandardScaler)

# If classification problem:
# Use LogisticRegression instead

# =============================================================