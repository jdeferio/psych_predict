import pandas as pd
import datetime as dt


# ============================================= #
#
#            IMPORT DATA SETS
#
# ============================================= #

cdrn_psych_hosp_bef_15 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_bef_15.csv', encoding='utf-8', names=['person_id', 'visit_start_date', 'visit_concept_id', 'condition_type_concept_id'])

cdrn_all_visits_2014 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_visits_2014.csv', encoding='utf-8', names=['person_id', 'condition_start_date', 'visit_type'])

# Sorts df by 'person_id' and 'visit_start_date'
cdrn_psych_hosp_1315 = cdrn_psych_hosp_1315.sort_values(by=['person_id', 'visit_start_date'])
print("Length and Number of unique person_id's with psych hospitalization between 13-15: ", len(cdrn_psych_hosp_1315),
      ", ", cdrn_psych_hosp_1315.person_id.nunique())

# ============================================= #
#
# START CREATION OF 1ST PSYCH HOSP IN 2014 FILE
#
# ============================================= #

def dx_condense1(df):
    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_grouped1.csv'
    
    cdrn_ccs_results = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results1.csv',encoding='utf-8')
    print("Number of unique person_id in cdrn_ccs_results: ", cdrn_ccs_results.person_id.nunique())
    
    # Creates var 'hosp_num' which is a successive count of psychiatric hospitalizations per 'person_id' (ascending 
    # order by date)
    # Identifies the first psych hospitalization in 2014, but is not necessarily the first psych hosp ever
    df['hosp_num'] = df.groupby('person_id').visit_start_date.apply(pd.Series.rank)

    # Creates new df where only the first psychiatric hospitalization in 2014 is retained
    cdrn_psych_hosp_1315_1st = df[df['hosp_num'] < 2.0]
    cdrn_psych_hosp_1315_1st = cdrn_psych_hosp_1315_1st.drop_duplicates(subset='person_id', keep='first')
    cdrn_psych_hosp_1315_1st = cdrn_psych_hosp_1315_1st[cdrn_psych_hosp_1315_1st['visit_start_date'] > '2012-12-31']
    print("Length of psych hospitalization in 2013-2015: ", len(cdrn_psych_hosp_1315_1st))
    pd.DataFrame(cdrn_psych_hosp_1315_1st).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_1315_1st.csv', encoding='utf-8')

    # Merges the psych hospitalization file with the CCS results
    cdrn_1st_psych_dx = pd.merge(cdrn_psych_hosp_1315_1st_, cdrn_ccs_results, how='inner', on='person_id')
    print("Number of unique persons with psych hospitalization and dx / visit history:",
          cdrn_1st_psych_dx.person_id.nunique())
    print("Length of cdrn_1st_psych_dx:", len(cdrn_1st_psych_dx))

    # Filters the resultant df so that only the dx that occurred on or before the first psych hospitalization are 
    # present
    cdrn_1st_psych_dx = cdrn_1st_psych_dx[(cdrn_1st_psych_dx.condition_start_date < cdrn_1st_psych_dx.visit_start_date)]
    print("Number of unique persons with psych hospitalization and dx history < hospitalization date:",
          cdrn_1st_psych_dx.person_id.nunique())

    # ============================================= #
    #
    #     START CREATION OF NO PSYCH HOSP FILE
    #
    # ============================================= #

    # Creates a df of 'person_id' for people who had a psych hospitalization before end of 2014
    cdrn_psych_hosp = cdrn_psych_hosp_2014.person_id.append(cdrn_psych_hosp_bef_2014.person_id).drop_duplicates()

    psych_hosp_list = []
    for _ in cdrn_psych_hosp:
        psych_hosp_list.append(_)

    ids = [1 for i in range(len(psych_hosp_list))]
    psych_id = pd.DataFrame({"person_id": psych_hosp_list, "id": ids})
    cdrn_no_psych_flag = pd.merge(cdrn_ccs_results, psych_id, how='left', on='person_id')

    # Removes patients with a previous psych hospitalization
    cdrn_no_psych_dx = cdrn_no_psych_flag[cdrn_no_psych_flag['id'] != 1]
    print("Number of patients with no psych hospitalizations: ", cdrn_no_psych_dx.person_id.nunique())

    # cdrn_psych_hosp_missing = pd.read_csv(
    # '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_ccs_results.csv', encoding='utf-8')

    # cdrn_no_psych_dx = cdrn_no_psych_dx.drop(cdrn_no_psych_dx.columns[[0, 65]], axis=1)
    cdrn_no_psych_dx = cdrn_no_psych_dx.drop(columns=['Unnamed: 0', 'id'])

    cdrn_1st_psych_dx = cdrn_1st_psych_dx.drop(cdrn_1st_psych_dx.columns[[1, 2, 3, 4, 5]], axis=1)

    # cdrn_psych_hosp_missing = cdrn_psych_hosp_missing.drop(cdrn_psych_hosp_missing.columns[[0]], axis = 1)

    cdrn_psych_dx_all = cdrn_no_psych_dx.append(cdrn_1st_psych_dx, sort=False)
    print("Length cdrn_psych_dx_all: ", len(cdrn_psych_dx_all))

    # cdrn_psych_dx_all = cdrn_psych_dx_all.append(cdrn_psych_hosp_missing, sort=False)
    # print("Length cdrn_psych_dx_all: ",len(cdrn_psych_dx_all_))

    # Converts Longitudinal Data to Aggregate Counts Per Patient
    cdrn_ccs_grouped = cdrn_psych_dx_all.groupby('person_id').agg({"tuberculosis": sum, "septic": sum, "bact_infec": sum,
         "mycoses": sum, "hiv": sum, "hepatitis": sum, "viral_infec": sum, "other_infec": sum, "sti": sum,
         "screen_infec": sum, "head_ca": sum, "esophagus_ca": sum, "stomach_ca": sum, "colon_ca": sum,
         "rectum_ca": sum, "liver_ca": sum, "pancreas_ca": sum, "gi_ca": sum, "lung_ca": sum, "resp_ca": sum,
         "bone_ca": sum, "melanoma": sum, "nonepi_skin_ca": sum, "breast_ca": sum, "uterus_ca": sum,
         "cervix_ca": sum, "ovary_ca": sum, "fem_genital_ca": sum, "prostate_ca": sum, "testes_ca": sum,
         "male_genital_ca": sum, "bladder_ca": sum, "kidney_ca": sum, "urinary_ca": sum, "brain_ca": sum,
         "thyroid_ca": sum, "hodgkins_lymph": sum, "non_hodgkins_lymph": sum, "leukemia": sum,
         "mult_myeloma": sum, "other_ca": sum, "secndry_malig": sum, "malig_neoplasm": sum,
         "neoplasm_unspec": sum, "maint_chemo": sum, "ben_neoplasm_uterus": sum, "other_ben_neoplasm": sum,
         "thyroid": sum, "dm_wo_comp": sum, "dm_w_comp": sum, "other_endocrine": sum, "nutrition": sum,
         "lipid_metabo": sum, "gout": sum, "fluid_electrolyte": sum, "cyst_fibrosis": sum, "immunity": sum,
         "other_metabo": sum, "other_anemia": sum, "post_hemorr_anemia": sum, "sickle_cell": sum,
         "coag_anemia": sum, "wbc_disease": sum, "other_heme": sum, "meningitis_notb": sum,
         "encephalitis_notb": sum, "other_cns": sum, "parkinsons": sum})

    pd.DataFrame(cdrn_ccs_grouped).to_csv(output_filepath, encoding='utf-8')
    print("Finished condensing CCS Results 1")
    print("")


def dx_condense2(df):
    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_grouped2.csv'

    cdrn_ccs_results = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results2.csv',encoding='utf-8')
    print("Number of unique person_id in cdrn_ccs_results: ", cdrn_ccs_results.person_id.nunique())

    # Creates var 'hosp_num' which is a successive count of psychiatric hospitalizations per 'person_id' (ascending 
    # order by date)
    # Identifies the first psych hospitalization in 2014, but is not necessarily the first psych hosp ever
    df['hosp_num'] = df.groupby('person_id').visit_start_date.apply(pd.Series.rank)

    # Creates new df where only the first psychiatric hospitalization in 2014 is retained
    cdrn_psych_hosp_2014_1st = df[df['hosp_num'] == 1.0]
    print("Length of psych hospitalization in 2014: ", len(cdrn_psych_hosp_2014_1st))

    # Reset Index
    cdrn_psych_hosp_2014_1st = cdrn_psych_hosp_2014_1st.reset_index(drop=True)

    prev_psych_hosp = []
    for _ in cdrn_psych_hosp_2014_1st['person_id']:
        if _ in (set(list(cdrn_psych_hosp_bef_2014['person_id']))):
            prev_psych_hosp.append(1)
        else:
            prev_psych_hosp.append(0)
    print("Length prev_psych_hosp:", len(prev_psych_hosp))

    first_psych_id = pd.DataFrame({"id": prev_psych_hosp})

    # Join the filter first_psych_id['id'] with the analysis file
    cdrn_psych_flag = pd.merge(cdrn_psych_hosp_2014_1st, first_psych_id, left_index=True, right_index=True)
    print("Length cdrn_psych flag:", len(cdrn_psych_flag))

    # Remove Patients that had a previous hospitalization for psychiatric condition
    cdrn_psych_hosp_2014_1st_ = cdrn_psych_flag[cdrn_psych_flag['id'] == 0]

    # cdrn_psych_hosp_2014_1st_ = cdrn_psych_hosp_2014_1st_.drop(cdrn_psych_hosp_2014_1st_.columns[[1,2,3,4]], 
    # axis =1).drop_duplicates()
    print("Number of unique persons who do NOT have a psych hospitalization prior to 2014: ",
          len(cdrn_psych_hosp_2014_1st_), cdrn_psych_hosp_2014_1st_.person_id.nunique())
    pd.DataFrame(cdrn_psych_hosp_2014_1st_).to_csv(
        '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014_1st_.csv', encoding='utf-8')

    # Merges the 2014 psych hospitalization file with the CCS results
    cdrn_1st_psych_dx = pd.merge(cdrn_psych_hosp_2014_1st_, cdrn_ccs_results, how='inner', on='person_id')
    print("Number of unique persons with psych hospitalization and dx / visit history:",
          cdrn_1st_psych_dx.person_id.nunique())
    print("Length of cdrn_1st_psych_dx:", len(cdrn_1st_psych_dx))

    # Filters the resultant df so that only the dx that occurred on or before the first psych hospitalization are 
    # present
    cdrn_1st_psych_dx = cdrn_1st_psych_dx[(cdrn_1st_psych_dx.condition_start_date < cdrn_1st_psych_dx.visit_start_date)]
    print("Number of unique persons with psych hospitalization and dx history < hospitalization date:",
          cdrn_1st_psych_dx.person_id.nunique())

    # ============================================= #
    #
    #     START CREATION OF NO PSYCH HOSP FILE
    #
    # ============================================= #

    # Creates a df of 'person_id' for people who had a psych hospitalization before end of 2014
    cdrn_psych_hosp = cdrn_psych_hosp_2014.person_id.append(cdrn_psych_hosp_bef_2014.person_id).drop_duplicates()

    psych_hosp_list = []
    for _ in cdrn_psych_hosp:
        psych_hosp_list.append(_)

    ids = [1 for i in range(len(psych_hosp_list))]
    psych_id = pd.DataFrame({"person_id": psych_hosp_list, "id": ids})
    cdrn_no_psych_flag = pd.merge(cdrn_ccs_results, psych_id, how='left', on='person_id')

    # Removes patients with a previous psych hospitalization
    cdrn_no_psych_dx = cdrn_no_psych_flag[cdrn_no_psych_flag['id'] != 1]
    print("Number of patients with no psych hospitalizations: ", cdrn_no_psych_dx.person_id.nunique())

    # cdrn_psych_hosp_missing = pd.read_csv(
    # '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_ccs_results.csv', encoding='utf-8')

    # cdrn_no_psych_dx = cdrn_no_psych_dx.drop(cdrn_no_psych_dx.columns[[0, 65]], axis=1)
    cdrn_no_psych_dx = cdrn_no_psych_dx.drop(columns=['Unnamed: 0', 'id'])

    cdrn_1st_psych_dx = cdrn_1st_psych_dx.drop(cdrn_1st_psych_dx.columns[[1, 2, 3, 4, 5]], axis=1)

    # cdrn_psych_hosp_missing = cdrn_psych_hosp_missing.drop(cdrn_psych_hosp_missing.columns[[0]], axis = 1)

    cdrn_psych_dx_all = cdrn_no_psych_dx.append(cdrn_1st_psych_dx, sort=False)
    print("Length cdrn_psych_dx_all: ", len(cdrn_psych_dx_all))

    # cdrn_psych_dx_all = cdrn_psych_dx_all.append(cdrn_psych_hosp_missing, sort=False)
    # print("Length cdrn_psych_dx_all: ",len(cdrn_psych_dx_all_))

    # Converts Longitudinal Data to Aggregate Counts Per Patient
    cdrn_ccs_grouped = cdrn_psych_dx_all.groupby('person_id').agg({"mult_scler": sum, "other_hered_degen": sum, "paralysis": sum, "epilepsy": sum, "headache": sum, "coma": sum, "cataract": sum, "retinopathy": sum, "glaucoma": sum, "blindness": sum, "eye_inflam": sum,"other_eye": sum, "otitis_media": sum, "dizzy": sum, "other_ear_sense": sum, "other_ns_disorder": sum,
    "heart_valve": sum, "peri_endo_carditis": sum, "essential_htn": sum, "htn_w_comp": sum, "acute_mi": sum,
    "coronary_athero": sum, "chest_pain_nos": sum, "pulmonary_hd": sum, "other_heart_disease": sum,
    "conduction": sum, "cardiac_dysrhythm": sum, "cardiac_arrest": sum, "chf": sum, "acute_cvd": sum,
    "occlu_cereb_artery": sum, "other_cvd": sum, "tran_cereb_isch": sum, "late_effect_cvd": sum, "pvd": sum,
    "artery_aneurysm": sum, "artery_embolism": sum, "other_circ": sum, "phlebitis": sum,
    "varicose_vein": sum, "hemorrhoid": sum, "other_vein_lymph": sum, "pneumonia": sum, "influenza": sum,
    "acute_tonsil": sum, "acute_bronch": sum, "upper_resp_infec": sum, "copd": sum, "asthma": sum,
    "asp_pneumonitis": sum, "pneumothorax": sum, "resp_failure": sum, "lung_disease": sum,
    "other_low_resp": sum, "other_up_resp": sum, "intestinal_infec": sum, "teeth_jaw": sum,
    "mouth_disease": sum, "esophagus": sum, "gastro_ulcer": sum, "gastritis": sum, "other_stomach_duo": sum})

    

    pd.DataFrame(cdrn_ccs_grouped).to_csv(output_filepath, encoding='utf-8')
    print("Finished condensing CCS Results 2")
    print("")


def dx_condense3(df):
    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_grouped3.csv'

    cdrn_ccs_results = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results3.csv',encoding='utf-8')
    print("Number of unique person_id in cdrn_ccs_results: ", cdrn_ccs_results.person_id.nunique())

    # Creates var 'hosp_num' which is a successive count of psychiatric hospitalizations per 'person_id' (ascending 
    # order by date)
    # Identifies the first psych hospitalization in 2014, but is not necessarily the first psych hosp ever
    df['hosp_num'] = df.groupby('person_id').visit_start_date.apply(pd.Series.rank)

    # Creates new df where only the first psychiatric hospitalization in 2014 is retained
    cdrn_psych_hosp_2014_1st = df[df['hosp_num'] == 1.0]
    print("Length of psych hospitalization in 2014: ", len(cdrn_psych_hosp_2014_1st))

    # Reset Index
    cdrn_psych_hosp_2014_1st = cdrn_psych_hosp_2014_1st.reset_index(drop=True)

    prev_psych_hosp = []
    for _ in cdrn_psych_hosp_2014_1st['person_id']:
        if _ in (set(list(cdrn_psych_hosp_bef_2014['person_id']))):
            prev_psych_hosp.append(1)
        else:
            prev_psych_hosp.append(0)
    print("Length prev_psych_hosp:", len(prev_psych_hosp))

    first_psych_id = pd.DataFrame({"id": prev_psych_hosp})

    # Join the filter first_psych_id['id'] with the analysis file
    cdrn_psych_flag = pd.merge(cdrn_psych_hosp_2014_1st, first_psych_id, left_index=True, right_index=True)
    print("Length cdrn_psych flag:", len(cdrn_psych_flag))

    # Remove Patients that had a previous hospitalization for psychiatric condition
    cdrn_psych_hosp_2014_1st_ = cdrn_psych_flag[cdrn_psych_flag['id'] == 0]

    # cdrn_psych_hosp_2014_1st_ = cdrn_psych_hosp_2014_1st_.drop(cdrn_psych_hosp_2014_1st_.columns[[1,2,3,4]], 
    # axis =1).drop_duplicates()
    print("Number of unique persons who do NOT have a psych hospitalization prior to 2014: ",len(cdrn_psych_hosp_2014_1st_), cdrn_psych_hosp_2014_1st_.person_id.nunique())
    pd.DataFrame(cdrn_psych_hosp_2014_1st_).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014_1st_.csv', encoding='utf-8')

    # Merges the 2014 psych hospitalization file with the CCS results
    cdrn_1st_psych_dx = pd.merge(cdrn_psych_hosp_2014_1st_, cdrn_ccs_results, how='inner', on='person_id')
    print("Number of unique persons with psych hospitalization and dx / visit history:", cdrn_1st_psych_dx.person_id.nunique())
    print("Length of cdrn_1st_psych_dx:", len(cdrn_1st_psych_dx))

    # Filters the resultant df so that only the dx that occurred on or before the first psych hospitalization are 
    # present
    cdrn_1st_psych_dx = cdrn_1st_psych_dx[(cdrn_1st_psych_dx.condition_start_date < cdrn_1st_psych_dx.visit_start_date)]
    print("Number of unique persons with psych hospitalization and dx history < hospitalization date:",
          cdrn_1st_psych_dx.person_id.nunique())

    # ============================================= #
    #
    #     START CREATION OF NO PSYCH HOSP FILE
    #
    # ============================================= #

    # Creates a df of 'person_id' for people who had a psych hospitalization before end of 2014
    cdrn_psych_hosp = cdrn_psych_hosp_2014.person_id.append(cdrn_psych_hosp_bef_2014.person_id).drop_duplicates()

    psych_hosp_list = []
    for _ in cdrn_psych_hosp:
        psych_hosp_list.append(_)

    ids = [1 for i in range(len(psych_hosp_list))]
    psych_id = pd.DataFrame({"person_id": psych_hosp_list, "id": ids})
    cdrn_no_psych_flag = pd.merge(cdrn_ccs_results, psych_id, how='left', on='person_id')

    # Removes patients with a previous psych hospitalization
    cdrn_no_psych_dx = cdrn_no_psych_flag[cdrn_no_psych_flag['id'] != 1]
    print("Number of patients with no psych hospitalizations: ", cdrn_no_psych_dx.person_id.nunique())

    # cdrn_psych_hosp_missing = pd.read_csv(
    # '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_ccs_results.csv', encoding='utf-8')

    # cdrn_no_psych_dx = cdrn_no_psych_dx.drop(cdrn_no_psych_dx.columns[[0, 65]], axis=1)
    cdrn_no_psych_dx = cdrn_no_psych_dx.drop(columns=['Unnamed: 0', 'id'])

    cdrn_1st_psych_dx = cdrn_1st_psych_dx.drop(cdrn_1st_psych_dx.columns[[1, 2, 3, 4, 5]], axis=1)

    # cdrn_psych_hosp_missing = cdrn_psych_hosp_missing.drop(cdrn_psych_hosp_missing.columns[[0]], axis = 1)

    cdrn_psych_dx_all = cdrn_no_psych_dx.append(cdrn_1st_psych_dx, sort=False)
    print("Length cdrn_psych_dx_all: ", len(cdrn_psych_dx_all))

    # cdrn_psych_dx_all = cdrn_psych_dx_all.append(cdrn_psych_hosp_missing, sort=False)
    # print("Length cdrn_psych_dx_all: ",len(cdrn_psych_dx_all_))

    # Converts Longitudinal Data to Aggregate Counts Per Patient
    cdrn_ccs_grouped = cdrn_psych_dx_all.groupby('person_id').agg({"appendicitis": sum, "hernia_abd": sum, "regional_enteriritis": sum, "intestinal_obstruct": sum,"diverticulitis": sum, "anal_condition": sum, "peritonitis": sum, "biliary_tract": sum,
"other_liver": sum, "pancreatic": sum, "gastro_hemorrhage": sum, "noninfec_gastro": sum,
"other_gastro": sum, "nephritis": sum, "acute_renal_fail": sum, "ckd": sum, "uti": sum,
"calculus_urinary": sum, "other_kidney": sum, "other_bladder": sum, "genitourinary_symp": sum,
"prostate_hyp": sum, "male_genital_inflam": sum, "other_male_genital": sum, "nonmalig_breast": sum,
"inflam_fem_pelvic": sum, "endometriosis": sum, "prolapse_fem_gen": sum, "menstrual": sum,
"ovarian_cyst": sum, "menopausal": sum, "fem_infert": sum, "other_fem_genital": sum,
"contraceptive_mgmt": sum, "spont_abortion": sum, "induce_abortion": sum, "postabort_comp": sum,
"ectopic_preg": sum, "other_comp_preg": sum, "hemorrhage_preg": sum, "htn_comp_preg": sum,
"early_labor": sum, "prolong_preg": sum, "dm_comp_preg": sum, "malposition": sum,
"fetopelvic_disrupt": sum, "prev_c_sect": sum, "fetal_distress": sum, "polyhydramnios": sum,
"umbilical_comp": sum, "ob_trauma": sum, "forceps_deliv": sum, "other_comp_birth": sum,
"other_preg_deliv": sum, "skin_tissue_infec": sum, "other_skin_inflam": sum, "chronic_skin_ulcer": sum,
"other_skin": sum, "infec_arthritis": sum, "rheum_arth": sum, "osteo_arth": sum, "other_joint": sum,
"spondylosis": sum, "osteoporosis": sum, "pathological_fract": sum, "acq_foot_deform": sum,
"other_acq_deform": sum, "systemic_lupus": sum, "other_connective": sum, "other_bone_disease": sum,
"cardiac_congen_anom": sum, "digest_congen_anom": sum, "genito_congen_anom": sum, "ns_congen_anom": sum,
"other_congen_anom": sum, "liveborn": sum, "short_gest": sum, "intrauter_hypoxia": sum,
"resp_distress_synd": sum, "hemolytic_jaundice": sum})

    pd.DataFrame(cdrn_ccs_grouped).to_csv(output_filepath, encoding='utf-8')
    print("Finished condensing CCS Results 3")
    print("")


def dx_condense4(df):
    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_grouped4.csv'

    cdrn_ccs_results = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results4.csv',encoding='utf-8')
    print("Number of unique person_id in cdrn_ccs_results: ", cdrn_ccs_results.person_id.nunique())

    # Creates var 'hosp_num' which is a successive count of psychiatric hospitalizations per 'person_id' (ascending 
    # order by date)
    # Identifies the first psych hospitalization in 2014, but is not necessarily the first psych hosp ever
    df['hosp_num'] = df.groupby('person_id').visit_start_date.apply(pd.Series.rank)

    # Creates new df where only the first psychiatric hospitalization in 2014 is retained
    cdrn_psych_hosp_2014_1st = df[df['hosp_num'] == 1.0]
    print("Length of psych hospitalization in 2014: ", len(cdrn_psych_hosp_2014_1st))

    # Reset Index
    cdrn_psych_hosp_2014_1st = cdrn_psych_hosp_2014_1st.reset_index(drop=True)

    prev_psych_hosp = []
    for _ in cdrn_psych_hosp_2014_1st['person_id']:
        if _ in (set(list(cdrn_psych_hosp_bef_2014['person_id']))):
            prev_psych_hosp.append(1)
        else:
            prev_psych_hosp.append(0)
    print("Length prev_psych_hosp:", len(prev_psych_hosp))

    first_psych_id = pd.DataFrame({"id": prev_psych_hosp})

    # Join the filter first_psych_id['id'] with the analysis file
    cdrn_psych_flag = pd.merge(cdrn_psych_hosp_2014_1st, first_psych_id, left_index=True, right_index=True)
    print("Length cdrn_psych flag:", len(cdrn_psych_flag))

    # Remove Patients that had a previous hospitalization for psychiatric condition
    cdrn_psych_hosp_2014_1st_ = cdrn_psych_flag[cdrn_psych_flag['id'] == 0]

    # cdrn_psych_hosp_2014_1st_ = cdrn_psych_hosp_2014_1st_.drop(cdrn_psych_hosp_2014_1st_.columns[[1,2,3,4]], 
    # axis =1).drop_duplicates()
    print("Number of unique persons who do NOT have a psych hospitalization prior to 2014: ",len(cdrn_psych_hosp_2014_1st_), cdrn_psych_hosp_2014_1st_.person_id.nunique())
    pd.DataFrame(cdrn_psych_hosp_2014_1st_).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014_1st_.csv', encoding='utf-8')

    # Merges the 2014 psych hospitalization file with the CCS results
    cdrn_1st_psych_dx = pd.merge(cdrn_psych_hosp_2014_1st_, cdrn_ccs_results, how='inner', on='person_id')
    print("Number of unique persons with psych hospitalization and dx / visit history:", cdrn_1st_psych_dx.person_id.nunique())
    print("Length of cdrn_1st_psych_dx:", len(cdrn_1st_psych_dx))

    # Filters the resultant df so that only the dx that occurred on or before the first psych hospitalization are 
    # present
    cdrn_1st_psych_dx = cdrn_1st_psych_dx[(cdrn_1st_psych_dx.condition_start_date < cdrn_1st_psych_dx.visit_start_date)]
    print("Number of unique persons with psych hospitalization and dx history < hospitalization date:",
          cdrn_1st_psych_dx.person_id.nunique())

    # ============================================= #
    #
    #     START CREATION OF NO PSYCH HOSP FILE
    #
    # ============================================= #

    # Creates a df of 'person_id' for people who had a psych hospitalization before end of 2014
    cdrn_psych_hosp = cdrn_psych_hosp_2014.person_id.append(cdrn_psych_hosp_bef_2014.person_id).drop_duplicates()

    psych_hosp_list = []
    for _ in cdrn_psych_hosp:
        psych_hosp_list.append(_)

    ids = [1 for i in range(len(psych_hosp_list))]
    psych_id = pd.DataFrame({"person_id": psych_hosp_list, "id": ids})
    cdrn_no_psych_flag = pd.merge(cdrn_ccs_results, psych_id, how='left', on='person_id')

    # Removes patients with a previous psych hospitalization
    cdrn_no_psych_dx = cdrn_no_psych_flag[cdrn_no_psych_flag['id'] != 1]
    print("Number of patients with no psych hospitalizations: ", cdrn_no_psych_dx.person_id.nunique())

    # cdrn_psych_hosp_missing = pd.read_csv(
    # '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_ccs_results.csv', encoding='utf-8')

    # cdrn_no_psych_dx = cdrn_no_psych_dx.drop(cdrn_no_psych_dx.columns[[0, 65]], axis=1)
    cdrn_no_psych_dx = cdrn_no_psych_dx.drop(columns=['Unnamed: 0', 'id'])
    pd.DataFrame(cdrn_no_psych_dx.loc[:,cdrn_no_psych_dx.columns == 'person_id']).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_no_psych_dx.csv', encoding='utf-8')


    cdrn_1st_psych_dx = cdrn_1st_psych_dx.drop(cdrn_1st_psych_dx.columns[[1, 2, 3, 4, 5]], axis=1)

    # cdrn_psych_hosp_missing = cdrn_psych_hosp_missing.drop(cdrn_psych_hosp_missing.columns[[0]], axis = 1)

    cdrn_psych_dx_all = cdrn_no_psych_dx.append(cdrn_1st_psych_dx, sort=False)
    print("Length cdrn_psych_dx_all: ", len(cdrn_psych_dx_all))

    # cdrn_psych_dx_all = cdrn_psych_dx_all.append(cdrn_psych_hosp_missing, sort=False)
    # print("Length cdrn_psych_dx_all: ",len(cdrn_psych_dx_all_))

    # Converts Longitudinal Data to Aggregate Counts Per Patient
    cdrn_ccs_grouped = cdrn_psych_dx_all.groupby('person_id').agg({"birth_trauma": sum, "other_perinatal": sum, "joint_trauma": sum,"fract_femur_neck": sum,"spinal_cord": sum, "skull_face_fract": sum, "upper_limb_fract": sum, "lower_limb_fract": sum,"other_fract": sum, "sprain_strain": sum, "intracranial": sum, "crush_injury": sum,"open_wound_head": sum, "open_wound_extr": sum, "comp_of_device": sum, "comp_surg_proc": sum,"superficial_inj": sum, "burns": sum, "poison_psycho": sum, "poison_other_med": sum,"poison_nonmed": sum, "other_ext_injury": sum, "syncope": sum, "fever_unknown": sum,"lymphadenitis": sum, "gangrene": sum, "shock": sum, "naus_vom": sum, "abdominal_pain": sum,"malaise_fatigue": sum, "allergy": sum, "rehab_care": sum, "admin_admiss": sum, "medical_eval": sum,"other_aftercare": sum, "other_screen": sum, "residual_codes": sum, "adjustment": sum,"anxiety": sum, "adhd": sum, "dementia": sum, "develop_dis": sum, "child_disorder": sum,"impule_control": sum, "mood": sum, "personality": sum, "schizo": sum, "alcohol": sum,"substance": sum, "suicide": sum, "mental_screen": sum, "misc_mental": sum, "e_cut_pierce": sum,"e_drown": sum, "e_fall": sum, "e_fire": sum, "e_firearm": sum, "e_machine": sum, "e_mvt": sum,"e_cyclist": sum, "e_pedestrian": sum, "e_transport": sum, "e_natural": sum, "e_overexert": sum,"e_poison": sum, "e_struckby": sum, "e_suffocate": sum, "e_ae_med_care": sum, "e_ae_med_drug": sum,"e_other_class": sum, "e_other_nec": sum, "e_unspecified": sum, "e_place": sum})

    pd.DataFrame(cdrn_ccs_grouped).to_csv(output_filepath, encoding='utf-8')
    print("Finished condensing CCS Results 4")
    print("")

# dx_condense1(cdrn_psych_hosp_2014)

# dx_condense2(cdrn_psych_hosp_2014)

# dx_condense3(cdrn_psych_hosp_2014)

dx_condense4(cdrn_psych_hosp_2014)



# ========================================================================= #
#
#     START CREATION OF 2014 UTILIZATION METRICS FOR PSYCH HOSP PTS
#
# ========================================================================= #

cdrn_psych_hosp_2014_1st_ = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014_1st_.csv', encoding='utf-8')
cdrn_no_psych_dx = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_no_psych_dx.csv', encoding='utf-8')

cdrn_hosp_util_2014 = pd.merge(cdrn_psych_hosp_2014_1st_.drop(cdrn_psych_hosp_2014_1st_.columns[[0,3,4,5]], axis=1),
                               cdrn_all_visits_2014, how='left', on='person_id')

cdrn_hosp_util_2014 = cdrn_hosp_util_2014[(cdrn_hosp_util_2014.condition_start_date < cdrn_hosp_util_2014.visit_start_date)]

cdrn_no_hosp_util_2014 = pd.merge(cdrn_no_psych_dx.drop(cdrn_no_psych_dx.columns[0], axis =1).drop_duplicates(),
                                  cdrn_all_visits_2014, how='left', on='person_id').fillna(0)

util2014 = {"person_id": [], "ed2014": [], "inpt_2014":[], "outpt_2014": [], "amb_2014": [], "other_2014": []}


def util_convert(df):
    output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_2014_util_vars_psych.csv'

    for _ in df['person_id']:
        util2014["person_id"].append(_)

    # ED Utilization 2014
    for _ in df['visit_type']:
        if _ == 9203:
            util2014["ed2014"].append(1)
        else:
            util2014["ed2014"].append(0)
    print("Completed Binary Recoding of: Emergency Department Visit 2014")

    # Inpatient Hospitalization Utilization 2014
    for _ in df['visit_type']:
        if _ == 9201:
            util2014["inpt_2014"].append(1)
        else:
            util2014["inpt_2014"].append(0)
    print("Completed Binary Recoding of: Inpatient Hospitalization 2014")

    # Outpatient Visit Utilization 2014
    for _ in df['visit_type']:
        if _ == 9202:
            util2014["outpt_2014"].append(1)
        else:
            util2014["outpt_2014"].append(0)
    print("Completed Binary Recoding of: Outpatient Visit Utilization 2014")

    # Other Ambulatory Visit Utilization 2014
    for _ in df['visit_type']:
        if _ == 44814711:
            util2014["amb_2014"].append(1)
        else:
            util2014["amb_2014"].append(0)
    print("Completed Binary Recoding of: Other Ambulatory Visit Utilization 2014")

    # Other Visit Utilization 2014
    for _ in df['visit_type']:
        if _ == 44814649:
            util2014["other_2014"].append(1)
        else:
            util2014["other_2014"].append(0)
    print("Completed Binary Recoding of: Other Visit Utilization 2014")

    pd.DataFrame(util2014).to_csv(output_filepath2, encoding='utf-8')


util_convert(cdrn_hosp_util_2014)

util_convert(cdrn_no_hosp_util_2014)

util2014_ = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_2014_util_vars_psych.csv', encoding='utf-8')

# Converts Longitudinal Data to Aggregate Counts Per Patient
cdrn_util2014_grouped = util2014_.groupby('person_id').agg({"ed2014":sum, "inpt_2014":sum, "outpt_2014":sum, "amb_2014":sum, "other_2014":sum})

pd.DataFrame(cdrn_util2014_grouped).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_util2014_psych_grouped.csv', encoding='utf-8')
