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


# ===================== EXAM MODIFICATIONS =====================

# IMPORTANT:
# No y (target) used in clustering

# Change number of clusters:
# model = KMeans(n_clusters=5)

# For text dataset:
# from sklearn.feature_extraction.text import TfidfVectorizer
# X = df.iloc[:, 0]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(X)

# Scaling:
# Recommended (especially for distance-based clustering)

# If dataset has only 2 columns:
# Plot works directly
# If more features → only first 2 used for visualization

# =============================================================