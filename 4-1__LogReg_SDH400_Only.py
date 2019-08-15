import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import cross_val_score
# from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report

cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_clin_util_all.csv', encoding='utf-8')
spatial_400m = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/spatial_400m.csv')

# Merge the CDRN file with Spatial_400m
cdrn = pd.merge(cdrn,spatial_400m,how='left', on='fips_census_code')

cdrn = cdrn.drop(cdrn.columns[0:72], axis =1)
cdrn = cdrn.drop(cdrn.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27]], axis =1)

# Assigns Target and Feature Columns to ['y'] and ['X'], respectively
y = cdrn.psych_hosp.values
feature_cols = [i for i in list(cdrn.columns) if i != 'psych_hosp']
X = cdrn.loc[:, feature_cols].values

# Define Hyperparameter Grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space, 'penalty': ['l1']}

# Instantiate the Logistic Regression
logreg = LogisticRegression()

# Split the data into test (80%) / train (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg,param_grid, cv=5)

# Fit it to the training data
logreg_cv.fit(X_train,y_train)

# Print the optimal parameters and best score
print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))

# Predict the labels of the test set: y_pred
y_pred = logreg_cv.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
