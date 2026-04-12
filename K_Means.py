import pandas as pd
import matplotlib.pyplot as plt

# -------------------- LOAD DATA --------------------
df = pd.read_csv("file.csv", header=None)

# -------------------- FEATURES ONLY --------------------
X = df.iloc[:, :-1]

# -------------------- PREPROCESSING --------------------
X = pd.get_dummies(X)
X = X.fillna(X.mean())

# -------------------- SCALING (RECOMMENDED) --------------------
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------- MODEL --------------------
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)

# -------------------- TRAIN --------------------
model.fit(X_scaled)

# -------------------- LABELS --------------------
labels = model.labels_

# -------------------- VISUALIZATION --------------------
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=labels)
plt.title("K-Means Clustering")
plt.show()


# ===================== EXAM MODIFICATIONS GUIDE =====================

# 1. IMPORTANT:
# K-Means is clustering, so this file uses only X.
# There is no y block to keep or edit.

# 2. CHANGE NUMBER OF CLUSTERS:
# In the MODEL block, replace:
# model = KMeans(n_clusters=3)
# with your required cluster count, for example:
# model = KMeans(n_clusters=5)

# 3. FOR TEXT DATASET:
# Comment these two full blocks:
# - # -------------------- FEATURES ONLY --------------------
# - # -------------------- PREPROCESSING --------------------
# Then add this code in the same place, after LOAD DATA and before SCALING:
# from sklearn.feature_extraction.text import TfidfVectorizer
# X = df.iloc[:, 0]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(X)

# 4. FOR SCALING:
# Keep the SCALING block.
# K-Means is distance-based, so scaling should usually remain active.

# 5. FOR VISUALIZATION:
# The current scatter plot uses only the first two columns.
# If your dataset has more than two features, keep the model code as it is,
# but remember that the plot is showing only the first two dimensions.

# =============================================================
