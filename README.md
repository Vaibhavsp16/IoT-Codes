# IoT-Codes

This repository contains ready-to-run Python templates for common machine learning algorithms. Each script follows a similar flow so it is easy to switch between models during study, lab work, or exam preparation:

1. Load a dataset from `file.csv`
2. Split features and target
3. Apply basic preprocessing
4. Train the selected model
5. Evaluate results
6. Plot a simple visualization where relevant

## Quick Start

1. Place your dataset in the repository folder as `file.csv`
2. Install the required Python packages
3. Run the script for the algorithm you want to test

Example:

```bash
pip install pandas matplotlib seaborn scikit-learn xgboost
python SVM.py
```

## Repository Index

| File | Algorithm | Category | Notes |
| --- | --- | --- | --- |
| `decision_tree.py` | Decision Tree | Classification / Regression | Tree-based model with optional tree visualization |
| `random_forest.py` | Random Forest | Classification / Regression | Ensemble of decision trees |
| `XGBoost.py` | XGBoost | Classification / Regression | Boosting-based tree model using `xgboost` |
| `Logistic_Reg.py` | Logistic Regression | Classification | Uses feature scaling and confusion matrix output |
| `Linear_Reg.py` | Linear Regression | Regression | Reports MSE and MAE with actual vs predicted plot |
| `SVM.py` | Support Vector Machine | Classification | Uses `StandardScaler` and RBF kernel |
| `KNN.py` | K-Nearest Neighbors | Classification / Regression | Distance-based model that requires scaling |
| `Naive_Bayes.py` | Naive Bayes | Classification | Includes notes for text classification use cases |
| `MLP.py` | Multi-Layer Perceptron | Classification / Regression | Neural network using `MLPClassifier` |
| `DNN.py` | Deep Neural Network Template | Classification / Regression | Similar neural-network workflow with sklearn MLP |
| `Ensemble.py` | Voting Ensemble | Classification | Combines Logistic Regression, Decision Tree, and SVM |
| `K_Means.py` | K-Means | Clustering | Unsupervised clustering with simple scatter plot |

## Files by Topic

### Classification

- `decision_tree.py`
- `random_forest.py`
- `XGBoost.py`
- `Logistic_Reg.py`
- `SVM.py`
- `KNN.py`
- `Naive_Bayes.py`
- `MLP.py`
- `DNN.py`
- `Ensemble.py`

### Regression

- `Linear_Reg.py`
- `decision_tree.py`
- `random_forest.py`
- `XGBoost.py`
- `KNN.py`
- `MLP.py`
- `DNN.py`

### Clustering

- `K_Means.py`

## Common Requirements

Most scripts use these libraries:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Additional requirement:

- `xgboost` for `XGBoost.py`

Install everything with:

```bash
pip install pandas matplotlib seaborn scikit-learn xgboost
```

## Script Pattern

Most files are organized in the same order:

- data loading
- feature and target split
- preprocessing
- train-test split
- model creation
- training
- prediction
- metrics
- visualization
- exam-focused modification notes

## Notes

- Update the `file.csv` path inside a script if your dataset is stored elsewhere.
- Some models require scaling and already include `StandardScaler`.
- Tree-based models such as Decision Tree, Random Forest, and XGBoost usually do not require scaling.
- `K_Means.py` is unsupervised and does not use a target column.

## Suggested GitHub Navigation

If you are browsing this repository on GitHub, start here:

1. Use the table in `Repository Index` to pick an algorithm
2. Open the corresponding `.py` file
3. Replace `file.csv` with your dataset
4. Run the script and compare outputs across models
