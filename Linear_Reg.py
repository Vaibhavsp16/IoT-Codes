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


# ===================== EXAM MODIFICATIONS GUIDE =====================

# 1. FOR TEXT DATASET:
# Do not use this file for text classification.
# If the exam gives a text classification problem, switch to a classification file
# such as Naive_Bayes.py, Logistic_Reg.py, or SVM.py.

# 2. FOR LABEL ENCODING:
# Usually not needed for numeric regression targets.
# If your target is categorical, do not force this file to work.
# Use Logistic Regression or another classifier instead.

# 3. FOR SCALING:
# Keep the file as it is.
# Do not add a StandardScaler block unless your teacher specifically asks for it.

# 4. IF THE PROBLEM IS CLASSIFICATION INSTEAD OF REGRESSION:
# Comment the MODEL block and use Logistic Regression in the same position:
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=200)
# Also comment the current METRICS block and use:
# from sklearn.metrics import accuracy_score, confusion_matrix
# print("Accuracy:", accuracy_score(y_test, y_pred))

# =============================================================
