import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, classification_report, r2_score, accuracy_score
from rfpimp import *
from xgboost.sklearn import XGBClassifier
import xgboost as xgb
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# ignore Deprecation Warning
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_modified_label2.csv', encoding='utf-8')


def data_processing(df):
    drugs = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/psych_outpt_drug_exp_1218.csv',
                        encoding='utf-8', index_col=False)
    drugs = drugs.drop(drugs.columns[0], axis=1)
    procs = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_procs_grouped_1218.csv',
                        encoding='utf-8', index_col=False)

    # Removes patients no diagnosis history prior to hospitalization / end of 2014
    df = df.loc[(df['age'] >= 18) & (df['visit_count'] >= 2) & (df['date_diff'] >= 30)] # Primary & Secondary
    df = df.loc[(df['mood'] > 1) | (df['schizo'] > 1) | (df['personality'] > 1) | (df['anxiety'] > 1) | (df['adjustment'] > 1)]

    # df = df.loc[(df['age'] >= 18) & (df['visit_count'] >= 2) & (df['date_diff'] >= 30) & (df['enc'] != 2)] # Primary ONLY

    features = ['person_id', 'tuberculosis', 'septic', 'bact_infec', 'mycoses', 'hiv', 'hepatitis', 'viral_infec',
                'other_infec', 'sti', 'screen_infec', 'head_ca', 'esophagus_ca', 'stomach_ca', 'colon_ca', 'rectum_ca',
                'liver_ca', 'pancreas_ca', 'gi_ca', 'lung_ca', 'resp_ca', 'bone_ca', 'melanoma', 'nonepi_skin_ca',
                'breast_ca', 'uterus_ca', 'cervix_ca', 'ovary_ca', 'fem_genital_ca', 'prostate_ca', 'testes_ca',
                'male_genital_ca', 'bladder_ca', 'kidney_ca', 'urinary_ca', 'brain_ca', 'thyroid_ca', 'hodgkins_lymph',
                'non_hodgkins_lymph', 'leukemia', 'mult_myeloma', 'other_ca', 'secndry_malig', 'malig_neoplasm',
                'neoplasm_unspec', 'maint_chemo', 'ben_neoplasm_uterus', 'other_ben_neoplasm', 'thyroid', 'dm_wo_comp',
                'dm_w_comp', 'other_endocrine', 'nutrition', 'lipid_metabo', 'gout', 'fluid_electrolyte',
                'cyst_fibrosis', 'immunity', 'other_metabo', 'other_anemia', 'post_hemorr_anemia', 'sickle_cell',
                'coag_anemia', 'wbc_disease', 'other_heme', 'meningitis_notb', 'encephalitis_notb', 'other_cns',
                'parkinsons', 'mult_scler', 'other_hered_degen', 'paralysis', 'epilepsy', 'headache', 'coma',
                'cataract', 'retinopathy', 'glaucoma', 'blindness', 'eye_inflam', 'other_eye', 'otitis_media', 'dizzy',
                'other_ear_sense', 'other_ns_disorder', 'heart_valve', 'peri_endo_carditis', 'essential_htn',
                'htn_w_comp', 'acute_mi', 'coronary_athero', 'chest_pain_nos', 'pulmonary_hd', 'other_heart_disease',
                'conduction', 'cardiac_dysrhythm', 'cardiac_arrest', 'chf', 'acute_cvd', 'occlu_cereb_artery',
                'other_cvd', 'tran_cereb_isch', 'late_effect_cvd', 'pvd', 'artery_aneurysm', 'artery_embolism',
                'other_circ', 'phlebitis', 'varicose_vein', 'hemorrhoid', 'other_vein_lymph', 'pneumonia', 'influenza',
                'acute_tonsil', 'acute_bronch', 'upper_resp_infec', 'copd', 'asthma', 'asp_pneumonitis', 'pneumothorax',
                'resp_failure', 'lung_disease', 'other_low_resp', 'other_up_resp', 'intestinal_infec', 'teeth_jaw',
                'mouth_disease', 'esophagus', 'gastro_ulcer', 'gastritis', 'other_stomach_duo', 'appendicitis',
                'hernia_abd', 'regional_enteriritis', 'intestinal_obstruct', 'diverticulitis', 'anal_condition',
                'peritonitis', 'biliary_tract', 'other_liver', 'pancreatic', 'gastro_hemorrhage', 'noninfec_gastro',
                'other_gastro', 'nephritis', 'acute_renal_fail', 'ckd', 'uti', 'calculus_urinary', 'other_kidney',
                'other_bladder', 'genitourinary_symp', 'prostate_hyp', 'male_genital_inflam', 'other_male_genital',
                'nonmalig_breast', 'inflam_fem_pelvic', 'endometriosis', 'prolapse_fem_gen', 'menstrual',
                'ovarian_cyst', 'menopausal', 'fem_infert', 'other_fem_genital', 'contraceptive_mgmt', 'spont_abortion',
                'induce_abortion', 'postabort_comp', 'ectopic_preg', 'other_comp_preg', 'hemorrhage_preg',
                'htn_comp_preg', 'early_labor', 'prolong_preg', 'dm_comp_preg', 'malposition', 'fetopelvic_disrupt',
                'prev_c_sect', 'fetal_distress', 'polyhydramnios', 'umbilical_comp', 'ob_trauma', 'forceps_deliv',
                'other_comp_birth', 'other_preg_deliv', 'skin_tissue_infec', 'other_skin_inflam', 'chronic_skin_ulcer',
                'other_skin', 'infec_arthritis', 'rheum_arth', 'osteo_arth', 'other_joint', 'spondylosis',
                'osteoporosis', 'pathological_fract', 'acq_foot_deform', 'other_acq_deform', 'systemic_lupus',
                'other_connective', 'other_bone_disease', 'cardiac_congen_anom', 'digest_congen_anom',
                'genito_congen_anom', 'ns_congen_anom', 'other_congen_anom', 'liveborn', 'short_gest',
                'intrauter_hypoxia', 'resp_distress_synd', 'hemolytic_jaundice', 'birth_trauma', 'other_perinatal',
                'joint_trauma', 'fract_femur_neck', 'spinal_cord', 'skull_face_fract', 'upper_limb_fract',
                'lower_limb_fract', 'other_fract', 'sprain_strain', 'intracranial', 'crush_injury', 'open_wound_head',
                'open_wound_extr', 'comp_of_device', 'comp_surg_proc', 'superficial_inj', 'burns', 'poison_psycho',
                'poison_other_med', 'poison_nonmed', 'other_ext_injury', 'syncope', 'fever_unknown', 'lymphadenitis',
                'gangrene', 'shock', 'naus_vom', 'abdominal_pain', 'malaise_fatigue', 'allergy', 'rehab_care',
                'admin_admiss', 'medical_eval', 'other_aftercare', 'other_screen', 'residual_codes', 'adjustment',
                'anxiety', 'adhd', 'dementia', 'develop_dis', 'child_disorder', 'impule_control', 'mood', 'personality',
                'schizo', 'alcohol', 'substance', 'suicide', 'mental_screen', 'misc_mental', 'e_cut_pierce', 'e_drown',
                'e_fall', 'e_fire', 'e_firearm', 'e_machine', 'e_mvt', 'e_cyclist', 'e_pedestrian', 'e_transport',
                'e_natural', 'e_overexert', 'e_poison', 'e_struckby', 'e_suffocate', 'e_ae_med_care', 'e_ae_med_drug',
                'e_other_class', 'e_other_nec', 'e_unspecified', 'e_place', 'age', 'sex', 'psych_hosp', 'ed_visit',
                'inpt_visit', 'outpt_visit', 'amb_visit']

    cdrn = df.loc[:, features]
    cdrn = cdrn.merge(drugs, on='person_id', how='left').fillna(0)
    cdrn = cdrn.merge(procs, on='person_id', how='left').fillna(0)
    cdrn = cdrn.drop(cdrn.columns[0], axis=1)

    # notna_feat = []
    # cols = list(cdrn.columns.values)
    # for col in cols:
    #     if sum(cdrn[col] != 0):
    #         notna_feat.append(col)
    # cdrn1 = cdrn.loc[:, notna_feat]


    X = cdrn.loc[:,cdrn.columns != 'psych_hosp']
    y = cdrn.loc[:,cdrn.columns == 'psych_hosp']

    X['random'] = np.random.random(size=len(X))

    cdrn_desc = X.describe()

    return X, y, cdrn_desc

def lr_model(x1, y1):
    X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=42)

    # # Create regularization penalty space
    # penalty = ['l1', 'l2']
    # # Create regularization hyperparameter space
    # C = np.logspace(0, 4, 10)
    # # Create hyperparameter options
    # hyperparameters = dict(C=C, penalty=penalty)
    #
    # # Create a based model
    # logreg = LogisticRegression()
    # # Instantiate the grid search model
    # grid_search = GridSearchCV(estimator=logreg, param_grid=hyperparameters,
    #                            cv=5, n_jobs=-1, verbose=0)
    #
    # grid_search.fit(X_train, np.ravel(y_train))
    # print("== LR Best Params ==", grid_search.best_params_, '\n')
    # == LR Best Params == {'C': 1.0, 'penalty': 'l1'}

    logreg = LogisticRegression(penalty='l2', C=7.742636826811269, solver='liblinear', class_weight='balanced', random_state=42, n_jobs=-1)
    lr_cv_score = cross_val_score(logreg, X_train, np.ravel(y_train), cv=10, scoring='roc_auc')

    logreg.fit(X_train, np.ravel(y_train))

    logreg_predict = logreg.predict(X_test)

    print("=== All AUC Scores [CV - Train] ===")
    print(lr_cv_score, '\n')
    print("=== Mean AUC Score [CV - Train] ===")
    print(lr_cv_score.mean(), '\n')
    print("=== Confusion Matrix [Test] ===")
    print(confusion_matrix(y_test, logreg_predict), '\n')
    print("=== Classification Report [Test] ===")
    print(classification_report(y_test, logreg_predict), '\n')
    print("=== AUC Score [Test] ===")
    print(roc_auc_score(y_test, logreg_predict), '\n')

    lr_roc_auc = roc_auc_score(y_test, logreg_predict)
    fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label='LR Classifier (area = %0.3f)' % lr_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic: Clinical Data Only [LR]')
    plt.legend(loc="lower right")
    plt.savefig('/Users/jdeferio/Documents/ROC_Psych_LR_primary_full.png')
    plt.savefig('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/ROC_Psych_LR_primary_full.png')
    plt.show()


def rf_model(x1, y1):
    X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=42)

    # # # Number of trees in random forest
    # n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
    # # Number of features to consider at every split
    # max_features = ['auto', 'sqrt']
    # # Maximum number of levels in tree
    # max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    # max_depth.append(None)
    # # Minimum number of samples required to split a node
    # min_samples_split = [2, 5, 10]
    # # Minimum number of samples required at each leaf node
    # min_samples_leaf = [1, 2, 4]
    # # Method of selecting samples for training each tree
    # bootstrap = [True, False]
    # weight = [None, 'balanced']
    # # Create the random grid
    # random_grid = {'n_estimators': n_estimators,
    #                'max_features': max_features,
    #                'max_depth': max_depth,
    #                'min_samples_split': min_samples_split,
    #                'min_samples_leaf': min_samples_leaf,
    #                'bootstrap': bootstrap,
    #                'class_weight':weight}
    # print("Random Grid Parameters:\n",random_grid,'\n')
    #
    # rf = RandomForestClassifier()
    # # Random search of parameters, using 3 fold cross validation,
    # # search across 100 different combinations, and use all available cores
    # rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2,
    #                                random_state=42, n_jobs=-1)
    # # Fit the random search model
    # rf_random.fit(X_train, np.ravel(y_train))
    # print("== RF Best Params ==", rf_random.best_params_, '\n')
    # {'n_estimators': 600, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 'auto', 'max_depth': 40, 'class_weight': None, 'bootstrap': False}

    rf = RandomForestClassifier(n_estimators= 600, min_samples_split= 5, min_samples_leaf= 1, max_features= 'auto', max_depth= 40, class_weight= None, bootstrap= False, n_jobs=-1)
    rf.fit(X_train, np.ravel(y_train))

    imp = importances(rf, X_test, y_test)  # permutation
    imp = imp.reset_index()
    imp_ = imp[imp['Importance'] >= 0.0002]

    feats = []
    for _ in imp_['Feature']:
        feats.append(_)
    # viz = plot_importances(imp)
    # viz.view()

    return imp, feats

def rf_model2(x1, y1, ft):
    x1 = x1.loc[:,ft]
    # x1['random'] = np.random.random(size=len(x1))

    X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=42)

    # # # Number of trees in random forest
    # n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
    # # Number of features to consider at every split
    # max_features = ['auto', 'sqrt']
    # # Maximum number of levels in tree
    # max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    # max_depth.append(None)
    # # Minimum number of samples required to split a node
    # min_samples_split = [2, 5, 10]
    # # Minimum number of samples required at each leaf node
    # min_samples_leaf = [1, 2, 4]
    # # Method of selecting samples for training each tree
    # bootstrap = [True, False]
    # weight = [None, 'balanced']
    # # Create the random grid
    # random_grid = {'n_estimators': n_estimators,
    #                'max_features': max_features,
    #                'max_depth': max_depth,
    #                'min_samples_split': min_samples_split,
    #                'min_samples_leaf': min_samples_leaf,
    #                'bootstrap': bootstrap,
    #                'class_weight':weight}
    # print("Random Grid Parameters:\n",random_grid,'\n')
    #
    # rf = RandomForestClassifier()
    # # Random search of parameters, using 3 fold cross validation,
    # # search across 100 different combinations, and use all available cores
    # rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2,
    #                                random_state=42, n_jobs=-1)
    # # Fit the random search model
    # rf_random.fit(X_train, np.ravel(y_train))
    # print("== RF Best Params ==", rf_random.best_params_, '\n')
    # # {'n_estimators': 400, 'min_samples_split': 2, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None, 'class_weight': None, 'bootstrap': True}

    rf = RandomForestClassifier(n_estimators= 400, min_samples_split= 2, min_samples_leaf= 4, max_features= 'sqrt', max_depth= None, class_weight= None, bootstrap= True, oob_score=True, n_jobs=-1)
    rf.fit(X_train, np.ravel(y_train))

    rfc_cv_score = cross_val_score(rf, X_test, np.ravel(y_test), cv=10, scoring='roc_auc')
    print("=== OOB Score ===")
    print(rf.oob_score_, '\n')
    print("=== RF Score ===")
    print(rf.score(X_test, y_test), '\n')

    D = feature_dependence_matrix(X_train)
    viz1 = plot_dependence_heatmap(D, figsize=(11,10))
    viz1.save('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/Psych_RF_feat_depend_primary_full.png')

    rf_predict = rf.predict(X_test)

    print("=== All AUC Scores [CV - Train] ===")
    print(rfc_cv_score, '\n')
    print("=== Mean AUC Score [CV - Train] ===")
    print(rfc_cv_score.mean(), '\n')
    print("=== Confusion Matrix [Test] ===")
    print(confusion_matrix(y_test, rf_predict), '\n')
    print("=== Classification Report [Test] ===")
    print(classification_report(y_test, rf_predict), '\n')
    print("=== AUC Score [Test] ===")
    print(roc_auc_score(y_test, rf_predict), '\n')


    imp = importances(rf, X_test, y_test)  # permutation
    viz2 = plot_importances(imp)
    viz2.save('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/Psych_RF_feat_imp_primary_full.png')

    rf_roc_auc = roc_auc_score(y_test, rf_predict)
    fpr, tpr, thresholds = roc_curve(y_test, rf.predict_proba(X_test)[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label='RF Classifier (area = %0.3f)' % rf_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic: Clinical Data Only [RF]')
    plt.legend(loc="lower right")
    plt.savefig('/Users/jdeferio/Documents/ROC_Psych_RF_primary_full.png')
    plt.savefig('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/ROC_Psych_RF_primary_full.png')
    plt.show()


def xgb_model(x1,y1):
    X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=42)

    columns = X_train.columns

    # Weight Rescale
    ratio = float(np.sum(y_train['psych_hosp'].values == 0) / np.sum(y_train['psych_hosp'].values == 1))

    # Instantiate the XGBClassifier and specify parameters
    xgb1 = XGBClassifier(
        learning_rate=0.1,
        n_estimators=1000,
        max_depth=5,
        min_child_weight=1,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        nthread=4,
        scale_pos_weight=ratio,
        seed=42)

    xgb_param = xgb1.get_xgb_params()
    xgtrain = xgb.DMatrix(X_train[columns].values, label=y_train['psych_hosp'].values)
    cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb1.get_params()['n_estimators'], nfold=5,
                      metrics='auc', early_stopping_rounds=50)
    xgb1.set_params(n_estimators=cvresult.shape[0])


    # Fit the algorithm on the data
    xgb1.fit(X_train, np.ravel(y_train), eval_metric='auc')

    imp = importances(xgb1, X_test, y_test)  # permutation
    imp = imp.reset_index()
    imp_ = imp[imp['Importance'] >= 0.0002]

    feats = []
    for _ in imp_['Feature']:
        feats.append(_)

    return imp, feats

def xgb_model2(x1,y1, ft):
    x1 = x1.loc[:, ft]
    X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3, random_state=42)

    columns = X_train.columns

    # Weight Rescale
    ratio = float(np.sum(y_train['psych_hosp'].values == 0) / np.sum(y_train['psych_hosp'].values == 1))

    # Instantiate the XGBClassifier and specify parameters
    xgb1 = XGBClassifier(
        learning_rate=0.1,
        n_estimators=1000,
        max_depth=5,
        min_child_weight=1,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        nthread=4,
        scale_pos_weight=ratio,
        seed=42)

    xgb_param = xgb1.get_xgb_params()
    xgtrain = xgb.DMatrix(X_train[columns].values, label=y_train['psych_hosp'].values)
    cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb1.get_params()['n_estimators'], nfold=5,
                      metrics='auc', early_stopping_rounds=50)
    xgb1.set_params(n_estimators=cvresult.shape[0])
    xgb_cv_score = cross_val_score(xgb1, X_train, np.ravel(y_train), cv=10, scoring='roc_auc')

    # Fit the algorithm on the data
    xgb1.fit(X_train, np.ravel(y_train), eval_metric='auc')

    D = feature_dependence_matrix(X_train)
    viz1 = plot_dependence_heatmap(D, figsize=(11, 10))
    viz1.save('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/Psych_prim_XGB_feat_depend_full.png')

    xgb_predict = xgb1.predict(X_test)

    print("=== All AUC Scores [CV - Train] ===")
    print(xgb_cv_score, '\n')
    print("=== Mean AUC Score [CV - Train] ===")
    print(xgb_cv_score.mean(), '\n')
    print("=== Confusion Matrix [Test] ===")
    print(confusion_matrix(y_test, xgb_predict), '\n')
    print("=== Classification Report [Test] ===")
    print(classification_report(y_test, xgb_predict), '\n')
    print("=== AUC Score [Test] ===")
    print(roc_auc_score(y_test, xgb_predict), '\n')

    imp = importances(xgb1, X_test, y_test)  # permutation
    viz2 = plot_importances(imp)
    viz2.save('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/Psych_XGB_feat_imp_primary_full.png')

    xgb_roc_auc = roc_auc_score(y_test, xgb1.predict(X_test))
    fpr, tpr, thresholds = roc_curve(y_test, xgb1.predict_proba(X_test)[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label='XGB Classifier (area = %0.3f)' % xgb_roc_auc)
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic: Clinical Data Only [XGB]')
    plt.legend(loc="lower right")
    plt.savefig('/Users/jdeferio/Documents/ROC_Psych_XGB_primary_full.png')
    plt.savefig('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/ROC_Psych_XGB_primary_full.png')
    plt.show()




X, y, cdrn_desc = data_processing(cdrn)

lr_model(X, y)

rf_imp, rf_feats = rf_model(X, y)

rf_model2(X, y, rf_feats)

xgb_imp, xgb_feats = xgb_model(X, y)

xgb_model2(X, y, xgb_feats)