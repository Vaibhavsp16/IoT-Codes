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
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

# -------------------- TRAIN --------------------
model.fit(X_train, y_train)

# -------------------- PREDICT --------------------
y_pred = model.predict(X_test)

# -------------------- METRICS --------------------
from sklearn.metrics import accuracy_score, confusion_matrix
print("Accuracy:", accuracy_score(y_test, y_pred))

import seaborn as sns
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
plt.title("Decision Tree")
plt.show()

# -------------------- TREE VISUALIZATION --------------------
from sklearn.tree import plot_tree
plt.figure(figsize=(10,6))
plot_tree(model)
plt.show()


# ===================== EXAM MODIFICATIONS =====================

# For text dataset:
# from sklearn.feature_extraction.text import TfidfVectorizer
# X = df.iloc[:, 0]
# y = df.iloc[:, 1]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(X)

# For label encoding:
# y = y.map({'Yes':1, 'No':0})
# OR
# from sklearn.preprocessing import LabelEncoder
# y = LabelEncoder().fit_transform(y)

# Scaling:
# NOT REQUIRED → do NOT use StandardScaler

# For regression:
# from sklearn.tree import DecisionTreeRegressor
# model = DecisionTreeRegressor()

# =============================================================