import pandas as pd
import numpy as np
# from scipy import stats
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, classification_report, r2_score, accuracy_score, pairwise
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from collections import Counter
from scipy.spatial import distance
from sklearn.utils import validation
from scipy.sparse import issparse
import logging
import time

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)



# load the dataset
cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_util_all_nta.csv', encoding='utf-8')

def data_processing(df):

    # Removes patients no diagnosis history prior to hospitalization / end of 2014
    df = df[df['no_dx_flag'] == 0]
    df = df[df['age_1_jan_2014'] >= 18]

    features = ['tuberculosis', 'septic', 'bact_infec', 'mycoses', 'hiv_x', 'hepatitis', 'viral_infec', 'other_infec', 'sti', 'screen_infec', 'head_ca', 'esophagus_ca', 'stomach_ca', 'colon_ca', 'rectum_ca', 'liver_ca', 'pancreas_ca', 'gi_ca', 'lung_ca', 'resp_ca', 'bone_ca', 'melanoma', 'nonepi_skin_ca', 'breast_ca', 'uterus_ca', 'cervix_ca', 'ovary_ca', 'fem_genital_ca', 'prostate_ca', 'testes_ca', 'male_genital_ca', 'bladder_ca', 'kidney_ca', 'urinary_ca', 'brain_ca', 'thyroid_ca', 'hodgkins_lymph', 'non_hodgkins_lymph', 'leukemia', 'mult_myeloma', 'other_ca', 'secndry_malig', 'malig_neoplasm', 'neoplasm_unspec', 'maint_chemo', 'ben_neoplasm_uterus', 'other_ben_neoplasm', 'thyroid', 'dm_wo_comp', 'dm_w_comp', 'other_endocrine', 'nutrition', 'lipid_metabo', 'gout', 'fluid_electrolyte', 'cyst_fibrosis', 'immunity', 'other_metabo', 'other_anemia', 'post_hemorr_anemia', 'sickle_cell', 'coag_anemia', 'wbc_disease', 'other_heme', 'meningitis_notb', 'encephalitis_notb', 'other_cns', 'parkinsons', 'mult_scler', 'other_hered_degen', 'paralysis', 'epilepsy', 'headache', 'coma', 'cataract', 'retinopathy', 'glaucoma', 'blindness', 'eye_inflam', 'other_eye', 'otitis_media', 'dizzy', 'other_ear_sense', 'other_ns_disorder', 'heart_valve', 'peri_endo_carditis', 'essential_htn', 'htn_w_comp', 'acute_mi', 'coronary_athero', 'chest_pain_nos', 'pulmonary_hd', 'other_heart_disease', 'conduction', 'cardiac_dysrhythm', 'cardiac_arrest', 'chf', 'acute_cvd', 'occlu_cereb_artery', 'other_cvd', 'tran_cereb_isch', 'late_effect_cvd', 'pvd', 'artery_aneurysm', 'artery_embolism', 'other_circ', 'phlebitis', 'varicose_vein', 'hemorrhoid', 'other_vein_lymph', 'pneumonia', 'influenza', 'acute_tonsil', 'acute_bronch', 'upper_resp_infec', 'copd', 'asthma', 'asp_pneumonitis', 'pneumothorax', 'resp_failure', 'lung_disease', 'other_low_resp', 'other_up_resp', 'intestinal_infec', 'teeth_jaw', 'mouth_disease', 'esophagus', 'gastro_ulcer', 'gastritis', 'other_stomach_duo', 'appendicitis', 'hernia_abd', 'regional_enteriritis', 'intestinal_obstruct', 'diverticulitis', 'anal_condition', 'peritonitis', 'biliary_tract', 'other_liver', 'pancreatic', 'gastro_hemorrhage', 'noninfec_gastro', 'other_gastro', 'nephritis', 'acute_renal_fail', 'ckd', 'uti', 'calculus_urinary', 'other_kidney', 'other_bladder', 'genitourinary_symp', 'prostate_hyp', 'male_genital_inflam', 'other_male_genital', 'nonmalig_breast', 'inflam_fem_pelvic', 'endometriosis', 'prolapse_fem_gen', 'menstrual', 'ovarian_cyst', 'menopausal', 'fem_infert', 'other_fem_genital', 'contraceptive_mgmt', 'spont_abortion', 'induce_abortion', 'postabort_comp', 'ectopic_preg', 'other_comp_preg', 'hemorrhage_preg', 'htn_comp_preg', 'early_labor', 'prolong_preg', 'dm_comp_preg', 'malposition', 'fetopelvic_disrupt', 'prev_c_sect', 'fetal_distress', 'polyhydramnios', 'umbilical_comp', 'ob_trauma', 'forceps_deliv', 'other_comp_birth', 'other_preg_deliv', 'skin_tissue_infec', 'other_skin_inflam', 'chronic_skin_ulcer', 'other_skin', 'infec_arthritis', 'rheum_arth', 'osteo_arth', 'other_joint', 'spondylosis', 'osteoporosis', 'pathological_fract', 'acq_foot_deform', 'other_acq_deform', 'systemic_lupus', 'other_connective', 'other_bone_disease', 'cardiac_congen_anom', 'digest_congen_anom', 'genito_congen_anom', 'ns_congen_anom', 'other_congen_anom', 'liveborn', 'short_gest', 'intrauter_hypoxia', 'resp_distress_synd', 'hemolytic_jaundice', 'birth_trauma', 'other_perinatal', 'joint_trauma', 'fract_femur_neck', 'spinal_cord', 'skull_face_fract', 'upper_limb_fract', 'lower_limb_fract', 'other_fract', 'sprain_strain', 'intracranial', 'crush_injury', 'open_wound_head', 'open_wound_extr', 'comp_of_device', 'comp_surg_proc', 'superficial_inj', 'burns', 'poison_psycho', 'poison_other_med', 'poison_nonmed', 'other_ext_injury', 'syncope', 'fever_unknown', 'lymphadenitis', 'gangrene', 'shock', 'naus_vom', 'abdominal_pain', 'malaise_fatigue', 'allergy', 'rehab_care', 'admin_admiss', 'medical_eval', 'other_aftercare', 'other_screen', 'residual_codes', 'adjustment', 'anxiety', 'adhd', 'dementia', 'develop_dis', 'child_disorder', 'impule_control', 'mood', 'personality', 'schizo', 'alcohol', 'substance', 'suicide', 'mental_screen', 'misc_mental', 'e_cut_pierce', 'e_drown', 'e_fall', 'e_fire', 'e_firearm', 'e_machine', 'e_mvt', 'e_cyclist', 'e_pedestrian', 'e_transport', 'e_natural', 'e_overexert', 'e_poison', 'e_struckby', 'e_suffocate', 'e_ae_med_care', 'e_ae_med_drug', 'e_other_class', 'e_other_nec', 'e_unspecified', 'e_place', 'age_1_jan_2014', 'sex', 'psych_hosp', 'ed_2012', 'ed_2013', 'inpt_2012', 'inpt_2013', 'outpt_2012', 'outpt_2013', 'amb_2012', 'amb_2013', 'other_2012', 'other_2013', 'ed2014', 'inpt_2014', 'outpt_2014', 'amb_2014', 'other_2014']

    df = df.loc[:, features]

    # # Filter Outliers Based on Z-score and
    # z = np.abs(stats.zscore(df))
    # df = df[(z < 25).all(axis=1)]

    # Split Data into Label (y) and Features (X)
    X = df.loc[:, df.columns != 'psych_hosp']
    y = df.loc[:, df.columns == 'psych_hosp']

    # Split into Training and Test Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)


    return X_train, X_test, y_train, y_test

def check_pairwise_arrays(X, Y, precomputed=False, dtype=None):
    X, Y, dtype_float = pairwise._return_float_dtype(X, Y)

    warn_on_dtype = dtype is not None
    estimator = 'check_pairwise_arrays'
    if dtype is None:
        dtype = dtype_float

    if Y is X or Y is None:
        X = Y = validation.check_array(X, accept_sparse='csr', dtype=dtype,
                            warn_on_dtype=warn_on_dtype, estimator=estimator)
    else:
        X = validation.check_array(X, accept_sparse='csr', dtype=dtype,
                        warn_on_dtype=warn_on_dtype, estimator=estimator)
        Y = validation.check_array(Y, accept_sparse='csr', dtype=dtype,
                        warn_on_dtype=warn_on_dtype, estimator=estimator)

    if precomputed:
        if X.shape[1] != Y.shape[0]:
            raise ValueError("Precomputed metric requires shape "
                             "(n_queries, n_indexed). Got (%d, %d) "
                             "for %d indexed." %
                             (X.shape[0], X.shape[1], Y.shape[0]))
    elif X.shape[1] != Y.shape[1]:
        raise ValueError("Incompatible dimension for X and Y matrices: "
                         "X.shape[1] == %d while Y.shape[1] == %d" % (
                             X.shape[1], Y.shape[1]))

    return X, Y

def gower_distances(X, Y=None, w=None,categorical_features=None):
    """Computes the gower distances between X and Y

    Gower is a similarity measure for categorical, boolean and numerical mixed
    data.


    Parameters
    ----------
    X : array-like, or pandas.DataFrame, shape (n_samples, n_features)

    Y : array-like, or pandas.DataFrame, shape (n_samples, n_features)

    w :  array-like, shape (n_features)
        According the Gower formula, w is an attribute weight.

    categorical_features: array-like, shape (n_features)
        Indicates with True/False whether a column is a categorical attribute.
        This is useful when categorical attributes are represented as integer
        values. Categorical ordinal attributes are treated as numeric, and must
        be marked as false.

        Alternatively, the categorical_features array can be represented only
        with the numerical indexes of the categorical attributes.

    Returns
    -------
    similarities : ndarray, shape (n_samples, n_samples)

    Notes
    ------
    The non-numeric features, and numeric feature ranges are determined from X and not Y.
    No support for sparse matrices.

    """
    rows, cols = X.shape

    if categorical_features is None:
        categorical_features = []
        for col in range(cols):
            if np.issubdtype(type(X[0, col]), np.number):
                categorical_features.append(False)
            else:
                categorical_features.append(True)
    # Calculates the normalized ranges and max values of numeric values
    ranges_of_numeric = [0.0] * cols
    max_of_numeric = [0.0] * cols
    for col in range(cols):
        #if not categorical_features[col]:
        maxx = None
        minn = None
        if issparse(X):
            col_array = X.getcol(col)
            maxx = col_array.max() + 0.0
            minn = col_array.min() + 0.0
        else:
            col_array = X[:, col].astype(np.double)
            maxx = np.nanmax(col_array)
            minn = np.nanmin(col_array)

        if np.isnan(maxx):
            maxx = 0.0
        if np.isnan(minn):
            minn = 0.0
        max_of_numeric[col] = maxx
        ranges_of_numeric[col] = (1 - minn / maxx) if (maxx != 0) else 0.0

    if w is None:
        w = [1] * cols

    ycols = len(Y)
    yrows = 1

    dm = np.zeros((rows, yrows), dtype=np.double)

    for i in range(0, rows):
        j_start = 0

        # for non square results
        # if rows != yrows:
        #     j_start = 0

        for j in range(j_start, yrows):
            sum_sij = 0.0
            sum_wij = 0.0
            for col in range(cols):
                value_xi = X[i, col]
                value_xj = Y[col]

                #if not categorical_features[col]:
                if max_of_numeric[col] != 0:
                    value_xi = value_xi / max_of_numeric[col]
                    value_xj = value_xj / max_of_numeric[col]
                else:
                    value_xi = 0
                    value_xj = 0

                if ranges_of_numeric[col] != 0:
                    sij = abs(value_xi - value_xj) / ranges_of_numeric[col]
                else:
                    sij = 0
                wij = (w[col], 0)[np.isnan(value_xi) or np.isnan(value_xj)]
                # else:
                #     sij = (1.0, 0.0)[value_xi == value_xj]
                #     wij = (w[col], 0)[value_xi is None and value_xj is None]
                sum_sij += (wij * sij)
                sum_wij += wij

            if sum_wij != 0:
                dm[i, j] = (sum_sij / sum_wij)
                if j < rows and i < yrows:
                    dm[j, i] = dm[i, j]

    return dm.reshape(1,-1)

def gower_function(X, Y):
    output_filename = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_gower_similar.csv'

    gower_similarities = []

    if issparse(X) or issparse(Y):
        raise TypeError("Sparse matrices are not supported for gower distance")

    X2, Y2 = check_pairwise_arrays(X, Y, precomputed=False, dtype=np.object)

    for row in Y2:
       D = gower_distances(np.array(X2),np.array(row))
       gower_similarities.append(D)

       # Print status every 10 Records
       if len(gower_similarities) % 3 == 0:
           logger.info("Completed {} of {} Records".format(len(gower_similarities), len(Y2)))

       # Every 500 records, save progress to file(in case of a failure so you have something!)
       if len(gower_similarities) % 500 == 0:
           pd.DataFrame(gower_similarities).to_csv("{}_bak".format(output_filename))

    # All done
    logger.info("Finished computing gower similarities for all records")
    # Write the full results to csv using the pandas library.
    pd.DataFrame(gower_similarities).to_csv(output_filename, encoding='utf8')

    return gower_similarities


X_train, X_test, y_train, y_test = data_processing(cdrn)


gower_function(X_train, X_test)