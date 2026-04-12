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

# -------------------- SCALING --------------------
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------- MODEL --------------------
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=200)

# -------------------- TRAIN --------------------
model.fit(X_train, y_train)

# -------------------- PREDICT --------------------
y_pred = model.predict(X_test)

# -------------------- METRICS --------------------
from sklearn.metrics import accuracy_score, confusion_matrix
print("Accuracy:", accuracy_score(y_test, y_pred))

import seaborn as sns
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
plt.title("Logistic Regression")
plt.show()


# ===================== EXAM MODIFICATIONS GUIDE =====================

# 1. FOR TEXT DATASET:
# Comment these two full blocks:
# - # -------------------- SPLIT --------------------
# - # -------------------- PREPROCESSING --------------------
# Then add this code in the same place, after LOAD DATA and before TRAIN TEST SPLIT:
# from sklearn.feature_extraction.text import TfidfVectorizer
# X = df.iloc[:, 0]
# y = df.iloc[:, 1]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(X)

# 2. FOR LABEL ENCODING:
# Add one of the following immediately after the active SPLIT block
# (or after the text-dataset block), and before TRAIN TEST SPLIT:
# y = y.map({'Yes': 1, 'No': 0})
# OR
# from sklearn.preprocessing import LabelEncoder
# y = LabelEncoder().fit_transform(y)

# 3. FOR SCALING:
# Keep the full SCALING block in the same place.
# Logistic Regression usually performs better with StandardScaler.

# 4. FOR MULTI-CLASS:
# No extra change is needed.
# Keep the same MODEL, TRAIN, PREDICT, and METRICS blocks.

# =============================================================
