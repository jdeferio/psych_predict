import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, classification_report, r2_score
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from imblearn.over_sampling import SMOTE
import statsmodels.api as sm



cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_util_all_nta.csv', encoding='utf-8')
spatial_1600m = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/spatial_1600m.csv')

# Merge the CDRN file with Spatial_400m
cdrn = pd.merge(cdrn,spatial_1600m,how='left', on='fips_census_code')

# Removes patients no diagnosis history prior to hospitalization / end of 2014
cdrn = cdrn[cdrn['no_dx_flag'] == 0]


features = ['tuberculosis', 'septic', 'bact_infec', 'mycoses', 'hiv_x', 'hepatitis', 'viral_infec', 'other_infec', 'sti', 'screen_infec', 'head_ca', 'esophagus_ca', 'stomach_ca', 'colon_ca', 'rectum_ca', 'liver_ca', 'pancreas_ca', 'gi_ca', 'lung_ca', 'resp_ca', 'bone_ca', 'melanoma', 'nonepi_skin_ca', 'breast_ca', 'uterus_ca', 'cervix_ca', 'ovary_ca', 'fem_genital_ca', 'prostate_ca', 'testes_ca', 'male_genital_ca', 'bladder_ca', 'kidney_ca', 'urinary_ca', 'brain_ca', 'thyroid_ca', 'hodgkins_lymph', 'non_hodgkins_lymph', 'leukemia', 'mult_myeloma', 'other_ca', 'secndry_malig', 'malig_neoplasm', 'neoplasm_unspec', 'maint_chemo', 'ben_neoplasm_uterus', 'other_ben_neoplasm', 'thyroid', 'dm_wo_comp', 'dm_w_comp', 'other_endocrine', 'nutrition', 'lipid_metabo', 'gout', 'fluid_electrolyte', 'cyst_fibrosis', 'immunity', 'other_metabo', 'other_anemia', 'post_hemorr_anemia', 'sickle_cell', 'coag_anemia', 'wbc_disease', 'other_heme', 'meningitis_notb', 'encephalitis_notb', 'other_cns', 'parkinsons', 'mult_scler', 'other_hered_degen', 'paralysis', 'epilepsy', 'headache', 'coma', 'cataract', 'retinopathy', 'glaucoma', 'blindness', 'eye_inflam', 'other_eye', 'otitis_media', 'dizzy', 'other_ear_sense', 'other_ns_disorder', 'heart_valve', 'peri_endo_carditis', 'essential_htn', 'htn_w_comp', 'acute_mi', 'coronary_athero', 'chest_pain_nos', 'pulmonary_hd', 'other_heart_disease', 'conduction', 'cardiac_dysrhythm', 'cardiac_arrest', 'chf', 'acute_cvd', 'occlu_cereb_artery', 'other_cvd', 'tran_cereb_isch', 'late_effect_cvd', 'pvd', 'artery_aneurysm', 'artery_embolism', 'other_circ', 'phlebitis', 'varicose_vein', 'hemorrhoid', 'other_vein_lymph', 'pneumonia', 'influenza', 'acute_tonsil', 'acute_bronch', 'upper_resp_infec', 'copd', 'asthma', 'asp_pneumonitis', 'pneumothorax', 'resp_failure', 'lung_disease', 'other_low_resp', 'other_up_resp', 'intestinal_infec', 'teeth_jaw', 'mouth_disease', 'esophagus', 'gastro_ulcer', 'gastritis', 'other_stomach_duo', 'appendicitis', 'hernia_abd', 'regional_enteriritis', 'intestinal_obstruct', 'diverticulitis', 'anal_condition', 'peritonitis', 'biliary_tract', 'other_liver', 'pancreatic', 'gastro_hemorrhage', 'noninfec_gastro', 'other_gastro', 'nephritis', 'acute_renal_fail', 'ckd', 'uti', 'calculus_urinary', 'other_kidney', 'other_bladder', 'genitourinary_symp', 'prostate_hyp', 'male_genital_inflam', 'other_male_genital', 'nonmalig_breast', 'inflam_fem_pelvic', 'endometriosis', 'prolapse_fem_gen', 'menstrual', 'ovarian_cyst', 'menopausal', 'fem_infert', 'other_fem_genital', 'contraceptive_mgmt', 'spont_abortion', 'induce_abortion', 'postabort_comp', 'ectopic_preg', 'other_comp_preg', 'hemorrhage_preg', 'htn_comp_preg', 'early_labor', 'prolong_preg', 'dm_comp_preg', 'malposition', 'fetopelvic_disrupt', 'prev_c_sect', 'fetal_distress', 'polyhydramnios', 'umbilical_comp', 'ob_trauma', 'forceps_deliv', 'other_comp_birth', 'other_preg_deliv', 'skin_tissue_infec', 'other_skin_inflam', 'chronic_skin_ulcer', 'other_skin', 'infec_arthritis', 'rheum_arth', 'osteo_arth', 'other_joint', 'spondylosis', 'osteoporosis', 'pathological_fract', 'acq_foot_deform', 'other_acq_deform', 'systemic_lupus', 'other_connective', 'other_bone_disease', 'cardiac_congen_anom', 'digest_congen_anom', 'genito_congen_anom', 'ns_congen_anom', 'other_congen_anom', 'liveborn', 'short_gest', 'intrauter_hypoxia', 'resp_distress_synd', 'hemolytic_jaundice', 'birth_trauma', 'other_perinatal', 'joint_trauma', 'fract_femur_neck', 'spinal_cord', 'skull_face_fract', 'upper_limb_fract', 'lower_limb_fract', 'other_fract', 'sprain_strain', 'intracranial', 'crush_injury', 'open_wound_head', 'open_wound_extr', 'comp_of_device', 'comp_surg_proc', 'superficial_inj', 'burns', 'poison_psycho', 'poison_other_med', 'poison_nonmed', 'other_ext_injury', 'syncope', 'fever_unknown', 'lymphadenitis', 'gangrene', 'shock', 'naus_vom', 'abdominal_pain', 'malaise_fatigue', 'allergy', 'rehab_care', 'admin_admiss', 'medical_eval', 'other_aftercare', 'other_screen', 'residual_codes', 'adjustment', 'anxiety', 'adhd', 'dementia', 'develop_dis', 'child_disorder', 'impule_control', 'mood', 'personality', 'schizo', 'alcohol', 'substance', 'suicide', 'mental_screen', 'misc_mental', 'e_cut_pierce', 'e_drown', 'e_fall', 'e_fire', 'e_firearm', 'e_machine', 'e_mvt', 'e_cyclist', 'e_pedestrian', 'e_transport', 'e_natural', 'e_overexert', 'e_poison', 'e_struckby', 'e_suffocate', 'e_ae_med_care', 'e_ae_med_drug', 'e_other_class', 'e_other_nec', 'e_unspecified', 'e_place', 'age_1_jan_2014', 'sex', 'psych_hosp', 'poverty', 'foodstampsnap', 'unemployment', 'disability', 'rentburden50', 'crowdedhousing', 'nychaperc', 'blackcarbon', 'pm25', 'nitricoxide', 'nitrogendioxide', 'ozone', 'sulfurdioxide', 'alcoholretailers', 'tobaccoretailers', 'felonycrime', 'propertycrime', 'violentcrime', 'ed_2012', 'ed_2013', 'inpt_2012', 'inpt_2013', 'outpt_2012', 'outpt_2013', 'amb_2012', 'amb_2013', 'other_2012', 'other_2013', 'ed2014', 'inpt_2014', 'outpt_2014', 'amb_2014', 'other_2014', 'Art1600', 'Bus1600', 'Bus_Ex_1600', 'Cultural1600', 'Diag1600', 'Hospitals1600', 'Humanities1600', 'Library1600', 'Museums1600', 'S_health1600', 'Sub1600', 'V_art1600', 'Park1600', 'Education_Facilities1600m', 'tree1600']

cdrn = cdrn.loc[:, features]


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

rfe = RFE(logreg, 40)
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
yy = os_data_y['psych_hosp']

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
cv_auc = cross_val_score(logreg, X_test, y_test, cv=5,scoring='roc_auc')

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
plt.title('Receiver operating characteristic: Clinical + 1600m SDOH (Psychiatric Hospitalizations)')
plt.legend(loc="lower right")
plt.savefig('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/CCS_ROC_Clin_1600m_Psych.png')
plt.savefig('/Users/jdeferio/Documents/CCS_ROC_Clin_1600m_Psych.png')
plt.show()