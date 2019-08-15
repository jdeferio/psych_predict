import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from imblearn.over_sampling import SMOTE
import statsmodels.api as sm
from sklearn.feature_selection import RFE


cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_clin_util_all_nta.csv', encoding='utf-8')

# Removes patients no diagnosis history prior to hospitalization / end of 2014
cdrn = cdrn[cdrn['no_dx_flag'] == 0]

# NTA Neighborhood Information for Education, Poverty, Disability, Rent Burden, Air Quality, Crime Rates, Public Housing
cdrn = cdrn.drop(cdrn.columns[[0,1,2,67,68,69]], axis =1)
cdrn = cdrn.drop(cdrn.columns[65:261], axis =1)
# cdrn = cdrn.drop(cdrn.columns[[66,67,69,70,71,72,73,74,75,76,77,78,79,81,82]], axis =1)
# cdrn = cdrn.drop(cdrn.columns[69:199], axis =1)
# cdrn = cdrn.drop(cdrn.columns[[70,71,72,73,74,75,76,84]], axis =1)

X = cdrn.loc[:,cdrn.columns != 'psych_hosp']
y = cdrn.loc[:,cdrn.columns == 'psych_hosp']

# OVER-SAMPLING USING SMOTE (Synthetic Minority Over-sampling Technique)
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
columns = X_train.columns

os_data_X, os_data_y = os.fit_sample(X_train, np.ravel(y_train))
os_data_X = pd.DataFrame(data = os_data_X, columns=columns)
os_data_y = pd.DataFrame(data = os_data_y, columns =['psych_hosp'])

# Check the Numbers of the dataset
print("Length of oversampled data is: ", len(os_data_X))
print("Number of non-hospitalized patients in oversampled data: ", len(os_data_y[os_data_y['psych_hosp']==0]))
print("Number of hospitalizations",len(os_data_y[os_data_y['psych_hosp']==1]))
print("Proportion of non-hospitalized patients in oversampled data is: ",len(os_data_y[os_data_y['psych_hosp']==0])/len(os_data_X))
print("Proportion of hospitalizations in oversampled data is: ",len(os_data_y[os_data_y['psych_hosp']==1])/len(os_data_X))

if len(os_data_y[os_data_y['psych_hosp']==1])/len(os_data_X) == len(os_data_y[os_data_y['psych_hosp']==0])/len(os_data_X):
    print("Achieved a balanced data set! Great job!")
else: print("Data set is still imbalanced. Consider adjusting.")

# RECURSIVE FEATURE ELIMINATION
cdrn_vars = cdrn.columns.values.tolist()
y = ['psych_hosp']
X=[i for i in cdrn_vars if i not in y]

logreg = LogisticRegression()

rfe = RFE(logreg, 25)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)
# Selected Variables
# 2,5,7,10,11,13,14,16,22,24,28,29,30,31,32,36,40,41,42,46,48,49,52,53,58


# IMPLEMENT THE MODEL
cols = ['alzheimers','cataract','depression','diabetes','heart_fail','hip_pelv_frac','htn','stroke_tia','colorectal_ca','lung_ca','autism','bipolar','cerebral_p','cystic_f','epilepsy','learn_disable','mobility','personality','ulcers','schizo','spina_bifida','spinal_cord','suicide']

XX = os_data_X[cols]
yy = os_data_y['psych_hosp']

logit_model = sm.Logit(yy,XX)
result = logit_model.fit()
print(result.summary2())

logreg = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(XX,yy, test_size=0.2, random_state=0)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.3f}'.format(logreg.score(X_test, y_test)))

cfm = confusion_matrix(y_test, y_pred)
print(cfm)
print(classification_report(y_test, y_pred))

print("R^2 Score: {}".format(r2_score(y_test, y_pred)))

# Compute cross-validated AUC scores: cv_auc
cv_auc = cross_val_score(logreg, XX, yy, cv=5,scoring='roc_auc')

# Print list of AUC scores for 5-fold CV
print("AUC scores computed using 5-fold cross-validation: {}".format(cv_auc))

logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.3f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic: Clinical Data Only')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()


# y = cdrn.psych_hosp.values
# feature_cols = [i for i in list(cdrn.columns) if i != 'psych_hosp']
# X = cdrn.loc[:, feature_cols].values


# logreg = LogisticRegression(penalty='l1')
#
# # Split the data into test (80%) / train (20%)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#
# # Fit the classifier to the training data
# logreg.fit(X_train, y_train)
#
# # Compute predicted probabilities: y_pred_prob
# y_pred_prob = logreg.predict_proba(X_test)[:,1]
#
# # Compute and print AUC score
# print("AUC: {}".format(roc_auc_score(y_test, y_pred_prob)))
#
# # Generate ROC curve values: fpr, tpr, thresholds
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
#
# # Plot ROC curve
# plt.plot([0, 1], [0, 1], 'k--')
# plt.plot(fpr, tpr)
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC Curve')
# plt.show()
#
# # Predict the labels of the test set: y_pred
# y_pred = logreg.predict(X_test)
#
# # Compute and print the confusion matrix and classification report
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print("R2 Score: {}".format(r2_score(y_test, y_pred)))
#
#
# # Compute cross-validated AUC scores: cv_auc
# cv_auc = cross_val_score(logreg, X, y, cv=5,scoring='roc_auc')
#
# # Print list of AUC scores for 5-fold CV
# print("AUC scores computed using 5-fold cross-validation: {}".format(cv_auc))
