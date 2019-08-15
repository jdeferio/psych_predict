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


cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_clin_util_all_nta_prevent.csv', encoding='utf-8')

# Removes patients no diagnosis history prior to hospitalization / end of 2014
cdrn = cdrn[cdrn['no_dx_flag'] == 0]

# NTA Neighborhood Information for Education, Poverty, Disability, Rent Burden, Air Quality, Crime Rates, Public Housing
cdrn = cdrn.drop(cdrn.columns[[0,1,2,67,68,69]], axis =1)
cdrn = cdrn.drop(cdrn.columns[65:261], axis =1)


X = cdrn.loc[:,cdrn.columns != 'hosp_any']
y = cdrn.loc[:,cdrn.columns == 'hosp_any']

# OVER-SAMPLING USING SMOTE (Synthetic Minority Over-sampling Technique)
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
columns = X_train.columns

os_data_X, os_data_y = os.fit_sample(X_train, np.ravel(y_train))
os_data_X = pd.DataFrame(data = os_data_X, columns=columns)
os_data_y = pd.DataFrame(data = os_data_y, columns =['hosp_any'])

# Check the Numbers of the dataset
print("Length of oversampled data is: ", len(os_data_X))
print("Number of non-hospitalized patients in oversampled data: ", len(os_data_y[os_data_y['hosp_any']==0]))
print("Number of hospitalizations",len(os_data_y[os_data_y['hosp_any']==1]))
print("Proportion of non-hospitalized patients in oversampled data is: ",len(os_data_y[os_data_y['hosp_any']==0])/len(os_data_X))
print("Proportion of hospitalizations in oversampled data is: ",len(os_data_y[os_data_y['hosp_any']==1])/len(os_data_X))

if len(os_data_y[os_data_y['hosp_any']==1])/len(os_data_X) == len(os_data_y[os_data_y['hosp_any']==0])/len(os_data_X):
    print("Achieved a balanced data set! Great job!")
else: print("Data set is still imbalanced. Consider adjusting.")

# RECURSIVE FEATURE ELIMINATION
cdrn_vars = cdrn.columns.values.tolist()
y = ['hosp_any']
X = [i for i in cdrn_vars if i not in y]

logreg = LogisticRegression()

rfe = RFE(logreg, 25)
rfe = rfe.fit(os_data_X, os_data_y.values.ravel())
print(rfe.support_)
print(rfe.ranking_)

rfe_rank = list(rfe.ranking_)
rfe_support = list(rfe.support_)
rfe_features = pd.DataFrame({"features":list(os_data_X.columns.values), "rank":rfe_rank, "support":rfe_support})
rfe_features_ = rfe_features[rfe_features['rank'] == 1]


# IMPLEMENT THE MODEL
cols = list(rfe_features_.features.values)
print(cols)

XX = os_data_X[cols]
yy = os_data_y['hosp_any']

logit_model = sm.Logit(yy,XX)
result = logit_model.fit()
print(result.summary2())
p_values = list(result.pvalues)


## BEGIN FEATURE SELECTION BASED ON SIGNIFICANCE
sig_features = pd.DataFrame({"features":cols, "pvalues":p_values})
sig_features_ = sig_features[sig_features['pvalues'] < 0.05 ]


# IMPLEMENT THE NEW MODEL
cols_ = list(sig_features_.features.values)
print(cols_)

XX = os_data_X[cols_]
yy = os_data_y['hosp_any']

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
plt.title('Receiver operating characteristic: Clinical Data Only (Preventable Hospitalizations)')
plt.legend(loc="lower right")
plt.savefig('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/ROC_Clin_Prevent.png')
plt.savefig('/Users/jdeferio/Documents/ROC_Clin_Prevent.png')
plt.show()
