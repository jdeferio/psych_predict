import pandas as pd
import datetime as dt

cdrn_dx = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_individual_dx_1215.csv',encoding='utf-8',names=["person_id","condition_start_date","condition_source_value"])
print("Number of records in cdrn_dx: ", len(cdrn_dx))
print("Number of patients in cdrn_dx: ", cdrn_dx.person_id.nunique())

cdrn_all_individual_visits = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_individual_visits.csv', encoding='utf-8', names=['person_id'])
print("Number of records in cdrn_all_individual_visits: ", len(cdrn_all_individual_visits))
print("Number of patients in cdrn_all_individual_visits: ", cdrn_all_individual_visits.person_id.nunique())


# Reset the Index
cdrn_all_individual_visits = cdrn_all_individual_visits.reset_index(drop=True)

missing_dx_hist = {"missing_dx":[]}
dx_hist_included = set(list(cdrn_dx.person_id.values))
for _ in cdrn_all_individual_visits['person_id']:
    if _ in dx_hist_included:
        missing_dx_hist["missing_dx"].append(0)
    else: missing_dx_hist["missing_dx"].append(1)

print("cdrn_all_individual_visits length: ", len(cdrn_all_individual_visits))
print("missing_dx_hist length: ", len(missing_dx_hist["missing_dx"]))

# Creates DataFrame of the List
missing_dx_hist_df = pd.DataFrame({"missing_dx":missing_dx_hist["missing_dx"]})
print("Number of patients with missing dx history: ", missing_dx_hist_df.sum())

# Merges df psych_missing with the visits
cdrn_all_individual_visits_edit = pd.merge(cdrn_all_individual_visits, missing_dx_hist_df, left_index=True, right_index=True)

# Removes Patient Records Whom Have A Diagnosis History
cdrn_all_individual_visits_nodx = cdrn_all_individual_visits_edit[cdrn_all_individual_visits_edit['missing_dx'] == 1]
print("Patients missing Dx history but meet visit criteria: ", len(cdrn_all_individual_visits_nodx))


def dx_convert1(df):

    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results1.csv'

    # Establish the CCS Results Dictionary
    results_ccs1 = {"person_id": [], "condition_start_date": [], "tuberculosis": [], "septic": [], "bact_infec": [],
                    "mycoses": [], "hiv": [], "hepatitis": [], "viral_infec": [], "other_infec": [], "sti": [],
                    "screen_infec": [], "head_ca": [], "esophagus_ca": [], "stomach_ca": [], "colon_ca": [],
                    "rectum_ca": [], "liver_ca": [], "pancreas_ca": [], "gi_ca": [], "lung_ca": [], "resp_ca": [],
                    "bone_ca": [], "melanoma": [], "nonepi_skin_ca": [], "breast_ca": [], "uterus_ca": [],
                    "cervix_ca": [], "ovary_ca": [], "fem_genital_ca": [], "prostate_ca": [], "testes_ca": [],
                    "male_genital_ca": [], "bladder_ca": [], "kidney_ca": [], "urinary_ca": [], "brain_ca": [],
                    "thyroid_ca": [], "hodgkins_lymph": [], "non_hodgkins_lymph": [], "leukemia": [],
                    "mult_myeloma": [], "other_ca": [], "secndry_malig": [], "malig_neoplasm": [],
                    "neoplasm_unspec": [], "maint_chemo": [], "ben_neoplasm_uterus": [], "other_ben_neoplasm": [],
                    "thyroid": [], "dm_wo_comp": [], "dm_w_comp": [], "other_endocrine": [], "nutrition": [],
                    "lipid_metabo": [], "gout": [], "fluid_electrolyte": [], "cyst_fibrosis": [], "immunity": [],
                    "other_metabo": [], "other_anemia": [], "post_hemorr_anemia": [], "sickle_cell": [],
                    "coag_anemia": [], "wbc_disease": [], "other_heme": [], "meningitis_notb": [],
                    "encephalitis_notb": [], "other_cns": [], "parkinsons": []}

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs1["person_id"].append(_)
    print("Number of person_id with missing dx history: ", len(results_ccs1["person_id"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs1["condition_start_date"].append(dt.datetime.strptime('12/31/13', "%m/%d/%y"))
    print("Number of start dates added for patients with missing dx history: ",
          len(results_ccs1["condition_start_date"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs1["tuberculosis"].append(0)
        results_ccs1["septic"].append(0)
        results_ccs1["bact_infec"].append(0)
        results_ccs1["mycoses"].append(0)
        results_ccs1["hiv"].append(0)
        results_ccs1["hepatitis"].append(0)
        results_ccs1["viral_infec"].append(0)
        results_ccs1["other_infec"].append(0)
        results_ccs1["sti"].append(0)
        results_ccs1["screen_infec"].append(0)
        results_ccs1["head_ca"].append(0)
        results_ccs1["esophagus_ca"].append(0)
        results_ccs1["stomach_ca"].append(0)
        results_ccs1["colon_ca"].append(0)
        results_ccs1["rectum_ca"].append(0)
        results_ccs1["liver_ca"].append(0)
        results_ccs1["pancreas_ca"].append(0)
        results_ccs1["gi_ca"].append(0)
        results_ccs1["lung_ca"].append(0)
        results_ccs1["resp_ca"].append(0)
        results_ccs1["bone_ca"].append(0)
        results_ccs1["melanoma"].append(0)
        results_ccs1["nonepi_skin_ca"].append(0)
        results_ccs1["breast_ca"].append(0)
        results_ccs1["uterus_ca"].append(0)
        results_ccs1["cervix_ca"].append(0)
        results_ccs1["ovary_ca"].append(0)
        results_ccs1["fem_genital_ca"].append(0)
        results_ccs1["prostate_ca"].append(0)
        results_ccs1["testes_ca"].append(0)
        results_ccs1["male_genital_ca"].append(0)
        results_ccs1["bladder_ca"].append(0)
        results_ccs1["kidney_ca"].append(0)
        results_ccs1["urinary_ca"].append(0)
        results_ccs1["brain_ca"].append(0)
        results_ccs1["thyroid_ca"].append(0)
        results_ccs1["hodgkins_lymph"].append(0)
        results_ccs1["non_hodgkins_lymph"].append(0)
        results_ccs1["leukemia"].append(0)
        results_ccs1["mult_myeloma"].append(0)
        results_ccs1["other_ca"].append(0)
        results_ccs1["secndry_malig"].append(0)
        results_ccs1["malig_neoplasm"].append(0)
        results_ccs1["neoplasm_unspec"].append(0)
        results_ccs1["maint_chemo"].append(0)
        results_ccs1["ben_neoplasm_uterus"].append(0)
        results_ccs1["other_ben_neoplasm"].append(0)
        results_ccs1["thyroid"].append(0)
        results_ccs1["dm_wo_comp"].append(0)
        results_ccs1["dm_w_comp"].append(0)
        results_ccs1["other_endocrine"].append(0)
        results_ccs1["nutrition"].append(0)
        results_ccs1["lipid_metabo"].append(0)
        results_ccs1["gout"].append(0)
        results_ccs1["fluid_electrolyte"].append(0)
        results_ccs1["cyst_fibrosis"].append(0)
        results_ccs1["immunity"].append(0)
        results_ccs1["other_metabo"].append(0)
        results_ccs1["other_anemia"].append(0)
        results_ccs1["post_hemorr_anemia"].append(0)
        results_ccs1["sickle_cell"].append(0)
        results_ccs1["coag_anemia"].append(0)
        results_ccs1["wbc_disease"].append(0)
        results_ccs1["other_heme"].append(0)
        results_ccs1["meningitis_notb"].append(0)
        results_ccs1["encephalitis_notb"].append(0)
        results_ccs1["other_cns"].append(0)
        results_ccs1["parkinsons"].append(0)
    print("Completed null dx recode for pts that are missing dx but meet visit criteria")

    for _ in df['person_id']:
        results_ccs1["person_id"].append(_)
    print("Number of patients in results_ccs1", len(results_ccs1["person_id"]))

    for _ in df['condition_start_date']:
        results_ccs1["condition_start_date"].append(_)
    print("Number of start dates in results_ccs1", len(results_ccs1["condition_start_date"]))

    # Tuberculosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:010.00', 'ICD9CM:010.01', 'ICD9CM:010.02', 'ICD9CM:010.03', 'ICD9CM:010.04', 'ICD9CM:010.05', 'ICD9CM:010.06', 'ICD9CM:010.10', 'ICD9CM:010.11', 'ICD9CM:010.12', 'ICD9CM:010.13', 'ICD9CM:010.14', 'ICD9CM:010.15', 'ICD9CM:010.16', 'ICD9CM:010.80', 'ICD9CM:010.81', 'ICD9CM:010.82', 'ICD9CM:010.83', 'ICD9CM:010.84', 'ICD9CM:010.85', 'ICD9CM:010.86', 'ICD9CM:010.90', 'ICD9CM:010.91', 'ICD9CM:010.92', 'ICD9CM:010.93', 'ICD9CM:010.94', 'ICD9CM:010.95', 'ICD9CM:010.96', 'ICD9CM:011.00', 'ICD9CM:011.01', 'ICD9CM:011.02', 'ICD9CM:011.03', 'ICD9CM:011.04', 'ICD9CM:011.05', 'ICD9CM:011.06', 'ICD9CM:011.10', 'ICD9CM:011.11', 'ICD9CM:011.12', 'ICD9CM:011.13', 'ICD9CM:011.14', 'ICD9CM:011.15', 'ICD9CM:011.16', 'ICD9CM:011.20', 'ICD9CM:011.21', 'ICD9CM:011.22', 'ICD9CM:011.23', 'ICD9CM:011.24', 'ICD9CM:011.25', 'ICD9CM:011.26', 'ICD9CM:011.30', 'ICD9CM:011.31', 'ICD9CM:011.32', 'ICD9CM:011.33', 'ICD9CM:011.34', 'ICD9CM:011.35', 'ICD9CM:011.36', 'ICD9CM:011.40', 'ICD9CM:011.41', 'ICD9CM:011.42', 'ICD9CM:011.43', 'ICD9CM:011.44', 'ICD9CM:011.45', 'ICD9CM:011.46', 'ICD9CM:011.50', 'ICD9CM:011.51', 'ICD9CM:011.52', 'ICD9CM:011.53', 'ICD9CM:011.54', 'ICD9CM:011.55', 'ICD9CM:011.56', 'ICD9CM:011.60', 'ICD9CM:011.61', 'ICD9CM:011.62', 'ICD9CM:011.63', 'ICD9CM:011.64', 'ICD9CM:011.65', 'ICD9CM:011.66', 'ICD9CM:011.70', 'ICD9CM:011.71', 'ICD9CM:011.72', 'ICD9CM:011.73', 'ICD9CM:011.74', 'ICD9CM:011.75', 'ICD9CM:011.76', 'ICD9CM:011.80', 'ICD9CM:011.81', 'ICD9CM:011.82', 'ICD9CM:011.83', 'ICD9CM:011.84', 'ICD9CM:011.85', 'ICD9CM:011.86', 'ICD9CM:011.90', 'ICD9CM:011.91', 'ICD9CM:011.92', 'ICD9CM:011.93', 'ICD9CM:011.94', 'ICD9CM:011.95', 'ICD9CM:011.96', 'ICD9CM:012.00', 'ICD9CM:012.01', 'ICD9CM:012.02', 'ICD9CM:012.03', 'ICD9CM:012.04', 'ICD9CM:012.05', 'ICD9CM:012.06', 'ICD9CM:012.10', 'ICD9CM:012.11', 'ICD9CM:012.12', 'ICD9CM:012.13', 'ICD9CM:012.14', 'ICD9CM:012.15', 'ICD9CM:012.16', 'ICD9CM:012.20', 'ICD9CM:012.21', 'ICD9CM:012.22', 'ICD9CM:012.23', 'ICD9CM:012.24', 'ICD9CM:012.25', 'ICD9CM:012.26', 'ICD9CM:012.30', 'ICD9CM:012.31', 'ICD9CM:012.32', 'ICD9CM:012.33', 'ICD9CM:012.34', 'ICD9CM:012.35', 'ICD9CM:012.36', 'ICD9CM:012.80', 'ICD9CM:012.81', 'ICD9CM:012.82', 'ICD9CM:012.83', 'ICD9CM:012.84', 'ICD9CM:012.85', 'ICD9CM:012.86', 'ICD9CM:013.00', 'ICD9CM:013.01', 'ICD9CM:013.02', 'ICD9CM:013.03', 'ICD9CM:013.04', 'ICD9CM:013.05', 'ICD9CM:013.06', 'ICD9CM:013.10', 'ICD9CM:013.11', 'ICD9CM:013.12', 'ICD9CM:013.13', 'ICD9CM:013.14', 'ICD9CM:013.15', 'ICD9CM:013.16', 'ICD9CM:013.20', 'ICD9CM:013.21', 'ICD9CM:013.22', 'ICD9CM:013.23', 'ICD9CM:013.24', 'ICD9CM:013.25', 'ICD9CM:013.26', 'ICD9CM:013.30', 'ICD9CM:013.31', 'ICD9CM:013.32', 'ICD9CM:013.33', 'ICD9CM:013.34', 'ICD9CM:013.35', 'ICD9CM:013.36', 'ICD9CM:013.40', 'ICD9CM:013.41', 'ICD9CM:013.42', 'ICD9CM:013.43', 'ICD9CM:013.44', 'ICD9CM:013.45', 'ICD9CM:013.46', 'ICD9CM:013.50', 'ICD9CM:013.51', 'ICD9CM:013.52', 'ICD9CM:013.53', 'ICD9CM:013.54', 'ICD9CM:013.55', 'ICD9CM:013.56', 'ICD9CM:013.60', 'ICD9CM:013.61', 'ICD9CM:013.62', 'ICD9CM:013.63', 'ICD9CM:013.64', 'ICD9CM:013.65', 'ICD9CM:013.66', 'ICD9CM:013.80', 'ICD9CM:013.81', 'ICD9CM:013.82', 'ICD9CM:013.83', 'ICD9CM:013.84', 'ICD9CM:013.85', 'ICD9CM:013.86', 'ICD9CM:013.90', 'ICD9CM:013.91', 'ICD9CM:013.92', 'ICD9CM:013.93', 'ICD9CM:013.94', 'ICD9CM:013.95', 'ICD9CM:013.96', 'ICD9CM:014.00', 'ICD9CM:014.01', 'ICD9CM:014.02', 'ICD9CM:014.03', 'ICD9CM:014.04', 'ICD9CM:014.05', 'ICD9CM:014.06', 'ICD9CM:014.80', 'ICD9CM:014.81', 'ICD9CM:014.82', 'ICD9CM:014.83', 'ICD9CM:014.84', 'ICD9CM:014.85', 'ICD9CM:014.86', 'ICD9CM:015.00', 'ICD9CM:015.01', 'ICD9CM:015.02', 'ICD9CM:015.03', 'ICD9CM:015.04', 'ICD9CM:015.05', 'ICD9CM:015.06', 'ICD9CM:015.10', 'ICD9CM:015.11', 'ICD9CM:015.12', 'ICD9CM:015.13', 'ICD9CM:015.14', 'ICD9CM:015.15', 'ICD9CM:015.16', 'ICD9CM:015.20', 'ICD9CM:015.21', 'ICD9CM:015.22', 'ICD9CM:015.23', 'ICD9CM:015.24', 'ICD9CM:015.25', 'ICD9CM:015.26', 'ICD9CM:015.50', 'ICD9CM:015.51', 'ICD9CM:015.52', 'ICD9CM:015.53', 'ICD9CM:015.54', 'ICD9CM:015.55', 'ICD9CM:015.56', 'ICD9CM:015.60', 'ICD9CM:015.61', 'ICD9CM:015.62', 'ICD9CM:015.63', 'ICD9CM:015.64', 'ICD9CM:015.65', 'ICD9CM:015.66', 'ICD9CM:015.70', 'ICD9CM:015.71', 'ICD9CM:015.72', 'ICD9CM:015.73', 'ICD9CM:015.74', 'ICD9CM:015.75', 'ICD9CM:015.76', 'ICD9CM:015.80', 'ICD9CM:015.81', 'ICD9CM:015.82', 'ICD9CM:015.83', 'ICD9CM:015.84', 'ICD9CM:015.85', 'ICD9CM:015.86', 'ICD9CM:015.90', 'ICD9CM:015.91', 'ICD9CM:015.92', 'ICD9CM:015.93', 'ICD9CM:015.94', 'ICD9CM:015.95', 'ICD9CM:015.96', 'ICD9CM:016.00', 'ICD9CM:016.01', 'ICD9CM:016.02', 'ICD9CM:016.03', 'ICD9CM:016.04', 'ICD9CM:016.05', 'ICD9CM:016.06', 'ICD9CM:016.10', 'ICD9CM:016.11', 'ICD9CM:016.12', 'ICD9CM:016.13', 'ICD9CM:016.14', 'ICD9CM:016.15', 'ICD9CM:016.16', 'ICD9CM:016.20', 'ICD9CM:016.21', 'ICD9CM:016.22', 'ICD9CM:016.23', 'ICD9CM:016.24', 'ICD9CM:016.25', 'ICD9CM:016.26', 'ICD9CM:016.30', 'ICD9CM:016.31', 'ICD9CM:016.32', 'ICD9CM:016.33', 'ICD9CM:016.34', 'ICD9CM:016.35', 'ICD9CM:016.36', 'ICD9CM:016.40', 'ICD9CM:016.41', 'ICD9CM:016.42', 'ICD9CM:016.43', 'ICD9CM:016.44', 'ICD9CM:016.45', 'ICD9CM:016.46', 'ICD9CM:016.50', 'ICD9CM:016.51', 'ICD9CM:016.52', 'ICD9CM:016.53', 'ICD9CM:016.54', 'ICD9CM:016.55', 'ICD9CM:016.56', 'ICD9CM:016.60', 'ICD9CM:016.61', 'ICD9CM:016.62', 'ICD9CM:016.63', 'ICD9CM:016.64', 'ICD9CM:016.65', 'ICD9CM:016.66', 'ICD9CM:016.70', 'ICD9CM:016.71', 'ICD9CM:016.72', 'ICD9CM:016.73', 'ICD9CM:016.74', 'ICD9CM:016.75', 'ICD9CM:016.76', 'ICD9CM:016.90', 'ICD9CM:016.91', 'ICD9CM:016.92', 'ICD9CM:016.93', 'ICD9CM:016.94', 'ICD9CM:016.95', 'ICD9CM:016.96', 'ICD9CM:017.00', 'ICD9CM:017.01', 'ICD9CM:017.02', 'ICD9CM:017.03', 'ICD9CM:017.04', 'ICD9CM:017.05', 'ICD9CM:017.06', 'ICD9CM:017.10', 'ICD9CM:017.11', 'ICD9CM:017.12', 'ICD9CM:017.13', 'ICD9CM:017.14', 'ICD9CM:017.15', 'ICD9CM:017.16', 'ICD9CM:017.20', 'ICD9CM:017.21', 'ICD9CM:017.22', 'ICD9CM:017.23', 'ICD9CM:017.24', 'ICD9CM:017.25', 'ICD9CM:017.26', 'ICD9CM:017.30', 'ICD9CM:017.31', 'ICD9CM:017.32', 'ICD9CM:017.33', 'ICD9CM:017.34', 'ICD9CM:017.35', 'ICD9CM:017.36', 'ICD9CM:017.40', 'ICD9CM:017.41', 'ICD9CM:017.42', 'ICD9CM:017.43', 'ICD9CM:017.44', 'ICD9CM:017.45', 'ICD9CM:017.46', 'ICD9CM:017.50', 'ICD9CM:017.51', 'ICD9CM:017.52', 'ICD9CM:017.53', 'ICD9CM:017.54', 'ICD9CM:017.55', 'ICD9CM:017.56', 'ICD9CM:017.60', 'ICD9CM:017.61', 'ICD9CM:017.62', 'ICD9CM:017.63', 'ICD9CM:017.64', 'ICD9CM:017.65', 'ICD9CM:017.66', 'ICD9CM:017.70', 'ICD9CM:017.71', 'ICD9CM:017.72', 'ICD9CM:017.73', 'ICD9CM:017.74', 'ICD9CM:017.75', 'ICD9CM:017.76', 'ICD9CM:017.80', 'ICD9CM:017.81', 'ICD9CM:017.82', 'ICD9CM:017.83', 'ICD9CM:017.84', 'ICD9CM:017.85', 'ICD9CM:017.86', 'ICD9CM:017.90', 'ICD9CM:017.91', 'ICD9CM:017.92', 'ICD9CM:017.93', 'ICD9CM:017.94', 'ICD9CM:017.95', 'ICD9CM:017.96', 'ICD9CM:018.00', 'ICD9CM:018.01', 'ICD9CM:018.02', 'ICD9CM:018.03', 'ICD9CM:018.04', 'ICD9CM:018.05', 'ICD9CM:018.06', 'ICD9CM:018.80', 'ICD9CM:018.81', 'ICD9CM:018.82', 'ICD9CM:018.83', 'ICD9CM:018.84', 'ICD9CM:018.85', 'ICD9CM:018.86', 'ICD9CM:018.90', 'ICD9CM:018.91', 'ICD9CM:018.92', 'ICD9CM:018.93', 'ICD9CM:018.94', 'ICD9CM:018.95', 'ICD9CM:018.96', 'ICD9CM:137.0', 'ICD9CM:137.1', 'ICD9CM:137.2', 'ICD9CM:137.3', 'ICD9CM:137.4', 'ICD9CM:V12.01'):
            results_ccs1["tuberculosis"].append(1)
        else: results_ccs1["tuberculosis"].append(0)
    print("Completed Binary Recode of: Tuberculosis")

    # Septicemia_(_except_in_labor)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:003.1', 'ICD9CM:020.2', 'ICD9CM:022.3', 'ICD9CM:036.2', 'ICD9CM:038.0', 'ICD9CM:038.1', 'ICD9CM:038.10', 'ICD9CM:038.11', 'ICD9CM:038.12', 'ICD9CM:038.19', 'ICD9CM:038.2', 'ICD9CM:038.3', 'ICD9CM:038.40', 'ICD9CM:038.41', 'ICD9CM:038.42', 'ICD9CM:038.43', 'ICD9CM:038.44', 'ICD9CM:038.49', 'ICD9CM:038.8', 'ICD9CM:038.9', 'ICD9CM:054.5', 'ICD9CM:449', 'ICD9CM:771.81', 'ICD9CM:790.7', 'ICD9CM:995.91', 'ICD9CM:995.92'):
            results_ccs1["septic"].append(1)
        else: results_ccs1["septic"].append(0)
    print("Completed Binary Recode of: Septicemia_(_except_in_labor)")

    # Bacterial_infection;_unspecified_site
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:020.0', 'ICD9CM:020.8', 'ICD9CM:020.9', 'ICD9CM:021.8', 'ICD9CM:021.9', 'ICD9CM:022.8', 'ICD9CM:022.9', 'ICD9CM:023.0', 'ICD9CM:023.1', 'ICD9CM:023.2', 'ICD9CM:023.3', 'ICD9CM:023.8', 'ICD9CM:023.9', 'ICD9CM:024', 'ICD9CM:025', 'ICD9CM:026.0', 'ICD9CM:026.9', 'ICD9CM:027.0', 'ICD9CM:027.1', 'ICD9CM:027.2', 'ICD9CM:027.8', 'ICD9CM:027.9', 'ICD9CM:030.0', 'ICD9CM:030.1', 'ICD9CM:030.2', 'ICD9CM:030.3', 'ICD9CM:030.8', 'ICD9CM:030.9', 'ICD9CM:031.2', 'ICD9CM:031.8', 'ICD9CM:031.9', 'ICD9CM:032.89', 'ICD9CM:032.9', 'ICD9CM:033.0', 'ICD9CM:033.1', 'ICD9CM:033.8', 'ICD9CM:033.9', 'ICD9CM:034.1', 'ICD9CM:036.3', 'ICD9CM:036.81', 'ICD9CM:036.89', 'ICD9CM:036.9', 'ICD9CM:037', 'ICD9CM:039.2', 'ICD9CM:039.3', 'ICD9CM:039.4', 'ICD9CM:039.8', 'ICD9CM:039.9', 'ICD9CM:040.0', 'ICD9CM:040.1', 'ICD9CM:040.2', 'ICD9CM:040.3', 'ICD9CM:040.42', 'ICD9CM:040.81', 'ICD9CM:040.82', 'ICD9CM:040.89', 'ICD9CM:041.0', 'ICD9CM:041.00', 'ICD9CM:041.01', 'ICD9CM:041.02', 'ICD9CM:041.03', 'ICD9CM:041.04', 'ICD9CM:041.05', 'ICD9CM:041.09', 'ICD9CM:041.1', 'ICD9CM:041.10', 'ICD9CM:041.11', 'ICD9CM:041.12', 'ICD9CM:041.19', 'ICD9CM:041.2', 'ICD9CM:041.3', 'ICD9CM:041.4', 'ICD9CM:041.41', 'ICD9CM:041.42', 'ICD9CM:041.43', 'ICD9CM:041.49', 'ICD9CM:041.5', 'ICD9CM:041.6', 'ICD9CM:041.7', 'ICD9CM:041.8', 'ICD9CM:041.81', 'ICD9CM:041.82', 'ICD9CM:041.83', 'ICD9CM:041.84', 'ICD9CM:041.85', 'ICD9CM:041.86', 'ICD9CM:041.89', 'ICD9CM:041.9', 'ICD9CM:390', 'ICD9CM:392.9', 'ICD9CM:795.3', 'ICD9CM:795.31', 'ICD9CM:795.39', 'ICD9CM:V09.0', 'ICD9CM:V09.1', 'ICD9CM:V09.2', 'ICD9CM:V09.3', 'ICD9CM:V09.4', 'ICD9CM:V09.50', 'ICD9CM:V09.51', 'ICD9CM:V09.6', 'ICD9CM:V09.70', 'ICD9CM:V09.71', 'ICD9CM:V09.80', 'ICD9CM:V09.81', 'ICD9CM:V09.90', 'ICD9CM:V09.91', 'ICD9CM:V12.04'):
            results_ccs1["bact_infec"].append(1)
        else: results_ccs1["bact_infec"].append(0)
    print("Completed Binary Recode of: bact_infec")

    # Mycoses
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:110.0', 'ICD9CM:110.1', 'ICD9CM:110.2', 'ICD9CM:110.3', 'ICD9CM:110.4', 'ICD9CM:110.5', 'ICD9CM:110.6', 'ICD9CM:110.8', 'ICD9CM:110.9', 'ICD9CM:111.0', 'ICD9CM:111.1', 'ICD9CM:111.2', 'ICD9CM:111.3', 'ICD9CM:111.8', 'ICD9CM:111.9', 'ICD9CM:112.0', 'ICD9CM:112.1', 'ICD9CM:112.2', 'ICD9CM:112.3', 'ICD9CM:112.5', 'ICD9CM:112.82', 'ICD9CM:112.84', 'ICD9CM:112.85', 'ICD9CM:112.89', 'ICD9CM:112.9', 'ICD9CM:114.1', 'ICD9CM:114.3', 'ICD9CM:114.9', 'ICD9CM:115.00', 'ICD9CM:115.09', 'ICD9CM:115.10', 'ICD9CM:115.19', 'ICD9CM:115.90', 'ICD9CM:115.99', 'ICD9CM:116.0', 'ICD9CM:116.1', 'ICD9CM:116.2', 'ICD9CM:117.0', 'ICD9CM:117.1', 'ICD9CM:117.2', 'ICD9CM:117.3', 'ICD9CM:117.4', 'ICD9CM:117.5', 'ICD9CM:117.6', 'ICD9CM:117.7', 'ICD9CM:117.8', 'ICD9CM:117.9', 'ICD9CM:118'):
            results_ccs1["mycoses"].append(1)
        else: results_ccs1["mycoses"].append(0)
    print("Completed Binary Recode of: mycoses")

    # HIV_infection
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:042', 'ICD9CM:042.0', 'ICD9CM:042.1', 'ICD9CM:042.2', 'ICD9CM:042.9', 'ICD9CM:043.0', 'ICD9CM:043.1', 'ICD9CM:043.2', 'ICD9CM:043.3', 'ICD9CM:043.9', 'ICD9CM:044.0', 'ICD9CM:044.9', 'ICD9CM:079.53', 'ICD9CM:279.10', 'ICD9CM:279.19', 'ICD9CM:795.71', 'ICD9CM:795.8', 'ICD9CM:V08'):
            results_ccs1["hiv"].append(1)
        else: results_ccs1["hiv"].append(0)
    print("Completed Binary Recode of: hiv")

    # Hepatitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:070.0', 'ICD9CM:070.1', 'ICD9CM:070.2', 'ICD9CM:070.20', 'ICD9CM:070.21', 'ICD9CM:070.22', 'ICD9CM:070.23', 'ICD9CM:070.3', 'ICD9CM:070.30', 'ICD9CM:070.31', 'ICD9CM:070.32', 'ICD9CM:070.33', 'ICD9CM:070.4', 'ICD9CM:070.41', 'ICD9CM:070.42', 'ICD9CM:070.43', 'ICD9CM:070.44', 'ICD9CM:070.49', 'ICD9CM:070.5', 'ICD9CM:070.51', 'ICD9CM:070.52', 'ICD9CM:070.53', 'ICD9CM:070.54', 'ICD9CM:070.59', 'ICD9CM:070.6', 'ICD9CM:070.70', 'ICD9CM:070.71', 'ICD9CM:070.9', 'ICD9CM:072.71', 'ICD9CM:571.40', 'ICD9CM:571.41', 'ICD9CM:571.42', 'ICD9CM:571.49', 'ICD9CM:573.1', 'ICD9CM:573.2', 'ICD9CM:573.3'):
            results_ccs1["hepatitis"].append(1)
        else: results_ccs1["hepatitis"].append(0)
    print("Completed Binary Recode of: hepatitis")

    # Viral_infection
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:050.0', 'ICD9CM:050.1', 'ICD9CM:050.2', 'ICD9CM:050.9', 'ICD9CM:051.0', 'ICD9CM:051.01', 'ICD9CM:051.02', 'ICD9CM:051.1', 'ICD9CM:051.2', 'ICD9CM:051.9', 'ICD9CM:052.2', 'ICD9CM:052.7', 'ICD9CM:052.8', 'ICD9CM:052.9', 'ICD9CM:053.10', 'ICD9CM:053.11', 'ICD9CM:053.12', 'ICD9CM:053.13', 'ICD9CM:053.14', 'ICD9CM:053.19', 'ICD9CM:053.71', 'ICD9CM:053.79', 'ICD9CM:053.8', 'ICD9CM:053.9', 'ICD9CM:054.0', 'ICD9CM:054.10', 'ICD9CM:054.11', 'ICD9CM:054.12', 'ICD9CM:054.13', 'ICD9CM:054.19', 'ICD9CM:054.2', 'ICD9CM:054.6', 'ICD9CM:054.71', 'ICD9CM:054.73', 'ICD9CM:054.74', 'ICD9CM:054.79', 'ICD9CM:054.8', 'ICD9CM:054.9', 'ICD9CM:055.79', 'ICD9CM:055.8', 'ICD9CM:055.9', 'ICD9CM:056.00', 'ICD9CM:056.09', 'ICD9CM:056.79', 'ICD9CM:056.8', 'ICD9CM:056.9', 'ICD9CM:057.0', 'ICD9CM:057.8', 'ICD9CM:057.9', 'ICD9CM:058.10', 'ICD9CM:058.11', 'ICD9CM:058.12', 'ICD9CM:058.81', 'ICD9CM:058.82', 'ICD9CM:058.89', 'ICD9CM:059.00', 'ICD9CM:059.01', 'ICD9CM:059.09', 'ICD9CM:059.10', 'ICD9CM:059.11', 'ICD9CM:059.12', 'ICD9CM:059.19', 'ICD9CM:059.20', 'ICD9CM:059.21', 'ICD9CM:059.22', 'ICD9CM:059.8', 'ICD9CM:059.9', 'ICD9CM:060.0', 'ICD9CM:060.1', 'ICD9CM:060.9', 'ICD9CM:061', 'ICD9CM:065.0', 'ICD9CM:065.1', 'ICD9CM:065.2', 'ICD9CM:065.3', 'ICD9CM:065.4', 'ICD9CM:065.8', 'ICD9CM:065.9', 'ICD9CM:066.0', 'ICD9CM:066.1', 'ICD9CM:066.3', 'ICD9CM:066.4', 'ICD9CM:066.40', 'ICD9CM:066.42', 'ICD9CM:066.49', 'ICD9CM:066.8', 'ICD9CM:066.9', 'ICD9CM:071', 'ICD9CM:072.0', 'ICD9CM:072.3', 'ICD9CM:072.72', 'ICD9CM:072.79', 'ICD9CM:072.8', 'ICD9CM:072.9', 'ICD9CM:073.7', 'ICD9CM:073.8', 'ICD9CM:073.9', 'ICD9CM:074.0', 'ICD9CM:074.1', 'ICD9CM:074.3', 'ICD9CM:074.8', 'ICD9CM:075', 'ICD9CM:078.0', 'ICD9CM:078.1', 'ICD9CM:078.10', 'ICD9CM:078.11', 'ICD9CM:078.12', 'ICD9CM:078.19', 'ICD9CM:078.2', 'ICD9CM:078.3', 'ICD9CM:078.4', 'ICD9CM:078.5', 'ICD9CM:078.6', 'ICD9CM:078.7', 'ICD9CM:078.81', 'ICD9CM:078.82', 'ICD9CM:078.88', 'ICD9CM:078.89', 'ICD9CM:079.0', 'ICD9CM:079.1', 'ICD9CM:079.2', 'ICD9CM:079.3', 'ICD9CM:079.4', 'ICD9CM:079.50', 'ICD9CM:079.51', 'ICD9CM:079.52', 'ICD9CM:079.59', 'ICD9CM:079.6', 'ICD9CM:079.8', 'ICD9CM:079.81', 'ICD9CM:079.82', 'ICD9CM:079.83', 'ICD9CM:079.88', 'ICD9CM:079.89', 'ICD9CM:079.9', 'ICD9CM:079.98', 'ICD9CM:079.99', 'ICD9CM:790.8'):
            results_ccs1["viral_infec"].append(1)
        else: results_ccs1["viral_infec"].append(0)
    print("Completed Binary Recode of: viral_infec")

    # Other_infections;_including_parasitic
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:080', 'ICD9CM:081.0', 'ICD9CM:081.1', 'ICD9CM:081.2', 'ICD9CM:081.9', 'ICD9CM:082.0', 'ICD9CM:082.1', 'ICD9CM:082.2', 'ICD9CM:082.3', 'ICD9CM:082.40', 'ICD9CM:082.41', 'ICD9CM:082.49', 'ICD9CM:082.8', 'ICD9CM:082.9', 'ICD9CM:083.1', 'ICD9CM:083.2', 'ICD9CM:083.8', 'ICD9CM:083.9', 'ICD9CM:084.0', 'ICD9CM:084.1', 'ICD9CM:084.2', 'ICD9CM:084.3', 'ICD9CM:084.4', 'ICD9CM:084.5', 'ICD9CM:084.6', 'ICD9CM:084.7', 'ICD9CM:084.8', 'ICD9CM:084.9', 'ICD9CM:085.0', 'ICD9CM:085.1', 'ICD9CM:085.2', 'ICD9CM:085.3', 'ICD9CM:085.4', 'ICD9CM:085.5', 'ICD9CM:085.9', 'ICD9CM:086.0', 'ICD9CM:086.1', 'ICD9CM:086.2', 'ICD9CM:086.3', 'ICD9CM:086.4', 'ICD9CM:086.5', 'ICD9CM:086.9', 'ICD9CM:087.0', 'ICD9CM:087.1', 'ICD9CM:087.9', 'ICD9CM:088.0', 'ICD9CM:088.8', 'ICD9CM:088.81', 'ICD9CM:088.82', 'ICD9CM:088.89', 'ICD9CM:088.9', 'ICD9CM:100.0', 'ICD9CM:100.89', 'ICD9CM:100.9', 'ICD9CM:101', 'ICD9CM:102.0', 'ICD9CM:102.1', 'ICD9CM:102.2', 'ICD9CM:102.3', 'ICD9CM:102.4', 'ICD9CM:102.5', 'ICD9CM:102.6', 'ICD9CM:102.7', 'ICD9CM:102.8', 'ICD9CM:102.9', 'ICD9CM:103.0', 'ICD9CM:103.1', 'ICD9CM:103.2', 'ICD9CM:103.3', 'ICD9CM:103.9', 'ICD9CM:104.0', 'ICD9CM:104.8', 'ICD9CM:104.9', 'ICD9CM:120.0', 'ICD9CM:120.1', 'ICD9CM:120.2', 'ICD9CM:120.3', 'ICD9CM:120.8', 'ICD9CM:120.9', 'ICD9CM:121.0', 'ICD9CM:121.1', 'ICD9CM:121.2', 'ICD9CM:121.3', 'ICD9CM:121.4', 'ICD9CM:121.5', 'ICD9CM:121.6', 'ICD9CM:121.8', 'ICD9CM:121.9', 'ICD9CM:122.0', 'ICD9CM:122.1', 'ICD9CM:122.2', 'ICD9CM:122.3', 'ICD9CM:122.4', 'ICD9CM:122.5', 'ICD9CM:122.6', 'ICD9CM:122.7', 'ICD9CM:122.8', 'ICD9CM:122.9', 'ICD9CM:123.0', 'ICD9CM:123.1', 'ICD9CM:123.2', 'ICD9CM:123.3', 'ICD9CM:123.4', 'ICD9CM:123.5', 'ICD9CM:123.6', 'ICD9CM:123.8', 'ICD9CM:123.9', 'ICD9CM:124', 'ICD9CM:125.0', 'ICD9CM:125.1', 'ICD9CM:125.2', 'ICD9CM:125.3', 'ICD9CM:125.4', 'ICD9CM:125.5', 'ICD9CM:125.6', 'ICD9CM:125.7', 'ICD9CM:125.9', 'ICD9CM:126.0', 'ICD9CM:126.1', 'ICD9CM:126.2', 'ICD9CM:126.3', 'ICD9CM:126.8', 'ICD9CM:126.9', 'ICD9CM:127.0', 'ICD9CM:127.1', 'ICD9CM:127.2', 'ICD9CM:127.3', 'ICD9CM:127.4', 'ICD9CM:127.5', 'ICD9CM:127.6', 'ICD9CM:127.7', 'ICD9CM:127.8', 'ICD9CM:127.9', 'ICD9CM:128.0', 'ICD9CM:128.1', 'ICD9CM:128.8', 'ICD9CM:128.9', 'ICD9CM:129', 'ICD9CM:130.5', 'ICD9CM:130.7', 'ICD9CM:130.8', 'ICD9CM:130.9', 'ICD9CM:131.00', 'ICD9CM:131.01', 'ICD9CM:131.02', 'ICD9CM:131.03', 'ICD9CM:131.09', 'ICD9CM:131.8', 'ICD9CM:131.9', 'ICD9CM:132.0', 'ICD9CM:132.1', 'ICD9CM:132.2', 'ICD9CM:132.3', 'ICD9CM:132.9', 'ICD9CM:133.0', 'ICD9CM:133.8', 'ICD9CM:133.9', 'ICD9CM:134.0', 'ICD9CM:134.1', 'ICD9CM:134.2', 'ICD9CM:134.8', 'ICD9CM:134.9', 'ICD9CM:135', 'ICD9CM:136.0', 'ICD9CM:136.1', 'ICD9CM:136.2', 'ICD9CM:136.21', 'ICD9CM:136.29', 'ICD9CM:136.4', 'ICD9CM:136.5', 'ICD9CM:136.8', 'ICD9CM:136.9', 'ICD9CM:139.8', 'ICD9CM:V12.0', 'ICD9CM:V12.00', 'ICD9CM:V12.03', 'ICD9CM:V12.09'):
            results_ccs1["other_infec"].append(1)
        else: results_ccs1["other_infec"].append(0)
    print("Completed Binary Recode of: other_infec")

    # Sexually_transmitted_infections_(_not_HIV_or_hepatitis)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:090.0', 'ICD9CM:090.1', 'ICD9CM:090.2', 'ICD9CM:090.3', 'ICD9CM:090.40', 'ICD9CM:090.41', 'ICD9CM:090.42', 'ICD9CM:090.49', 'ICD9CM:090.5', 'ICD9CM:090.6', 'ICD9CM:090.7', 'ICD9CM:090.9', 'ICD9CM:091.0', 'ICD9CM:091.1', 'ICD9CM:091.2', 'ICD9CM:091.3', 'ICD9CM:091.4', 'ICD9CM:091.50', 'ICD9CM:091.51', 'ICD9CM:091.52', 'ICD9CM:091.61', 'ICD9CM:091.62', 'ICD9CM:091.69', 'ICD9CM:091.7', 'ICD9CM:091.81', 'ICD9CM:091.82', 'ICD9CM:091.89', 'ICD9CM:091.9', 'ICD9CM:092.0', 'ICD9CM:092.9', 'ICD9CM:093.0', 'ICD9CM:093.1', 'ICD9CM:093.20', 'ICD9CM:093.21', 'ICD9CM:093.22', 'ICD9CM:093.23', 'ICD9CM:093.24', 'ICD9CM:093.81', 'ICD9CM:093.82', 'ICD9CM:093.89', 'ICD9CM:093.9', 'ICD9CM:094.0', 'ICD9CM:094.1', 'ICD9CM:094.2', 'ICD9CM:094.3', 'ICD9CM:094.81', 'ICD9CM:094.82', 'ICD9CM:094.83', 'ICD9CM:094.84', 'ICD9CM:094.85', 'ICD9CM:094.86', 'ICD9CM:094.87', 'ICD9CM:094.89', 'ICD9CM:094.9', 'ICD9CM:095.0', 'ICD9CM:095.1', 'ICD9CM:095.2', 'ICD9CM:095.3', 'ICD9CM:095.4', 'ICD9CM:095.5', 'ICD9CM:095.6', 'ICD9CM:095.7', 'ICD9CM:095.8', 'ICD9CM:095.9', 'ICD9CM:096', 'ICD9CM:097.0', 'ICD9CM:097.1', 'ICD9CM:097.9', 'ICD9CM:098.0', 'ICD9CM:098.10', 'ICD9CM:098.11', 'ICD9CM:098.12', 'ICD9CM:098.13', 'ICD9CM:098.14', 'ICD9CM:098.15', 'ICD9CM:098.16', 'ICD9CM:098.17', 'ICD9CM:098.19', 'ICD9CM:098.2', 'ICD9CM:098.30', 'ICD9CM:098.31', 'ICD9CM:098.32', 'ICD9CM:098.33', 'ICD9CM:098.34', 'ICD9CM:098.35', 'ICD9CM:098.36', 'ICD9CM:098.37', 'ICD9CM:098.39', 'ICD9CM:098.40', 'ICD9CM:098.41', 'ICD9CM:098.42', 'ICD9CM:098.43', 'ICD9CM:098.49', 'ICD9CM:098.50', 'ICD9CM:098.51', 'ICD9CM:098.52', 'ICD9CM:098.53', 'ICD9CM:098.59', 'ICD9CM:098.6', 'ICD9CM:098.7', 'ICD9CM:098.81', 'ICD9CM:098.82', 'ICD9CM:098.83', 'ICD9CM:098.84', 'ICD9CM:098.85', 'ICD9CM:098.86', 'ICD9CM:098.89', 'ICD9CM:099.0', 'ICD9CM:099.1', 'ICD9CM:099.2', 'ICD9CM:099.3', 'ICD9CM:099.4', 'ICD9CM:099.40', 'ICD9CM:099.41', 'ICD9CM:099.49', 'ICD9CM:099.50', 'ICD9CM:099.51', 'ICD9CM:099.52', 'ICD9CM:099.53', 'ICD9CM:099.54', 'ICD9CM:099.55', 'ICD9CM:099.56', 'ICD9CM:099.59', 'ICD9CM:099.8', 'ICD9CM:099.9', 'ICD9CM:795.05', 'ICD9CM:795.15', 'ICD9CM:795.19', 'ICD9CM:796.75', 'ICD9CM:796.79'):
            results_ccs1["sti"].append(1)
        else: results_ccs1["sti"].append(0)
    print("Completed Binary Recode of: sti")

    # Immunizations_and_screening_for_infectious_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:795.5', 'ICD9CM:795.51', 'ICD9CM:795.52', 'ICD9CM:795.6', 'ICD9CM:795.79', 'ICD9CM:V01.0', 'ICD9CM:V01.1', 'ICD9CM:V01.2', 'ICD9CM:V01.3', 'ICD9CM:V01.4', 'ICD9CM:V01.5', 'ICD9CM:V01.6', 'ICD9CM:V01.7', 'ICD9CM:V01.71', 'ICD9CM:V01.79', 'ICD9CM:V01.8', 'ICD9CM:V01.81', 'ICD9CM:V01.82', 'ICD9CM:V01.83', 'ICD9CM:V01.84', 'ICD9CM:V01.89', 'ICD9CM:V01.9', 'ICD9CM:V02.0', 'ICD9CM:V02.1', 'ICD9CM:V02.2', 'ICD9CM:V02.3', 'ICD9CM:V02.4', 'ICD9CM:V02.5', 'ICD9CM:V02.51', 'ICD9CM:V02.52', 'ICD9CM:V02.53', 'ICD9CM:V02.54', 'ICD9CM:V02.59', 'ICD9CM:V02.6', 'ICD9CM:V02.60', 'ICD9CM:V02.61', 'ICD9CM:V02.62', 'ICD9CM:V02.69', 'ICD9CM:V02.7', 'ICD9CM:V02.8', 'ICD9CM:V02.9', 'ICD9CM:V03.0', 'ICD9CM:V03.1', 'ICD9CM:V03.2', 'ICD9CM:V03.3', 'ICD9CM:V03.4', 'ICD9CM:V03.5', 'ICD9CM:V03.6', 'ICD9CM:V03.7', 'ICD9CM:V03.8', 'ICD9CM:V03.81', 'ICD9CM:V03.82', 'ICD9CM:V03.89', 'ICD9CM:V03.9', 'ICD9CM:V04.0', 'ICD9CM:V04.1', 'ICD9CM:V04.2', 'ICD9CM:V04.3', 'ICD9CM:V04.4', 'ICD9CM:V04.5', 'ICD9CM:V04.6', 'ICD9CM:V04.7', 'ICD9CM:V04.8', 'ICD9CM:V04.81', 'ICD9CM:V04.82', 'ICD9CM:V04.89', 'ICD9CM:V05.0', 'ICD9CM:V05.1', 'ICD9CM:V05.2', 'ICD9CM:V05.3', 'ICD9CM:V05.4', 'ICD9CM:V05.8', 'ICD9CM:V05.9', 'ICD9CM:V06.0', 'ICD9CM:V06.1', 'ICD9CM:V06.2', 'ICD9CM:V06.3', 'ICD9CM:V06.4', 'ICD9CM:V06.5', 'ICD9CM:V06.6', 'ICD9CM:V06.8', 'ICD9CM:V06.9', 'ICD9CM:V28.6', 'ICD9CM:V71.2', 'ICD9CM:V71.82', 'ICD9CM:V71.83', 'ICD9CM:V73.0', 'ICD9CM:V73.1', 'ICD9CM:V73.2', 'ICD9CM:V73.3', 'ICD9CM:V73.4', 'ICD9CM:V73.5', 'ICD9CM:V73.6', 'ICD9CM:V73.8', 'ICD9CM:V73.81', 'ICD9CM:V73.88', 'ICD9CM:V73.89', 'ICD9CM:V73.9', 'ICD9CM:V73.98', 'ICD9CM:V73.99', 'ICD9CM:V74.0', 'ICD9CM:V74.1', 'ICD9CM:V74.2', 'ICD9CM:V74.3', 'ICD9CM:V74.4', 'ICD9CM:V74.5', 'ICD9CM:V74.6', 'ICD9CM:V74.8', 'ICD9CM:V74.9', 'ICD9CM:V75.0', 'ICD9CM:V75.1', 'ICD9CM:V75.2', 'ICD9CM:V75.3', 'ICD9CM:V75.4', 'ICD9CM:V75.5', 'ICD9CM:V75.6', 'ICD9CM:V75.7', 'ICD9CM:V75.8', 'ICD9CM:V75.9'):
            results_ccs1["screen_infec"].append(1)
        else: results_ccs1["screen_infec"].append(0)
    print("Completed Binary Recode of: screen_infec")

    # Cancer_of_head_and_neck
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:140.0', 'ICD9CM:140.1', 'ICD9CM:140.3', 'ICD9CM:140.4', 'ICD9CM:140.5', 'ICD9CM:140.6', 'ICD9CM:140.8', 'ICD9CM:140.9', 'ICD9CM:141.0', 'ICD9CM:141.1', 'ICD9CM:141.2', 'ICD9CM:141.3', 'ICD9CM:141.4', 'ICD9CM:141.5', 'ICD9CM:141.6', 'ICD9CM:141.8', 'ICD9CM:141.9', 'ICD9CM:142.0', 'ICD9CM:142.1', 'ICD9CM:142.2', 'ICD9CM:142.8', 'ICD9CM:142.9', 'ICD9CM:143.0', 'ICD9CM:143.1', 'ICD9CM:143.8', 'ICD9CM:143.9', 'ICD9CM:144.0', 'ICD9CM:144.1', 'ICD9CM:144.8', 'ICD9CM:144.9', 'ICD9CM:145.0', 'ICD9CM:145.1', 'ICD9CM:145.2', 'ICD9CM:145.3', 'ICD9CM:145.4', 'ICD9CM:145.5', 'ICD9CM:145.6', 'ICD9CM:145.8', 'ICD9CM:145.9', 'ICD9CM:146.0', 'ICD9CM:146.1', 'ICD9CM:146.2', 'ICD9CM:146.3', 'ICD9CM:146.4', 'ICD9CM:146.5', 'ICD9CM:146.6', 'ICD9CM:146.7', 'ICD9CM:146.8', 'ICD9CM:146.9', 'ICD9CM:147.0', 'ICD9CM:147.1', 'ICD9CM:147.2', 'ICD9CM:147.3', 'ICD9CM:147.8', 'ICD9CM:147.9', 'ICD9CM:148.0', 'ICD9CM:148.1', 'ICD9CM:148.2', 'ICD9CM:148.3', 'ICD9CM:148.8', 'ICD9CM:148.9', 'ICD9CM:149.0', 'ICD9CM:149.1', 'ICD9CM:149.8', 'ICD9CM:149.9', 'ICD9CM:160.0', 'ICD9CM:160.1', 'ICD9CM:160.2', 'ICD9CM:160.3', 'ICD9CM:160.4', 'ICD9CM:160.5', 'ICD9CM:160.8', 'ICD9CM:160.9', 'ICD9CM:161.0', 'ICD9CM:161.1', 'ICD9CM:161.2', 'ICD9CM:161.3', 'ICD9CM:161.8', 'ICD9CM:161.9', 'ICD9CM:195.0', 'ICD9CM:230.0', 'ICD9CM:231.0', 'ICD9CM:V10.01', 'ICD9CM:V10.02', 'ICD9CM:V10.21'):
            results_ccs1["head_ca"].append(1)
        else: results_ccs1["head_ca"].append(0)
    print("Completed Binary Recode of: head_ca")

    # Cancer_of_esophagus
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:150.0', 'ICD9CM:150.1', 'ICD9CM:150.2', 'ICD9CM:150.3', 'ICD9CM:150.4', 'ICD9CM:150.5', 'ICD9CM:150.8', 'ICD9CM:150.9', 'ICD9CM:230.1', 'ICD9CM:V10.03'):
            results_ccs1["esophagus_ca"].append(1)
        else: results_ccs1["esophagus_ca"].append(0)
    print("Completed Binary Recode of: esophagus_ca")

    # Cancer_of_stomach
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:151.0', 'ICD9CM:151.1', 'ICD9CM:151.2', 'ICD9CM:151.3', 'ICD9CM:151.4', 'ICD9CM:151.5', 'ICD9CM:151.6', 'ICD9CM:151.8', 'ICD9CM:151.9', 'ICD9CM:209.23', 'ICD9CM:230.2', 'ICD9CM:V10.04'):
            results_ccs1["stomach_ca"].append(1)
        else: results_ccs1["stomach_ca"].append(0)
    print("Completed Binary Recode of: stomach_ca")

    # Cancer_of_colon
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:153.0', 'ICD9CM:153.1', 'ICD9CM:153.2', 'ICD9CM:153.3', 'ICD9CM:153.4', 'ICD9CM:153.5', 'ICD9CM:153.6', 'ICD9CM:153.7', 'ICD9CM:153.8', 'ICD9CM:153.9', 'ICD9CM:159.0', 'ICD9CM:209.10', 'ICD9CM:209.11', 'ICD9CM:209.12', 'ICD9CM:209.13', 'ICD9CM:209.14', 'ICD9CM:209.15', 'ICD9CM:209.16', 'ICD9CM:230.3', 'ICD9CM:V10.05'):
            results_ccs1["colon_ca"].append(1)
        else: results_ccs1["colon_ca"].append(0)
    print("Completed Binary Recode of: colon_ca")

    # Cancer_of_rectum_and_anus
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:154.0', 'ICD9CM:154.1', 'ICD9CM:154.2', 'ICD9CM:154.3', 'ICD9CM:154.8', 'ICD9CM:209.17', 'ICD9CM:230.4', 'ICD9CM:230.5', 'ICD9CM:230.6', 'ICD9CM:796.70', 'ICD9CM:796.71', 'ICD9CM:796.72', 'ICD9CM:796.73', 'ICD9CM:796.74', 'ICD9CM:796.76', 'ICD9CM:V10.06'):
            results_ccs1["rectum_ca"].append(1)
        else: results_ccs1["rectum_ca"].append(0)
    print("Completed Binary Recode of: rectum_ca")

    # Cancer_of_liver_and_intrahepatic_bile_duct
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:155.0', 'ICD9CM:155.1', 'ICD9CM:155.2', 'ICD9CM:230.8', 'ICD9CM:V10.07'):
            results_ccs1["liver_ca"].append(1)
        else: results_ccs1["liver_ca"].append(0)
    print("Completed Binary Recode of: liver_ca")

    # Cancer_of_pancreas
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:157.0', 'ICD9CM:157.1', 'ICD9CM:157.2', 'ICD9CM:157.3', 'ICD9CM:157.4', 'ICD9CM:157.8', 'ICD9CM:157.9'):
            results_ccs1["pancreas_ca"].append(1)
        else: results_ccs1["pancreas_ca"].append(0)
    print("Completed Binary Recode of: pancreas_ca")

    # Cancer_of_other_GI_organs;_peritoneum
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:152.0', 'ICD9CM:152.1', 'ICD9CM:152.2', 'ICD9CM:152.3', 'ICD9CM:152.8', 'ICD9CM:152.9', 'ICD9CM:156.0', 'ICD9CM:156.1', 'ICD9CM:156.2', 'ICD9CM:156.8', 'ICD9CM:156.9', 'ICD9CM:158.0', 'ICD9CM:158.8', 'ICD9CM:158.9', 'ICD9CM:159.1', 'ICD9CM:159.8', 'ICD9CM:159.9', 'ICD9CM:209.00', 'ICD9CM:209.01', 'ICD9CM:209.02', 'ICD9CM:209.03', 'ICD9CM:230.7', 'ICD9CM:230.9', 'ICD9CM:V10.00', 'ICD9CM:V10.09'):
            results_ccs1["gi_ca"].append(1)
        else: results_ccs1["gi_ca"].append(0)
    print("Completed Binary Recode of: gi_ca")

    # Cancer_of_bronchus;_lung
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:162.2', 'ICD9CM:162.3', 'ICD9CM:162.4', 'ICD9CM:162.5', 'ICD9CM:162.8', 'ICD9CM:162.9', 'ICD9CM:209.21', 'ICD9CM:231.2', 'ICD9CM:V10.11'):
            results_ccs1["lung_ca"].append(1)
        else: results_ccs1["lung_ca"].append(0)
    print("Completed Binary Recode of: lung_ca")

    # Cancer;_other_respiratory_and_intrathoracic
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:162.0', 'ICD9CM:163.0', 'ICD9CM:163.1', 'ICD9CM:163.8', 'ICD9CM:163.9', 'ICD9CM:165.0', 'ICD9CM:165.8', 'ICD9CM:165.9', 'ICD9CM:231.1', 'ICD9CM:231.8', 'ICD9CM:231.9', 'ICD9CM:V10.12', 'ICD9CM:V10.20', 'ICD9CM:V10.22'):
            results_ccs1["resp_ca"].append(1)
        else: results_ccs1["resp_ca"].append(0)
    print("Completed Binary Recode of: resp_ca")

    # Cancer_of_bone_and_connective_tissue
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:170.0', 'ICD9CM:170.1', 'ICD9CM:170.2', 'ICD9CM:170.3', 'ICD9CM:170.4', 'ICD9CM:170.5', 'ICD9CM:170.6', 'ICD9CM:170.7', 'ICD9CM:170.8', 'ICD9CM:170.9', 'ICD9CM:171.0', 'ICD9CM:171.2', 'ICD9CM:171.3', 'ICD9CM:171.4', 'ICD9CM:171.5', 'ICD9CM:171.6', 'ICD9CM:171.7', 'ICD9CM:171.8', 'ICD9CM:171.9'):
            results_ccs1["bone_ca"].append(1)
        else: results_ccs1["bone_ca"].append(0)
    print("Completed Binary Recode of: bone_ca")

    # Melanomas_of_skin
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:172.0', 'ICD9CM:172.1', 'ICD9CM:172.2', 'ICD9CM:172.3', 'ICD9CM:172.4', 'ICD9CM:172.5', 'ICD9CM:172.6', 'ICD9CM:172.7', 'ICD9CM:172.8', 'ICD9CM:172.9', 'ICD9CM:V10.82'):
            results_ccs1["melanoma"].append(1)
        else: results_ccs1["melanoma"].append(0)
    print("Completed Binary Recode of: melanoma")

    # Other_non-_epithelial_cancer_of_skin
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:173.0', 'ICD9CM:173.00', 'ICD9CM:173.01', 'ICD9CM:173.02', 'ICD9CM:173.09', 'ICD9CM:173.1', 'ICD9CM:173.10', 'ICD9CM:173.11', 'ICD9CM:173.12', 'ICD9CM:173.19', 'ICD9CM:173.2', 'ICD9CM:173.20', 'ICD9CM:173.21', 'ICD9CM:173.22', 'ICD9CM:173.29', 'ICD9CM:173.3', 'ICD9CM:173.30', 'ICD9CM:173.31', 'ICD9CM:173.32', 'ICD9CM:173.39', 'ICD9CM:173.4', 'ICD9CM:173.40', 'ICD9CM:173.41', 'ICD9CM:173.42', 'ICD9CM:173.49', 'ICD9CM:173.5', 'ICD9CM:173.50', 'ICD9CM:173.51', 'ICD9CM:173.52', 'ICD9CM:173.59', 'ICD9CM:173.6', 'ICD9CM:173.60', 'ICD9CM:173.61', 'ICD9CM:173.62', 'ICD9CM:173.69', 'ICD9CM:173.7', 'ICD9CM:173.70', 'ICD9CM:173.71', 'ICD9CM:173.72', 'ICD9CM:173.79', 'ICD9CM:173.8', 'ICD9CM:173.80', 'ICD9CM:173.81', 'ICD9CM:173.82', 'ICD9CM:173.89', 'ICD9CM:173.9', 'ICD9CM:173.90', 'ICD9CM:173.91', 'ICD9CM:173.92', 'ICD9CM:173.99', 'ICD9CM:209.31', 'ICD9CM:209.32', 'ICD9CM:209.33', 'ICD9CM:209.34', 'ICD9CM:209.35', 'ICD9CM:209.36', 'ICD9CM:232.0', 'ICD9CM:232.1', 'ICD9CM:232.2', 'ICD9CM:232.3', 'ICD9CM:232.4', 'ICD9CM:232.5', 'ICD9CM:232.6', 'ICD9CM:232.7', 'ICD9CM:232.8', 'ICD9CM:232.9', 'ICD9CM:V10.83'):
            results_ccs1["nonepi_skin_ca"].append(1)
        else: results_ccs1["nonepi_skin_ca"].append(0)
    print("Completed Binary Recode of: nonepi_skin_ca")

    # Cancer_of_breast
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:174.0', 'ICD9CM:174.1', 'ICD9CM:174.2', 'ICD9CM:174.3', 'ICD9CM:174.4', 'ICD9CM:174.5', 'ICD9CM:174.6', 'ICD9CM:174.8', 'ICD9CM:174.9', 'ICD9CM:175.0', 'ICD9CM:175.9', 'ICD9CM:233.0', 'ICD9CM:V10.3'):
            results_ccs1["breast_ca"].append(1)
        else: results_ccs1["breast_ca"].append(0)
    print("Completed Binary Recode of: breast_ca")

    # Cancer_of_uterus
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:179', 'ICD9CM:182.0', 'ICD9CM:182.1', 'ICD9CM:182.8', 'ICD9CM:233.2', 'ICD9CM:V10.42'):
            results_ccs1["uterus_ca"].append(1)
        else: results_ccs1["uterus_ca"].append(0)
    print("Completed Binary Recode of: uterus_ca")

    # Cancer_of_cervix
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:180.0', 'ICD9CM:180.1', 'ICD9CM:180.8', 'ICD9CM:180.9', 'ICD9CM:233.1', 'ICD9CM:795.0', 'ICD9CM:795.01', 'ICD9CM:795.02', 'ICD9CM:795.03', 'ICD9CM:795.04', 'ICD9CM:795.06', 'ICD9CM:V10.41'):
            results_ccs1["cervix_ca"].append(1)
        else: results_ccs1["cervix_ca"].append(0)
    print("Completed Binary Recode of: cervix_ca")

    # Cancer_of_ovary
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:183.0', 'ICD9CM:V10.43'):
            results_ccs1["ovary_ca"].append(1)
        else: results_ccs1["ovary_ca"].append(0)
    print("Completed Binary Recode of: ovary_ca")

    # Cancer_of_other_female_genital_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:181', 'ICD9CM:183.2', 'ICD9CM:183.3', 'ICD9CM:183.4', 'ICD9CM:183.5', 'ICD9CM:183.8', 'ICD9CM:183.9', 'ICD9CM:184.0', 'ICD9CM:184.1', 'ICD9CM:184.2', 'ICD9CM:184.3', 'ICD9CM:184.4', 'ICD9CM:184.8', 'ICD9CM:184.9', 'ICD9CM:233.3', 'ICD9CM:233.30', 'ICD9CM:233.31', 'ICD9CM:233.32', 'ICD9CM:233.39', 'ICD9CM:795.16', 'ICD9CM:V10.40', 'ICD9CM:V10.44'):
            results_ccs1["fem_genital_ca"].append(1)
        else: results_ccs1["fem_genital_ca"].append(0)
    print("Completed Binary Recode of: fem_genital_ca")

    # Cancer_of_prostate
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:185', 'ICD9CM:233.4', 'ICD9CM:V10.46'):
            results_ccs1["prostate_ca"].append(1)
        else: results_ccs1["prostate_ca"].append(0)
    print("Completed Binary Recode of: prostate_ca")

    # Cancer_of_testis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:186.0', 'ICD9CM:186.9', 'ICD9CM:V10.47'):
            results_ccs1["testes_ca"].append(1)
        else: results_ccs1["testes_ca"].append(0)
    print("Completed Binary Recode of: testes_ca")

    # Cancer_of_other_male_genital_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:187.1', 'ICD9CM:187.2', 'ICD9CM:187.3', 'ICD9CM:187.4', 'ICD9CM:187.5', 'ICD9CM:187.6', 'ICD9CM:187.7', 'ICD9CM:187.8', 'ICD9CM:187.9', 'ICD9CM:233.5', 'ICD9CM:233.6', 'ICD9CM:V10.45', 'ICD9CM:V10.48', 'ICD9CM:V10.49'):
            results_ccs1["male_genital_ca"].append(1)
        else: results_ccs1["male_genital_ca"].append(0)
    print("Completed Binary Recode of: male_genital_ca")

    # Cancer_of_bladder
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:188.0', 'ICD9CM:188.1', 'ICD9CM:188.2', 'ICD9CM:188.3', 'ICD9CM:188.4', 'ICD9CM:188.5', 'ICD9CM:188.6', 'ICD9CM:188.7', 'ICD9CM:188.8', 'ICD9CM:188.9', 'ICD9CM:233.7', 'ICD9CM:V10.51'):
            results_ccs1["bladder_ca"].append(1)
        else: results_ccs1["bladder_ca"].append(0)
    print("Completed Binary Recode of: bladder_ca")

    # Cancer_of_kidney_and_renal_pelvis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:189.0', 'ICD9CM:189.1', 'ICD9CM:209.24', 'ICD9CM:V10.52', 'ICD9CM:V10.53'):
            results_ccs1["kidney_ca"].append(1)
        else: results_ccs1["kidney_ca"].append(0)
    print("Completed Binary Recode of: kidney_ca")

    # Cancer_of_other_urinary_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:189.2', 'ICD9CM:189.3', 'ICD9CM:189.4', 'ICD9CM:189.8', 'ICD9CM:189.9', 'ICD9CM:233.9', 'ICD9CM:V10.50', 'ICD9CM:V10.59'):
            results_ccs1["urinary_ca"].append(1)
        else: results_ccs1["urinary_ca"].append(0)
    print("Completed Binary Recode of: urinary_ca")

    # Cancer_of_brain_and_nervous_system
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:191.0', 'ICD9CM:191.1', 'ICD9CM:191.2', 'ICD9CM:191.3', 'ICD9CM:191.4', 'ICD9CM:191.5', 'ICD9CM:191.6', 'ICD9CM:191.7', 'ICD9CM:191.8', 'ICD9CM:191.9', 'ICD9CM:192.0', 'ICD9CM:192.1', 'ICD9CM:192.2', 'ICD9CM:192.3', 'ICD9CM:192.8', 'ICD9CM:192.9', 'ICD9CM:V10.85', 'ICD9CM:V10.86'):
            results_ccs1["brain_ca"].append(1)
        else: results_ccs1["brain_ca"].append(0)
    print("Completed Binary Recode of: brain_ca")

    # Cancer_of_thyroid
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:193', 'ICD9CM:258.02', 'ICD9CM:258.03', 'ICD9CM:V10.87'):
            results_ccs1["thyroid_ca"].append(1)
        else: results_ccs1["thyroid_ca"].append(0)
    print("Completed Binary Recode of: thyroid_ca")

    # Hodgkin`_s_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:201.00', 'ICD9CM:201.01', 'ICD9CM:201.02', 'ICD9CM:201.03', 'ICD9CM:201.04', 'ICD9CM:201.05', 'ICD9CM:201.06', 'ICD9CM:201.07', 'ICD9CM:201.08', 'ICD9CM:201.10', 'ICD9CM:201.11', 'ICD9CM:201.12', 'ICD9CM:201.13', 'ICD9CM:201.14', 'ICD9CM:201.15', 'ICD9CM:201.16', 'ICD9CM:201.17', 'ICD9CM:201.18', 'ICD9CM:201.20', 'ICD9CM:201.21', 'ICD9CM:201.22', 'ICD9CM:201.23', 'ICD9CM:201.24', 'ICD9CM:201.25', 'ICD9CM:201.26', 'ICD9CM:201.27', 'ICD9CM:201.28', 'ICD9CM:201.40', 'ICD9CM:201.41', 'ICD9CM:201.42', 'ICD9CM:201.43', 'ICD9CM:201.44', 'ICD9CM:201.45', 'ICD9CM:201.46', 'ICD9CM:201.47', 'ICD9CM:201.48', 'ICD9CM:201.50', 'ICD9CM:201.51', 'ICD9CM:201.52', 'ICD9CM:201.53', 'ICD9CM:201.54', 'ICD9CM:201.55', 'ICD9CM:201.56', 'ICD9CM:201.57', 'ICD9CM:201.58', 'ICD9CM:201.60', 'ICD9CM:201.61', 'ICD9CM:201.62', 'ICD9CM:201.63', 'ICD9CM:201.64', 'ICD9CM:201.65', 'ICD9CM:201.66', 'ICD9CM:201.67', 'ICD9CM:201.68', 'ICD9CM:201.70', 'ICD9CM:201.71', 'ICD9CM:201.72', 'ICD9CM:201.73', 'ICD9CM:201.74', 'ICD9CM:201.75', 'ICD9CM:201.76', 'ICD9CM:201.77', 'ICD9CM:201.78', 'ICD9CM:201.90', 'ICD9CM:201.91', 'ICD9CM:201.92', 'ICD9CM:201.93', 'ICD9CM:201.94', 'ICD9CM:201.95', 'ICD9CM:201.96', 'ICD9CM:201.97', 'ICD9CM:201.98', 'ICD9CM:V10.72'):
            results_ccs1["hodgkins_lymph"].append(1)
        else: results_ccs1["hodgkins_lymph"].append(0)
    print("Completed Binary Recode of: hodgkins_lymph")

    # Non-_Hodgkin`_s_lymphoma
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:200.00', 'ICD9CM:200.01', 'ICD9CM:200.02', 'ICD9CM:200.03', 'ICD9CM:200.04', 'ICD9CM:200.05', 'ICD9CM:200.06', 'ICD9CM:200.07', 'ICD9CM:200.08', 'ICD9CM:200.10', 'ICD9CM:200.11', 'ICD9CM:200.12', 'ICD9CM:200.13', 'ICD9CM:200.14', 'ICD9CM:200.15', 'ICD9CM:200.16', 'ICD9CM:200.17', 'ICD9CM:200.18', 'ICD9CM:200.20', 'ICD9CM:200.21', 'ICD9CM:200.22', 'ICD9CM:200.23', 'ICD9CM:200.24', 'ICD9CM:200.25', 'ICD9CM:200.26', 'ICD9CM:200.27', 'ICD9CM:200.28', 'ICD9CM:200.30', 'ICD9CM:200.31', 'ICD9CM:200.32', 'ICD9CM:200.33', 'ICD9CM:200.34', 'ICD9CM:200.35', 'ICD9CM:200.36', 'ICD9CM:200.37', 'ICD9CM:200.38', 'ICD9CM:200.40', 'ICD9CM:200.41', 'ICD9CM:200.42', 'ICD9CM:200.43', 'ICD9CM:200.44', 'ICD9CM:200.45', 'ICD9CM:200.46', 'ICD9CM:200.47', 'ICD9CM:200.48', 'ICD9CM:200.50', 'ICD9CM:200.51', 'ICD9CM:200.52', 'ICD9CM:200.53', 'ICD9CM:200.54', 'ICD9CM:200.55', 'ICD9CM:200.56', 'ICD9CM:200.57', 'ICD9CM:200.58', 'ICD9CM:200.60', 'ICD9CM:200.61', 'ICD9CM:200.62', 'ICD9CM:200.63', 'ICD9CM:200.64', 'ICD9CM:200.65', 'ICD9CM:200.66', 'ICD9CM:200.67', 'ICD9CM:200.68', 'ICD9CM:200.70', 'ICD9CM:200.71', 'ICD9CM:200.72', 'ICD9CM:200.73', 'ICD9CM:200.74', 'ICD9CM:200.75', 'ICD9CM:200.76', 'ICD9CM:200.77', 'ICD9CM:200.78', 'ICD9CM:200.80', 'ICD9CM:200.81', 'ICD9CM:200.82', 'ICD9CM:200.83', 'ICD9CM:200.84', 'ICD9CM:200.85', 'ICD9CM:200.86', 'ICD9CM:200.87', 'ICD9CM:200.88', 'ICD9CM:202.00', 'ICD9CM:202.01', 'ICD9CM:202.02', 'ICD9CM:202.03', 'ICD9CM:202.04', 'ICD9CM:202.05', 'ICD9CM:202.06', 'ICD9CM:202.07', 'ICD9CM:202.08', 'ICD9CM:202.10', 'ICD9CM:202.11', 'ICD9CM:202.12', 'ICD9CM:202.13', 'ICD9CM:202.14', 'ICD9CM:202.15', 'ICD9CM:202.16', 'ICD9CM:202.17', 'ICD9CM:202.18', 'ICD9CM:202.20', 'ICD9CM:202.21', 'ICD9CM:202.22', 'ICD9CM:202.23', 'ICD9CM:202.24', 'ICD9CM:202.25', 'ICD9CM:202.26', 'ICD9CM:202.27', 'ICD9CM:202.28', 'ICD9CM:202.70', 'ICD9CM:202.71', 'ICD9CM:202.72', 'ICD9CM:202.73', 'ICD9CM:202.74', 'ICD9CM:202.75', 'ICD9CM:202.76', 'ICD9CM:202.77', 'ICD9CM:202.78', 'ICD9CM:202.80', 'ICD9CM:202.81', 'ICD9CM:202.82', 'ICD9CM:202.83', 'ICD9CM:202.84', 'ICD9CM:202.85', 'ICD9CM:202.86', 'ICD9CM:202.87', 'ICD9CM:202.88', 'ICD9CM:202.90', 'ICD9CM:202.91', 'ICD9CM:202.92', 'ICD9CM:202.93', 'ICD9CM:202.94', 'ICD9CM:202.95', 'ICD9CM:202.96', 'ICD9CM:202.97', 'ICD9CM:202.98', 'ICD9CM:V10.71', 'ICD9CM:V10.79'):
            results_ccs1["non_hodgkins_lymph"].append(1)
        else: results_ccs1["non_hodgkins_lymph"].append(0)
    print("Completed Binary Recode of: non_hodgkins_lymph")

    # Leukemias
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:202.40', 'ICD9CM:202.41', 'ICD9CM:202.42', 'ICD9CM:202.43', 'ICD9CM:202.44', 'ICD9CM:202.45', 'ICD9CM:202.46', 'ICD9CM:202.47', 'ICD9CM:202.48', 'ICD9CM:203.1', 'ICD9CM:203.10', 'ICD9CM:203.11', 'ICD9CM:203.12', 'ICD9CM:204.0', 'ICD9CM:204.00', 'ICD9CM:204.01', 'ICD9CM:204.02', 'ICD9CM:204.1', 'ICD9CM:204.10', 'ICD9CM:204.11', 'ICD9CM:204.12', 'ICD9CM:204.2', 'ICD9CM:204.20', 'ICD9CM:204.21', 'ICD9CM:204.22', 'ICD9CM:204.8', 'ICD9CM:204.80', 'ICD9CM:204.81', 'ICD9CM:204.82', 'ICD9CM:204.9', 'ICD9CM:204.90', 'ICD9CM:204.91', 'ICD9CM:204.92', 'ICD9CM:205.0', 'ICD9CM:205.00', 'ICD9CM:205.01', 'ICD9CM:205.02', 'ICD9CM:205.1', 'ICD9CM:205.10', 'ICD9CM:205.11', 'ICD9CM:205.12', 'ICD9CM:205.2', 'ICD9CM:205.20', 'ICD9CM:205.21', 'ICD9CM:205.22', 'ICD9CM:205.3', 'ICD9CM:205.30', 'ICD9CM:205.31', 'ICD9CM:205.32', 'ICD9CM:205.8', 'ICD9CM:205.80', 'ICD9CM:205.81', 'ICD9CM:205.82', 'ICD9CM:205.9', 'ICD9CM:205.90', 'ICD9CM:205.91', 'ICD9CM:205.92', 'ICD9CM:206.0', 'ICD9CM:206.00', 'ICD9CM:206.01', 'ICD9CM:206.02', 'ICD9CM:206.1', 'ICD9CM:206.10', 'ICD9CM:206.11', 'ICD9CM:206.12', 'ICD9CM:206.2', 'ICD9CM:206.20', 'ICD9CM:206.21', 'ICD9CM:206.22', 'ICD9CM:206.8', 'ICD9CM:206.80', 'ICD9CM:206.81', 'ICD9CM:206.82', 'ICD9CM:206.9', 'ICD9CM:206.90', 'ICD9CM:206.91', 'ICD9CM:206.92', 'ICD9CM:207.0', 'ICD9CM:207.00', 'ICD9CM:207.01', 'ICD9CM:207.02', 'ICD9CM:207.1', 'ICD9CM:207.10', 'ICD9CM:207.11', 'ICD9CM:207.12', 'ICD9CM:207.2', 'ICD9CM:207.20', 'ICD9CM:207.21', 'ICD9CM:207.22', 'ICD9CM:207.8', 'ICD9CM:207.80', 'ICD9CM:207.81', 'ICD9CM:207.82', 'ICD9CM:208.0', 'ICD9CM:208.00', 'ICD9CM:208.01', 'ICD9CM:208.02', 'ICD9CM:208.1', 'ICD9CM:208.10', 'ICD9CM:208.11', 'ICD9CM:208.12', 'ICD9CM:208.2', 'ICD9CM:208.20', 'ICD9CM:208.21', 'ICD9CM:208.22', 'ICD9CM:208.8', 'ICD9CM:208.80', 'ICD9CM:208.81', 'ICD9CM:208.82', 'ICD9CM:208.9', 'ICD9CM:208.90', 'ICD9CM:208.91', 'ICD9CM:208.92', 'ICD9CM:V10.60', 'ICD9CM:V10.61', 'ICD9CM:V10.62', 'ICD9CM:V10.63', 'ICD9CM:V10.69'):
            results_ccs1["leukemia"].append(1)
        else: results_ccs1["leukemia"].append(0)
    print("Completed Binary Recode of: leukemia")

    # Multiple_myeloma
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:203.0', 'ICD9CM:203.00', 'ICD9CM:203.01', 'ICD9CM:203.02', 'ICD9CM:203.8', 'ICD9CM:203.80', 'ICD9CM:203.81', 'ICD9CM:203.82'):
            results_ccs1["mult_myeloma"].append(1)
        else: results_ccs1["mult_myeloma"].append(0)
    print("Completed Binary Recode of: mult_myeloma")

    # Cancer;_other_and_unspecified_primary
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:164.0', 'ICD9CM:164.1', 'ICD9CM:164.2', 'ICD9CM:164.3', 'ICD9CM:164.8', 'ICD9CM:164.9', 'ICD9CM:176.0', 'ICD9CM:176.1', 'ICD9CM:176.2', 'ICD9CM:176.3', 'ICD9CM:176.4', 'ICD9CM:176.5', 'ICD9CM:176.8', 'ICD9CM:176.9', 'ICD9CM:190.0', 'ICD9CM:190.1', 'ICD9CM:190.2', 'ICD9CM:190.3', 'ICD9CM:190.4', 'ICD9CM:190.5', 'ICD9CM:190.6', 'ICD9CM:190.7', 'ICD9CM:190.8', 'ICD9CM:190.9', 'ICD9CM:194.0', 'ICD9CM:194.1', 'ICD9CM:194.3', 'ICD9CM:194.4', 'ICD9CM:194.5', 'ICD9CM:194.6', 'ICD9CM:194.8', 'ICD9CM:194.9', 'ICD9CM:195.1', 'ICD9CM:195.2', 'ICD9CM:195.3', 'ICD9CM:195.4', 'ICD9CM:195.5', 'ICD9CM:195.8', 'ICD9CM:202.30', 'ICD9CM:202.31', 'ICD9CM:202.32', 'ICD9CM:202.33', 'ICD9CM:202.34', 'ICD9CM:202.35', 'ICD9CM:202.36', 'ICD9CM:202.37', 'ICD9CM:202.38', 'ICD9CM:202.50', 'ICD9CM:202.51', 'ICD9CM:202.52', 'ICD9CM:202.53', 'ICD9CM:202.54', 'ICD9CM:202.55', 'ICD9CM:202.56', 'ICD9CM:202.57', 'ICD9CM:202.58', 'ICD9CM:202.60', 'ICD9CM:202.61', 'ICD9CM:202.62', 'ICD9CM:202.63', 'ICD9CM:202.64', 'ICD9CM:202.65', 'ICD9CM:202.66', 'ICD9CM:202.67', 'ICD9CM:202.68', 'ICD9CM:209.22', 'ICD9CM:209.25', 'ICD9CM:209.26', 'ICD9CM:209.27', 'ICD9CM:234.0', 'ICD9CM:234.8', 'ICD9CM:234.9', 'ICD9CM:795.1', 'ICD9CM:795.10', 'ICD9CM:795.11', 'ICD9CM:795.12', 'ICD9CM:795.13', 'ICD9CM:795.14', 'ICD9CM:V10.29', 'ICD9CM:V10.81', 'ICD9CM:V10.84', 'ICD9CM:V10.88', 'ICD9CM:V10.89', 'ICD9CM:V10.9', 'ICD9CM:V10.90', 'ICD9CM:V10.91', 'ICD9CM:V71.1'):
            results_ccs1["other_ca"].append(1)
        else: results_ccs1["other_ca"].append(0)
    print("Completed Binary Recode of: other_ca")

    # Secondary_malignancies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:196.0', 'ICD9CM:196.1', 'ICD9CM:196.2', 'ICD9CM:196.3', 'ICD9CM:196.5', 'ICD9CM:196.6', 'ICD9CM:196.8', 'ICD9CM:196.9', 'ICD9CM:197.0', 'ICD9CM:197.1', 'ICD9CM:197.2', 'ICD9CM:197.3', 'ICD9CM:197.4', 'ICD9CM:197.5', 'ICD9CM:197.6', 'ICD9CM:197.7', 'ICD9CM:197.8', 'ICD9CM:198.0', 'ICD9CM:198.1', 'ICD9CM:198.2', 'ICD9CM:198.3', 'ICD9CM:198.4', 'ICD9CM:198.5', 'ICD9CM:198.6', 'ICD9CM:198.7', 'ICD9CM:198.81', 'ICD9CM:198.82', 'ICD9CM:198.89', 'ICD9CM:209.71', 'ICD9CM:209.72', 'ICD9CM:209.73', 'ICD9CM:209.74', 'ICD9CM:511.81', 'ICD9CM:789.51'):
            results_ccs1["secndry_malig"].append(1)
        else: results_ccs1["secndry_malig"].append(0)
    print("Completed Binary Recode of: secndry_malig")

    # Malignant_neoplasm_without_specification_of_site
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:199.0', 'ICD9CM:199.1', 'ICD9CM:199.2', 'ICD9CM:209.20', 'ICD9CM:209.29', 'ICD9CM:209.30', 'ICD9CM:209.70', 'ICD9CM:209.75', 'ICD9CM:209.79'):
            results_ccs1["malig_neoplasm"].append(1)
        else: results_ccs1["malig_neoplasm"].append(0)
    print("Completed Binary Recode of: malig_neoplasm")

    # Neoplasms_of_unspecified_nature_or_uncertain_behavior
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:235.0', 'ICD9CM:235.1', 'ICD9CM:235.2', 'ICD9CM:235.3', 'ICD9CM:235.4', 'ICD9CM:235.5', 'ICD9CM:235.6', 'ICD9CM:235.7', 'ICD9CM:235.8', 'ICD9CM:235.9', 'ICD9CM:236.0', 'ICD9CM:236.1', 'ICD9CM:236.2', 'ICD9CM:236.3', 'ICD9CM:236.4', 'ICD9CM:236.5', 'ICD9CM:236.6', 'ICD9CM:236.7', 'ICD9CM:236.90', 'ICD9CM:236.91', 'ICD9CM:236.99', 'ICD9CM:237.0', 'ICD9CM:237.1', 'ICD9CM:237.2', 'ICD9CM:237.3', 'ICD9CM:237.4', 'ICD9CM:237.5', 'ICD9CM:237.6', 'ICD9CM:237.7', 'ICD9CM:237.70', 'ICD9CM:237.71', 'ICD9CM:237.72', 'ICD9CM:237.73', 'ICD9CM:237.79', 'ICD9CM:237.9', 'ICD9CM:238.0', 'ICD9CM:238.1', 'ICD9CM:238.2', 'ICD9CM:238.3', 'ICD9CM:238.4', 'ICD9CM:238.5', 'ICD9CM:238.6', 'ICD9CM:238.7', 'ICD9CM:238.71', 'ICD9CM:238.72', 'ICD9CM:238.73', 'ICD9CM:238.74', 'ICD9CM:238.75', 'ICD9CM:238.76', 'ICD9CM:238.77', 'ICD9CM:238.79', 'ICD9CM:238.8', 'ICD9CM:238.9', 'ICD9CM:239.0', 'ICD9CM:239.1', 'ICD9CM:239.2', 'ICD9CM:239.3', 'ICD9CM:239.4', 'ICD9CM:239.5', 'ICD9CM:239.6', 'ICD9CM:239.7', 'ICD9CM:239.8', 'ICD9CM:239.81', 'ICD9CM:239.89', 'ICD9CM:239.9'):
            results_ccs1["neoplasm_unspec"].append(1)
        else: results_ccs1["neoplasm_unspec"].append(0)
    print("Completed Binary Recode of: neoplasm_unspec")

    # Maintenance_chemotherapy;_radiotherapy
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V58.0', 'ICD9CM:V58.1', 'ICD9CM:V58.11', 'ICD9CM:V58.12', 'ICD9CM:V66.1', 'ICD9CM:V66.2', 'ICD9CM:V67.1', 'ICD9CM:V67.2'):
            results_ccs1["maint_chemo"].append(1)
        else: results_ccs1["maint_chemo"].append(0)
    print("Completed Binary Recode of: maint_chemo")

    # Benign_neoplasm_of_uterus
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:218.0', 'ICD9CM:218.1', 'ICD9CM:218.2', 'ICD9CM:218.9', 'ICD9CM:219.0', 'ICD9CM:219.1', 'ICD9CM:219.8', 'ICD9CM:219.9'):
            results_ccs1["ben_neoplasm_uterus"].append(1)
        else: results_ccs1["ben_neoplasm_uterus"].append(0)
    print("Completed Binary Recode of: ben_neoplasm_uterus")

    # Other_and_unspecified_benign_neoplasm
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:209.40', 'ICD9CM:209.41', 'ICD9CM:209.42', 'ICD9CM:209.43', 'ICD9CM:209.50', 'ICD9CM:209.51', 'ICD9CM:209.52', 'ICD9CM:209.53', 'ICD9CM:209.54', 'ICD9CM:209.55', 'ICD9CM:209.56', 'ICD9CM:209.57', 'ICD9CM:209.60', 'ICD9CM:209.61', 'ICD9CM:209.62', 'ICD9CM:209.63', 'ICD9CM:209.64', 'ICD9CM:209.65', 'ICD9CM:209.66', 'ICD9CM:209.67', 'ICD9CM:209.69', 'ICD9CM:210.0', 'ICD9CM:210.1', 'ICD9CM:210.2', 'ICD9CM:210.3', 'ICD9CM:210.4', 'ICD9CM:210.5', 'ICD9CM:210.6', 'ICD9CM:210.7', 'ICD9CM:210.8', 'ICD9CM:210.9', 'ICD9CM:211.0', 'ICD9CM:211.1', 'ICD9CM:211.2', 'ICD9CM:211.3', 'ICD9CM:211.4', 'ICD9CM:211.5', 'ICD9CM:211.6', 'ICD9CM:211.7', 'ICD9CM:211.8', 'ICD9CM:211.9', 'ICD9CM:212.0', 'ICD9CM:212.1', 'ICD9CM:212.2', 'ICD9CM:212.3', 'ICD9CM:212.4', 'ICD9CM:212.5', 'ICD9CM:212.6', 'ICD9CM:212.7', 'ICD9CM:212.8', 'ICD9CM:212.9', 'ICD9CM:213.0', 'ICD9CM:213.1', 'ICD9CM:213.2', 'ICD9CM:213.3', 'ICD9CM:213.4', 'ICD9CM:213.5', 'ICD9CM:213.6', 'ICD9CM:213.7', 'ICD9CM:213.8', 'ICD9CM:213.9', 'ICD9CM:214.0', 'ICD9CM:214.1', 'ICD9CM:214.2', 'ICD9CM:214.3', 'ICD9CM:214.4', 'ICD9CM:214.8', 'ICD9CM:214.9', 'ICD9CM:215.0', 'ICD9CM:215.2', 'ICD9CM:215.3', 'ICD9CM:215.4', 'ICD9CM:215.5', 'ICD9CM:215.6', 'ICD9CM:215.7', 'ICD9CM:215.8', 'ICD9CM:215.9', 'ICD9CM:216.0', 'ICD9CM:216.1', 'ICD9CM:216.2', 'ICD9CM:216.3', 'ICD9CM:216.4', 'ICD9CM:216.5', 'ICD9CM:216.6', 'ICD9CM:216.7', 'ICD9CM:216.8', 'ICD9CM:216.9', 'ICD9CM:217', 'ICD9CM:220', 'ICD9CM:221.0', 'ICD9CM:221.1', 'ICD9CM:221.2', 'ICD9CM:221.8', 'ICD9CM:221.9', 'ICD9CM:222.0', 'ICD9CM:222.1', 'ICD9CM:222.2', 'ICD9CM:222.3', 'ICD9CM:222.4', 'ICD9CM:222.8', 'ICD9CM:222.9', 'ICD9CM:223.0', 'ICD9CM:223.1', 'ICD9CM:223.2', 'ICD9CM:223.3', 'ICD9CM:223.81', 'ICD9CM:223.89', 'ICD9CM:223.9', 'ICD9CM:224.0', 'ICD9CM:224.1', 'ICD9CM:224.2', 'ICD9CM:224.3', 'ICD9CM:224.4', 'ICD9CM:224.5', 'ICD9CM:224.6', 'ICD9CM:224.7', 'ICD9CM:224.8', 'ICD9CM:224.9', 'ICD9CM:225.0', 'ICD9CM:225.1', 'ICD9CM:225.2', 'ICD9CM:225.3', 'ICD9CM:225.4', 'ICD9CM:225.8', 'ICD9CM:225.9', 'ICD9CM:226', 'ICD9CM:227.0', 'ICD9CM:227.1', 'ICD9CM:227.3', 'ICD9CM:227.4', 'ICD9CM:227.5', 'ICD9CM:227.6', 'ICD9CM:227.8', 'ICD9CM:227.9', 'ICD9CM:228.00', 'ICD9CM:228.01', 'ICD9CM:228.02', 'ICD9CM:228.03', 'ICD9CM:228.04', 'ICD9CM:228.09', 'ICD9CM:228.1', 'ICD9CM:229.0', 'ICD9CM:229.8', 'ICD9CM:229.9', 'ICD9CM:V12.72'):
            results_ccs1["other_ben_neoplasm"].append(1)
        else: results_ccs1["other_ben_neoplasm"].append(0)
    print("Completed Binary Recode of: other_ben_neoplasm")

    # Thyroid_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:240.0', 'ICD9CM:240.9', 'ICD9CM:241.0', 'ICD9CM:241.1', 'ICD9CM:241.9', 'ICD9CM:242.00', 'ICD9CM:242.01', 'ICD9CM:242.10', 'ICD9CM:242.11', 'ICD9CM:242.20', 'ICD9CM:242.21', 'ICD9CM:242.30', 'ICD9CM:242.31', 'ICD9CM:242.40', 'ICD9CM:242.41', 'ICD9CM:242.80', 'ICD9CM:242.81', 'ICD9CM:242.90', 'ICD9CM:242.91', 'ICD9CM:243', 'ICD9CM:244.0', 'ICD9CM:244.1', 'ICD9CM:244.2', 'ICD9CM:244.3', 'ICD9CM:244.8', 'ICD9CM:244.9', 'ICD9CM:245.0', 'ICD9CM:245.1', 'ICD9CM:245.2', 'ICD9CM:245.3', 'ICD9CM:245.4', 'ICD9CM:245.8', 'ICD9CM:245.9', 'ICD9CM:246.0', 'ICD9CM:246.1', 'ICD9CM:246.2', 'ICD9CM:246.3', 'ICD9CM:246.8', 'ICD9CM:246.9', 'ICD9CM:794.5'):
            results_ccs1["thyroid"].append(1)
        else: results_ccs1["thyroid"].append(0)
    print("Completed Binary Recode of: thyroid")

    # Diabetes_mellitus_without_complication
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:249.00', 'ICD9CM:250.00', 'ICD9CM:250.01', 'ICD9CM:790.2', 'ICD9CM:790.21', 'ICD9CM:790.22', 'ICD9CM:790.29', 'ICD9CM:791.5', 'ICD9CM:791.6', 'ICD9CM:V45.85', 'ICD9CM:V53.91', 'ICD9CM:V65.46'):
            results_ccs1["dm_wo_comp"].append(1)
        else: results_ccs1["dm_wo_comp"].append(0)
    print("Completed Binary Recode of: dm_wo_comp")

    # Diabetes_mellitus_with_complications
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:249.01', 'ICD9CM:249.10', 'ICD9CM:249.11', 'ICD9CM:249.20', 'ICD9CM:249.21', 'ICD9CM:249.30', 'ICD9CM:249.31', 'ICD9CM:249.40', 'ICD9CM:249.41', 'ICD9CM:249.50', 'ICD9CM:249.51', 'ICD9CM:249.60', 'ICD9CM:249.61', 'ICD9CM:249.70', 'ICD9CM:249.71', 'ICD9CM:249.80', 'ICD9CM:249.81', 'ICD9CM:249.90', 'ICD9CM:249.91', 'ICD9CM:250.02', 'ICD9CM:250.03', 'ICD9CM:250.10', 'ICD9CM:250.11', 'ICD9CM:250.12', 'ICD9CM:250.13', 'ICD9CM:250.20', 'ICD9CM:250.21', 'ICD9CM:250.22', 'ICD9CM:250.23', 'ICD9CM:250.30', 'ICD9CM:250.31', 'ICD9CM:250.32', 'ICD9CM:250.33', 'ICD9CM:250.40', 'ICD9CM:250.41', 'ICD9CM:250.42', 'ICD9CM:250.43', 'ICD9CM:250.50', 'ICD9CM:250.51', 'ICD9CM:250.52', 'ICD9CM:250.53', 'ICD9CM:250.60', 'ICD9CM:250.61', 'ICD9CM:250.62', 'ICD9CM:250.63', 'ICD9CM:250.70', 'ICD9CM:250.71', 'ICD9CM:250.72', 'ICD9CM:250.73', 'ICD9CM:250.80', 'ICD9CM:250.81', 'ICD9CM:250.82', 'ICD9CM:250.83', 'ICD9CM:250.90', 'ICD9CM:250.91', 'ICD9CM:250.92', 'ICD9CM:250.93'):
            results_ccs1["dm_w_comp"].append(1)
        else: results_ccs1["dm_w_comp"].append(0)
    print("Completed Binary Recode of: dm_w_comp")

    # Other_endocrine_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:251.0', 'ICD9CM:251.1', 'ICD9CM:251.2', 'ICD9CM:251.3', 'ICD9CM:251.4', 'ICD9CM:251.5', 'ICD9CM:251.8', 'ICD9CM:251.9', 'ICD9CM:252.0', 'ICD9CM:252.00', 'ICD9CM:252.01', 'ICD9CM:252.02', 'ICD9CM:252.08', 'ICD9CM:252.1', 'ICD9CM:252.8', 'ICD9CM:252.9', 'ICD9CM:253.0', 'ICD9CM:253.1', 'ICD9CM:253.2', 'ICD9CM:253.3', 'ICD9CM:253.4', 'ICD9CM:253.5', 'ICD9CM:253.6', 'ICD9CM:253.7', 'ICD9CM:253.8', 'ICD9CM:253.9', 'ICD9CM:254.0', 'ICD9CM:254.1', 'ICD9CM:254.8', 'ICD9CM:254.9', 'ICD9CM:255.0', 'ICD9CM:255.1', 'ICD9CM:255.10', 'ICD9CM:255.11', 'ICD9CM:255.12', 'ICD9CM:255.13', 'ICD9CM:255.14', 'ICD9CM:255.2', 'ICD9CM:255.3', 'ICD9CM:255.4', 'ICD9CM:255.41', 'ICD9CM:255.42', 'ICD9CM:255.5', 'ICD9CM:255.6', 'ICD9CM:255.8', 'ICD9CM:255.9', 'ICD9CM:256.0', 'ICD9CM:256.1', 'ICD9CM:256.2', 'ICD9CM:256.3', 'ICD9CM:256.4', 'ICD9CM:256.8', 'ICD9CM:256.9', 'ICD9CM:257.0', 'ICD9CM:257.1', 'ICD9CM:257.2', 'ICD9CM:257.8', 'ICD9CM:257.9', 'ICD9CM:258.0', 'ICD9CM:258.01', 'ICD9CM:258.1', 'ICD9CM:258.8', 'ICD9CM:258.9', 'ICD9CM:259.0', 'ICD9CM:259.1', 'ICD9CM:259.2', 'ICD9CM:259.3', 'ICD9CM:259.4', 'ICD9CM:259.5', 'ICD9CM:259.50', 'ICD9CM:259.51', 'ICD9CM:259.52', 'ICD9CM:259.8', 'ICD9CM:259.9', 'ICD9CM:794.6'):
            results_ccs1["other_endocrine"].append(1)
        else: results_ccs1["other_endocrine"].append(0)
    print("Completed Binary Recode of: other_endocrine")

    # Nutritional_deficiencies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:260', 'ICD9CM:261', 'ICD9CM:262', 'ICD9CM:263.0', 'ICD9CM:263.1', 'ICD9CM:263.2', 'ICD9CM:263.8', 'ICD9CM:263.9', 'ICD9CM:264.0', 'ICD9CM:264.1', 'ICD9CM:264.2', 'ICD9CM:264.3', 'ICD9CM:264.4', 'ICD9CM:264.5', 'ICD9CM:264.6', 'ICD9CM:264.7', 'ICD9CM:264.8', 'ICD9CM:264.9', 'ICD9CM:265.0', 'ICD9CM:265.1', 'ICD9CM:265.2', 'ICD9CM:266.0', 'ICD9CM:266.1', 'ICD9CM:266.2', 'ICD9CM:266.9', 'ICD9CM:267', 'ICD9CM:268.0', 'ICD9CM:268.1', 'ICD9CM:268.2', 'ICD9CM:268.9', 'ICD9CM:269.0', 'ICD9CM:269.1', 'ICD9CM:269.2', 'ICD9CM:269.3', 'ICD9CM:269.8', 'ICD9CM:269.9', 'ICD9CM:799.4', 'ICD9CM:V12.1'):
            results_ccs1["nutrition"].append(1)
        else: results_ccs1["nutrition"].append(0)
    print("Completed Binary Recode of: nutrition")

    # Disorders_of_lipid_metabolism
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:272.0', 'ICD9CM:272.1', 'ICD9CM:272.2', 'ICD9CM:272.3', 'ICD9CM:272.4'):
            results_ccs1["lipid_metabo"].append(1)
        else: results_ccs1["lipid_metabo"].append(0)
    print("Completed Binary Recode of: lipid_metabo")

    # Gout_and_other_crystal_arthropathies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:274.0', 'ICD9CM:274.00', 'ICD9CM:274.01', 'ICD9CM:274.02', 'ICD9CM:274.03', 'ICD9CM:274.10', 'ICD9CM:274.11', 'ICD9CM:274.19', 'ICD9CM:274.81', 'ICD9CM:274.82', 'ICD9CM:274.89', 'ICD9CM:274.9', 'ICD9CM:712.10', 'ICD9CM:712.11', 'ICD9CM:712.12', 'ICD9CM:712.13', 'ICD9CM:712.14', 'ICD9CM:712.15', 'ICD9CM:712.16', 'ICD9CM:712.17', 'ICD9CM:712.18', 'ICD9CM:712.19', 'ICD9CM:712.20', 'ICD9CM:712.21', 'ICD9CM:712.22', 'ICD9CM:712.23', 'ICD9CM:712.24', 'ICD9CM:712.25', 'ICD9CM:712.26', 'ICD9CM:712.27', 'ICD9CM:712.28', 'ICD9CM:712.29', 'ICD9CM:712.30', 'ICD9CM:712.31', 'ICD9CM:712.32', 'ICD9CM:712.33', 'ICD9CM:712.34', 'ICD9CM:712.35', 'ICD9CM:712.36', 'ICD9CM:712.37', 'ICD9CM:712.38', 'ICD9CM:712.39', 'ICD9CM:712.80', 'ICD9CM:712.81', 'ICD9CM:712.82', 'ICD9CM:712.83', 'ICD9CM:712.84', 'ICD9CM:712.85', 'ICD9CM:712.86', 'ICD9CM:712.87', 'ICD9CM:712.88', 'ICD9CM:712.89', 'ICD9CM:712.90', 'ICD9CM:712.91', 'ICD9CM:712.92', 'ICD9CM:712.93', 'ICD9CM:712.94', 'ICD9CM:712.95', 'ICD9CM:712.96', 'ICD9CM:712.97', 'ICD9CM:712.98', 'ICD9CM:712.99'):
            results_ccs1["gout"].append(1)
        else: results_ccs1["gout"].append(0)
    print("Completed Binary Recode of: gout")

    # Fluid_and_electrolyte_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:276.0', 'ICD9CM:276.1', 'ICD9CM:276.2', 'ICD9CM:276.3', 'ICD9CM:276.4', 'ICD9CM:276.5', 'ICD9CM:276.50', 'ICD9CM:276.51', 'ICD9CM:276.52', 'ICD9CM:276.6', 'ICD9CM:276.69', 'ICD9CM:276.7', 'ICD9CM:276.8', 'ICD9CM:276.9', 'ICD9CM:995.1'):
            results_ccs1["fluid_electrolyte"].append(1)
        else: results_ccs1["fluid_electrolyte"].append(0)
    print("Completed Binary Recode of: fluid_electrolyte")

    # Cystic_fibrosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09'):
            results_ccs1["cyst_fibrosis"].append(1)
        else: results_ccs1["cyst_fibrosis"].append(0)
    print("Completed Binary Recode of: cyst_fibrosis")

    # Immunity_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:279.00', 'ICD9CM:279.01', 'ICD9CM:279.02', 'ICD9CM:279.03', 'ICD9CM:279.04', 'ICD9CM:279.05', 'ICD9CM:279.06', 'ICD9CM:279.09', 'ICD9CM:279.11', 'ICD9CM:279.12', 'ICD9CM:279.13', 'ICD9CM:279.2', 'ICD9CM:279.3', 'ICD9CM:279.4', 'ICD9CM:279.41', 'ICD9CM:279.49', 'ICD9CM:279.8', 'ICD9CM:279.9'):
            results_ccs1["immunity"].append(1)
        else: results_ccs1["immunity"].append(0)
    print("Completed Binary Recode of: immunity")

    # Other_nutritional;_endocrine;_and_metabolic_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:270.0', 'ICD9CM:270.1', 'ICD9CM:270.2', 'ICD9CM:270.3', 'ICD9CM:270.4', 'ICD9CM:270.5', 'ICD9CM:270.6', 'ICD9CM:270.7', 'ICD9CM:270.8', 'ICD9CM:270.9', 'ICD9CM:271.0', 'ICD9CM:271.1', 'ICD9CM:271.2', 'ICD9CM:271.3', 'ICD9CM:271.4', 'ICD9CM:271.8', 'ICD9CM:271.9', 'ICD9CM:272.5', 'ICD9CM:272.6', 'ICD9CM:272.7', 'ICD9CM:272.8', 'ICD9CM:272.9', 'ICD9CM:273.0', 'ICD9CM:273.1', 'ICD9CM:273.2', 'ICD9CM:273.3', 'ICD9CM:273.4', 'ICD9CM:273.8', 'ICD9CM:273.9', 'ICD9CM:275.0', 'ICD9CM:275.01', 'ICD9CM:275.02', 'ICD9CM:275.03', 'ICD9CM:275.09', 'ICD9CM:275.1', 'ICD9CM:275.2', 'ICD9CM:275.3', 'ICD9CM:275.4', 'ICD9CM:275.40', 'ICD9CM:275.41', 'ICD9CM:275.42', 'ICD9CM:275.49', 'ICD9CM:275.5', 'ICD9CM:275.8', 'ICD9CM:275.9', 'ICD9CM:277.1', 'ICD9CM:277.2', 'ICD9CM:277.3', 'ICD9CM:277.30', 'ICD9CM:277.31', 'ICD9CM:277.39', 'ICD9CM:277.4', 'ICD9CM:277.5', 'ICD9CM:277.6', 'ICD9CM:277.7', 'ICD9CM:277.8', 'ICD9CM:277.81', 'ICD9CM:277.82', 'ICD9CM:277.84', 'ICD9CM:277.85', 'ICD9CM:277.86', 'ICD9CM:277.87', 'ICD9CM:277.89', 'ICD9CM:277.9', 'ICD9CM:278.0', 'ICD9CM:278.00', 'ICD9CM:278.01', 'ICD9CM:278.02', 'ICD9CM:278.03', 'ICD9CM:278.1', 'ICD9CM:278.2', 'ICD9CM:278.3', 'ICD9CM:278.4', 'ICD9CM:278.8', 'ICD9CM:783.1', 'ICD9CM:783.2', 'ICD9CM:783.21', 'ICD9CM:783.22', 'ICD9CM:783.3', 'ICD9CM:783.4', 'ICD9CM:783.40', 'ICD9CM:783.41', 'ICD9CM:783.42', 'ICD9CM:783.43', 'ICD9CM:783.5', 'ICD9CM:783.7', 'ICD9CM:783.9', 'ICD9CM:793.91', 'ICD9CM:794.7', 'ICD9CM:795.7', 'ICD9CM:V12.2', 'ICD9CM:V12.21', 'ICD9CM:V12.29', 'ICD9CM:V85.0', 'ICD9CM:V85.21', 'ICD9CM:V85.22', 'ICD9CM:V85.23', 'ICD9CM:V85.24', 'ICD9CM:V85.25', 'ICD9CM:V85.30', 'ICD9CM:V85.31', 'ICD9CM:V85.32', 'ICD9CM:V85.33', 'ICD9CM:V85.34', 'ICD9CM:V85.35', 'ICD9CM:V85.36', 'ICD9CM:V85.37', 'ICD9CM:V85.38', 'ICD9CM:V85.39', 'ICD9CM:V85.4', 'ICD9CM:V85.41', 'ICD9CM:V85.42', 'ICD9CM:V85.43', 'ICD9CM:V85.44', 'ICD9CM:V85.45', 'ICD9CM:V85.51', 'ICD9CM:V85.53', 'ICD9CM:V85.54'):
            results_ccs1["other_metabo"].append(1)
        else: results_ccs1["other_metabo"].append(0)
    print("Completed Binary Recode of: other_metabo")

    # Deficiency_and_other_anemia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:280.0', 'ICD9CM:280.1', 'ICD9CM:280.8', 'ICD9CM:280.9', 'ICD9CM:281.0', 'ICD9CM:281.1', 'ICD9CM:281.2', 'ICD9CM:281.3', 'ICD9CM:281.4', 'ICD9CM:281.8', 'ICD9CM:281.9', 'ICD9CM:282.0', 'ICD9CM:282.1', 'ICD9CM:282.2', 'ICD9CM:282.3', 'ICD9CM:282.4', 'ICD9CM:282.40', 'ICD9CM:282.43', 'ICD9CM:282.44', 'ICD9CM:282.45', 'ICD9CM:282.46', 'ICD9CM:282.47', 'ICD9CM:282.49', 'ICD9CM:282.7', 'ICD9CM:282.8', 'ICD9CM:282.9', 'ICD9CM:283.0', 'ICD9CM:283.1', 'ICD9CM:283.10', 'ICD9CM:283.11', 'ICD9CM:283.19', 'ICD9CM:283.2', 'ICD9CM:283.9', 'ICD9CM:284.0', 'ICD9CM:284.01', 'ICD9CM:284.09', 'ICD9CM:284.1', 'ICD9CM:284.11', 'ICD9CM:284.12', 'ICD9CM:284.19', 'ICD9CM:284.2', 'ICD9CM:284.8', 'ICD9CM:284.81', 'ICD9CM:284.89', 'ICD9CM:284.9', 'ICD9CM:285.0', 'ICD9CM:285.21', 'ICD9CM:285.22', 'ICD9CM:285.29', 'ICD9CM:285.8', 'ICD9CM:285.9'):
            results_ccs1["other_anemia"].append(1)
        else: results_ccs1["other_anemia"].append(0)
    print("Completed Binary Recode of: other_anemia")

    # Acute_posthemorrhagic_anemia
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:285.1':
            results_ccs1["post_hemorr_anemia"].append(1)
        else: results_ccs1["post_hemorr_anemia"].append(0)
    print("Completed Binary Recode of: post_hemorr_anemia")

    # Sickle_cell_anemia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:282.41', 'ICD9CM:282.42', 'ICD9CM:282.5', 'ICD9CM:282.60', 'ICD9CM:282.61', 'ICD9CM:282.62', 'ICD9CM:282.63', 'ICD9CM:282.64', 'ICD9CM:282.68', 'ICD9CM:282.69'):
            results_ccs1["sickle_cell"].append(1)
        else: results_ccs1["sickle_cell"].append(0)
    print("Completed Binary Recode of: sickle_cell")

    # Coagulation_and_hemorrhagic_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:286.0', 'ICD9CM:286.1', 'ICD9CM:286.2', 'ICD9CM:286.3', 'ICD9CM:286.4', 'ICD9CM:286.5', 'ICD9CM:286.52', 'ICD9CM:286.53', 'ICD9CM:286.59', 'ICD9CM:286.6', 'ICD9CM:286.7', 'ICD9CM:286.9', 'ICD9CM:287.0', 'ICD9CM:287.1', 'ICD9CM:287.2', 'ICD9CM:287.3', 'ICD9CM:287.30', 'ICD9CM:287.31', 'ICD9CM:287.32', 'ICD9CM:287.33', 'ICD9CM:287.39', 'ICD9CM:287.4', 'ICD9CM:287.49', 'ICD9CM:287.5', 'ICD9CM:287.8', 'ICD9CM:287.9', 'ICD9CM:289.81', 'ICD9CM:289.82', 'ICD9CM:289.84', 'ICD9CM:782.7'):
            results_ccs1["coag_anemia"].append(1)
        else: results_ccs1["coag_anemia"].append(0)
    print("Completed Binary Recode of: coag_anemia")

    # Diseases_of_white_blood_cells
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:288.0', 'ICD9CM:288.00', 'ICD9CM:288.01', 'ICD9CM:288.02', 'ICD9CM:288.03', 'ICD9CM:288.04', 'ICD9CM:288.09', 'ICD9CM:288.1', 'ICD9CM:288.2', 'ICD9CM:288.3', 'ICD9CM:288.4', 'ICD9CM:288.50', 'ICD9CM:288.51', 'ICD9CM:288.59', 'ICD9CM:288.60', 'ICD9CM:288.61', 'ICD9CM:288.62', 'ICD9CM:288.63', 'ICD9CM:288.64', 'ICD9CM:288.65', 'ICD9CM:288.66', 'ICD9CM:288.69', 'ICD9CM:288.8', 'ICD9CM:288.9', 'ICD9CM:289.53'):
            results_ccs1["wbc_disease"].append(1)
        else: results_ccs1["wbc_disease"].append(0)
    print("Completed Binary Recode of: wbc_disease")

    # Other_hematologic_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:289.0', 'ICD9CM:289.4', 'ICD9CM:289.50', 'ICD9CM:289.51', 'ICD9CM:289.52', 'ICD9CM:289.59', 'ICD9CM:289.6', 'ICD9CM:289.7', 'ICD9CM:289.8', 'ICD9CM:289.83', 'ICD9CM:289.89', 'ICD9CM:289.9', 'ICD9CM:790.0', 'ICD9CM:790.01', 'ICD9CM:790.09', 'ICD9CM:V12.3', 'ICD9CM:V58.2'):
            results_ccs1["other_heme"].append(1)
        else: results_ccs1["other_heme"].append(0)
    print("Completed Binary Recode of: other_heme")

    # Meningitis_(_except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:003.21', 'ICD9CM:036.0', 'ICD9CM:047.0', 'ICD9CM:047.1', 'ICD9CM:047.8', 'ICD9CM:047.9', 'ICD9CM:049.0', 'ICD9CM:049.1', 'ICD9CM:053.0', 'ICD9CM:054.72', 'ICD9CM:072.1', 'ICD9CM:100.81', 'ICD9CM:112.83', 'ICD9CM:114.2', 'ICD9CM:115.01', 'ICD9CM:115.11', 'ICD9CM:115.91', 'ICD9CM:320.0', 'ICD9CM:320.1', 'ICD9CM:320.2', 'ICD9CM:320.3', 'ICD9CM:320.7', 'ICD9CM:320.8', 'ICD9CM:320.81', 'ICD9CM:320.82', 'ICD9CM:320.89', 'ICD9CM:320.9', 'ICD9CM:321.0', 'ICD9CM:321.1', 'ICD9CM:321.2', 'ICD9CM:321.3', 'ICD9CM:321.4', 'ICD9CM:321.8', 'ICD9CM:322.0', 'ICD9CM:322.1', 'ICD9CM:322.2', 'ICD9CM:322.9'):
            results_ccs1["meningitis_notb"].append(1)
        else: results_ccs1["meningitis_notb"].append(0)
    print("Completed Binary Recode of: meningitis_notb")

    # Encephalitis_(_except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:036.1', 'ICD9CM:046.2', 'ICD9CM:049.8', 'ICD9CM:049.9', 'ICD9CM:052.0', 'ICD9CM:054.3', 'ICD9CM:055.0', 'ICD9CM:056.01', 'ICD9CM:058.21', 'ICD9CM:058.29', 'ICD9CM:062.0', 'ICD9CM:062.1', 'ICD9CM:062.2', 'ICD9CM:062.3', 'ICD9CM:062.4', 'ICD9CM:062.5', 'ICD9CM:062.8', 'ICD9CM:062.9', 'ICD9CM:063.0', 'ICD9CM:063.1', 'ICD9CM:063.2', 'ICD9CM:063.8', 'ICD9CM:063.9', 'ICD9CM:064', 'ICD9CM:066.2', 'ICD9CM:066.41', 'ICD9CM:072.2', 'ICD9CM:130.0', 'ICD9CM:139.0', 'ICD9CM:323.0', 'ICD9CM:323.01', 'ICD9CM:323.02', 'ICD9CM:323.1', 'ICD9CM:323.2', 'ICD9CM:323.4', 'ICD9CM:323.41', 'ICD9CM:323.42', 'ICD9CM:323.5', 'ICD9CM:323.51', 'ICD9CM:323.52', 'ICD9CM:323.6', 'ICD9CM:323.61', 'ICD9CM:323.62', 'ICD9CM:323.63', 'ICD9CM:323.7', 'ICD9CM:323.71', 'ICD9CM:323.72', 'ICD9CM:323.8', 'ICD9CM:323.81', 'ICD9CM:323.82', 'ICD9CM:323.9', 'ICD9CM:341.20', 'ICD9CM:341.21', 'ICD9CM:341.22'):
            results_ccs1["encephalitis_notb"].append(1)
        else: results_ccs1["encephalitis_notb"].append(0)
    print("Completed Binary Recode of: encephalitis_notb")

    # Other_CNS_infection_and_poliomyelitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:045.00', 'ICD9CM:045.01', 'ICD9CM:045.02', 'ICD9CM:045.03', 'ICD9CM:045.10', 'ICD9CM:045.11', 'ICD9CM:045.12', 'ICD9CM:045.13', 'ICD9CM:045.20', 'ICD9CM:045.21', 'ICD9CM:045.22', 'ICD9CM:045.23', 'ICD9CM:045.90', 'ICD9CM:045.91', 'ICD9CM:045.92', 'ICD9CM:045.93', 'ICD9CM:046.0', 'ICD9CM:046.1', 'ICD9CM:046.11', 'ICD9CM:046.19', 'ICD9CM:046.3', 'ICD9CM:046.71', 'ICD9CM:046.72', 'ICD9CM:046.79', 'ICD9CM:046.8', 'ICD9CM:046.9', 'ICD9CM:048', 'ICD9CM:138', 'ICD9CM:324.0', 'ICD9CM:324.1', 'ICD9CM:324.9', 'ICD9CM:326', 'ICD9CM:V12.02'):
            results_ccs1["other_cns"].append(1)
        else: results_ccs1["other_cns"].append(0)
    print("Completed Binary Recode of: other_cns")

    # Parkinson`_s_disease
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:332.0':
            results_ccs1["parkinsons"].append(1)
        else: results_ccs1["parkinsons"].append(0)
    print("Completed Binary Recode of: parkinsons")

    pd.DataFrame(results_ccs1).to_csv(output_filepath, encoding='utf-8')
    print("CDRN - CCS Dx Recode Part 1: Complete")
    print("")



###########################
###########################
###########################
###########################
###########################
###########################


def dx_convert2(df):

    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results2.csv'

    results_ccs2 = {"person_id":[],"condition_start_date":[],"mult_scler": [], "other_hered_degen": [], "paralysis": [], "epilepsy": [], "headache": [],"coma": [], "cataract": [], "retinopathy": [], "glaucoma": [], "blindness": [], "eye_inflam": [],
"other_eye": [], "otitis_media": [], "dizzy": [], "other_ear_sense": [], "other_ns_disorder": [],
"heart_valve": [], "peri_endo_carditis": [], "essential_htn": [], "htn_w_comp": [], "acute_mi": [],
"coronary_athero": [], "chest_pain_nos": [], "pulmonary_hd": [], "other_heart_disease": [],
"conduction": [], "cardiac_dysrhythm": [], "cardiac_arrest": [], "chf": [], "acute_cvd": [],
"occlu_cereb_artery": [], "other_cvd": [], "tran_cereb_isch": [], "late_effect_cvd": [], "pvd": [],
"artery_aneurysm": [], "artery_embolism": [], "other_circ": [], "phlebitis": [],
"varicose_vein": [], "hemorrhoid": [], "other_vein_lymph": [], "pneumonia": [], "influenza": [],
"acute_tonsil": [], "acute_bronch": [], "upper_resp_infec": [], "copd": [], "asthma": [],
"asp_pneumonitis": [], "pneumothorax": [], "resp_failure": [], "lung_disease": [],
"other_low_resp": [], "other_up_resp": [], "intestinal_infec": [], "teeth_jaw": [],
"mouth_disease": [], "esophagus": [], "gastro_ulcer": [], "gastritis": [], "other_stomach_duo": []}

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs2["person_id"].append(_)
    print("Number of person_id with missing dx history: ", len(results_ccs2["person_id"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs2["condition_start_date"].append(dt.datetime.strptime('12/31/13', "%m/%d/%y"))
    print("Number of start dates added for patients with missing dx history: ",
          len(results_ccs2["condition_start_date"]))
    
    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs2["mult_scler"].append(0)
        results_ccs2["other_hered_degen"].append(0)
        results_ccs2["paralysis"].append(0)
        results_ccs2["epilepsy"].append(0)
        results_ccs2["headache"].append(0)
        results_ccs2["coma"].append(0)
        results_ccs2["cataract"].append(0)
        results_ccs2["retinopathy"].append(0)
        results_ccs2["glaucoma"].append(0)
        results_ccs2["blindness"].append(0)
        results_ccs2["eye_inflam"].append(0)
        results_ccs2["other_eye"].append(0)
        results_ccs2["otitis_media"].append(0)
        results_ccs2["dizzy"].append(0)
        results_ccs2["other_ear_sense"].append(0)
        results_ccs2["other_ns_disorder"].append(0)
        results_ccs2["heart_valve"].append(0)
        results_ccs2["peri_endo_carditis"].append(0)
        results_ccs2["essential_htn"].append(0)
        results_ccs2["htn_w_comp"].append(0)
        results_ccs2["acute_mi"].append(0)
        results_ccs2["coronary_athero"].append(0)
        results_ccs2["chest_pain_nos"].append(0)
        results_ccs2["pulmonary_hd"].append(0)
        results_ccs2["other_heart_disease"].append(0)
        results_ccs2["conduction"].append(0)
        results_ccs2["cardiac_dysrhythm"].append(0)
        results_ccs2["cardiac_arrest"].append(0)
        results_ccs2["chf"].append(0)
        results_ccs2["acute_cvd"].append(0)
        results_ccs2["occlu_cereb_artery"].append(0)
        results_ccs2["other_cvd"].append(0)
        results_ccs2["tran_cereb_isch"].append(0)
        results_ccs2["late_effect_cvd"].append(0)
        results_ccs2["pvd"].append(0)
        results_ccs2["artery_aneurysm"].append(0)
        results_ccs2["artery_embolism"].append(0)
        results_ccs2["other_circ"].append(0)
        results_ccs2["phlebitis"].append(0)
        results_ccs2["varicose_vein"].append(0)
        results_ccs2["hemorrhoid"].append(0)
        results_ccs2["other_vein_lymph"].append(0)
        results_ccs2["pneumonia"].append(0)
        results_ccs2["influenza"].append(0)
        results_ccs2["acute_tonsil"].append(0)
        results_ccs2["acute_bronch"].append(0)
        results_ccs2["upper_resp_infec"].append(0)
        results_ccs2["copd"].append(0)
        results_ccs2["asthma"].append(0)
        results_ccs2["asp_pneumonitis"].append(0)
        results_ccs2["pneumothorax"].append(0)
        results_ccs2["resp_failure"].append(0)
        results_ccs2["lung_disease"].append(0)
        results_ccs2["other_low_resp"].append(0)
        results_ccs2["other_up_resp"].append(0)
        results_ccs2["intestinal_infec"].append(0)
        results_ccs2["teeth_jaw"].append(0)
        results_ccs2["mouth_disease"].append(0)
        results_ccs2["esophagus"].append(0)
        results_ccs2["gastro_ulcer"].append(0)
        results_ccs2["gastritis"].append(0)
        results_ccs2["other_stomach_duo"].append(0)
    print("Completed null dx recode for pts that are missing dx but meet visit criteria")

    for _ in df['person_id']:
        results_ccs2["person_id"].append(_)
    print("Number of patients in results_ccs2", len(results_ccs2["person_id"]))

    for _ in df['condition_start_date']:
        results_ccs2["condition_start_date"].append(_)
    print("Number of start dates in results_ccs2", len(results_ccs2["condition_start_date"]))

    # Multiple_sclerosis
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:340':
            results_ccs2["mult_scler"].append(1)
        else: results_ccs2["mult_scler"].append(0)
    print("Completed Binary Recode of: mult_scler")

    # Other_hereditary_and_degenerative_nervous_system_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:330.0', 'ICD9CM:330.1', 'ICD9CM:330.2', 'ICD9CM:330.3', 'ICD9CM:330.8', 'ICD9CM:330.9', 'ICD9CM:331.3', 'ICD9CM:331.4', 'ICD9CM:331.5', 'ICD9CM:331.6', 'ICD9CM:331.7', 'ICD9CM:331.81', 'ICD9CM:331.89', 'ICD9CM:331.9', 'ICD9CM:333.0', 'ICD9CM:333.1', 'ICD9CM:333.2', 'ICD9CM:333.3', 'ICD9CM:333.4', 'ICD9CM:333.5', 'ICD9CM:333.6', 'ICD9CM:333.7', 'ICD9CM:333.71', 'ICD9CM:333.72', 'ICD9CM:333.79', 'ICD9CM:333.81', 'ICD9CM:333.82', 'ICD9CM:333.83', 'ICD9CM:333.84', 'ICD9CM:333.85', 'ICD9CM:333.89', 'ICD9CM:333.90', 'ICD9CM:333.91', 'ICD9CM:333.93', 'ICD9CM:333.94', 'ICD9CM:333.99', 'ICD9CM:334.0', 'ICD9CM:334.1', 'ICD9CM:334.2', 'ICD9CM:334.3', 'ICD9CM:334.4', 'ICD9CM:334.8', 'ICD9CM:334.9', 'ICD9CM:335.0', 'ICD9CM:335.10', 'ICD9CM:335.11', 'ICD9CM:335.19', 'ICD9CM:335.20', 'ICD9CM:335.21', 'ICD9CM:335.22', 'ICD9CM:335.23', 'ICD9CM:335.24', 'ICD9CM:335.29', 'ICD9CM:335.8', 'ICD9CM:335.9', 'ICD9CM:336.0', 'ICD9CM:336.1', 'ICD9CM:336.2', 'ICD9CM:336.3', 'ICD9CM:336.8', 'ICD9CM:336.9', 'ICD9CM:337.0', 'ICD9CM:337.00', 'ICD9CM:337.01', 'ICD9CM:337.09', 'ICD9CM:337.1', 'ICD9CM:337.3', 'ICD9CM:337.9'):
            results_ccs2["other_hered_degen"].append(1)
        else: results_ccs2["other_hered_degen"].append(0)
    print("Completed Binary Recode of: other_hered_degen")

    # Paralysis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:342.0', 'ICD9CM:342.00', 'ICD9CM:342.01', 'ICD9CM:342.02', 'ICD9CM:342.1', 'ICD9CM:342.10', 'ICD9CM:342.11', 'ICD9CM:342.12', 'ICD9CM:342.80', 'ICD9CM:342.81', 'ICD9CM:342.82', 'ICD9CM:342.9', 'ICD9CM:342.90', 'ICD9CM:342.91', 'ICD9CM:342.92', 'ICD9CM:343.0', 'ICD9CM:343.1', 'ICD9CM:343.2', 'ICD9CM:343.3', 'ICD9CM:343.4', 'ICD9CM:343.8', 'ICD9CM:343.9', 'ICD9CM:344.0', 'ICD9CM:344.00', 'ICD9CM:344.01', 'ICD9CM:344.02', 'ICD9CM:344.03', 'ICD9CM:344.04', 'ICD9CM:344.09', 'ICD9CM:344.1', 'ICD9CM:344.2', 'ICD9CM:344.3', 'ICD9CM:344.30', 'ICD9CM:344.31', 'ICD9CM:344.32', 'ICD9CM:344.4', 'ICD9CM:344.40', 'ICD9CM:344.41', 'ICD9CM:344.42', 'ICD9CM:344.5', 'ICD9CM:344.60', 'ICD9CM:344.8', 'ICD9CM:344.81', 'ICD9CM:344.89', 'ICD9CM:344.9', 'ICD9CM:780.72', 'ICD9CM:781.4'):
            results_ccs2["paralysis"].append(1)
        else: results_ccs2["paralysis"].append(0)
    print("Completed Binary Recode of: paralysis")

    # Epilepsy;_convulsions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:345.0', 'ICD9CM:345.00', 'ICD9CM:345.01', 'ICD9CM:345.1', 'ICD9CM:345.10', 'ICD9CM:345.11', 'ICD9CM:345.2', 'ICD9CM:345.3', 'ICD9CM:345.4', 'ICD9CM:345.40', 'ICD9CM:345.41', 'ICD9CM:345.5', 'ICD9CM:345.50', 'ICD9CM:345.51', 'ICD9CM:345.6', 'ICD9CM:345.60', 'ICD9CM:345.61', 'ICD9CM:345.7', 'ICD9CM:345.70', 'ICD9CM:345.71', 'ICD9CM:345.8', 'ICD9CM:345.80', 'ICD9CM:345.81', 'ICD9CM:345.9', 'ICD9CM:345.90', 'ICD9CM:345.91', 'ICD9CM:780.3', 'ICD9CM:780.31', 'ICD9CM:780.32', 'ICD9CM:780.33', 'ICD9CM:780.39'):
            results_ccs2["epilepsy"].append(1)
        else: results_ccs2["epilepsy"].append(0)
    print("Completed Binary Recode of: epilepsy")

    # Headache;_including_migraine
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:339.00', 'ICD9CM:339.01', 'ICD9CM:339.02', 'ICD9CM:339.03', 'ICD9CM:339.04', 'ICD9CM:339.05', 'ICD9CM:339.09', 'ICD9CM:339.10', 'ICD9CM:339.11', 'ICD9CM:339.12', 'ICD9CM:339.20', 'ICD9CM:339.21', 'ICD9CM:339.22', 'ICD9CM:339.3', 'ICD9CM:339.41', 'ICD9CM:339.42', 'ICD9CM:339.43', 'ICD9CM:339.44', 'ICD9CM:339.81', 'ICD9CM:339.82', 'ICD9CM:339.83', 'ICD9CM:339.84', 'ICD9CM:339.85', 'ICD9CM:339.89', 'ICD9CM:346.0', 'ICD9CM:346.00', 'ICD9CM:346.01', 'ICD9CM:346.02', 'ICD9CM:346.03', 'ICD9CM:346.1', 'ICD9CM:346.10', 'ICD9CM:346.11', 'ICD9CM:346.12', 'ICD9CM:346.13', 'ICD9CM:346.2', 'ICD9CM:346.20', 'ICD9CM:346.21', 'ICD9CM:346.22', 'ICD9CM:346.23', 'ICD9CM:346.30', 'ICD9CM:346.31', 'ICD9CM:346.32', 'ICD9CM:346.33', 'ICD9CM:346.40', 'ICD9CM:346.41', 'ICD9CM:346.42', 'ICD9CM:346.43', 'ICD9CM:346.50', 'ICD9CM:346.51', 'ICD9CM:346.52', 'ICD9CM:346.53', 'ICD9CM:346.70', 'ICD9CM:346.71', 'ICD9CM:346.72', 'ICD9CM:346.73', 'ICD9CM:346.8', 'ICD9CM:346.80', 'ICD9CM:346.81', 'ICD9CM:346.82', 'ICD9CM:346.83', 'ICD9CM:346.9', 'ICD9CM:346.90', 'ICD9CM:346.91', 'ICD9CM:346.92', 'ICD9CM:346.93', 'ICD9CM:784.0'):
            results_ccs2["headache"].append(1)
        else: results_ccs2["headache"].append(0)
    print("Completed Binary Recode of: headache")

    # Coma;_stupor;_and_brain_damage
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:348.1', 'ICD9CM:780.0', 'ICD9CM:780.01', 'ICD9CM:780.03', 'ICD9CM:780.09'):
            results_ccs2["coma"].append(1)
        else: results_ccs2["coma"].append(0)
    print("Completed Binary Recode of: coma")

    # Cataract
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:366.00', 'ICD9CM:366.01', 'ICD9CM:366.02', 'ICD9CM:366.03', 'ICD9CM:366.04', 'ICD9CM:366.09', 'ICD9CM:366.10', 'ICD9CM:366.11', 'ICD9CM:366.12', 'ICD9CM:366.13', 'ICD9CM:366.14', 'ICD9CM:366.15', 'ICD9CM:366.16', 'ICD9CM:366.17', 'ICD9CM:366.18', 'ICD9CM:366.19', 'ICD9CM:366.20', 'ICD9CM:366.21', 'ICD9CM:366.22', 'ICD9CM:366.23', 'ICD9CM:366.30', 'ICD9CM:366.31', 'ICD9CM:366.32', 'ICD9CM:366.33', 'ICD9CM:366.34', 'ICD9CM:366.41', 'ICD9CM:366.42', 'ICD9CM:366.43', 'ICD9CM:366.44', 'ICD9CM:366.45', 'ICD9CM:366.46', 'ICD9CM:366.50', 'ICD9CM:366.51', 'ICD9CM:366.52', 'ICD9CM:366.53', 'ICD9CM:366.8', 'ICD9CM:366.9', 'ICD9CM:V43.1'):
            results_ccs2["cataract"].append(1)
        else: results_ccs2["cataract"].append(0)
    print("Completed Binary Recode of: cataract")

    # Retinal_detachments;_defects;_vascular_occlusion;_and_retinopathy
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:361.00', 'ICD9CM:361.01', 'ICD9CM:361.02', 'ICD9CM:361.03', 'ICD9CM:361.04', 'ICD9CM:361.05', 'ICD9CM:361.06', 'ICD9CM:361.07', 'ICD9CM:361.10', 'ICD9CM:361.11', 'ICD9CM:361.12', 'ICD9CM:361.13', 'ICD9CM:361.14', 'ICD9CM:361.19', 'ICD9CM:361.2', 'ICD9CM:361.30', 'ICD9CM:361.31', 'ICD9CM:361.32', 'ICD9CM:361.33', 'ICD9CM:361.81', 'ICD9CM:361.89', 'ICD9CM:361.9', 'ICD9CM:362.01', 'ICD9CM:362.02', 'ICD9CM:362.03', 'ICD9CM:362.04', 'ICD9CM:362.05', 'ICD9CM:362.06', 'ICD9CM:362.07', 'ICD9CM:362.10', 'ICD9CM:362.11', 'ICD9CM:362.12', 'ICD9CM:362.13', 'ICD9CM:362.14', 'ICD9CM:362.15', 'ICD9CM:362.16', 'ICD9CM:362.17', 'ICD9CM:362.18', 'ICD9CM:362.20', 'ICD9CM:362.21', 'ICD9CM:362.22', 'ICD9CM:362.23', 'ICD9CM:362.24', 'ICD9CM:362.25', 'ICD9CM:362.26', 'ICD9CM:362.27', 'ICD9CM:362.29', 'ICD9CM:362.30', 'ICD9CM:362.31', 'ICD9CM:362.32', 'ICD9CM:362.33', 'ICD9CM:362.34', 'ICD9CM:362.35', 'ICD9CM:362.36', 'ICD9CM:362.37', 'ICD9CM:362.40', 'ICD9CM:362.41', 'ICD9CM:362.42', 'ICD9CM:362.43', 'ICD9CM:362.50', 'ICD9CM:362.51', 'ICD9CM:362.52', 'ICD9CM:362.53', 'ICD9CM:362.54', 'ICD9CM:362.55', 'ICD9CM:362.56', 'ICD9CM:362.57', 'ICD9CM:362.60', 'ICD9CM:362.61', 'ICD9CM:362.62', 'ICD9CM:362.63', 'ICD9CM:362.64', 'ICD9CM:362.65', 'ICD9CM:362.66', 'ICD9CM:362.70', 'ICD9CM:362.71', 'ICD9CM:362.72', 'ICD9CM:362.73', 'ICD9CM:362.74', 'ICD9CM:362.75', 'ICD9CM:362.76', 'ICD9CM:362.77', 'ICD9CM:362.81', 'ICD9CM:362.82', 'ICD9CM:362.83', 'ICD9CM:362.84', 'ICD9CM:362.85', 'ICD9CM:362.89', 'ICD9CM:362.9'):
            results_ccs2["retinopathy"].append(1)
        else: results_ccs2["retinopathy"].append(0)
    print("Completed Binary Recode of: retinopathy")

    # Glaucoma
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:365.00', 'ICD9CM:365.01', 'ICD9CM:365.02', 'ICD9CM:365.03', 'ICD9CM:365.04', 'ICD9CM:365.05', 'ICD9CM:365.06', 'ICD9CM:365.10', 'ICD9CM:365.11', 'ICD9CM:365.12', 'ICD9CM:365.13', 'ICD9CM:365.14', 'ICD9CM:365.15', 'ICD9CM:365.20', 'ICD9CM:365.21', 'ICD9CM:365.22', 'ICD9CM:365.23', 'ICD9CM:365.24', 'ICD9CM:365.31', 'ICD9CM:365.32', 'ICD9CM:365.41', 'ICD9CM:365.42', 'ICD9CM:365.43', 'ICD9CM:365.44', 'ICD9CM:365.51', 'ICD9CM:365.52', 'ICD9CM:365.59', 'ICD9CM:365.60', 'ICD9CM:365.61', 'ICD9CM:365.62', 'ICD9CM:365.63', 'ICD9CM:365.64', 'ICD9CM:365.65', 'ICD9CM:365.70', 'ICD9CM:365.71', 'ICD9CM:365.72', 'ICD9CM:365.73', 'ICD9CM:365.74', 'ICD9CM:365.81', 'ICD9CM:365.82', 'ICD9CM:365.83', 'ICD9CM:365.89', 'ICD9CM:365.9'):
            results_ccs2["glaucoma"].append(1)
        else: results_ccs2["glaucoma"].append(0)
    print("Completed Binary Recode of: glaucoma")

    # Blindness_and_vision_defects
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:367.0', 'ICD9CM:367.1', 'ICD9CM:367.20', 'ICD9CM:367.21', 'ICD9CM:367.22', 'ICD9CM:367.31', 'ICD9CM:367.32', 'ICD9CM:367.4', 'ICD9CM:367.51', 'ICD9CM:367.52', 'ICD9CM:367.53', 'ICD9CM:367.81', 'ICD9CM:367.89', 'ICD9CM:367.9', 'ICD9CM:368.00', 'ICD9CM:368.01', 'ICD9CM:368.02', 'ICD9CM:368.03', 'ICD9CM:368.10', 'ICD9CM:368.11', 'ICD9CM:368.12', 'ICD9CM:368.13', 'ICD9CM:368.14', 'ICD9CM:368.15', 'ICD9CM:368.16', 'ICD9CM:368.2', 'ICD9CM:368.30', 'ICD9CM:368.31', 'ICD9CM:368.32', 'ICD9CM:368.33', 'ICD9CM:368.34', 'ICD9CM:368.40', 'ICD9CM:368.41', 'ICD9CM:368.42', 'ICD9CM:368.43', 'ICD9CM:368.44', 'ICD9CM:368.45', 'ICD9CM:368.46', 'ICD9CM:368.47', 'ICD9CM:368.51', 'ICD9CM:368.52', 'ICD9CM:368.53', 'ICD9CM:368.54', 'ICD9CM:368.55', 'ICD9CM:368.59', 'ICD9CM:368.60', 'ICD9CM:368.61', 'ICD9CM:368.62', 'ICD9CM:368.63', 'ICD9CM:368.69', 'ICD9CM:368.8', 'ICD9CM:368.9', 'ICD9CM:369.00', 'ICD9CM:369.01', 'ICD9CM:369.02', 'ICD9CM:369.03', 'ICD9CM:369.04', 'ICD9CM:369.05', 'ICD9CM:369.06', 'ICD9CM:369.07', 'ICD9CM:369.08', 'ICD9CM:369.10', 'ICD9CM:369.11', 'ICD9CM:369.12', 'ICD9CM:369.13', 'ICD9CM:369.14', 'ICD9CM:369.15', 'ICD9CM:369.16', 'ICD9CM:369.17', 'ICD9CM:369.18', 'ICD9CM:369.20', 'ICD9CM:369.21', 'ICD9CM:369.22', 'ICD9CM:369.23', 'ICD9CM:369.24', 'ICD9CM:369.25', 'ICD9CM:369.3', 'ICD9CM:369.4', 'ICD9CM:369.60', 'ICD9CM:369.61', 'ICD9CM:369.62', 'ICD9CM:369.63', 'ICD9CM:369.64', 'ICD9CM:369.65', 'ICD9CM:369.66', 'ICD9CM:369.67', 'ICD9CM:369.68', 'ICD9CM:369.69', 'ICD9CM:369.70', 'ICD9CM:369.71', 'ICD9CM:369.72', 'ICD9CM:369.73', 'ICD9CM:369.74', 'ICD9CM:369.75', 'ICD9CM:369.76', 'ICD9CM:369.8', 'ICD9CM:369.9', 'ICD9CM:V41.0'):
            results_ccs2["blindness"].append(1)
        else: results_ccs2["blindness"].append(0)
    print("Completed Binary Recode of: blindness")

    # Inflammation;_infection_of_eye_(_except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:021.3', 'ICD9CM:032.81', 'ICD9CM:053.20', 'ICD9CM:053.21', 'ICD9CM:053.22', 'ICD9CM:053.29', 'ICD9CM:054.40', 'ICD9CM:054.41', 'ICD9CM:054.42', 'ICD9CM:054.43', 'ICD9CM:054.44', 'ICD9CM:054.49', 'ICD9CM:055.71', 'ICD9CM:076.0', 'ICD9CM:076.1', 'ICD9CM:076.9', 'ICD9CM:077.0', 'ICD9CM:077.1', 'ICD9CM:077.2', 'ICD9CM:077.3', 'ICD9CM:077.4', 'ICD9CM:077.8', 'ICD9CM:077.9', 'ICD9CM:077.98', 'ICD9CM:077.99', 'ICD9CM:115.02', 'ICD9CM:115.12', 'ICD9CM:115.92', 'ICD9CM:130.1', 'ICD9CM:130.2', 'ICD9CM:139.1', 'ICD9CM:360.00', 'ICD9CM:360.01', 'ICD9CM:360.02', 'ICD9CM:360.03', 'ICD9CM:360.04', 'ICD9CM:360.11', 'ICD9CM:360.12', 'ICD9CM:360.13', 'ICD9CM:360.14', 'ICD9CM:360.19', 'ICD9CM:363.00', 'ICD9CM:363.01', 'ICD9CM:363.03', 'ICD9CM:363.04', 'ICD9CM:363.05', 'ICD9CM:363.06', 'ICD9CM:363.07', 'ICD9CM:363.08', 'ICD9CM:363.10', 'ICD9CM:363.11', 'ICD9CM:363.12', 'ICD9CM:363.13', 'ICD9CM:363.14', 'ICD9CM:363.15', 'ICD9CM:363.20', 'ICD9CM:363.21', 'ICD9CM:363.22', 'ICD9CM:364.00', 'ICD9CM:364.01', 'ICD9CM:364.02', 'ICD9CM:364.03', 'ICD9CM:364.04', 'ICD9CM:364.05', 'ICD9CM:364.10', 'ICD9CM:364.11', 'ICD9CM:364.21', 'ICD9CM:364.22', 'ICD9CM:364.23', 'ICD9CM:364.24', 'ICD9CM:364.3', 'ICD9CM:370.20', 'ICD9CM:370.21', 'ICD9CM:370.22', 'ICD9CM:370.23', 'ICD9CM:370.24', 'ICD9CM:370.31', 'ICD9CM:370.32', 'ICD9CM:370.33', 'ICD9CM:370.34', 'ICD9CM:370.35', 'ICD9CM:370.40', 'ICD9CM:370.44', 'ICD9CM:370.49', 'ICD9CM:370.50', 'ICD9CM:370.52', 'ICD9CM:370.54', 'ICD9CM:370.55', 'ICD9CM:370.59', 'ICD9CM:370.8', 'ICD9CM:370.9', 'ICD9CM:372.00', 'ICD9CM:372.01', 'ICD9CM:372.02', 'ICD9CM:372.03', 'ICD9CM:372.04', 'ICD9CM:372.05', 'ICD9CM:372.06', 'ICD9CM:372.10', 'ICD9CM:372.11', 'ICD9CM:372.12', 'ICD9CM:372.13', 'ICD9CM:372.14', 'ICD9CM:372.15', 'ICD9CM:372.20', 'ICD9CM:372.21', 'ICD9CM:372.22', 'ICD9CM:372.30', 'ICD9CM:372.31', 'ICD9CM:372.33', 'ICD9CM:372.39', 'ICD9CM:373.00', 'ICD9CM:373.01', 'ICD9CM:373.02', 'ICD9CM:373.11', 'ICD9CM:373.12', 'ICD9CM:373.13', 'ICD9CM:373.31', 'ICD9CM:373.32', 'ICD9CM:373.33', 'ICD9CM:373.34', 'ICD9CM:373.4', 'ICD9CM:373.5', 'ICD9CM:373.6', 'ICD9CM:373.8', 'ICD9CM:373.9', 'ICD9CM:375.00', 'ICD9CM:375.01', 'ICD9CM:375.02', 'ICD9CM:375.03', 'ICD9CM:375.30', 'ICD9CM:375.31', 'ICD9CM:375.32', 'ICD9CM:375.33', 'ICD9CM:375.41', 'ICD9CM:375.42', 'ICD9CM:375.43', 'ICD9CM:376.00', 'ICD9CM:376.01', 'ICD9CM:376.02', 'ICD9CM:376.03', 'ICD9CM:376.04', 'ICD9CM:376.10', 'ICD9CM:376.11', 'ICD9CM:376.12', 'ICD9CM:376.13', 'ICD9CM:377.30', 'ICD9CM:377.31', 'ICD9CM:377.32', 'ICD9CM:377.33', 'ICD9CM:377.34', 'ICD9CM:377.39', 'ICD9CM:379.00', 'ICD9CM:379.01', 'ICD9CM:379.02', 'ICD9CM:379.03', 'ICD9CM:379.04', 'ICD9CM:379.05', 'ICD9CM:379.06', 'ICD9CM:379.07', 'ICD9CM:379.09', 'ICD9CM:379.60', 'ICD9CM:379.61', 'ICD9CM:379.62', 'ICD9CM:379.63'):
            results_ccs2["eye_inflam"].append(1)
        else: results_ccs2["eye_inflam"].append(0)
    print("Completed Binary Recode of: eye_inflam")

    # Other_eye_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:360.20', 'ICD9CM:360.21', 'ICD9CM:360.23', 'ICD9CM:360.24', 'ICD9CM:360.29', 'ICD9CM:360.30', 'ICD9CM:360.31', 'ICD9CM:360.32', 'ICD9CM:360.33', 'ICD9CM:360.34', 'ICD9CM:360.40', 'ICD9CM:360.41', 'ICD9CM:360.42', 'ICD9CM:360.43', 'ICD9CM:360.44', 'ICD9CM:360.50', 'ICD9CM:360.51', 'ICD9CM:360.52', 'ICD9CM:360.53', 'ICD9CM:360.54', 'ICD9CM:360.55', 'ICD9CM:360.59', 'ICD9CM:360.60', 'ICD9CM:360.61', 'ICD9CM:360.62', 'ICD9CM:360.63', 'ICD9CM:360.64', 'ICD9CM:360.65', 'ICD9CM:360.69', 'ICD9CM:360.81', 'ICD9CM:360.89', 'ICD9CM:360.9', 'ICD9CM:363.30', 'ICD9CM:363.31', 'ICD9CM:363.32', 'ICD9CM:363.33', 'ICD9CM:363.34', 'ICD9CM:363.35', 'ICD9CM:363.40', 'ICD9CM:363.41', 'ICD9CM:363.42', 'ICD9CM:363.43', 'ICD9CM:363.50', 'ICD9CM:363.51', 'ICD9CM:363.52', 'ICD9CM:363.53', 'ICD9CM:363.54', 'ICD9CM:363.55', 'ICD9CM:363.56', 'ICD9CM:363.57', 'ICD9CM:363.61', 'ICD9CM:363.62', 'ICD9CM:363.63', 'ICD9CM:363.70', 'ICD9CM:363.71', 'ICD9CM:363.72', 'ICD9CM:363.8', 'ICD9CM:363.9', 'ICD9CM:364.41', 'ICD9CM:364.42', 'ICD9CM:364.51', 'ICD9CM:364.52', 'ICD9CM:364.53', 'ICD9CM:364.54', 'ICD9CM:364.55', 'ICD9CM:364.56', 'ICD9CM:364.57', 'ICD9CM:364.59', 'ICD9CM:364.60', 'ICD9CM:364.61', 'ICD9CM:364.62', 'ICD9CM:364.63', 'ICD9CM:364.64', 'ICD9CM:364.70', 'ICD9CM:364.71', 'ICD9CM:364.72', 'ICD9CM:364.73', 'ICD9CM:364.74', 'ICD9CM:364.75', 'ICD9CM:364.76', 'ICD9CM:364.77', 'ICD9CM:364.8', 'ICD9CM:364.81', 'ICD9CM:364.82', 'ICD9CM:364.89', 'ICD9CM:364.9', 'ICD9CM:370.00', 'ICD9CM:370.01', 'ICD9CM:370.02', 'ICD9CM:370.03', 'ICD9CM:370.04', 'ICD9CM:370.05', 'ICD9CM:370.06', 'ICD9CM:370.07', 'ICD9CM:370.60', 'ICD9CM:370.61', 'ICD9CM:370.62', 'ICD9CM:370.63', 'ICD9CM:370.64', 'ICD9CM:371.00', 'ICD9CM:371.01', 'ICD9CM:371.02', 'ICD9CM:371.03', 'ICD9CM:371.04', 'ICD9CM:371.05', 'ICD9CM:371.10', 'ICD9CM:371.11', 'ICD9CM:371.12', 'ICD9CM:371.13', 'ICD9CM:371.14', 'ICD9CM:371.15', 'ICD9CM:371.16', 'ICD9CM:371.20', 'ICD9CM:371.21', 'ICD9CM:371.22', 'ICD9CM:371.23', 'ICD9CM:371.24', 'ICD9CM:371.30', 'ICD9CM:371.31', 'ICD9CM:371.32', 'ICD9CM:371.33', 'ICD9CM:371.40', 'ICD9CM:371.41', 'ICD9CM:371.42', 'ICD9CM:371.43', 'ICD9CM:371.44', 'ICD9CM:371.45', 'ICD9CM:371.46', 'ICD9CM:371.48', 'ICD9CM:371.49', 'ICD9CM:371.50', 'ICD9CM:371.51', 'ICD9CM:371.52', 'ICD9CM:371.53', 'ICD9CM:371.54', 'ICD9CM:371.55', 'ICD9CM:371.56', 'ICD9CM:371.57', 'ICD9CM:371.58', 'ICD9CM:371.60', 'ICD9CM:371.61', 'ICD9CM:371.62', 'ICD9CM:371.70', 'ICD9CM:371.71', 'ICD9CM:371.72', 'ICD9CM:371.73', 'ICD9CM:371.81', 'ICD9CM:371.82', 'ICD9CM:371.89', 'ICD9CM:371.9', 'ICD9CM:372.34', 'ICD9CM:372.40', 'ICD9CM:372.41', 'ICD9CM:372.42', 'ICD9CM:372.43', 'ICD9CM:372.44', 'ICD9CM:372.45', 'ICD9CM:372.50', 'ICD9CM:372.51', 'ICD9CM:372.52', 'ICD9CM:372.53', 'ICD9CM:372.54', 'ICD9CM:372.55', 'ICD9CM:372.56', 'ICD9CM:372.61', 'ICD9CM:372.62', 'ICD9CM:372.63', 'ICD9CM:372.64', 'ICD9CM:372.71', 'ICD9CM:372.72', 'ICD9CM:372.73', 'ICD9CM:372.74', 'ICD9CM:372.75', 'ICD9CM:372.8', 'ICD9CM:372.81', 'ICD9CM:372.89', 'ICD9CM:372.9', 'ICD9CM:373.2', 'ICD9CM:374.00', 'ICD9CM:374.01', 'ICD9CM:374.02', 'ICD9CM:374.03', 'ICD9CM:374.04', 'ICD9CM:374.05', 'ICD9CM:374.10', 'ICD9CM:374.11', 'ICD9CM:374.12', 'ICD9CM:374.13', 'ICD9CM:374.14', 'ICD9CM:374.20', 'ICD9CM:374.21', 'ICD9CM:374.22', 'ICD9CM:374.23', 'ICD9CM:374.30', 'ICD9CM:374.31', 'ICD9CM:374.32', 'ICD9CM:374.33', 'ICD9CM:374.34', 'ICD9CM:374.41', 'ICD9CM:374.43', 'ICD9CM:374.44', 'ICD9CM:374.45', 'ICD9CM:374.46', 'ICD9CM:374.50', 'ICD9CM:374.51', 'ICD9CM:374.52', 'ICD9CM:374.53', 'ICD9CM:374.54', 'ICD9CM:374.55', 'ICD9CM:374.56', 'ICD9CM:374.81', 'ICD9CM:374.82', 'ICD9CM:374.83', 'ICD9CM:374.84', 'ICD9CM:374.85', 'ICD9CM:374.86', 'ICD9CM:374.87', 'ICD9CM:374.89', 'ICD9CM:374.9', 'ICD9CM:375.11', 'ICD9CM:375.12', 'ICD9CM:375.13', 'ICD9CM:375.14', 'ICD9CM:375.15', 'ICD9CM:375.16', 'ICD9CM:375.20', 'ICD9CM:375.21', 'ICD9CM:375.22', 'ICD9CM:375.51', 'ICD9CM:375.52', 'ICD9CM:375.53', 'ICD9CM:375.54', 'ICD9CM:375.55', 'ICD9CM:375.56', 'ICD9CM:375.57', 'ICD9CM:375.61', 'ICD9CM:375.69', 'ICD9CM:375.81', 'ICD9CM:375.89', 'ICD9CM:375.9', 'ICD9CM:376.21', 'ICD9CM:376.22', 'ICD9CM:376.30', 'ICD9CM:376.31', 'ICD9CM:376.32', 'ICD9CM:376.33', 'ICD9CM:376.34', 'ICD9CM:376.35', 'ICD9CM:376.36', 'ICD9CM:376.40', 'ICD9CM:376.41', 'ICD9CM:376.42', 'ICD9CM:376.43', 'ICD9CM:376.44', 'ICD9CM:376.45', 'ICD9CM:376.46', 'ICD9CM:376.47', 'ICD9CM:376.50', 'ICD9CM:376.51', 'ICD9CM:376.52', 'ICD9CM:376.6', 'ICD9CM:376.81', 'ICD9CM:376.82', 'ICD9CM:376.89', 'ICD9CM:376.9', 'ICD9CM:377.00', 'ICD9CM:377.01', 'ICD9CM:377.02', 'ICD9CM:377.03', 'ICD9CM:377.04', 'ICD9CM:377.10', 'ICD9CM:377.11', 'ICD9CM:377.12', 'ICD9CM:377.13', 'ICD9CM:377.14', 'ICD9CM:377.15', 'ICD9CM:377.16', 'ICD9CM:377.21', 'ICD9CM:377.22', 'ICD9CM:377.23', 'ICD9CM:377.24', 'ICD9CM:377.41', 'ICD9CM:377.42', 'ICD9CM:377.43', 'ICD9CM:377.49', 'ICD9CM:377.51', 'ICD9CM:377.52', 'ICD9CM:377.53', 'ICD9CM:377.54', 'ICD9CM:377.61', 'ICD9CM:377.62', 'ICD9CM:377.63', 'ICD9CM:377.71', 'ICD9CM:377.72', 'ICD9CM:377.73', 'ICD9CM:377.75', 'ICD9CM:377.9', 'ICD9CM:378.00', 'ICD9CM:378.01', 'ICD9CM:378.02', 'ICD9CM:378.03', 'ICD9CM:378.04', 'ICD9CM:378.05', 'ICD9CM:378.06', 'ICD9CM:378.07', 'ICD9CM:378.08', 'ICD9CM:378.10', 'ICD9CM:378.11', 'ICD9CM:378.12', 'ICD9CM:378.13', 'ICD9CM:378.14', 'ICD9CM:378.15', 'ICD9CM:378.16', 'ICD9CM:378.17', 'ICD9CM:378.18', 'ICD9CM:378.20', 'ICD9CM:378.21', 'ICD9CM:378.22', 'ICD9CM:378.23', 'ICD9CM:378.24', 'ICD9CM:378.30', 'ICD9CM:378.31', 'ICD9CM:378.32', 'ICD9CM:378.33', 'ICD9CM:378.34', 'ICD9CM:378.35', 'ICD9CM:378.40', 'ICD9CM:378.41', 'ICD9CM:378.42', 'ICD9CM:378.43', 'ICD9CM:378.44', 'ICD9CM:378.45', 'ICD9CM:378.50', 'ICD9CM:378.51', 'ICD9CM:378.52', 'ICD9CM:378.53', 'ICD9CM:378.54', 'ICD9CM:378.55', 'ICD9CM:378.56', 'ICD9CM:378.60', 'ICD9CM:378.61', 'ICD9CM:378.62', 'ICD9CM:378.63', 'ICD9CM:378.71', 'ICD9CM:378.72', 'ICD9CM:378.73', 'ICD9CM:378.81', 'ICD9CM:378.82', 'ICD9CM:378.83', 'ICD9CM:378.84', 'ICD9CM:378.85', 'ICD9CM:378.86', 'ICD9CM:378.87', 'ICD9CM:378.9', 'ICD9CM:379.11', 'ICD9CM:379.12', 'ICD9CM:379.13', 'ICD9CM:379.14', 'ICD9CM:379.15', 'ICD9CM:379.16', 'ICD9CM:379.19', 'ICD9CM:379.21', 'ICD9CM:379.22', 'ICD9CM:379.23', 'ICD9CM:379.24', 'ICD9CM:379.25', 'ICD9CM:379.26', 'ICD9CM:379.27', 'ICD9CM:379.29', 'ICD9CM:379.31', 'ICD9CM:379.32', 'ICD9CM:379.33', 'ICD9CM:379.34', 'ICD9CM:379.39', 'ICD9CM:379.40', 'ICD9CM:379.41', 'ICD9CM:379.42', 'ICD9CM:379.43', 'ICD9CM:379.45', 'ICD9CM:379.46', 'ICD9CM:379.49', 'ICD9CM:379.50', 'ICD9CM:379.51', 'ICD9CM:379.52', 'ICD9CM:379.53', 'ICD9CM:379.54', 'ICD9CM:379.55', 'ICD9CM:379.56', 'ICD9CM:379.57', 'ICD9CM:379.58', 'ICD9CM:379.59', 'ICD9CM:379.8', 'ICD9CM:379.90', 'ICD9CM:379.91', 'ICD9CM:379.92', 'ICD9CM:379.93', 'ICD9CM:379.99', 'ICD9CM:781.93', 'ICD9CM:V41.1', 'ICD9CM:V42.5', 'ICD9CM:V43.0', 'ICD9CM:V45.6', 'ICD9CM:V45.61', 'ICD9CM:V45.69', 'ICD9CM:V52.2', 'ICD9CM:V53.1', 'ICD9CM:V72.0'):
            results_ccs2["other_eye"].append(1)
        else: results_ccs2["other_eye"].append(0)
    print("Completed Binary Recode of: other_eye")

    # Otitis_media_and_related_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:055.2', 'ICD9CM:381.00', 'ICD9CM:381.01', 'ICD9CM:381.02', 'ICD9CM:381.03', 'ICD9CM:381.04', 'ICD9CM:381.05', 'ICD9CM:381.06', 'ICD9CM:381.10', 'ICD9CM:381.19', 'ICD9CM:381.20', 'ICD9CM:381.29', 'ICD9CM:381.3', 'ICD9CM:381.4', 'ICD9CM:381.50', 'ICD9CM:381.51', 'ICD9CM:381.52', 'ICD9CM:381.60', 'ICD9CM:381.61', 'ICD9CM:381.62', 'ICD9CM:381.63', 'ICD9CM:381.7', 'ICD9CM:381.81', 'ICD9CM:381.89', 'ICD9CM:381.9', 'ICD9CM:382.00', 'ICD9CM:382.01', 'ICD9CM:382.02', 'ICD9CM:382.1', 'ICD9CM:382.2', 'ICD9CM:382.3', 'ICD9CM:382.4', 'ICD9CM:382.9', 'ICD9CM:383.00', 'ICD9CM:383.01', 'ICD9CM:383.02', 'ICD9CM:383.1', 'ICD9CM:383.20', 'ICD9CM:383.21', 'ICD9CM:383.22', 'ICD9CM:383.30', 'ICD9CM:383.31', 'ICD9CM:383.32', 'ICD9CM:383.33', 'ICD9CM:383.81', 'ICD9CM:383.89', 'ICD9CM:383.9', 'ICD9CM:384.20', 'ICD9CM:384.21', 'ICD9CM:384.22', 'ICD9CM:384.23', 'ICD9CM:384.24', 'ICD9CM:384.25', 'ICD9CM:384.81', 'ICD9CM:384.82', 'ICD9CM:384.9', 'ICD9CM:385.00', 'ICD9CM:385.01', 'ICD9CM:385.02', 'ICD9CM:385.03', 'ICD9CM:385.09', 'ICD9CM:385.10', 'ICD9CM:385.11', 'ICD9CM:385.12', 'ICD9CM:385.13', 'ICD9CM:385.19', 'ICD9CM:385.21', 'ICD9CM:385.22', 'ICD9CM:385.23', 'ICD9CM:385.24', 'ICD9CM:387.0', 'ICD9CM:387.1', 'ICD9CM:387.2', 'ICD9CM:387.8', 'ICD9CM:387.9'):
            results_ccs2["otitis_media"].append(1)
        else: results_ccs2["otitis_media"].append(0)
    print("Completed Binary Recode of: otitis_media")

    # Conditions_associated_with_dizziness_or_vertigo
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:386.00', 'ICD9CM:386.01', 'ICD9CM:386.02', 'ICD9CM:386.03', 'ICD9CM:386.04', 'ICD9CM:386.10', 'ICD9CM:386.11', 'ICD9CM:386.12', 'ICD9CM:386.19', 'ICD9CM:386.2', 'ICD9CM:386.30', 'ICD9CM:386.31', 'ICD9CM:386.32', 'ICD9CM:386.33', 'ICD9CM:386.34', 'ICD9CM:386.35', 'ICD9CM:386.40', 'ICD9CM:386.41', 'ICD9CM:386.42', 'ICD9CM:386.43', 'ICD9CM:386.48', 'ICD9CM:386.50', 'ICD9CM:386.51', 'ICD9CM:386.52', 'ICD9CM:386.53', 'ICD9CM:386.54', 'ICD9CM:386.55', 'ICD9CM:386.56', 'ICD9CM:386.58', 'ICD9CM:386.8', 'ICD9CM:386.9', 'ICD9CM:780.4'):
            results_ccs2["dizzy"].append(1)
        else: results_ccs2["dizzy"].append(0)
    print("Completed Binary Recode of: dizzy")

    # Other_ear_and_sense_organ_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:380.00', 'ICD9CM:380.01', 'ICD9CM:380.02', 'ICD9CM:380.03', 'ICD9CM:380.10', 'ICD9CM:380.11', 'ICD9CM:380.12', 'ICD9CM:380.13', 'ICD9CM:380.14', 'ICD9CM:380.15', 'ICD9CM:380.16', 'ICD9CM:380.21', 'ICD9CM:380.22', 'ICD9CM:380.23', 'ICD9CM:380.30', 'ICD9CM:380.31', 'ICD9CM:380.32', 'ICD9CM:380.39', 'ICD9CM:380.4', 'ICD9CM:380.50', 'ICD9CM:380.51', 'ICD9CM:380.52', 'ICD9CM:380.53', 'ICD9CM:380.81', 'ICD9CM:380.89', 'ICD9CM:380.9', 'ICD9CM:384.00', 'ICD9CM:384.01', 'ICD9CM:384.09', 'ICD9CM:384.1', 'ICD9CM:385.30', 'ICD9CM:385.31', 'ICD9CM:385.32', 'ICD9CM:385.33', 'ICD9CM:385.35', 'ICD9CM:385.82', 'ICD9CM:385.83', 'ICD9CM:385.89', 'ICD9CM:385.9', 'ICD9CM:388.00', 'ICD9CM:388.01', 'ICD9CM:388.02', 'ICD9CM:388.10', 'ICD9CM:388.11', 'ICD9CM:388.12', 'ICD9CM:388.2', 'ICD9CM:388.30', 'ICD9CM:388.31', 'ICD9CM:388.32', 'ICD9CM:388.40', 'ICD9CM:388.41', 'ICD9CM:388.42', 'ICD9CM:388.43', 'ICD9CM:388.44', 'ICD9CM:388.45', 'ICD9CM:388.5', 'ICD9CM:388.60', 'ICD9CM:388.61', 'ICD9CM:388.69', 'ICD9CM:388.70', 'ICD9CM:388.71', 'ICD9CM:388.72', 'ICD9CM:388.8', 'ICD9CM:388.9', 'ICD9CM:389.00', 'ICD9CM:389.01', 'ICD9CM:389.02', 'ICD9CM:389.03', 'ICD9CM:389.04', 'ICD9CM:389.05', 'ICD9CM:389.06', 'ICD9CM:389.08', 'ICD9CM:389.10', 'ICD9CM:389.11', 'ICD9CM:389.12', 'ICD9CM:389.13', 'ICD9CM:389.14', 'ICD9CM:389.15', 'ICD9CM:389.16', 'ICD9CM:389.17', 'ICD9CM:389.18', 'ICD9CM:389.2', 'ICD9CM:389.20', 'ICD9CM:389.21', 'ICD9CM:389.22', 'ICD9CM:389.7', 'ICD9CM:389.8', 'ICD9CM:389.9', 'ICD9CM:V41.2', 'ICD9CM:V41.3', 'ICD9CM:V49.85', 'ICD9CM:V53.2', 'ICD9CM:V72.1', 'ICD9CM:V72.11', 'ICD9CM:V72.12', 'ICD9CM:V72.19'):
            results_ccs2["other_ear_sense"].append(1)
        else: results_ccs2["other_ear_sense"].append(0)
    print("Completed Binary Recode of: other_ear_sense")

    # Other_nervous_system_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:325', 'ICD9CM:327.02', 'ICD9CM:327.15', 'ICD9CM:327.30', 'ICD9CM:327.31', 'ICD9CM:327.32', 'ICD9CM:327.33', 'ICD9CM:327.34', 'ICD9CM:327.35', 'ICD9CM:327.36', 'ICD9CM:327.37', 'ICD9CM:327.39', 'ICD9CM:327.53', 'ICD9CM:331.83', 'ICD9CM:332.1', 'ICD9CM:337.20', 'ICD9CM:337.21', 'ICD9CM:337.22', 'ICD9CM:337.29', 'ICD9CM:338.0', 'ICD9CM:338.11', 'ICD9CM:338.12', 'ICD9CM:338.18', 'ICD9CM:338.19', 'ICD9CM:338.21', 'ICD9CM:338.22', 'ICD9CM:338.28', 'ICD9CM:338.29', 'ICD9CM:338.3', 'ICD9CM:338.4', 'ICD9CM:341.0', 'ICD9CM:341.1', 'ICD9CM:341.8', 'ICD9CM:341.9', 'ICD9CM:344.61', 'ICD9CM:347', 'ICD9CM:347.00', 'ICD9CM:347.01', 'ICD9CM:347.10', 'ICD9CM:347.11', 'ICD9CM:348.0', 'ICD9CM:348.2', 'ICD9CM:348.3', 'ICD9CM:348.30', 'ICD9CM:348.31', 'ICD9CM:348.39', 'ICD9CM:348.4', 'ICD9CM:348.5', 'ICD9CM:348.8', 'ICD9CM:348.81', 'ICD9CM:348.82', 'ICD9CM:348.89', 'ICD9CM:348.9', 'ICD9CM:349.2', 'ICD9CM:349.81', 'ICD9CM:349.82', 'ICD9CM:349.89', 'ICD9CM:349.9', 'ICD9CM:350.1', 'ICD9CM:350.2', 'ICD9CM:350.8', 'ICD9CM:350.9', 'ICD9CM:351.0', 'ICD9CM:351.1', 'ICD9CM:351.8', 'ICD9CM:351.9', 'ICD9CM:352.0', 'ICD9CM:352.1', 'ICD9CM:352.2', 'ICD9CM:352.3', 'ICD9CM:352.4', 'ICD9CM:352.5', 'ICD9CM:352.6', 'ICD9CM:352.9', 'ICD9CM:353.0', 'ICD9CM:353.1', 'ICD9CM:353.2', 'ICD9CM:353.3', 'ICD9CM:353.4', 'ICD9CM:353.5', 'ICD9CM:353.6', 'ICD9CM:353.8', 'ICD9CM:353.9', 'ICD9CM:354.0', 'ICD9CM:354.1', 'ICD9CM:354.2', 'ICD9CM:354.3', 'ICD9CM:354.4', 'ICD9CM:354.5', 'ICD9CM:354.8', 'ICD9CM:354.9', 'ICD9CM:355.0', 'ICD9CM:355.1', 'ICD9CM:355.2', 'ICD9CM:355.3', 'ICD9CM:355.4', 'ICD9CM:355.5', 'ICD9CM:355.6', 'ICD9CM:355.7', 'ICD9CM:355.71', 'ICD9CM:355.79', 'ICD9CM:355.8', 'ICD9CM:355.9', 'ICD9CM:356.0', 'ICD9CM:356.1', 'ICD9CM:356.2', 'ICD9CM:356.3', 'ICD9CM:356.4', 'ICD9CM:356.8', 'ICD9CM:356.9', 'ICD9CM:357.0', 'ICD9CM:357.1', 'ICD9CM:357.2', 'ICD9CM:357.3', 'ICD9CM:357.4', 'ICD9CM:357.6', 'ICD9CM:357.7', 'ICD9CM:357.8', 'ICD9CM:357.81', 'ICD9CM:357.82', 'ICD9CM:357.89', 'ICD9CM:357.9', 'ICD9CM:358.0', 'ICD9CM:358.00', 'ICD9CM:358.01', 'ICD9CM:358.1', 'ICD9CM:358.2', 'ICD9CM:358.30', 'ICD9CM:358.31', 'ICD9CM:358.39', 'ICD9CM:358.8', 'ICD9CM:358.9', 'ICD9CM:359.0', 'ICD9CM:359.1', 'ICD9CM:359.2', 'ICD9CM:359.21', 'ICD9CM:359.22', 'ICD9CM:359.23', 'ICD9CM:359.24', 'ICD9CM:359.29', 'ICD9CM:359.3', 'ICD9CM:359.4', 'ICD9CM:359.5', 'ICD9CM:359.6', 'ICD9CM:359.71', 'ICD9CM:359.79', 'ICD9CM:359.8', 'ICD9CM:359.81', 'ICD9CM:359.89', 'ICD9CM:359.9', 'ICD9CM:781.0', 'ICD9CM:781.1', 'ICD9CM:781.2', 'ICD9CM:781.3', 'ICD9CM:781.7', 'ICD9CM:781.8', 'ICD9CM:782.0', 'ICD9CM:784.3', 'ICD9CM:784.5', 'ICD9CM:784.51', 'ICD9CM:784.52', 'ICD9CM:784.59', 'ICD9CM:784.60', 'ICD9CM:784.61', 'ICD9CM:784.69', 'ICD9CM:792.0', 'ICD9CM:793.0', 'ICD9CM:794.00', 'ICD9CM:794.01', 'ICD9CM:794.02', 'ICD9CM:794.09', 'ICD9CM:794.10', 'ICD9CM:794.11', 'ICD9CM:794.12', 'ICD9CM:794.13', 'ICD9CM:794.14', 'ICD9CM:794.15', 'ICD9CM:794.16', 'ICD9CM:794.17', 'ICD9CM:794.19', 'ICD9CM:796.1', 'ICD9CM:799.51', 'ICD9CM:799.52', 'ICD9CM:799.53', 'ICD9CM:799.54', 'ICD9CM:799.55', 'ICD9CM:799.59', 'ICD9CM:V12.4', 'ICD9CM:V12.40', 'ICD9CM:V12.41', 'ICD9CM:V12.42', 'ICD9CM:V12.49', 'ICD9CM:V41.5', 'ICD9CM:V45.2', 'ICD9CM:V48.4', 'ICD9CM:V48.5', 'ICD9CM:V49.3', 'ICD9CM:V53.0', 'ICD9CM:V53.01', 'ICD9CM:V53.02', 'ICD9CM:V53.09'):
            results_ccs2["other_ns_disorder"].append(1)
        else: results_ccs2["other_ns_disorder"].append(0)
    print("Completed Binary Recode of: other_ns_disorder")

    # Heart_valve_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:394.0', 'ICD9CM:394.1', 'ICD9CM:394.2', 'ICD9CM:394.9', 'ICD9CM:395.0', 'ICD9CM:395.1', 'ICD9CM:395.2', 'ICD9CM:395.9', 'ICD9CM:396.0', 'ICD9CM:396.1', 'ICD9CM:396.2', 'ICD9CM:396.3', 'ICD9CM:396.8', 'ICD9CM:396.9', 'ICD9CM:397.0', 'ICD9CM:397.1', 'ICD9CM:397.9', 'ICD9CM:424.0', 'ICD9CM:424.1', 'ICD9CM:424.2', 'ICD9CM:424.3', 'ICD9CM:424.90', 'ICD9CM:424.91', 'ICD9CM:424.99', 'ICD9CM:785.2', 'ICD9CM:785.3', 'ICD9CM:V42.2', 'ICD9CM:V43.3'):
            results_ccs2["heart_valve"].append(1)
        else: results_ccs2["heart_valve"].append(0)
    print("Completed Binary Recode of: heart_valve")

    # Peri-;_endo-;_and_myocarditis;_cardiomyopathy_(except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:032.82', 'ICD9CM:036.40', 'ICD9CM:036.41', 'ICD9CM:036.42', 'ICD9CM:036.43', 'ICD9CM:074.20', 'ICD9CM:074.21', 'ICD9CM:074.22', 'ICD9CM:074.23', 'ICD9CM:112.81', 'ICD9CM:115.03', 'ICD9CM:115.04', 'ICD9CM:115.13', 'ICD9CM:115.14', 'ICD9CM:115.93', 'ICD9CM:115.94', 'ICD9CM:130.3', 'ICD9CM:391.0', 'ICD9CM:391.1', 'ICD9CM:391.2', 'ICD9CM:391.8', 'ICD9CM:391.9', 'ICD9CM:392.0', 'ICD9CM:393', 'ICD9CM:398.0', 'ICD9CM:398.90', 'ICD9CM:398.99', 'ICD9CM:420.0', 'ICD9CM:420.90', 'ICD9CM:420.91', 'ICD9CM:420.99', 'ICD9CM:421.0', 'ICD9CM:421.1', 'ICD9CM:421.9', 'ICD9CM:422.0', 'ICD9CM:422.90', 'ICD9CM:422.91', 'ICD9CM:422.92', 'ICD9CM:422.93', 'ICD9CM:422.99', 'ICD9CM:423.0', 'ICD9CM:423.1', 'ICD9CM:423.2', 'ICD9CM:423.3', 'ICD9CM:423.8', 'ICD9CM:423.9', 'ICD9CM:425.0', 'ICD9CM:425.1', 'ICD9CM:425.11', 'ICD9CM:425.18', 'ICD9CM:425.2', 'ICD9CM:425.3', 'ICD9CM:425.4', 'ICD9CM:425.7', 'ICD9CM:425.8', 'ICD9CM:425.9', 'ICD9CM:429.0'):
            results_ccs2["peri_endo_carditis"].append(1)
        else: results_ccs2["peri_endo_carditis"].append(0)
    print("Completed Binary Recode of: peri_endo_carditis")

    # Essential_hypertension
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:401.1', 'ICD9CM:401.9'):
            results_ccs2["essential_htn"].append(1)
        else: results_ccs2["essential_htn"].append(0)
    print("Completed Binary Recode of: essential_htn")

    # Hypertension_with_complications_and_secondary_hypertension
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:401.0', 'ICD9CM:402.00', 'ICD9CM:402.01', 'ICD9CM:402.10', 'ICD9CM:402.11', 'ICD9CM:402.90', 'ICD9CM:402.91', 'ICD9CM:403.0', 'ICD9CM:403.00', 'ICD9CM:403.01', 'ICD9CM:403.1', 'ICD9CM:403.10', 'ICD9CM:403.11', 'ICD9CM:403.9', 'ICD9CM:403.90', 'ICD9CM:403.91', 'ICD9CM:404.0', 'ICD9CM:404.00', 'ICD9CM:404.01', 'ICD9CM:404.02', 'ICD9CM:404.03', 'ICD9CM:404.1', 'ICD9CM:404.10', 'ICD9CM:404.11', 'ICD9CM:404.12', 'ICD9CM:404.13', 'ICD9CM:404.9', 'ICD9CM:404.90', 'ICD9CM:404.91', 'ICD9CM:404.92', 'ICD9CM:404.93', 'ICD9CM:405.01', 'ICD9CM:405.09', 'ICD9CM:405.11', 'ICD9CM:405.19', 'ICD9CM:405.91', 'ICD9CM:405.99', 'ICD9CM:437.2'):
            results_ccs2["htn_w_comp"].append(1)
        else: results_ccs2["htn_w_comp"].append(0)
    print("Completed Binary Recode of: htn_w_comp")

    # Acute_myocardial_infarction
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:410.0', 'ICD9CM:410.00', 'ICD9CM:410.01', 'ICD9CM:410.02', 'ICD9CM:410.1', 'ICD9CM:410.10', 'ICD9CM:410.11', 'ICD9CM:410.12', 'ICD9CM:410.2', 'ICD9CM:410.20', 'ICD9CM:410.21', 'ICD9CM:410.22', 'ICD9CM:410.3', 'ICD9CM:410.30', 'ICD9CM:410.31', 'ICD9CM:410.32', 'ICD9CM:410.4', 'ICD9CM:410.40', 'ICD9CM:410.41', 'ICD9CM:410.42', 'ICD9CM:410.5', 'ICD9CM:410.50', 'ICD9CM:410.51', 'ICD9CM:410.52', 'ICD9CM:410.6', 'ICD9CM:410.60', 'ICD9CM:410.61', 'ICD9CM:410.62', 'ICD9CM:410.7', 'ICD9CM:410.70', 'ICD9CM:410.71', 'ICD9CM:410.72', 'ICD9CM:410.8', 'ICD9CM:410.80', 'ICD9CM:410.81', 'ICD9CM:410.82', 'ICD9CM:410.9', 'ICD9CM:410.90', 'ICD9CM:410.91', 'ICD9CM:410.92'):
            results_ccs2["acute_mi"].append(1)
        else: results_ccs2["acute_mi"].append(0)
    print("Completed Binary Recode of: acute_mi")

    # Coronary_atherosclerosis_and_other_heart_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:411.0', 'ICD9CM:411.1', 'ICD9CM:411.8', 'ICD9CM:411.81', 'ICD9CM:411.89', 'ICD9CM:412', 'ICD9CM:413.0', 'ICD9CM:413.1', 'ICD9CM:413.9', 'ICD9CM:414.0', 'ICD9CM:414.00', 'ICD9CM:414.01', 'ICD9CM:414.06', 'ICD9CM:414.2', 'ICD9CM:414.3', 'ICD9CM:414.4', 'ICD9CM:414.8', 'ICD9CM:414.9', 'ICD9CM:V45.81', 'ICD9CM:V45.82'):
            results_ccs2["coronary_athero"].append(1)
        else: results_ccs2["coronary_athero"].append(0)
    print("Completed Binary Recode of: coronary_athero")

    # Nonspecific_chest_pain
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:786.50', 'ICD9CM:786.51', 'ICD9CM:786.59'):
            results_ccs2["chest_pain_nos"].append(1)
        else: results_ccs2["chest_pain_nos"].append(0)
    print("Completed Binary Recode of: chest_pain_nos")

    # Pulmonary_heart_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:415.0', 'ICD9CM:415.1', 'ICD9CM:415.12', 'ICD9CM:415.13', 'ICD9CM:415.19', 'ICD9CM:416.0', 'ICD9CM:416.1', 'ICD9CM:416.2', 'ICD9CM:416.8', 'ICD9CM:416.9', 'ICD9CM:417.0', 'ICD9CM:417.1', 'ICD9CM:417.8', 'ICD9CM:417.9', 'ICD9CM:V12.55'):
            results_ccs2["pulmonary_hd"].append(1)
        else: results_ccs2["pulmonary_hd"].append(0)
    print("Completed Binary Recode of: pulmonary_hd")

    # Other_and_ill-_defined_heart_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:414.10', 'ICD9CM:414.11', 'ICD9CM:414.12', 'ICD9CM:414.19', 'ICD9CM:429.1', 'ICD9CM:429.2', 'ICD9CM:429.3', 'ICD9CM:429.5', 'ICD9CM:429.6', 'ICD9CM:429.71', 'ICD9CM:429.79', 'ICD9CM:429.81', 'ICD9CM:429.82', 'ICD9CM:429.83', 'ICD9CM:429.89', 'ICD9CM:429.9'):
            results_ccs2["other_heart_disease"].append(1)
        else: results_ccs2["other_heart_disease"].append(0)
    print("Completed Binary Recode of: other_heart_disease")

    # Conduction_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:426.0', 'ICD9CM:426.10', 'ICD9CM:426.11', 'ICD9CM:426.12', 'ICD9CM:426.13', 'ICD9CM:426.2', 'ICD9CM:426.3', 'ICD9CM:426.4', 'ICD9CM:426.50', 'ICD9CM:426.51', 'ICD9CM:426.52', 'ICD9CM:426.53', 'ICD9CM:426.54', 'ICD9CM:426.6', 'ICD9CM:426.7', 'ICD9CM:426.81', 'ICD9CM:426.82', 'ICD9CM:426.89', 'ICD9CM:426.9', 'ICD9CM:V45.0', 'ICD9CM:V45.00', 'ICD9CM:V45.01', 'ICD9CM:V45.02', 'ICD9CM:V45.09', 'ICD9CM:V53.3', 'ICD9CM:V53.31', 'ICD9CM:V53.32', 'ICD9CM:V53.39'):
            results_ccs2["conduction"].append(1)
        else: results_ccs2["conduction"].append(0)
    print("Completed Binary Recode of: conduction")

    # Cardiac_dysrhythmias
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:427.0', 'ICD9CM:427.1', 'ICD9CM:427.2', 'ICD9CM:427.31', 'ICD9CM:427.32', 'ICD9CM:427.60', 'ICD9CM:427.61', 'ICD9CM:427.69', 'ICD9CM:427.81', 'ICD9CM:427.89', 'ICD9CM:427.9', 'ICD9CM:785.0', 'ICD9CM:785.1'):
            results_ccs2["cardiac_dysrhythm"].append(1)
        else: results_ccs2["cardiac_dysrhythm"].append(0)
    print("Completed Binary Recode of: cardiac_dysrhythm")

    # Cardiac_arrest_and_ventricular_fibrillation
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:427.41', 'ICD9CM:427.42', 'ICD9CM:427.5'):
            results_ccs2["cardiac_arrest"].append(1)
        else: results_ccs2["cardiac_arrest"].append(0)
    print("Completed Binary Recode of: cardiac_arrest")

    # Congestive_heart_failure;_nonhypertensive
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:398.91', 'ICD9CM:428.0', 'ICD9CM:428.1', 'ICD9CM:428.20', 'ICD9CM:428.21', 'ICD9CM:428.22', 'ICD9CM:428.23', 'ICD9CM:428.30', 'ICD9CM:428.31', 'ICD9CM:428.32', 'ICD9CM:428.33', 'ICD9CM:428.40', 'ICD9CM:428.41', 'ICD9CM:428.42', 'ICD9CM:428.43', 'ICD9CM:428.9'):
            results_ccs2["chf"].append(1)
        else: results_ccs2["chf"].append(0)
    print("Completed Binary Recode of: chf")

    # Acute_cerebrovascular_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:346.60', 'ICD9CM:346.61', 'ICD9CM:346.62', 'ICD9CM:346.63', 'ICD9CM:430', 'ICD9CM:431', 'ICD9CM:432.0', 'ICD9CM:432.1', 'ICD9CM:432.9', 'ICD9CM:433.01', 'ICD9CM:433.11', 'ICD9CM:433.21', 'ICD9CM:433.31', 'ICD9CM:433.81', 'ICD9CM:433.91', 'ICD9CM:434.0', 'ICD9CM:434.00', 'ICD9CM:434.01', 'ICD9CM:434.1', 'ICD9CM:434.10', 'ICD9CM:434.11', 'ICD9CM:434.9', 'ICD9CM:434.90', 'ICD9CM:434.91', 'ICD9CM:436'):
            results_ccs2["acute_cvd"].append(1)
        else: results_ccs2["acute_cvd"].append(0)
    print("Completed Binary Recode of: acute_cvd")

    # Occlusion_or_stenosis_of_precerebral_arteries
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:433.0', 'ICD9CM:433.00', 'ICD9CM:433.1', 'ICD9CM:433.10', 'ICD9CM:433.2', 'ICD9CM:433.20', 'ICD9CM:433.3', 'ICD9CM:433.30', 'ICD9CM:433.8', 'ICD9CM:433.80', 'ICD9CM:433.9', 'ICD9CM:433.90'):
            results_ccs2["occlu_cereb_artery"].append(1)
        else: results_ccs2["occlu_cereb_artery"].append(0)
    print("Completed Binary Recode of: occlu_cereb_artery")

    # Other_and_ill-_defined_cerebrovascular_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:437.0', 'ICD9CM:437.1', 'ICD9CM:437.3', 'ICD9CM:437.4', 'ICD9CM:437.5', 'ICD9CM:437.6', 'ICD9CM:437.7', 'ICD9CM:437.8', 'ICD9CM:437.9'):
            results_ccs2["other_cvd"].append(1)
        else: results_ccs2["other_cvd"].append(0)
    print("Completed Binary Recode of: other_cvd")

    # Transient_cerebral_ischemia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:435.0', 'ICD9CM:435.1', 'ICD9CM:435.2', 'ICD9CM:435.3', 'ICD9CM:435.8', 'ICD9CM:435.9'):
            results_ccs2["tran_cereb_isch"].append(1)
        else: results_ccs2["tran_cereb_isch"].append(0)
    print("Completed Binary Recode of: tran_cereb_isch")

    # Late_effects_of_cerebrovascular_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:438', 'ICD9CM:438.0', 'ICD9CM:438.10', 'ICD9CM:438.11', 'ICD9CM:438.12', 'ICD9CM:438.13', 'ICD9CM:438.14', 'ICD9CM:438.19', 'ICD9CM:438.20', 'ICD9CM:438.21', 'ICD9CM:438.22', 'ICD9CM:438.30', 'ICD9CM:438.31', 'ICD9CM:438.32', 'ICD9CM:438.40', 'ICD9CM:438.41', 'ICD9CM:438.42', 'ICD9CM:438.50', 'ICD9CM:438.51', 'ICD9CM:438.52', 'ICD9CM:438.53', 'ICD9CM:438.6', 'ICD9CM:438.7', 'ICD9CM:438.81', 'ICD9CM:438.82', 'ICD9CM:438.83', 'ICD9CM:438.84', 'ICD9CM:438.85', 'ICD9CM:438.89', 'ICD9CM:438.9'):
            results_ccs2["late_effect_cvd"].append(1)
        else: results_ccs2["late_effect_cvd"].append(0)
    print("Completed Binary Recode of: late_effect_cvd")

    # Peripheral_and_visceral_atherosclerosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:440.0', 'ICD9CM:440.1', 'ICD9CM:440.2', 'ICD9CM:440.20', 'ICD9CM:440.21', 'ICD9CM:440.22', 'ICD9CM:440.23', 'ICD9CM:440.29', 'ICD9CM:440.4', 'ICD9CM:440.8', 'ICD9CM:440.9', 'ICD9CM:443.9', 'ICD9CM:557.0', 'ICD9CM:557.1', 'ICD9CM:557.9'):
            results_ccs2["pvd"].append(1)
        else: results_ccs2["pvd"].append(0)
    print("Completed Binary Recode of: pvd")

    # Aortic;_peripheral;_and_visceral_artery_aneurysms
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:441.0', 'ICD9CM:441.00', 'ICD9CM:441.01', 'ICD9CM:441.02', 'ICD9CM:441.03', 'ICD9CM:441.1', 'ICD9CM:441.2', 'ICD9CM:441.3', 'ICD9CM:441.4', 'ICD9CM:441.5', 'ICD9CM:441.6', 'ICD9CM:441.7', 'ICD9CM:441.9', 'ICD9CM:442.0', 'ICD9CM:442.1', 'ICD9CM:442.2', 'ICD9CM:442.3', 'ICD9CM:442.81', 'ICD9CM:442.82', 'ICD9CM:442.83', 'ICD9CM:442.84', 'ICD9CM:442.89', 'ICD9CM:442.9', 'ICD9CM:443.21', 'ICD9CM:443.22', 'ICD9CM:443.23', 'ICD9CM:443.24', 'ICD9CM:443.29', 'ICD9CM:447.70', 'ICD9CM:447.71', 'ICD9CM:447.72', 'ICD9CM:447.73'):
            results_ccs2["artery_aneurysm"].append(1)
        else: results_ccs2["artery_aneurysm"].append(0)
    print("Completed Binary Recode of: artery_aneurysm")

    # Aortic_and_peripheral_arterial_embolism_or_thrombosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:444.0', 'ICD9CM:444.01', 'ICD9CM:444.09', 'ICD9CM:444.1', 'ICD9CM:444.21', 'ICD9CM:444.22', 'ICD9CM:444.81', 'ICD9CM:444.89', 'ICD9CM:444.9', 'ICD9CM:445.01', 'ICD9CM:445.02', 'ICD9CM:445.81', 'ICD9CM:445.89'):
            results_ccs2["artery_embolism"].append(1)
        else: results_ccs2["artery_embolism"].append(0)
    print("Completed Binary Recode of: artery_embolism")

    # Other_circulatory_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:443.0', 'ICD9CM:443.1', 'ICD9CM:443.81', 'ICD9CM:443.82', 'ICD9CM:443.89', 'ICD9CM:446.0', 'ICD9CM:446.1', 'ICD9CM:446.2', 'ICD9CM:446.20', 'ICD9CM:446.21', 'ICD9CM:446.29', 'ICD9CM:446.3', 'ICD9CM:446.4', 'ICD9CM:446.5', 'ICD9CM:446.6', 'ICD9CM:446.7', 'ICD9CM:447.0', 'ICD9CM:447.1', 'ICD9CM:447.2', 'ICD9CM:447.3', 'ICD9CM:447.4', 'ICD9CM:447.5', 'ICD9CM:447.6', 'ICD9CM:447.8', 'ICD9CM:447.9', 'ICD9CM:448.0', 'ICD9CM:448.1', 'ICD9CM:448.9', 'ICD9CM:458.0', 'ICD9CM:458.1', 'ICD9CM:458.8', 'ICD9CM:458.9', 'ICD9CM:459.0', 'ICD9CM:459.89', 'ICD9CM:459.9', 'ICD9CM:785.9', 'ICD9CM:794.30', 'ICD9CM:794.31', 'ICD9CM:794.39', 'ICD9CM:796.2', 'ICD9CM:V12.5', 'ICD9CM:V12.50', 'ICD9CM:V12.53', 'ICD9CM:V12.54', 'ICD9CM:V12.59', 'ICD9CM:V15.1', 'ICD9CM:V42.1', 'ICD9CM:V43.2', 'ICD9CM:V43.21', 'ICD9CM:V43.22', 'ICD9CM:V43.4', 'ICD9CM:V71.7'):
            results_ccs2["other_circ"].append(1)
        else: results_ccs2["other_circ"].append(0)
    print("Completed Binary Recode of: other_circ")

    # Phlebitis;_thrombophlebitis_and_thromboembolism
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:451.0', 'ICD9CM:451.11', 'ICD9CM:451.19', 'ICD9CM:451.2', 'ICD9CM:451.81', 'ICD9CM:451.82', 'ICD9CM:451.83', 'ICD9CM:451.84', 'ICD9CM:451.89', 'ICD9CM:451.9', 'ICD9CM:452', 'ICD9CM:453.0', 'ICD9CM:453.1', 'ICD9CM:453.2', 'ICD9CM:453.3', 'ICD9CM:453.40', 'ICD9CM:453.41', 'ICD9CM:453.42', 'ICD9CM:453.50', 'ICD9CM:453.51', 'ICD9CM:453.52', 'ICD9CM:453.6', 'ICD9CM:453.71', 'ICD9CM:453.72', 'ICD9CM:453.73', 'ICD9CM:453.74', 'ICD9CM:453.75', 'ICD9CM:453.76', 'ICD9CM:453.77', 'ICD9CM:453.79', 'ICD9CM:453.8', 'ICD9CM:453.81', 'ICD9CM:453.82', 'ICD9CM:453.83', 'ICD9CM:453.84', 'ICD9CM:453.85', 'ICD9CM:453.86', 'ICD9CM:453.87', 'ICD9CM:453.89', 'ICD9CM:453.9', 'ICD9CM:V12.51', 'ICD9CM:V12.52'):
            results_ccs2["phlebitis"].append(1)
        else: results_ccs2["phlebitis"].append(0)
    print("Completed Binary Recode of: phlebitis")

    # Varicose_veins_of_lower_extremity
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:454.0', 'ICD9CM:454.1', 'ICD9CM:454.2', 'ICD9CM:454.8', 'ICD9CM:454.9'):
            results_ccs2["varicose_vein"].append(1)
        else: results_ccs2["varicose_vein"].append(0)
    print("Completed Binary Recode of: varicose_vein")

    # Hemorrhoids
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:455.0', 'ICD9CM:455.1', 'ICD9CM:455.2', 'ICD9CM:455.3', 'ICD9CM:455.4', 'ICD9CM:455.5', 'ICD9CM:455.6', 'ICD9CM:455.7', 'ICD9CM:455.8', 'ICD9CM:455.9'):
            results_ccs2["hemorrhoid"].append(1)
        else: results_ccs2["hemorrhoid"].append(0)
    print("Completed Binary Recode of: hemorrhoid")

    # Other_diseases_of_veins_and_lymphatics
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:456.3', 'ICD9CM:456.4', 'ICD9CM:456.5', 'ICD9CM:456.6', 'ICD9CM:456.8', 'ICD9CM:457.0', 'ICD9CM:457.1', 'ICD9CM:457.2', 'ICD9CM:457.8', 'ICD9CM:457.9', 'ICD9CM:459.1', 'ICD9CM:459.10', 'ICD9CM:459.11', 'ICD9CM:459.12', 'ICD9CM:459.13', 'ICD9CM:459.19', 'ICD9CM:459.2', 'ICD9CM:459.30', 'ICD9CM:459.31', 'ICD9CM:459.32', 'ICD9CM:459.33', 'ICD9CM:459.39', 'ICD9CM:459.81'):
            results_ccs2["other_vein_lymph"].append(1)
        else: results_ccs2["other_vein_lymph"].append(0)
    print("Completed Binary Recode of: other_vein_lymph")

    # Pneumonia_(_except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:003.22', 'ICD9CM:020.3', 'ICD9CM:020.4', 'ICD9CM:020.5', 'ICD9CM:021.2', 'ICD9CM:022.1', 'ICD9CM:031.0', 'ICD9CM:039.1', 'ICD9CM:052.1', 'ICD9CM:055.1', 'ICD9CM:073.0', 'ICD9CM:083.0', 'ICD9CM:112.4', 'ICD9CM:114.0', 'ICD9CM:114.4', 'ICD9CM:114.5', 'ICD9CM:115.05', 'ICD9CM:115.15', 'ICD9CM:115.95', 'ICD9CM:130.4', 'ICD9CM:136.3', 'ICD9CM:480.0', 'ICD9CM:480.1', 'ICD9CM:480.2', 'ICD9CM:480.3', 'ICD9CM:480.8', 'ICD9CM:480.9', 'ICD9CM:481', 'ICD9CM:482.0', 'ICD9CM:482.1', 'ICD9CM:482.2', 'ICD9CM:482.3', 'ICD9CM:482.30', 'ICD9CM:482.31', 'ICD9CM:482.32', 'ICD9CM:482.39', 'ICD9CM:482.4', 'ICD9CM:482.40', 'ICD9CM:482.41', 'ICD9CM:482.42', 'ICD9CM:482.49', 'ICD9CM:482.8', 'ICD9CM:482.81', 'ICD9CM:482.82', 'ICD9CM:482.83', 'ICD9CM:482.84', 'ICD9CM:482.89', 'ICD9CM:482.9', 'ICD9CM:483', 'ICD9CM:483.0', 'ICD9CM:483.1', 'ICD9CM:483.8', 'ICD9CM:484.1', 'ICD9CM:484.3', 'ICD9CM:484.5', 'ICD9CM:484.6', 'ICD9CM:484.7', 'ICD9CM:484.8', 'ICD9CM:485', 'ICD9CM:486', 'ICD9CM:513.0', 'ICD9CM:517.1'):
            results_ccs2["pneumonia"].append(1)
        else: results_ccs2["pneumonia"].append(0)
    print("Completed Binary Recode of: pneumonia")

    # Influenza
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:487.0', 'ICD9CM:487.1', 'ICD9CM:487.8', 'ICD9CM:488', 'ICD9CM:488.0', 'ICD9CM:488.01', 'ICD9CM:488.02', 'ICD9CM:488.09', 'ICD9CM:488.1', 'ICD9CM:488.11', 'ICD9CM:488.12', 'ICD9CM:488.19', 'ICD9CM:488.81', 'ICD9CM:488.82', 'ICD9CM:488.89'):
            results_ccs2["influenza"].append(1)
        else: results_ccs2["influenza"].append(0)
    print("Completed Binary Recode of: influenza")

    # Acute_and_chronic_tonsillitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:463', 'ICD9CM:474.0', 'ICD9CM:474.00', 'ICD9CM:474.01', 'ICD9CM:474.02', 'ICD9CM:474.10', 'ICD9CM:474.11', 'ICD9CM:474.12', 'ICD9CM:474.2', 'ICD9CM:474.8', 'ICD9CM:474.9', 'ICD9CM:475'):
            results_ccs2["acute_tonsil"].append(1)
        else: results_ccs2["acute_tonsil"].append(0)
    print("Completed Binary Recode of: acute_tonsil")

    # Acute_bronchitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:466.0', 'ICD9CM:466.1', 'ICD9CM:466.11', 'ICD9CM:466.19'):
            results_ccs2["acute_bronch"].append(1)
        else: results_ccs2["acute_bronch"].append(0)
    print("Completed Binary Recode of: acute_bronch")

    # Other_upper_respiratory_infections
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:032.0', 'ICD9CM:032.1', 'ICD9CM:032.2', 'ICD9CM:032.3', 'ICD9CM:034.0', 'ICD9CM:460', 'ICD9CM:461.0', 'ICD9CM:461.1', 'ICD9CM:461.2', 'ICD9CM:461.3', 'ICD9CM:461.8', 'ICD9CM:461.9', 'ICD9CM:462', 'ICD9CM:464.0', 'ICD9CM:464.00', 'ICD9CM:464.01', 'ICD9CM:464.10', 'ICD9CM:464.11', 'ICD9CM:464.20', 'ICD9CM:464.21', 'ICD9CM:464.30', 'ICD9CM:464.31', 'ICD9CM:464.4', 'ICD9CM:464.50', 'ICD9CM:464.51', 'ICD9CM:465.0', 'ICD9CM:465.8', 'ICD9CM:465.9', 'ICD9CM:473.0', 'ICD9CM:473.1', 'ICD9CM:473.2', 'ICD9CM:473.3', 'ICD9CM:473.8', 'ICD9CM:473.9', 'ICD9CM:784.91'):
            results_ccs2["upper_resp_infec"].append(1)
        else: results_ccs2["upper_resp_infec"].append(0)
    print("Completed Binary Recode of: upper_resp_infec")

    # Chronic_obstructive_pulmonary_disease_and_bronchiectasis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:490', 'ICD9CM:491.0', 'ICD9CM:491.1', 'ICD9CM:491.2', 'ICD9CM:491.20', 'ICD9CM:491.21', 'ICD9CM:491.22', 'ICD9CM:491.8', 'ICD9CM:491.9', 'ICD9CM:492.0', 'ICD9CM:492.8', 'ICD9CM:494', 'ICD9CM:494.0', 'ICD9CM:494.1', 'ICD9CM:496'):
            results_ccs2["copd"].append(1)
        else: results_ccs2["copd"].append(0)
    print("Completed Binary Recode of: copd")

    # Asthma
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:493.00', 'ICD9CM:493.01', 'ICD9CM:493.02', 'ICD9CM:493.10', 'ICD9CM:493.11', 'ICD9CM:493.12', 'ICD9CM:493.20', 'ICD9CM:493.21', 'ICD9CM:493.22', 'ICD9CM:493.81', 'ICD9CM:493.82', 'ICD9CM:493.90', 'ICD9CM:493.91', 'ICD9CM:493.92'):
            results_ccs2["asthma"].append(1)
        else: results_ccs2["asthma"].append(0)
    print("Completed Binary Recode of: asthma")

    # Aspiration_pneumonitis;_food/_vomitus
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:507.0':
            results_ccs2["asp_pneumonitis"].append(1)
        else: results_ccs2["asp_pneumonitis"].append(0)
    print("Completed Binary Recode of: asp_pneumonitis")

    # Pleurisy;_pneumothorax;_pulmonary_collapse
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:510.0', 'ICD9CM:510.9', 'ICD9CM:511.0', 'ICD9CM:511.1', 'ICD9CM:511.8', 'ICD9CM:511.89', 'ICD9CM:511.9', 'ICD9CM:512.0', 'ICD9CM:512.8', 'ICD9CM:512.81', 'ICD9CM:512.82', 'ICD9CM:512.83', 'ICD9CM:512.84', 'ICD9CM:512.89', 'ICD9CM:518.0', 'ICD9CM:518.1', 'ICD9CM:518.2'):
            results_ccs2["pneumothorax"].append(1)
        else: results_ccs2["pneumothorax"].append(0)
    print("Completed Binary Recode of: pneumothorax")

    # Respiratory_failure;_insufficiency;_arrest_(_adult)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:517.3', 'ICD9CM:518.5', 'ICD9CM:518.51', 'ICD9CM:518.52', 'ICD9CM:518.53', 'ICD9CM:518.81', 'ICD9CM:518.82', 'ICD9CM:518.83', 'ICD9CM:518.84', 'ICD9CM:799.1', 'ICD9CM:V46.1', 'ICD9CM:V46.11', 'ICD9CM:V46.12', 'ICD9CM:V46.13', 'ICD9CM:V46.14', 'ICD9CM:V46.2'):
            results_ccs2["resp_failure"].append(1)
        else: results_ccs2["resp_failure"].append(0)
    print("Completed Binary Recode of: resp_failure")

    # Lung_disease_due_to_external_agents
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:495.0', 'ICD9CM:495.1', 'ICD9CM:495.2', 'ICD9CM:495.3', 'ICD9CM:495.4', 'ICD9CM:495.5', 'ICD9CM:495.6', 'ICD9CM:495.7', 'ICD9CM:495.8', 'ICD9CM:495.9', 'ICD9CM:500', 'ICD9CM:501', 'ICD9CM:502', 'ICD9CM:503', 'ICD9CM:504', 'ICD9CM:505', 'ICD9CM:506.0', 'ICD9CM:506.1', 'ICD9CM:506.2', 'ICD9CM:506.3', 'ICD9CM:506.4', 'ICD9CM:506.9', 'ICD9CM:507.1', 'ICD9CM:507.8', 'ICD9CM:508.0', 'ICD9CM:508.1', 'ICD9CM:508.2', 'ICD9CM:508.8', 'ICD9CM:508.9'):
            results_ccs2["lung_disease"].append(1)
        else: results_ccs2["lung_disease"].append(0)
    print("Completed Binary Recode of: lung_disease")

    # Other_lower_respiratory_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:513.1', 'ICD9CM:514', 'ICD9CM:515', 'ICD9CM:516.0', 'ICD9CM:516.1', 'ICD9CM:516.2', 'ICD9CM:516.3', 'ICD9CM:516.30', 'ICD9CM:516.31', 'ICD9CM:516.32', 'ICD9CM:516.33', 'ICD9CM:516.34', 'ICD9CM:516.35', 'ICD9CM:516.36', 'ICD9CM:516.37', 'ICD9CM:516.4', 'ICD9CM:516.5', 'ICD9CM:516.61', 'ICD9CM:516.62', 'ICD9CM:516.63', 'ICD9CM:516.64', 'ICD9CM:516.69', 'ICD9CM:516.8', 'ICD9CM:516.9', 'ICD9CM:517.2', 'ICD9CM:517.8', 'ICD9CM:518.3', 'ICD9CM:518.4', 'ICD9CM:518.89', 'ICD9CM:519.4', 'ICD9CM:519.8', 'ICD9CM:519.9', 'ICD9CM:782.5', 'ICD9CM:786.00', 'ICD9CM:786.01', 'ICD9CM:786.02', 'ICD9CM:786.03', 'ICD9CM:786.04', 'ICD9CM:786.05', 'ICD9CM:786.06', 'ICD9CM:786.07', 'ICD9CM:786.09', 'ICD9CM:786.2', 'ICD9CM:786.3', 'ICD9CM:786.30', 'ICD9CM:786.31', 'ICD9CM:786.39', 'ICD9CM:786.4', 'ICD9CM:786.52', 'ICD9CM:786.6', 'ICD9CM:786.7', 'ICD9CM:786.8', 'ICD9CM:786.9', 'ICD9CM:793.1', 'ICD9CM:793.11', 'ICD9CM:793.19', 'ICD9CM:794.2', 'ICD9CM:V12.6', 'ICD9CM:V12.60', 'ICD9CM:V12.61', 'ICD9CM:V12.69', 'ICD9CM:V42.6'):
            results_ccs2["other_low_resp"].append(1)
        else: results_ccs2["other_low_resp"].append(0)
    print("Completed Binary Recode of: other_low_resp")

    # Other_upper_respiratory_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:470', 'ICD9CM:471.0', 'ICD9CM:471.1', 'ICD9CM:471.8', 'ICD9CM:471.9', 'ICD9CM:472.0', 'ICD9CM:472.1', 'ICD9CM:472.2', 'ICD9CM:476.0', 'ICD9CM:476.1', 'ICD9CM:477.0', 'ICD9CM:477.2', 'ICD9CM:477.8', 'ICD9CM:477.9', 'ICD9CM:478.0', 'ICD9CM:478.1', 'ICD9CM:478.11', 'ICD9CM:478.19', 'ICD9CM:478.20', 'ICD9CM:478.21', 'ICD9CM:478.22', 'ICD9CM:478.24', 'ICD9CM:478.25', 'ICD9CM:478.26', 'ICD9CM:478.29', 'ICD9CM:478.30', 'ICD9CM:478.31', 'ICD9CM:478.32', 'ICD9CM:478.33', 'ICD9CM:478.34', 'ICD9CM:478.4', 'ICD9CM:478.5', 'ICD9CM:478.6', 'ICD9CM:478.70', 'ICD9CM:478.71', 'ICD9CM:478.74', 'ICD9CM:478.75', 'ICD9CM:478.79', 'ICD9CM:478.8', 'ICD9CM:478.9', 'ICD9CM:519.1', 'ICD9CM:519.11', 'ICD9CM:519.19', 'ICD9CM:519.2', 'ICD9CM:519.3', 'ICD9CM:784.1', 'ICD9CM:784.40', 'ICD9CM:784.41', 'ICD9CM:784.42', 'ICD9CM:784.43', 'ICD9CM:784.44', 'ICD9CM:784.49', 'ICD9CM:784.7', 'ICD9CM:784.8', 'ICD9CM:784.9', 'ICD9CM:784.99', 'ICD9CM:786.1', 'ICD9CM:V41.4', 'ICD9CM:V44.0', 'ICD9CM:V55.0'):
            results_ccs2["other_up_resp"].append(1)
        else: results_ccs2["other_up_resp"].append(0)
    print("Completed Binary Recode of: other_up_resp")

    # Intestinal_infection
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:001.0', 'ICD9CM:001.1', 'ICD9CM:001.9', 'ICD9CM:002.0', 'ICD9CM:002.1', 'ICD9CM:002.2', 'ICD9CM:002.3', 'ICD9CM:002.9', 'ICD9CM:003.0', 'ICD9CM:003.20', 'ICD9CM:003.29', 'ICD9CM:003.8', 'ICD9CM:003.9', 'ICD9CM:004.0', 'ICD9CM:004.1', 'ICD9CM:004.2', 'ICD9CM:004.3', 'ICD9CM:004.8', 'ICD9CM:004.9', 'ICD9CM:005.0', 'ICD9CM:005.1', 'ICD9CM:005.2', 'ICD9CM:005.3', 'ICD9CM:005.4', 'ICD9CM:005.8', 'ICD9CM:005.81', 'ICD9CM:005.89', 'ICD9CM:005.9', 'ICD9CM:006.0', 'ICD9CM:006.1', 'ICD9CM:006.2', 'ICD9CM:006.3', 'ICD9CM:006.4', 'ICD9CM:006.5', 'ICD9CM:006.6', 'ICD9CM:006.8', 'ICD9CM:006.9', 'ICD9CM:007.0', 'ICD9CM:007.1', 'ICD9CM:007.2', 'ICD9CM:007.3', 'ICD9CM:007.4', 'ICD9CM:007.5', 'ICD9CM:007.8', 'ICD9CM:007.9', 'ICD9CM:008.0', 'ICD9CM:008.00', 'ICD9CM:008.01', 'ICD9CM:008.02', 'ICD9CM:008.03', 'ICD9CM:008.04', 'ICD9CM:008.09', 'ICD9CM:008.1', 'ICD9CM:008.2', 'ICD9CM:008.3', 'ICD9CM:008.41', 'ICD9CM:008.42', 'ICD9CM:008.43', 'ICD9CM:008.44', 'ICD9CM:008.45', 'ICD9CM:008.46', 'ICD9CM:008.47', 'ICD9CM:008.49', 'ICD9CM:008.5', 'ICD9CM:008.6', 'ICD9CM:008.61', 'ICD9CM:008.62', 'ICD9CM:008.63', 'ICD9CM:008.64', 'ICD9CM:008.65', 'ICD9CM:008.66', 'ICD9CM:008.67', 'ICD9CM:008.69', 'ICD9CM:008.8', 'ICD9CM:009.0', 'ICD9CM:009.1', 'ICD9CM:009.2', 'ICD9CM:009.3', 'ICD9CM:021.1', 'ICD9CM:022.2'):
            results_ccs2["intestinal_infec"].append(1)
        else: results_ccs2["intestinal_infec"].append(0)
    print("Completed Binary Recode of: intestinal_infec")

    # Disorders_of_teeth_and_jaw
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:520.0', 'ICD9CM:520.1', 'ICD9CM:520.2', 'ICD9CM:520.3', 'ICD9CM:520.4', 'ICD9CM:520.5', 'ICD9CM:520.6', 'ICD9CM:520.7', 'ICD9CM:520.8', 'ICD9CM:520.9', 'ICD9CM:521.0', 'ICD9CM:521.00', 'ICD9CM:521.01', 'ICD9CM:521.02', 'ICD9CM:521.03', 'ICD9CM:521.04', 'ICD9CM:521.05', 'ICD9CM:521.06', 'ICD9CM:521.07', 'ICD9CM:521.08', 'ICD9CM:521.09', 'ICD9CM:521.1', 'ICD9CM:521.10', 'ICD9CM:521.11', 'ICD9CM:521.12', 'ICD9CM:521.13', 'ICD9CM:521.14', 'ICD9CM:521.15', 'ICD9CM:521.2', 'ICD9CM:521.20', 'ICD9CM:521.21', 'ICD9CM:521.22', 'ICD9CM:521.23', 'ICD9CM:521.24', 'ICD9CM:521.25', 'ICD9CM:521.3', 'ICD9CM:521.30', 'ICD9CM:521.31', 'ICD9CM:521.32', 'ICD9CM:521.33', 'ICD9CM:521.34', 'ICD9CM:521.35', 'ICD9CM:521.4', 'ICD9CM:521.40', 'ICD9CM:521.41', 'ICD9CM:521.42', 'ICD9CM:521.49', 'ICD9CM:521.5', 'ICD9CM:521.6', 'ICD9CM:521.7', 'ICD9CM:521.8', 'ICD9CM:521.81', 'ICD9CM:521.89', 'ICD9CM:521.9', 'ICD9CM:522.0', 'ICD9CM:522.1', 'ICD9CM:522.2', 'ICD9CM:522.3', 'ICD9CM:522.4', 'ICD9CM:522.5', 'ICD9CM:522.6', 'ICD9CM:522.7', 'ICD9CM:522.8', 'ICD9CM:522.9', 'ICD9CM:523.0', 'ICD9CM:523.00', 'ICD9CM:523.01', 'ICD9CM:523.1', 'ICD9CM:523.10', 'ICD9CM:523.11', 'ICD9CM:523.2', 'ICD9CM:523.20', 'ICD9CM:523.21', 'ICD9CM:523.22', 'ICD9CM:523.23', 'ICD9CM:523.24', 'ICD9CM:523.25', 'ICD9CM:523.3', 'ICD9CM:523.30', 'ICD9CM:523.31', 'ICD9CM:523.32', 'ICD9CM:523.33', 'ICD9CM:523.4', 'ICD9CM:523.40', 'ICD9CM:523.41', 'ICD9CM:523.42', 'ICD9CM:523.5', 'ICD9CM:523.6', 'ICD9CM:523.8', 'ICD9CM:523.9', 'ICD9CM:524.0', 'ICD9CM:524.00', 'ICD9CM:524.01', 'ICD9CM:524.02', 'ICD9CM:524.03', 'ICD9CM:524.04', 'ICD9CM:524.05', 'ICD9CM:524.06', 'ICD9CM:524.07', 'ICD9CM:524.09', 'ICD9CM:524.1', 'ICD9CM:524.10', 'ICD9CM:524.11', 'ICD9CM:524.12', 'ICD9CM:524.19', 'ICD9CM:524.2', 'ICD9CM:524.20', 'ICD9CM:524.21', 'ICD9CM:524.22', 'ICD9CM:524.23', 'ICD9CM:524.24', 'ICD9CM:524.25', 'ICD9CM:524.26', 'ICD9CM:524.27', 'ICD9CM:524.28', 'ICD9CM:524.29', 'ICD9CM:524.3', 'ICD9CM:524.30', 'ICD9CM:524.31', 'ICD9CM:524.32', 'ICD9CM:524.33', 'ICD9CM:524.34', 'ICD9CM:524.35', 'ICD9CM:524.36', 'ICD9CM:524.37', 'ICD9CM:524.39', 'ICD9CM:524.4', 'ICD9CM:524.5', 'ICD9CM:524.50', 'ICD9CM:524.51', 'ICD9CM:524.52', 'ICD9CM:524.53', 'ICD9CM:524.54', 'ICD9CM:524.55', 'ICD9CM:524.56', 'ICD9CM:524.57', 'ICD9CM:524.59', 'ICD9CM:524.6', 'ICD9CM:524.60', 'ICD9CM:524.61', 'ICD9CM:524.62', 'ICD9CM:524.63', 'ICD9CM:524.64', 'ICD9CM:524.69', 'ICD9CM:524.70', 'ICD9CM:524.71', 'ICD9CM:524.72', 'ICD9CM:524.73', 'ICD9CM:524.74', 'ICD9CM:524.75', 'ICD9CM:524.76', 'ICD9CM:524.79', 'ICD9CM:524.8', 'ICD9CM:524.81', 'ICD9CM:524.82', 'ICD9CM:524.89', 'ICD9CM:524.9', 'ICD9CM:525.0', 'ICD9CM:525.1', 'ICD9CM:525.10', 'ICD9CM:525.11', 'ICD9CM:525.12', 'ICD9CM:525.13', 'ICD9CM:525.19', 'ICD9CM:525.2', 'ICD9CM:525.20', 'ICD9CM:525.21', 'ICD9CM:525.22', 'ICD9CM:525.23', 'ICD9CM:525.24', 'ICD9CM:525.25', 'ICD9CM:525.26', 'ICD9CM:525.3', 'ICD9CM:525.40', 'ICD9CM:525.41', 'ICD9CM:525.42', 'ICD9CM:525.43', 'ICD9CM:525.44', 'ICD9CM:525.50', 'ICD9CM:525.51', 'ICD9CM:525.52', 'ICD9CM:525.53', 'ICD9CM:525.54', 'ICD9CM:525.60', 'ICD9CM:525.61', 'ICD9CM:525.62', 'ICD9CM:525.63', 'ICD9CM:525.64', 'ICD9CM:525.65', 'ICD9CM:525.66', 'ICD9CM:525.67', 'ICD9CM:525.69', 'ICD9CM:525.71', 'ICD9CM:525.72', 'ICD9CM:525.73', 'ICD9CM:525.79', 'ICD9CM:525.8', 'ICD9CM:525.9', 'ICD9CM:526.0', 'ICD9CM:526.1', 'ICD9CM:526.2', 'ICD9CM:526.3', 'ICD9CM:526.4', 'ICD9CM:526.5', 'ICD9CM:526.61', 'ICD9CM:526.62', 'ICD9CM:526.63', 'ICD9CM:526.69', 'ICD9CM:526.81', 'ICD9CM:526.89', 'ICD9CM:526.9', 'ICD9CM:784.92', 'ICD9CM:V52.3', 'ICD9CM:V53.4', 'ICD9CM:V58.5', 'ICD9CM:V72.2'):
            results_ccs2["teeth_jaw"].append(1)
        else: results_ccs2["teeth_jaw"].append(0)
    print("Completed Binary Recode of: teeth_jaw")

    # Diseases_of_mouth;_excluding_dental
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:527.0', 'ICD9CM:527.1', 'ICD9CM:527.2', 'ICD9CM:527.3', 'ICD9CM:527.4', 'ICD9CM:527.5', 'ICD9CM:527.6', 'ICD9CM:527.7', 'ICD9CM:527.8', 'ICD9CM:527.9', 'ICD9CM:528.0', 'ICD9CM:528.00', 'ICD9CM:528.09', 'ICD9CM:528.1', 'ICD9CM:528.2', 'ICD9CM:528.3', 'ICD9CM:528.4', 'ICD9CM:528.5', 'ICD9CM:528.6', 'ICD9CM:528.7', 'ICD9CM:528.71', 'ICD9CM:528.72', 'ICD9CM:528.79', 'ICD9CM:528.8', 'ICD9CM:528.9', 'ICD9CM:529.0', 'ICD9CM:529.1', 'ICD9CM:529.2', 'ICD9CM:529.3', 'ICD9CM:529.4', 'ICD9CM:529.5', 'ICD9CM:529.6', 'ICD9CM:529.8', 'ICD9CM:529.9', 'ICD9CM:792.4'):
            results_ccs2["mouth_disease"].append(1)
        else: results_ccs2["mouth_disease"].append(0)
    print("Completed Binary Recode of: mouth_disease")

    # Esophageal_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:456.1', 'ICD9CM:456.21', 'ICD9CM:530.0', 'ICD9CM:530.1', 'ICD9CM:530.10', 'ICD9CM:530.11', 'ICD9CM:530.12', 'ICD9CM:530.13', 'ICD9CM:530.19', 'ICD9CM:530.2', 'ICD9CM:530.20', 'ICD9CM:530.21', 'ICD9CM:530.3', 'ICD9CM:530.4', 'ICD9CM:530.5', 'ICD9CM:530.6', 'ICD9CM:530.8', 'ICD9CM:530.81', 'ICD9CM:530.83', 'ICD9CM:530.84', 'ICD9CM:530.85', 'ICD9CM:530.89', 'ICD9CM:530.9'):
            results_ccs2["esophagus"].append(1)
        else: results_ccs2["esophagus"].append(0)
    print("Completed Binary Recode of: esophagus")

    # Gastroduodenal_ulcer_(_except_hemorrhage)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:531.10', 'ICD9CM:531.11', 'ICD9CM:531.30', 'ICD9CM:531.31', 'ICD9CM:531.50', 'ICD9CM:531.51', 'ICD9CM:531.70', 'ICD9CM:531.71', 'ICD9CM:531.90', 'ICD9CM:531.91', 'ICD9CM:532.10', 'ICD9CM:532.11', 'ICD9CM:532.30', 'ICD9CM:532.31', 'ICD9CM:532.50', 'ICD9CM:532.51', 'ICD9CM:532.70', 'ICD9CM:532.71', 'ICD9CM:532.90', 'ICD9CM:532.91', 'ICD9CM:533.10', 'ICD9CM:533.11', 'ICD9CM:533.30', 'ICD9CM:533.31', 'ICD9CM:533.50', 'ICD9CM:533.51', 'ICD9CM:533.70', 'ICD9CM:533.71', 'ICD9CM:533.90', 'ICD9CM:533.91', 'ICD9CM:534.10', 'ICD9CM:534.11', 'ICD9CM:534.30', 'ICD9CM:534.31', 'ICD9CM:534.50', 'ICD9CM:534.51', 'ICD9CM:534.70', 'ICD9CM:534.71', 'ICD9CM:534.90', 'ICD9CM:534.91', 'ICD9CM:V12.71'):
            results_ccs2["gastro_ulcer"].append(1)
        else: results_ccs2["gastro_ulcer"].append(0)
    print("Completed Binary Recode of: gastro_ulcer")

    # Gastritis_and_duodenitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:535.0', 'ICD9CM:535.00', 'ICD9CM:535.01', 'ICD9CM:535.1', 'ICD9CM:535.10', 'ICD9CM:535.11', 'ICD9CM:535.2', 'ICD9CM:535.20', 'ICD9CM:535.21', 'ICD9CM:535.4', 'ICD9CM:535.40', 'ICD9CM:535.41', 'ICD9CM:535.5', 'ICD9CM:535.50', 'ICD9CM:535.51', 'ICD9CM:535.6', 'ICD9CM:535.60', 'ICD9CM:535.61', 'ICD9CM:535.70', 'ICD9CM:535.71'):
            results_ccs2["gastritis"].append(1)
        else: results_ccs2["gastritis"].append(0)
    print("Completed Binary Recode of: gastritis")

    # Other_disorders_of_stomach_and_duodenum
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:536.0', 'ICD9CM:536.1', 'ICD9CM:536.2', 'ICD9CM:536.3', 'ICD9CM:536.8', 'ICD9CM:536.9', 'ICD9CM:537.0', 'ICD9CM:537.1', 'ICD9CM:537.2', 'ICD9CM:537.3', 'ICD9CM:537.4', 'ICD9CM:537.5', 'ICD9CM:537.6', 'ICD9CM:537.81', 'ICD9CM:537.82', 'ICD9CM:537.83', 'ICD9CM:537.84', 'ICD9CM:537.89', 'ICD9CM:537.9'):
            results_ccs2["other_stomach_duo"].append(1)
        else: results_ccs2["other_stomach_duo"].append(0)
    print("Completed Binary Recode of: other_stomach_duo")

    pd.DataFrame(results_ccs2).to_csv(output_filepath, encoding='utf-8')
    print("CDRN - CCS Dx Recode Part 2: Complete")
    print("")
    

###########################
###########################
###########################
###########################
###########################
###########################


def dx_convert3(df):

    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results3.csv'

    results_ccs3 = {"person_id":[],"condition_start_date":[],"appendicitis": [], "hernia_abd": [], "regional_enteriritis": [], "intestinal_obstruct": [],"diverticulitis": [], "anal_condition": [], "peritonitis": [], "biliary_tract": [],
"other_liver": [], "pancreatic": [], "gastro_hemorrhage": [], "noninfec_gastro": [],
"other_gastro": [], "nephritis": [], "acute_renal_fail": [], "ckd": [], "uti": [],
"calculus_urinary": [], "other_kidney": [], "other_bladder": [], "genitourinary_symp": [],
"prostate_hyp": [], "male_genital_inflam": [], "other_male_genital": [], "nonmalig_breast": [],
"inflam_fem_pelvic": [], "endometriosis": [], "prolapse_fem_gen": [], "menstrual": [],
"ovarian_cyst": [], "menopausal": [], "fem_infert": [], "other_fem_genital": [],
"contraceptive_mgmt": [], "spont_abortion": [], "induce_abortion": [], "postabort_comp": [],
"ectopic_preg": [], "other_comp_preg": [], "hemorrhage_preg": [], "htn_comp_preg": [],
"early_labor": [], "prolong_preg": [], "dm_comp_preg": [], "malposition": [],
"fetopelvic_disrupt": [], "prev_c_sect": [], "fetal_distress": [], "polyhydramnios": [],
"umbilical_comp": [], "ob_trauma": [], "forceps_deliv": [], "other_comp_birth": [],
"other_preg_deliv": [], "skin_tissue_infec": [], "other_skin_inflam": [], "chronic_skin_ulcer": [],
"other_skin": [], "infec_arthritis": [], "rheum_arth": [], "osteo_arth": [], "other_joint": [],
"spondylosis": [], "osteoporosis": [], "pathological_fract": [], "acq_foot_deform": [],
"other_acq_deform": [], "systemic_lupus": [], "other_connective": [], "other_bone_disease": [],
"cardiac_congen_anom": [], "digest_congen_anom": [], "genito_congen_anom": [], "ns_congen_anom": [],
"other_congen_anom": [], "liveborn": [], "short_gest": [], "intrauter_hypoxia": [],
"resp_distress_synd": [], "hemolytic_jaundice": []}

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs3["person_id"].append(_)
    print("Number of person_id with missing dx history: ", len(results_ccs3["person_id"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs3["condition_start_date"].append(dt.datetime.strptime('12/31/13', "%m/%d/%y"))
    print("Number of start dates added for patients with missing dx history: ",
          len(results_ccs3["condition_start_date"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs3["appendicitis"].append(0)
        results_ccs3["hernia_abd"].append(0)
        results_ccs3["regional_enteriritis"].append(0)
        results_ccs3["intestinal_obstruct"].append(0)
        results_ccs3["diverticulitis"].append(0)
        results_ccs3["anal_condition"].append(0)
        results_ccs3["peritonitis"].append(0)
        results_ccs3["biliary_tract"].append(0)
        results_ccs3["other_liver"].append(0)
        results_ccs3["pancreatic"].append(0)
        results_ccs3["gastro_hemorrhage"].append(0)
        results_ccs3["noninfec_gastro"].append(0)
        results_ccs3["other_gastro"].append(0)
        results_ccs3["nephritis"].append(0)
        results_ccs3["acute_renal_fail"].append(0)
        results_ccs3["ckd"].append(0)
        results_ccs3["uti"].append(0)
        results_ccs3["calculus_urinary"].append(0)
        results_ccs3["other_kidney"].append(0)
        results_ccs3["other_bladder"].append(0)
        results_ccs3["genitourinary_symp"].append(0)
        results_ccs3["prostate_hyp"].append(0)
        results_ccs3["male_genital_inflam"].append(0)
        results_ccs3["other_male_genital"].append(0)
        results_ccs3["nonmalig_breast"].append(0)
        results_ccs3["inflam_fem_pelvic"].append(0)
        results_ccs3["endometriosis"].append(0)
        results_ccs3["prolapse_fem_gen"].append(0)
        results_ccs3["menstrual"].append(0)
        results_ccs3["ovarian_cyst"].append(0)
        results_ccs3["menopausal"].append(0)
        results_ccs3["fem_infert"].append(0)
        results_ccs3["other_fem_genital"].append(0)
        results_ccs3["contraceptive_mgmt"].append(0)
        results_ccs3["spont_abortion"].append(0)
        results_ccs3["induce_abortion"].append(0)
        results_ccs3["postabort_comp"].append(0)
        results_ccs3["ectopic_preg"].append(0)
        results_ccs3["other_comp_preg"].append(0)
        results_ccs3["hemorrhage_preg"].append(0)
        results_ccs3["htn_comp_preg"].append(0)
        results_ccs3["early_labor"].append(0)
        results_ccs3["prolong_preg"].append(0)
        results_ccs3["dm_comp_preg"].append(0)
        results_ccs3["malposition"].append(0)
        results_ccs3["fetopelvic_disrupt"].append(0)
        results_ccs3["prev_c_sect"].append(0)
        results_ccs3["fetal_distress"].append(0)
        results_ccs3["polyhydramnios"].append(0)
        results_ccs3["umbilical_comp"].append(0)
        results_ccs3["ob_trauma"].append(0)
        results_ccs3["forceps_deliv"].append(0)
        results_ccs3["other_comp_birth"].append(0)
        results_ccs3["other_preg_deliv"].append(0)
        results_ccs3["skin_tissue_infec"].append(0)
        results_ccs3["other_skin_inflam"].append(0)
        results_ccs3["chronic_skin_ulcer"].append(0)
        results_ccs3["other_skin"].append(0)
        results_ccs3["infec_arthritis"].append(0)
        results_ccs3["rheum_arth"].append(0)
        results_ccs3["osteo_arth"].append(0)
        results_ccs3["other_joint"].append(0)
        results_ccs3["spondylosis"].append(0)
        results_ccs3["osteoporosis"].append(0)
        results_ccs3["pathological_fract"].append(0)
        results_ccs3["acq_foot_deform"].append(0)
        results_ccs3["other_acq_deform"].append(0)
        results_ccs3["systemic_lupus"].append(0)
        results_ccs3["other_connective"].append(0)
        results_ccs3["other_bone_disease"].append(0)
        results_ccs3["cardiac_congen_anom"].append(0)
        results_ccs3["digest_congen_anom"].append(0)
        results_ccs3["genito_congen_anom"].append(0)
        results_ccs3["ns_congen_anom"].append(0)
        results_ccs3["other_congen_anom"].append(0)
        results_ccs3["liveborn"].append(0)
        results_ccs3["short_gest"].append(0)
        results_ccs3["intrauter_hypoxia"].append(0)
        results_ccs3["resp_distress_synd"].append(0)
        results_ccs3["hemolytic_jaundice"].append(0)
    print("Completed null dx recode for pts that are missing dx but meet visit criteria")

    for _ in df['person_id']:
        results_ccs3["person_id"].append(_)
    print("Number of patients in results_ccs3", len(results_ccs3["person_id"]))

    for _ in df['condition_start_date']:
        results_ccs3["condition_start_date"].append(_)
    print("Number of start dates in results_ccs3", len(results_ccs3["condition_start_date"]))

    # Appendicitis_and_other_appendiceal_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:540.0', 'ICD9CM:540.1', 'ICD9CM:540.9', 'ICD9CM:541', 'ICD9CM:542', 'ICD9CM:543.0', 'ICD9CM:543.9'):
            results_ccs3["appendicitis"].append(1)
        else: results_ccs3["appendicitis"].append(0)
    print("Completed Binary Recode of: appendicitis")

    # Abdominal_hernia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:550.00', 'ICD9CM:550.01', 'ICD9CM:550.02', 'ICD9CM:550.03', 'ICD9CM:550.10', 'ICD9CM:550.11', 'ICD9CM:550.12', 'ICD9CM:550.13', 'ICD9CM:550.90', 'ICD9CM:550.91', 'ICD9CM:550.92', 'ICD9CM:550.93', 'ICD9CM:551.00', 'ICD9CM:551.01', 'ICD9CM:551.02', 'ICD9CM:551.03', 'ICD9CM:551.1', 'ICD9CM:551.20', 'ICD9CM:551.21', 'ICD9CM:551.29', 'ICD9CM:551.3', 'ICD9CM:551.8', 'ICD9CM:551.9', 'ICD9CM:552.00', 'ICD9CM:552.01', 'ICD9CM:552.02', 'ICD9CM:552.03', 'ICD9CM:552.1', 'ICD9CM:552.20', 'ICD9CM:552.21', 'ICD9CM:552.29', 'ICD9CM:552.3', 'ICD9CM:552.8', 'ICD9CM:552.9', 'ICD9CM:553.00', 'ICD9CM:553.01', 'ICD9CM:553.02', 'ICD9CM:553.03', 'ICD9CM:553.1', 'ICD9CM:553.20', 'ICD9CM:553.21', 'ICD9CM:553.29', 'ICD9CM:553.3', 'ICD9CM:553.8', 'ICD9CM:553.9'):
            results_ccs3["hernia_abd"].append(1)
        else: results_ccs3["hernia_abd"].append(0)
    print("Completed Binary Recode of: hernia_abd")

    # Regional_enteritis_and_ulcerative_colitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:555.0', 'ICD9CM:555.1', 'ICD9CM:555.2', 'ICD9CM:555.9', 'ICD9CM:556', 'ICD9CM:556.0', 'ICD9CM:556.1', 'ICD9CM:556.2', 'ICD9CM:556.3', 'ICD9CM:556.4', 'ICD9CM:556.5', 'ICD9CM:556.6', 'ICD9CM:556.8', 'ICD9CM:556.9'):
            results_ccs3["regional_enteriritis"].append(1)
        else: results_ccs3["regional_enteriritis"].append(0)
    print("Completed Binary Recode of: regional_enteriritis")

    # Intestinal_obstruction_without_hernia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:560.0', 'ICD9CM:560.1', 'ICD9CM:560.2', 'ICD9CM:560.30', 'ICD9CM:560.31', 'ICD9CM:560.32', 'ICD9CM:560.39', 'ICD9CM:560.81', 'ICD9CM:560.89', 'ICD9CM:560.9'):
            results_ccs3["intestinal_obstruct"].append(1)
        else: results_ccs3["intestinal_obstruct"].append(0)
    print("Completed Binary Recode of: intestinal_obstruct")

    # Diverticulosis_and_diverticulitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:562.00', 'ICD9CM:562.01', 'ICD9CM:562.02', 'ICD9CM:562.03', 'ICD9CM:562.10', 'ICD9CM:562.11', 'ICD9CM:562.12', 'ICD9CM:562.13'):
            results_ccs3["diverticulitis"].append(1)
        else: results_ccs3["diverticulitis"].append(0)
    print("Completed Binary Recode of: diverticulitis")

    # Anal_and_rectal_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:564.6', 'ICD9CM:565.0', 'ICD9CM:565.1', 'ICD9CM:566', 'ICD9CM:569.0', 'ICD9CM:569.1', 'ICD9CM:569.2', 'ICD9CM:569.41', 'ICD9CM:569.42', 'ICD9CM:569.43', 'ICD9CM:569.44', 'ICD9CM:569.49'):
            results_ccs3["anal_condition"].append(1)
        else: results_ccs3["anal_condition"].append(0)
    print("Completed Binary Recode of: anal_condition")

    # Peritonitis_and_intestinal_abscess
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:032.83', 'ICD9CM:567.0', 'ICD9CM:567.1', 'ICD9CM:567.2', 'ICD9CM:567.21', 'ICD9CM:567.22', 'ICD9CM:567.23', 'ICD9CM:567.29', 'ICD9CM:567.38', 'ICD9CM:567.39', 'ICD9CM:567.8', 'ICD9CM:567.81', 'ICD9CM:567.82', 'ICD9CM:567.89', 'ICD9CM:567.9', 'ICD9CM:569.5'):
            results_ccs3["peritonitis"].append(1)
        else: results_ccs3["peritonitis"].append(0)
    print("Completed Binary Recode of: peritonitis")

    # Biliary_tract_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:574.00', 'ICD9CM:574.01', 'ICD9CM:574.10', 'ICD9CM:574.11', 'ICD9CM:574.20', 'ICD9CM:574.21', 'ICD9CM:574.30', 'ICD9CM:574.31', 'ICD9CM:574.40', 'ICD9CM:574.41', 'ICD9CM:574.50', 'ICD9CM:574.51', 'ICD9CM:574.60', 'ICD9CM:574.61', 'ICD9CM:574.70', 'ICD9CM:574.71', 'ICD9CM:574.80', 'ICD9CM:574.81', 'ICD9CM:574.90', 'ICD9CM:574.91', 'ICD9CM:575.0', 'ICD9CM:575.1', 'ICD9CM:575.10', 'ICD9CM:575.11', 'ICD9CM:575.12', 'ICD9CM:575.2', 'ICD9CM:575.3', 'ICD9CM:575.4', 'ICD9CM:575.5', 'ICD9CM:575.6', 'ICD9CM:575.8', 'ICD9CM:575.9', 'ICD9CM:576.0', 'ICD9CM:576.1', 'ICD9CM:576.2', 'ICD9CM:576.3', 'ICD9CM:576.4', 'ICD9CM:576.5', 'ICD9CM:576.8', 'ICD9CM:576.9', 'ICD9CM:793.3'):
            results_ccs3["biliary_tract"].append(1)
        else: results_ccs3["biliary_tract"].append(0)
    print("Completed Binary Recode of: biliary_tract")

    # Other_liver_diseases
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:570', 'ICD9CM:571.5', 'ICD9CM:571.6', 'ICD9CM:571.8', 'ICD9CM:571.9', 'ICD9CM:572.0', 'ICD9CM:572.1', 'ICD9CM:572.2', 'ICD9CM:572.3', 'ICD9CM:572.4', 'ICD9CM:572.8', 'ICD9CM:573.0', 'ICD9CM:573.4', 'ICD9CM:573.5', 'ICD9CM:573.8', 'ICD9CM:573.9', 'ICD9CM:782.4', 'ICD9CM:789.1', 'ICD9CM:789.5', 'ICD9CM:789.59', 'ICD9CM:790.4', 'ICD9CM:790.5', 'ICD9CM:794.8', 'ICD9CM:V42.7'):
            results_ccs3["other_liver"].append(1)
        else: results_ccs3["other_liver"].append(0)
    print("Completed Binary Recode of: other_liver")

    # Pancreatic_disorders_(_not_diabetes)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:577.0', 'ICD9CM:577.1', 'ICD9CM:577.2', 'ICD9CM:577.8', 'ICD9CM:577.9', 'ICD9CM:579.4'):
            results_ccs3["pancreatic"].append(1)
        else: results_ccs3["pancreatic"].append(0)
    print("Completed Binary Recode of: pancreatic")

    # Gastrointestinal_hemorrhage
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:456.0', 'ICD9CM:456.20', 'ICD9CM:530.7', 'ICD9CM:530.82', 'ICD9CM:531.00', 'ICD9CM:531.01', 'ICD9CM:531.20', 'ICD9CM:531.21', 'ICD9CM:531.40', 'ICD9CM:531.41', 'ICD9CM:531.60', 'ICD9CM:531.61', 'ICD9CM:532.00', 'ICD9CM:532.01', 'ICD9CM:532.20', 'ICD9CM:532.21', 'ICD9CM:532.40', 'ICD9CM:532.41', 'ICD9CM:532.60', 'ICD9CM:532.61', 'ICD9CM:533.00', 'ICD9CM:533.01', 'ICD9CM:533.20', 'ICD9CM:533.21', 'ICD9CM:533.40', 'ICD9CM:533.41', 'ICD9CM:533.60', 'ICD9CM:533.61', 'ICD9CM:534.00', 'ICD9CM:534.01', 'ICD9CM:534.20', 'ICD9CM:534.21', 'ICD9CM:534.40', 'ICD9CM:534.41', 'ICD9CM:534.60', 'ICD9CM:534.61', 'ICD9CM:569.3', 'ICD9CM:578.0', 'ICD9CM:578.1', 'ICD9CM:578.9'):
            results_ccs3["gastro_hemorrhage"].append(1)
        else: results_ccs3["gastro_hemorrhage"].append(0)
    print("Completed Binary Recode of: gastro_hemorrhage")

    # Noninfectious_gastroenteritis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:558.41', 'ICD9CM:558.42', 'ICD9CM:558.9'):
            results_ccs3["noninfec_gastro"].append(1)
        else: results_ccs3["noninfec_gastro"].append(0)
    print("Completed Binary Recode of: noninfec_gastro")

    # Other_gastrointestinal_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:538', 'ICD9CM:558.1', 'ICD9CM:558.2', 'ICD9CM:564.0', 'ICD9CM:564.00', 'ICD9CM:564.01', 'ICD9CM:564.02', 'ICD9CM:564.09', 'ICD9CM:564.1', 'ICD9CM:564.5', 'ICD9CM:564.7', 'ICD9CM:564.8', 'ICD9CM:564.81', 'ICD9CM:564.89', 'ICD9CM:564.9', 'ICD9CM:568.0', 'ICD9CM:568.81', 'ICD9CM:568.82', 'ICD9CM:568.89', 'ICD9CM:568.9', 'ICD9CM:569.81', 'ICD9CM:569.82', 'ICD9CM:569.83', 'ICD9CM:569.84', 'ICD9CM:569.85', 'ICD9CM:569.86', 'ICD9CM:569.87', 'ICD9CM:569.89', 'ICD9CM:569.9', 'ICD9CM:579.0', 'ICD9CM:579.1', 'ICD9CM:579.2', 'ICD9CM:579.8', 'ICD9CM:579.9', 'ICD9CM:787.1', 'ICD9CM:787.2', 'ICD9CM:787.20', 'ICD9CM:787.21', 'ICD9CM:787.22', 'ICD9CM:787.23', 'ICD9CM:787.24', 'ICD9CM:787.29', 'ICD9CM:787.3', 'ICD9CM:787.4', 'ICD9CM:787.5', 'ICD9CM:787.6', 'ICD9CM:787.60', 'ICD9CM:787.61', 'ICD9CM:787.62', 'ICD9CM:787.63', 'ICD9CM:787.7', 'ICD9CM:787.9', 'ICD9CM:787.91', 'ICD9CM:787.99', 'ICD9CM:789.2', 'ICD9CM:789.3', 'ICD9CM:789.30', 'ICD9CM:789.31', 'ICD9CM:789.32', 'ICD9CM:789.33', 'ICD9CM:789.34', 'ICD9CM:789.35', 'ICD9CM:789.36', 'ICD9CM:789.37', 'ICD9CM:789.39', 'ICD9CM:789.4', 'ICD9CM:789.40', 'ICD9CM:789.41', 'ICD9CM:789.42', 'ICD9CM:789.43', 'ICD9CM:789.44', 'ICD9CM:789.45', 'ICD9CM:789.46', 'ICD9CM:789.47', 'ICD9CM:789.49', 'ICD9CM:789.9', 'ICD9CM:792.1', 'ICD9CM:793.4', 'ICD9CM:793.6', 'ICD9CM:V12.7', 'ICD9CM:V12.70', 'ICD9CM:V12.79', 'ICD9CM:V41.6', 'ICD9CM:V44.1', 'ICD9CM:V44.2', 'ICD9CM:V44.3', 'ICD9CM:V44.4', 'ICD9CM:V45.3', 'ICD9CM:V47.3', 'ICD9CM:V53.5', 'ICD9CM:V53.50', 'ICD9CM:V53.51', 'ICD9CM:V53.59', 'ICD9CM:V55.1', 'ICD9CM:V55.2', 'ICD9CM:V55.3', 'ICD9CM:V55.4'):
            results_ccs3["other_gastro"].append(1)
        else: results_ccs3["other_gastro"].append(0)
    print("Completed Binary Recode of: other_gastro")

    # Nephritis;_nephrosis;_renal_sclerosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:580.0', 'ICD9CM:580.4', 'ICD9CM:580.81', 'ICD9CM:580.89', 'ICD9CM:580.9', 'ICD9CM:581.0', 'ICD9CM:581.1', 'ICD9CM:581.2', 'ICD9CM:581.3', 'ICD9CM:581.81', 'ICD9CM:581.89', 'ICD9CM:581.9', 'ICD9CM:582.0', 'ICD9CM:582.1', 'ICD9CM:582.2', 'ICD9CM:582.4', 'ICD9CM:582.81', 'ICD9CM:582.89', 'ICD9CM:582.9', 'ICD9CM:583.0', 'ICD9CM:583.1', 'ICD9CM:583.2', 'ICD9CM:583.4', 'ICD9CM:583.6', 'ICD9CM:583.7', 'ICD9CM:583.81', 'ICD9CM:583.89', 'ICD9CM:583.9', 'ICD9CM:587'):
            results_ccs3["nephritis"].append(1)
        else: results_ccs3["nephritis"].append(0)
    print("Completed Binary Recode of: nephritis")

    # Acute_and_unspecified_renal_failure
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:584.5', 'ICD9CM:584.6', 'ICD9CM:584.7', 'ICD9CM:584.8', 'ICD9CM:584.9', 'ICD9CM:586'):
            results_ccs3["acute_renal_fail"].append(1)
        else: results_ccs3["acute_renal_fail"].append(0)
    print("Completed Binary Recode of: acute_renal_fail")

    # Chronic_kidney_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:585', 'ICD9CM:585.1', 'ICD9CM:585.2', 'ICD9CM:585.3', 'ICD9CM:585.4', 'ICD9CM:585.5', 'ICD9CM:585.6', 'ICD9CM:585.9', 'ICD9CM:792.5', 'ICD9CM:V42.0', 'ICD9CM:V45.1', 'ICD9CM:V45.11', 'ICD9CM:V45.12', 'ICD9CM:V56.0', 'ICD9CM:V56.1', 'ICD9CM:V56.2', 'ICD9CM:V56.31', 'ICD9CM:V56.32', 'ICD9CM:V56.8'):
            results_ccs3["ckd"].append(1)
        else: results_ccs3["ckd"].append(0)
    print("Completed Binary Recode of: ckd")

    # Urinary_tract_infections
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:032.84', 'ICD9CM:590.00', 'ICD9CM:590.01', 'ICD9CM:590.10', 'ICD9CM:590.11', 'ICD9CM:590.2', 'ICD9CM:590.3', 'ICD9CM:590.80', 'ICD9CM:590.81', 'ICD9CM:590.9', 'ICD9CM:595.0', 'ICD9CM:595.1', 'ICD9CM:595.2', 'ICD9CM:595.3', 'ICD9CM:595.4', 'ICD9CM:595.81', 'ICD9CM:595.82', 'ICD9CM:595.89', 'ICD9CM:595.9', 'ICD9CM:597.0', 'ICD9CM:597.80', 'ICD9CM:597.81', 'ICD9CM:597.89', 'ICD9CM:598.00', 'ICD9CM:598.01', 'ICD9CM:599.0'):
            results_ccs3["uti"].append(1)
        else: results_ccs3["uti"].append(0)
    print("Completed Binary Recode of: uti")

    # Calculus_of_urinary_tract
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:592.0', 'ICD9CM:592.1', 'ICD9CM:592.9', 'ICD9CM:594.0', 'ICD9CM:594.1', 'ICD9CM:594.2', 'ICD9CM:594.8', 'ICD9CM:594.9', 'ICD9CM:788.0', 'ICD9CM:V13.01'):
            results_ccs3["calculus_urinary"].append(1)
        else: results_ccs3["calculus_urinary"].append(0)
    print("Completed Binary Recode of: calculus_urinary")

    # Other_diseases_of_kidney_and_ureters
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:588.0', 'ICD9CM:588.1', 'ICD9CM:588.8', 'ICD9CM:588.81', 'ICD9CM:588.89', 'ICD9CM:588.9', 'ICD9CM:589.0', 'ICD9CM:589.1', 'ICD9CM:589.9', 'ICD9CM:591', 'ICD9CM:593.0', 'ICD9CM:593.1', 'ICD9CM:593.2', 'ICD9CM:593.3', 'ICD9CM:593.4', 'ICD9CM:593.5', 'ICD9CM:593.6', 'ICD9CM:593.7', 'ICD9CM:593.70', 'ICD9CM:593.71', 'ICD9CM:593.72', 'ICD9CM:593.73', 'ICD9CM:593.81', 'ICD9CM:593.82', 'ICD9CM:593.89', 'ICD9CM:593.9'):
            results_ccs3["other_kidney"].append(1)
        else: results_ccs3["other_kidney"].append(0)
    print("Completed Binary Recode of: other_kidney")

    # Other_diseases_of_bladder_and_urethra
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:596.0', 'ICD9CM:596.1', 'ICD9CM:596.2', 'ICD9CM:596.3', 'ICD9CM:596.4', 'ICD9CM:596.5', 'ICD9CM:596.51', 'ICD9CM:596.52', 'ICD9CM:596.53', 'ICD9CM:596.54', 'ICD9CM:596.55', 'ICD9CM:596.59', 'ICD9CM:596.6', 'ICD9CM:596.7', 'ICD9CM:596.8', 'ICD9CM:596.89', 'ICD9CM:596.9', 'ICD9CM:598.1', 'ICD9CM:598.2', 'ICD9CM:598.8', 'ICD9CM:598.9', 'ICD9CM:599.1', 'ICD9CM:599.2', 'ICD9CM:599.3', 'ICD9CM:599.4', 'ICD9CM:599.5', 'ICD9CM:599.81', 'ICD9CM:599.82', 'ICD9CM:599.83', 'ICD9CM:599.84'):
            results_ccs3["other_bladder"].append(1)
        else: results_ccs3["other_bladder"].append(0)
    print("Completed Binary Recode of: other_bladder")

    # Genitourinary_symptoms_and_ill-_defined_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:599.6', 'ICD9CM:599.60', 'ICD9CM:599.69', 'ICD9CM:599.7', 'ICD9CM:599.70', 'ICD9CM:599.71', 'ICD9CM:599.72', 'ICD9CM:599.8', 'ICD9CM:599.89', 'ICD9CM:599.9', 'ICD9CM:788.1', 'ICD9CM:788.2', 'ICD9CM:788.20', 'ICD9CM:788.21', 'ICD9CM:788.29', 'ICD9CM:788.3', 'ICD9CM:788.30', 'ICD9CM:788.31', 'ICD9CM:788.32', 'ICD9CM:788.33', 'ICD9CM:788.34', 'ICD9CM:788.35', 'ICD9CM:788.36', 'ICD9CM:788.37', 'ICD9CM:788.38', 'ICD9CM:788.39', 'ICD9CM:788.4', 'ICD9CM:788.41', 'ICD9CM:788.42', 'ICD9CM:788.43', 'ICD9CM:788.5', 'ICD9CM:788.6', 'ICD9CM:788.61', 'ICD9CM:788.62', 'ICD9CM:788.63', 'ICD9CM:788.64', 'ICD9CM:788.65', 'ICD9CM:788.69', 'ICD9CM:788.7', 'ICD9CM:788.8', 'ICD9CM:788.9', 'ICD9CM:788.91', 'ICD9CM:788.99', 'ICD9CM:791.0', 'ICD9CM:791.1', 'ICD9CM:791.2', 'ICD9CM:791.3', 'ICD9CM:791.4', 'ICD9CM:791.7', 'ICD9CM:791.9', 'ICD9CM:793.5', 'ICD9CM:794.4', 'ICD9CM:V13.0', 'ICD9CM:V13.00', 'ICD9CM:V13.02', 'ICD9CM:V13.03', 'ICD9CM:V13.09', 'ICD9CM:V41.7', 'ICD9CM:V43.5', 'ICD9CM:V44.5', 'ICD9CM:V44.50', 'ICD9CM:V44.51', 'ICD9CM:V44.52', 'ICD9CM:V44.59', 'ICD9CM:V44.6', 'ICD9CM:V47.4', 'ICD9CM:V47.5', 'ICD9CM:V53.6', 'ICD9CM:V55.5', 'ICD9CM:V55.6'):
            results_ccs3["genitourinary_symp"].append(1)
        else: results_ccs3["genitourinary_symp"].append(0)
    print("Completed Binary Recode of: genitourinary_symp")

    # Hyperplasia_of_prostate
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:600', 'ICD9CM:600.0', 'ICD9CM:600.00', 'ICD9CM:600.01', 'ICD9CM:600.1', 'ICD9CM:600.10', 'ICD9CM:600.11', 'ICD9CM:600.2', 'ICD9CM:600.20', 'ICD9CM:600.21', 'ICD9CM:600.3', 'ICD9CM:600.9', 'ICD9CM:600.90', 'ICD9CM:600.91'):
            results_ccs3["prostate_hyp"].append(1)
        else: results_ccs3["prostate_hyp"].append(0)
    print("Completed Binary Recode of: prostate_hyp")

    # Inflammatory_conditions_of_male_genital_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:601.0', 'ICD9CM:601.1', 'ICD9CM:601.2', 'ICD9CM:601.3', 'ICD9CM:601.4', 'ICD9CM:601.8', 'ICD9CM:601.9', 'ICD9CM:603.1', 'ICD9CM:604.0', 'ICD9CM:604.90', 'ICD9CM:604.91', 'ICD9CM:604.99', 'ICD9CM:607.1', 'ICD9CM:607.2', 'ICD9CM:608.0', 'ICD9CM:608.4'):
            results_ccs3["male_genital_inflam"].append(1)
        else: results_ccs3["male_genital_inflam"].append(0)
    print("Completed Binary Recode of: male_genital_inflam")

    # Other_male_genital_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:602.0', 'ICD9CM:602.1', 'ICD9CM:602.2', 'ICD9CM:602.3', 'ICD9CM:602.8', 'ICD9CM:602.9', 'ICD9CM:603.0', 'ICD9CM:603.8', 'ICD9CM:603.9', 'ICD9CM:605', 'ICD9CM:606.0', 'ICD9CM:606.1', 'ICD9CM:606.8', 'ICD9CM:606.9', 'ICD9CM:607.0', 'ICD9CM:607.3', 'ICD9CM:607.81', 'ICD9CM:607.82', 'ICD9CM:607.83', 'ICD9CM:607.84', 'ICD9CM:607.85', 'ICD9CM:607.89', 'ICD9CM:607.9', 'ICD9CM:608.1', 'ICD9CM:608.2', 'ICD9CM:608.20', 'ICD9CM:608.21', 'ICD9CM:608.22', 'ICD9CM:608.23', 'ICD9CM:608.24', 'ICD9CM:608.3', 'ICD9CM:608.81', 'ICD9CM:608.82', 'ICD9CM:608.83', 'ICD9CM:608.84', 'ICD9CM:608.85', 'ICD9CM:608.86', 'ICD9CM:608.87', 'ICD9CM:608.89', 'ICD9CM:608.9', 'ICD9CM:792.2'):
            results_ccs3["other_male_genital"].append(1)
        else: results_ccs3["other_male_genital"].append(0)
    print("Completed Binary Recode of: other_male_genital")

    # Nonmalignant_breast_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:610.0', 'ICD9CM:610.1', 'ICD9CM:610.2', 'ICD9CM:610.3', 'ICD9CM:610.4', 'ICD9CM:610.8', 'ICD9CM:610.9', 'ICD9CM:611.0', 'ICD9CM:611.1', 'ICD9CM:611.2', 'ICD9CM:611.3', 'ICD9CM:611.4', 'ICD9CM:611.5', 'ICD9CM:611.6', 'ICD9CM:611.71', 'ICD9CM:611.72', 'ICD9CM:611.79', 'ICD9CM:611.8', 'ICD9CM:611.81', 'ICD9CM:611.82', 'ICD9CM:611.83', 'ICD9CM:611.89', 'ICD9CM:611.9', 'ICD9CM:612.0', 'ICD9CM:612.1', 'ICD9CM:793.8', 'ICD9CM:793.80', 'ICD9CM:793.81', 'ICD9CM:793.82', 'ICD9CM:793.89'):
            results_ccs3["nonmalig_breast"].append(1)
        else: results_ccs3["nonmalig_breast"].append(0)
    print("Completed Binary Recode of: nonmalig_breast")

    # Inflammatory_diseases_of_female_pelvic_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:614.0', 'ICD9CM:614.1', 'ICD9CM:614.2', 'ICD9CM:614.3', 'ICD9CM:614.4', 'ICD9CM:614.5', 'ICD9CM:614.6', 'ICD9CM:614.7', 'ICD9CM:614.8', 'ICD9CM:614.9', 'ICD9CM:615.0', 'ICD9CM:615.1', 'ICD9CM:615.9', 'ICD9CM:616.0', 'ICD9CM:616.10', 'ICD9CM:616.11', 'ICD9CM:616.2', 'ICD9CM:616.3', 'ICD9CM:616.4', 'ICD9CM:616.50', 'ICD9CM:616.51', 'ICD9CM:616.8', 'ICD9CM:616.81', 'ICD9CM:616.89', 'ICD9CM:616.9', 'ICD9CM:625.71'):
            results_ccs3["inflam_fem_pelvic"].append(1)
        else: results_ccs3["inflam_fem_pelvic"].append(0)
    print("Completed Binary Recode of: inflam_fem_pelvic")

    # Endometriosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:617.0', 'ICD9CM:617.1', 'ICD9CM:617.2', 'ICD9CM:617.3', 'ICD9CM:617.4', 'ICD9CM:617.5', 'ICD9CM:617.6', 'ICD9CM:617.8', 'ICD9CM:617.9'):
            results_ccs3["endometriosis"].append(1)
        else: results_ccs3["endometriosis"].append(0)
    print("Completed Binary Recode of: endometriosis")

    # Prolapse_of_female_genital_organs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:618.0', 'ICD9CM:618.00', 'ICD9CM:618.01', 'ICD9CM:618.02', 'ICD9CM:618.03', 'ICD9CM:618.04', 'ICD9CM:618.05', 'ICD9CM:618.09', 'ICD9CM:618.1', 'ICD9CM:618.2', 'ICD9CM:618.3', 'ICD9CM:618.4', 'ICD9CM:618.5', 'ICD9CM:618.6', 'ICD9CM:618.7', 'ICD9CM:618.8', 'ICD9CM:618.81', 'ICD9CM:618.82', 'ICD9CM:618.83', 'ICD9CM:618.84', 'ICD9CM:618.89', 'ICD9CM:618.9'):
            results_ccs3["prolapse_fem_gen"].append(1)
        else: results_ccs3["prolapse_fem_gen"].append(0)
    print("Completed Binary Recode of: prolapse_fem_gen")

    # Menstrual_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:625.3', 'ICD9CM:626.0', 'ICD9CM:626.1', 'ICD9CM:626.2', 'ICD9CM:626.3', 'ICD9CM:626.4', 'ICD9CM:626.5', 'ICD9CM:626.6', 'ICD9CM:626.8', 'ICD9CM:626.9'):
            results_ccs3["menstrual"].append(1)
        else: results_ccs3["menstrual"].append(0)
    print("Completed Binary Recode of: menstrual")

    # Ovarian_cyst
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:620.0', 'ICD9CM:620.1', 'ICD9CM:620.2'):
            results_ccs3["ovarian_cyst"].append(1)
        else: results_ccs3["ovarian_cyst"].append(0)
    print("Completed Binary Recode of: ovarian_cyst")

    # Menopausal_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:256.31', 'ICD9CM:256.39', 'ICD9CM:627.0', 'ICD9CM:627.1', 'ICD9CM:627.2', 'ICD9CM:627.3', 'ICD9CM:627.4', 'ICD9CM:627.8', 'ICD9CM:627.9', 'ICD9CM:V07.4'):
            results_ccs3["menopausal"].append(1)
        else: results_ccs3["menopausal"].append(0)
    print("Completed Binary Recode of: menopausal")

    # Female_infertility
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:628.0', 'ICD9CM:628.1', 'ICD9CM:628.2', 'ICD9CM:628.3', 'ICD9CM:628.4', 'ICD9CM:628.8', 'ICD9CM:628.9'):
            results_ccs3["fem_infert"].append(1)
        else: results_ccs3["fem_infert"].append(0)
    print("Completed Binary Recode of: fem_infert")

    # Other_female_genital_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:619.0', 'ICD9CM:619.1', 'ICD9CM:619.2', 'ICD9CM:619.8', 'ICD9CM:619.9', 'ICD9CM:620.3', 'ICD9CM:620.4', 'ICD9CM:620.5', 'ICD9CM:620.6', 'ICD9CM:620.7', 'ICD9CM:620.8', 'ICD9CM:620.9', 'ICD9CM:621.0', 'ICD9CM:621.1', 'ICD9CM:621.2', 'ICD9CM:621.3', 'ICD9CM:621.30', 'ICD9CM:621.31', 'ICD9CM:621.32', 'ICD9CM:621.33', 'ICD9CM:621.34', 'ICD9CM:621.35', 'ICD9CM:621.4', 'ICD9CM:621.5', 'ICD9CM:621.6', 'ICD9CM:621.7', 'ICD9CM:621.8', 'ICD9CM:621.9', 'ICD9CM:622.0', 'ICD9CM:622.1', 'ICD9CM:622.10', 'ICD9CM:622.11', 'ICD9CM:622.12', 'ICD9CM:622.2', 'ICD9CM:622.3', 'ICD9CM:622.4', 'ICD9CM:622.5', 'ICD9CM:622.6', 'ICD9CM:622.7', 'ICD9CM:622.8', 'ICD9CM:622.9', 'ICD9CM:623.0', 'ICD9CM:623.1', 'ICD9CM:623.2', 'ICD9CM:623.3', 'ICD9CM:623.4', 'ICD9CM:623.5', 'ICD9CM:623.6', 'ICD9CM:623.7', 'ICD9CM:623.8', 'ICD9CM:623.9', 'ICD9CM:624.0', 'ICD9CM:624.01', 'ICD9CM:624.02', 'ICD9CM:624.09', 'ICD9CM:624.1', 'ICD9CM:624.2', 'ICD9CM:624.3', 'ICD9CM:624.4', 'ICD9CM:624.5', 'ICD9CM:624.6', 'ICD9CM:624.8', 'ICD9CM:624.9', 'ICD9CM:625.0', 'ICD9CM:625.1', 'ICD9CM:625.2', 'ICD9CM:625.4', 'ICD9CM:625.5', 'ICD9CM:625.6', 'ICD9CM:625.70', 'ICD9CM:625.79', 'ICD9CM:625.8', 'ICD9CM:625.9', 'ICD9CM:626.7', 'ICD9CM:629.0', 'ICD9CM:629.1', 'ICD9CM:629.20', 'ICD9CM:629.21', 'ICD9CM:629.22', 'ICD9CM:629.23', 'ICD9CM:629.29', 'ICD9CM:629.8', 'ICD9CM:629.81', 'ICD9CM:629.89', 'ICD9CM:629.9', 'ICD9CM:795.09', 'ICD9CM:V13.2', 'ICD9CM:V13.21', 'ICD9CM:V13.22', 'ICD9CM:V13.23', 'ICD9CM:V13.24', 'ICD9CM:V13.29', 'ICD9CM:V55.7', 'ICD9CM:V72.3'):
            results_ccs3["other_fem_genital"].append(1)
        else: results_ccs3["other_fem_genital"].append(0)
    print("Completed Binary Recode of: other_fem_genital")

    # Contraceptive_and_procreative_management
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V15.7', 'ICD9CM:V25.01', 'ICD9CM:V25.02', 'ICD9CM:V25.03', 'ICD9CM:V25.04', 'ICD9CM:V25.09', 'ICD9CM:V25.1', 'ICD9CM:V25.11', 'ICD9CM:V25.12', 'ICD9CM:V25.13', 'ICD9CM:V25.2', 'ICD9CM:V25.3', 'ICD9CM:V25.40', 'ICD9CM:V25.41', 'ICD9CM:V25.42', 'ICD9CM:V25.43', 'ICD9CM:V25.49', 'ICD9CM:V25.5', 'ICD9CM:V25.8', 'ICD9CM:V25.9', 'ICD9CM:V26.0', 'ICD9CM:V26.1', 'ICD9CM:V26.2', 'ICD9CM:V26.21', 'ICD9CM:V26.22', 'ICD9CM:V26.29', 'ICD9CM:V26.3', 'ICD9CM:V26.31', 'ICD9CM:V26.32', 'ICD9CM:V26.33', 'ICD9CM:V26.34', 'ICD9CM:V26.35', 'ICD9CM:V26.39', 'ICD9CM:V26.4', 'ICD9CM:V26.41', 'ICD9CM:V26.42', 'ICD9CM:V26.49', 'ICD9CM:V26.51', 'ICD9CM:V26.52', 'ICD9CM:V26.8', 'ICD9CM:V26.81', 'ICD9CM:V26.82', 'ICD9CM:V26.89', 'ICD9CM:V26.9', 'ICD9CM:V45.5', 'ICD9CM:V45.51', 'ICD9CM:V45.52', 'ICD9CM:V45.59'):
            results_ccs3["contraceptive_mgmt"].append(1)
        else: results_ccs3["contraceptive_mgmt"].append(0)
    print("Completed Binary Recode of: contraceptive_mgmt")

    # Spontaneous_abortion
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:634.00', 'ICD9CM:634.01', 'ICD9CM:634.02', 'ICD9CM:634.10', 'ICD9CM:634.11', 'ICD9CM:634.12', 'ICD9CM:634.20', 'ICD9CM:634.21', 'ICD9CM:634.22', 'ICD9CM:634.30', 'ICD9CM:634.31', 'ICD9CM:634.32', 'ICD9CM:634.40', 'ICD9CM:634.41', 'ICD9CM:634.42', 'ICD9CM:634.50', 'ICD9CM:634.51', 'ICD9CM:634.52', 'ICD9CM:634.60', 'ICD9CM:634.61', 'ICD9CM:634.62', 'ICD9CM:634.70', 'ICD9CM:634.71', 'ICD9CM:634.72', 'ICD9CM:634.80', 'ICD9CM:634.81', 'ICD9CM:634.82', 'ICD9CM:634.90', 'ICD9CM:634.91', 'ICD9CM:634.92'):
            results_ccs3["spont_abortion"].append(1)
        else: results_ccs3["spont_abortion"].append(0)
    print("Completed Binary Recode of: spont_abortion")

    # Induced_abortion
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:635.00', 'ICD9CM:635.01', 'ICD9CM:635.02', 'ICD9CM:635.10', 'ICD9CM:635.11', 'ICD9CM:635.12', 'ICD9CM:635.20', 'ICD9CM:635.21', 'ICD9CM:635.22', 'ICD9CM:635.30', 'ICD9CM:635.31', 'ICD9CM:635.32', 'ICD9CM:635.40', 'ICD9CM:635.41', 'ICD9CM:635.42', 'ICD9CM:635.50', 'ICD9CM:635.51', 'ICD9CM:635.52', 'ICD9CM:635.60', 'ICD9CM:635.61', 'ICD9CM:635.62', 'ICD9CM:635.70', 'ICD9CM:635.71', 'ICD9CM:635.72', 'ICD9CM:635.80', 'ICD9CM:635.81', 'ICD9CM:635.82', 'ICD9CM:635.90', 'ICD9CM:635.91', 'ICD9CM:635.92', 'ICD9CM:636.00', 'ICD9CM:636.01', 'ICD9CM:636.02', 'ICD9CM:636.10', 'ICD9CM:636.11', 'ICD9CM:636.12', 'ICD9CM:636.20', 'ICD9CM:636.21', 'ICD9CM:636.22', 'ICD9CM:636.30', 'ICD9CM:636.31', 'ICD9CM:636.32', 'ICD9CM:636.40', 'ICD9CM:636.41', 'ICD9CM:636.42', 'ICD9CM:636.50', 'ICD9CM:636.51', 'ICD9CM:636.52', 'ICD9CM:636.60', 'ICD9CM:636.61', 'ICD9CM:636.62', 'ICD9CM:636.70', 'ICD9CM:636.71', 'ICD9CM:636.72', 'ICD9CM:636.80', 'ICD9CM:636.81', 'ICD9CM:636.82', 'ICD9CM:636.90', 'ICD9CM:636.91', 'ICD9CM:636.92', 'ICD9CM:637.00', 'ICD9CM:637.01', 'ICD9CM:637.02', 'ICD9CM:637.10', 'ICD9CM:637.11', 'ICD9CM:637.12', 'ICD9CM:637.20', 'ICD9CM:637.21', 'ICD9CM:637.22', 'ICD9CM:637.30', 'ICD9CM:637.31', 'ICD9CM:637.32', 'ICD9CM:637.40', 'ICD9CM:637.41', 'ICD9CM:637.42', 'ICD9CM:637.50', 'ICD9CM:637.51', 'ICD9CM:637.52', 'ICD9CM:637.60', 'ICD9CM:637.61', 'ICD9CM:637.62', 'ICD9CM:637.70', 'ICD9CM:637.71', 'ICD9CM:637.72', 'ICD9CM:637.80', 'ICD9CM:637.81', 'ICD9CM:637.82', 'ICD9CM:637.90', 'ICD9CM:637.91', 'ICD9CM:637.92', 'ICD9CM:638.0', 'ICD9CM:638.1', 'ICD9CM:638.2', 'ICD9CM:638.3', 'ICD9CM:638.4', 'ICD9CM:638.5', 'ICD9CM:638.6', 'ICD9CM:638.7', 'ICD9CM:638.8', 'ICD9CM:638.9'):
            results_ccs3["induce_abortion"].append(1)
        else: results_ccs3["induce_abortion"].append(0)
    print("Completed Binary Recode of: induce_abortion")

    # Postabortion_complications
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:639.0', 'ICD9CM:639.1', 'ICD9CM:639.2', 'ICD9CM:639.3', 'ICD9CM:639.4', 'ICD9CM:639.5', 'ICD9CM:639.6', 'ICD9CM:639.8', 'ICD9CM:639.9'):
            results_ccs3["postabort_comp"].append(1)
        else: results_ccs3["postabort_comp"].append(0)
    print("Completed Binary Recode of: postabort_comp")

    # Ectopic_pregnancy
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:633.0', 'ICD9CM:633.00', 'ICD9CM:633.01', 'ICD9CM:633.1', 'ICD9CM:633.10', 'ICD9CM:633.11', 'ICD9CM:633.2', 'ICD9CM:633.20', 'ICD9CM:633.21', 'ICD9CM:633.8', 'ICD9CM:633.80', 'ICD9CM:633.81', 'ICD9CM:633.9', 'ICD9CM:633.90', 'ICD9CM:633.91'):
            results_ccs3["ectopic_preg"].append(1)
        else: results_ccs3["ectopic_preg"].append(0)
    print("Completed Binary Recode of: ectopic_preg")

    # Other_complications_of_pregnancy
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:630', 'ICD9CM:631', 'ICD9CM:631.0', 'ICD9CM:631.8', 'ICD9CM:632', 'ICD9CM:643.00', 'ICD9CM:643.01', 'ICD9CM:643.03', 'ICD9CM:643.10', 'ICD9CM:643.11', 'ICD9CM:643.13', 'ICD9CM:643.20', 'ICD9CM:643.21', 'ICD9CM:643.23', 'ICD9CM:643.80', 'ICD9CM:643.81', 'ICD9CM:643.83', 'ICD9CM:643.90', 'ICD9CM:643.91', 'ICD9CM:643.93', 'ICD9CM:646.00', 'ICD9CM:646.01', 'ICD9CM:646.03', 'ICD9CM:646.10', 'ICD9CM:646.11', 'ICD9CM:646.12', 'ICD9CM:646.13', 'ICD9CM:646.14', 'ICD9CM:646.20', 'ICD9CM:646.21', 'ICD9CM:646.22', 'ICD9CM:646.23', 'ICD9CM:646.24', 'ICD9CM:646.30', 'ICD9CM:646.31', 'ICD9CM:646.33', 'ICD9CM:646.40', 'ICD9CM:646.41', 'ICD9CM:646.42', 'ICD9CM:646.43', 'ICD9CM:646.44', 'ICD9CM:646.50', 'ICD9CM:646.51', 'ICD9CM:646.52', 'ICD9CM:646.53', 'ICD9CM:646.54', 'ICD9CM:646.60', 'ICD9CM:646.61', 'ICD9CM:646.62', 'ICD9CM:646.63', 'ICD9CM:646.64', 'ICD9CM:646.70', 'ICD9CM:646.71', 'ICD9CM:646.73', 'ICD9CM:646.80', 'ICD9CM:646.81', 'ICD9CM:646.82', 'ICD9CM:646.83', 'ICD9CM:646.84', 'ICD9CM:646.90', 'ICD9CM:646.91', 'ICD9CM:646.93', 'ICD9CM:647.00', 'ICD9CM:647.01', 'ICD9CM:647.02', 'ICD9CM:647.03', 'ICD9CM:647.04', 'ICD9CM:647.10', 'ICD9CM:647.11', 'ICD9CM:647.12', 'ICD9CM:647.13', 'ICD9CM:647.14', 'ICD9CM:647.20', 'ICD9CM:647.21', 'ICD9CM:647.22', 'ICD9CM:647.23', 'ICD9CM:647.24', 'ICD9CM:647.30', 'ICD9CM:647.31', 'ICD9CM:647.32', 'ICD9CM:647.33', 'ICD9CM:647.34', 'ICD9CM:647.40', 'ICD9CM:647.41', 'ICD9CM:647.42', 'ICD9CM:647.43', 'ICD9CM:647.44', 'ICD9CM:647.50', 'ICD9CM:647.51', 'ICD9CM:647.52', 'ICD9CM:647.53', 'ICD9CM:647.54', 'ICD9CM:647.60', 'ICD9CM:647.61', 'ICD9CM:647.62', 'ICD9CM:647.63', 'ICD9CM:647.64', 'ICD9CM:647.80', 'ICD9CM:647.81', 'ICD9CM:647.82', 'ICD9CM:647.83', 'ICD9CM:647.84', 'ICD9CM:647.90', 'ICD9CM:647.91', 'ICD9CM:647.92', 'ICD9CM:647.93', 'ICD9CM:647.94', 'ICD9CM:648.10', 'ICD9CM:648.11', 'ICD9CM:648.12', 'ICD9CM:648.13', 'ICD9CM:648.14', 'ICD9CM:648.20', 'ICD9CM:648.21', 'ICD9CM:648.22', 'ICD9CM:648.23', 'ICD9CM:648.24', 'ICD9CM:648.50', 'ICD9CM:648.51', 'ICD9CM:648.52', 'ICD9CM:648.53', 'ICD9CM:648.54', 'ICD9CM:648.60', 'ICD9CM:648.61', 'ICD9CM:648.62', 'ICD9CM:648.63', 'ICD9CM:648.64', 'ICD9CM:648.70', 'ICD9CM:648.71', 'ICD9CM:648.72', 'ICD9CM:648.73', 'ICD9CM:648.74', 'ICD9CM:648.90', 'ICD9CM:648.91', 'ICD9CM:648.92', 'ICD9CM:648.93', 'ICD9CM:648.94', 'ICD9CM:649.00', 'ICD9CM:649.01', 'ICD9CM:649.02', 'ICD9CM:649.03', 'ICD9CM:649.04', 'ICD9CM:649.10', 'ICD9CM:649.11', 'ICD9CM:649.12', 'ICD9CM:649.13', 'ICD9CM:649.14', 'ICD9CM:649.20', 'ICD9CM:649.21', 'ICD9CM:649.22', 'ICD9CM:649.23', 'ICD9CM:649.24', 'ICD9CM:649.30', 'ICD9CM:649.31', 'ICD9CM:649.32', 'ICD9CM:649.33', 'ICD9CM:649.34', 'ICD9CM:649.40', 'ICD9CM:649.41', 'ICD9CM:649.42', 'ICD9CM:649.43', 'ICD9CM:649.44', 'ICD9CM:649.50', 'ICD9CM:649.51', 'ICD9CM:649.53', 'ICD9CM:649.60', 'ICD9CM:649.61', 'ICD9CM:649.62', 'ICD9CM:649.63', 'ICD9CM:649.64', 'ICD9CM:V23.42', 'ICD9CM:V23.87', 'ICD9CM:V27.1', 'ICD9CM:V27.2', 'ICD9CM:V27.3', 'ICD9CM:V27.4', 'ICD9CM:V27.5', 'ICD9CM:V27.6', 'ICD9CM:V27.7', 'ICD9CM:V27.9'):
            results_ccs3["other_comp_preg"].append(1)
        else: results_ccs3["other_comp_preg"].append(0)
    print("Completed Binary Recode of: other_comp_preg")

    # Hemorrhage_during_pregnancy;_abruptio_placenta;_placenta_previa
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:640.00', 'ICD9CM:640.01', 'ICD9CM:640.03', 'ICD9CM:640.80', 'ICD9CM:640.81', 'ICD9CM:640.83', 'ICD9CM:640.90', 'ICD9CM:640.91', 'ICD9CM:640.93', 'ICD9CM:641.00', 'ICD9CM:641.01', 'ICD9CM:641.03', 'ICD9CM:641.10', 'ICD9CM:641.11', 'ICD9CM:641.13', 'ICD9CM:641.20', 'ICD9CM:641.21', 'ICD9CM:641.23', 'ICD9CM:641.30', 'ICD9CM:641.31', 'ICD9CM:641.33', 'ICD9CM:641.80', 'ICD9CM:641.81', 'ICD9CM:641.83', 'ICD9CM:641.90', 'ICD9CM:641.91', 'ICD9CM:641.93'):
            results_ccs3["hemorrhage_preg"].append(1)
        else: results_ccs3["hemorrhage_preg"].append(0)
    print("Completed Binary Recode of: hemorrhage_preg")

    # Hypertension_complicating_pregnancy;_childbirth_and_the_puerperium
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:642.00', 'ICD9CM:642.01', 'ICD9CM:642.02', 'ICD9CM:642.03', 'ICD9CM:642.04', 'ICD9CM:642.10', 'ICD9CM:642.11', 'ICD9CM:642.12', 'ICD9CM:642.13', 'ICD9CM:642.14', 'ICD9CM:642.20', 'ICD9CM:642.21', 'ICD9CM:642.22', 'ICD9CM:642.23', 'ICD9CM:642.24', 'ICD9CM:642.30', 'ICD9CM:642.31', 'ICD9CM:642.32', 'ICD9CM:642.33', 'ICD9CM:642.34', 'ICD9CM:642.40', 'ICD9CM:642.41', 'ICD9CM:642.42', 'ICD9CM:642.43', 'ICD9CM:642.44', 'ICD9CM:642.50', 'ICD9CM:642.51', 'ICD9CM:642.52', 'ICD9CM:642.53', 'ICD9CM:642.54', 'ICD9CM:642.60', 'ICD9CM:642.61', 'ICD9CM:642.62', 'ICD9CM:642.63', 'ICD9CM:642.64', 'ICD9CM:642.70', 'ICD9CM:642.71', 'ICD9CM:642.72', 'ICD9CM:642.73', 'ICD9CM:642.74', 'ICD9CM:642.90', 'ICD9CM:642.91', 'ICD9CM:642.92', 'ICD9CM:642.93', 'ICD9CM:642.94'):
            results_ccs3["htn_comp_preg"].append(1)
        else: results_ccs3["htn_comp_preg"].append(0)
    print("Completed Binary Recode of: htn_comp_preg")

    # Early_or_threatened_labor
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:644.00', 'ICD9CM:644.03', 'ICD9CM:644.10', 'ICD9CM:644.13', 'ICD9CM:644.20', 'ICD9CM:644.21'):
            results_ccs3["early_labor"].append(1)
        else: results_ccs3["early_labor"].append(0)
    print("Completed Binary Recode of: early_labor")

    # Prolonged_pregnancy
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:645.00', 'ICD9CM:645.01', 'ICD9CM:645.03', 'ICD9CM:645.10', 'ICD9CM:645.11', 'ICD9CM:645.13', 'ICD9CM:645.20', 'ICD9CM:645.21', 'ICD9CM:645.23'):
            results_ccs3["prolong_preg"].append(1)
        else: results_ccs3["prolong_preg"].append(0)
    print("Completed Binary Recode of: prolong_preg")

    # Diabetes_or_abnormal_glucose_tolerance_complicating_pregnancy;_childbirth;_or_the_puerperium
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:648.00', 'ICD9CM:648.01', 'ICD9CM:648.02', 'ICD9CM:648.03', 'ICD9CM:648.04', 'ICD9CM:648.80', 'ICD9CM:648.81', 'ICD9CM:648.82', 'ICD9CM:648.83', 'ICD9CM:648.84'):
            results_ccs3["dm_comp_preg"].append(1)
        else: results_ccs3["dm_comp_preg"].append(0)
    print("Completed Binary Recode of: dm_comp_preg")

    # Malposition;_malpresentation
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:652.00', 'ICD9CM:652.01', 'ICD9CM:652.03', 'ICD9CM:652.10', 'ICD9CM:652.11', 'ICD9CM:652.13', 'ICD9CM:652.20', 'ICD9CM:652.21', 'ICD9CM:652.23', 'ICD9CM:652.30', 'ICD9CM:652.31', 'ICD9CM:652.33', 'ICD9CM:652.40', 'ICD9CM:652.41', 'ICD9CM:652.43', 'ICD9CM:652.50', 'ICD9CM:652.51', 'ICD9CM:652.53', 'ICD9CM:652.60', 'ICD9CM:652.61', 'ICD9CM:652.63', 'ICD9CM:652.70', 'ICD9CM:652.71', 'ICD9CM:652.73', 'ICD9CM:652.80', 'ICD9CM:652.81', 'ICD9CM:652.83', 'ICD9CM:652.90', 'ICD9CM:652.91', 'ICD9CM:652.93', 'ICD9CM:660.00', 'ICD9CM:660.01', 'ICD9CM:660.03'):
            results_ccs3["malposition"].append(1)
        else: results_ccs3["malposition"].append(0)
    print("Completed Binary Recode of: malposition")

    # Fetopelvic_disproportion;_obstruction
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:653.00', 'ICD9CM:653.01', 'ICD9CM:653.03', 'ICD9CM:653.10', 'ICD9CM:653.11', 'ICD9CM:653.13', 'ICD9CM:653.20', 'ICD9CM:653.21', 'ICD9CM:653.23', 'ICD9CM:653.30', 'ICD9CM:653.31', 'ICD9CM:653.33', 'ICD9CM:653.40', 'ICD9CM:653.41', 'ICD9CM:653.43', 'ICD9CM:653.50', 'ICD9CM:653.51', 'ICD9CM:653.53', 'ICD9CM:653.60', 'ICD9CM:653.61', 'ICD9CM:653.63', 'ICD9CM:653.70', 'ICD9CM:653.71', 'ICD9CM:653.73', 'ICD9CM:653.80', 'ICD9CM:653.81', 'ICD9CM:653.83', 'ICD9CM:653.90', 'ICD9CM:653.91', 'ICD9CM:653.93', 'ICD9CM:660.10', 'ICD9CM:660.11', 'ICD9CM:660.13', 'ICD9CM:660.20', 'ICD9CM:660.21', 'ICD9CM:660.23', 'ICD9CM:660.30', 'ICD9CM:660.31', 'ICD9CM:660.33', 'ICD9CM:660.40', 'ICD9CM:660.41', 'ICD9CM:660.43', 'ICD9CM:660.50', 'ICD9CM:660.51', 'ICD9CM:660.53', 'ICD9CM:660.60', 'ICD9CM:660.61', 'ICD9CM:660.63', 'ICD9CM:660.70', 'ICD9CM:660.71', 'ICD9CM:660.73', 'ICD9CM:660.80', 'ICD9CM:660.81', 'ICD9CM:660.83', 'ICD9CM:660.90', 'ICD9CM:660.91', 'ICD9CM:660.93', 'ICD9CM:678.10', 'ICD9CM:678.11', 'ICD9CM:678.13'):
            results_ccs3["fetopelvic_disrupt"].append(1)
        else: results_ccs3["fetopelvic_disrupt"].append(0)
    print("Completed Binary Recode of: fetopelvic_disrupt")

    # Previous_C-_section
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:654.20', 'ICD9CM:654.21', 'ICD9CM:654.23'):
            results_ccs3["prev_c_sect"].append(1)
        else: results_ccs3["prev_c_sect"].append(0)
    print("Completed Binary Recode of: prev_c_sect")

    # Fetal_distress_and_abnormal_forces_of_labor
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:656.30', 'ICD9CM:656.31', 'ICD9CM:656.33', 'ICD9CM:661.00', 'ICD9CM:661.01', 'ICD9CM:661.03', 'ICD9CM:661.10', 'ICD9CM:661.11', 'ICD9CM:661.13', 'ICD9CM:661.20', 'ICD9CM:661.21', 'ICD9CM:661.23', 'ICD9CM:661.30', 'ICD9CM:661.31', 'ICD9CM:661.33', 'ICD9CM:661.40', 'ICD9CM:661.41', 'ICD9CM:661.43', 'ICD9CM:661.90', 'ICD9CM:661.91', 'ICD9CM:661.93', 'ICD9CM:662.00', 'ICD9CM:662.01', 'ICD9CM:662.03', 'ICD9CM:662.10', 'ICD9CM:662.11', 'ICD9CM:662.13', 'ICD9CM:662.20', 'ICD9CM:662.21', 'ICD9CM:662.23', 'ICD9CM:662.30', 'ICD9CM:662.31', 'ICD9CM:662.33'):
            results_ccs3["fetal_distress"].append(1)
        else: results_ccs3["fetal_distress"].append(0)
    print("Completed Binary Recode of: fetal_distress")

    # Polyhydramnios_and_other_problems_of_amniotic_cavity
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:657.00', 'ICD9CM:657.01', 'ICD9CM:657.03', 'ICD9CM:658.00', 'ICD9CM:658.01', 'ICD9CM:658.03', 'ICD9CM:658.10', 'ICD9CM:658.11', 'ICD9CM:658.13', 'ICD9CM:658.20', 'ICD9CM:658.21', 'ICD9CM:658.23', 'ICD9CM:658.30', 'ICD9CM:658.31', 'ICD9CM:658.33', 'ICD9CM:658.40', 'ICD9CM:658.41', 'ICD9CM:658.43', 'ICD9CM:658.80', 'ICD9CM:658.81', 'ICD9CM:658.83', 'ICD9CM:658.90', 'ICD9CM:658.91', 'ICD9CM:658.93', 'ICD9CM:792.3'):
            results_ccs3["polyhydramnios"].append(1)
        else: results_ccs3["polyhydramnios"].append(0)
    print("Completed Binary Recode of: polyhydramnios")

    # Umbilical_cord_complication
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:663.00', 'ICD9CM:663.01', 'ICD9CM:663.03', 'ICD9CM:663.10', 'ICD9CM:663.11', 'ICD9CM:663.13', 'ICD9CM:663.20', 'ICD9CM:663.21', 'ICD9CM:663.23', 'ICD9CM:663.30', 'ICD9CM:663.31', 'ICD9CM:663.33', 'ICD9CM:663.40', 'ICD9CM:663.41', 'ICD9CM:663.43', 'ICD9CM:663.50', 'ICD9CM:663.51', 'ICD9CM:663.53', 'ICD9CM:663.60', 'ICD9CM:663.61', 'ICD9CM:663.63', 'ICD9CM:663.80', 'ICD9CM:663.81', 'ICD9CM:663.83', 'ICD9CM:663.90', 'ICD9CM:663.91', 'ICD9CM:663.93'):
            results_ccs3["umbilical_comp"].append(1)
        else: results_ccs3["umbilical_comp"].append(0)
    print("Completed Binary Recode of: umbilical_comp")

    # OB-_related_trauma_to_perineum_and_vulva
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:664.00', 'ICD9CM:664.01', 'ICD9CM:664.04', 'ICD9CM:664.10', 'ICD9CM:664.11', 'ICD9CM:664.14', 'ICD9CM:664.20', 'ICD9CM:664.21', 'ICD9CM:664.24', 'ICD9CM:664.30', 'ICD9CM:664.31', 'ICD9CM:664.34', 'ICD9CM:664.40', 'ICD9CM:664.41', 'ICD9CM:664.44', 'ICD9CM:664.50', 'ICD9CM:664.51', 'ICD9CM:664.54', 'ICD9CM:664.60', 'ICD9CM:664.61', 'ICD9CM:664.64', 'ICD9CM:664.80', 'ICD9CM:664.81', 'ICD9CM:664.84', 'ICD9CM:664.90', 'ICD9CM:664.91', 'ICD9CM:664.94'):
            results_ccs3["ob_trauma"].append(1)
        else: results_ccs3["ob_trauma"].append(0)
    print("Completed Binary Recode of: ob_trauma")

    # Forceps_delivery
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:669.50', 'ICD9CM:669.51'):
            results_ccs3["forceps_deliv"].append(1)
        else: results_ccs3["forceps_deliv"].append(0)
    print("Completed Binary Recode of: forceps_deliv")

    # Other_complications_of_birth;_puerperium_affecting_management_of_mother
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:649.70', 'ICD9CM:649.71', 'ICD9CM:649.73', 'ICD9CM:649.81', 'ICD9CM:649.82', 'ICD9CM:651.03', 'ICD9CM:651.13', 'ICD9CM:651.23', 'ICD9CM:651.30', 'ICD9CM:651.31', 'ICD9CM:651.33', 'ICD9CM:651.40', 'ICD9CM:651.41', 'ICD9CM:651.43', 'ICD9CM:651.50', 'ICD9CM:651.51', 'ICD9CM:651.53', 'ICD9CM:651.60', 'ICD9CM:651.61', 'ICD9CM:651.63', 'ICD9CM:651.83', 'ICD9CM:651.93', 'ICD9CM:654.00', 'ICD9CM:654.01', 'ICD9CM:654.02', 'ICD9CM:654.03', 'ICD9CM:654.04', 'ICD9CM:654.10', 'ICD9CM:654.11', 'ICD9CM:654.12', 'ICD9CM:654.13', 'ICD9CM:654.14', 'ICD9CM:654.30', 'ICD9CM:654.31', 'ICD9CM:654.32', 'ICD9CM:654.33', 'ICD9CM:654.34', 'ICD9CM:654.40', 'ICD9CM:654.41', 'ICD9CM:654.42', 'ICD9CM:654.43', 'ICD9CM:654.44', 'ICD9CM:654.50', 'ICD9CM:654.51', 'ICD9CM:654.52', 'ICD9CM:654.53', 'ICD9CM:654.54', 'ICD9CM:654.60', 'ICD9CM:654.61', 'ICD9CM:654.62', 'ICD9CM:654.63', 'ICD9CM:654.64', 'ICD9CM:654.70', 'ICD9CM:654.71', 'ICD9CM:654.72', 'ICD9CM:654.73', 'ICD9CM:654.74', 'ICD9CM:654.80', 'ICD9CM:654.81', 'ICD9CM:654.82', 'ICD9CM:654.83', 'ICD9CM:654.84', 'ICD9CM:654.90', 'ICD9CM:654.91', 'ICD9CM:654.92', 'ICD9CM:654.93', 'ICD9CM:654.94', 'ICD9CM:655.00', 'ICD9CM:655.01', 'ICD9CM:655.03', 'ICD9CM:655.10', 'ICD9CM:655.11', 'ICD9CM:655.13', 'ICD9CM:655.20', 'ICD9CM:655.21', 'ICD9CM:655.23', 'ICD9CM:655.30', 'ICD9CM:655.31', 'ICD9CM:655.33', 'ICD9CM:655.40', 'ICD9CM:655.41', 'ICD9CM:655.43', 'ICD9CM:655.60', 'ICD9CM:655.61', 'ICD9CM:655.63', 'ICD9CM:655.70', 'ICD9CM:655.71', 'ICD9CM:655.73', 'ICD9CM:655.80', 'ICD9CM:655.81', 'ICD9CM:655.83', 'ICD9CM:655.90', 'ICD9CM:655.91', 'ICD9CM:655.93', 'ICD9CM:656.00', 'ICD9CM:656.01', 'ICD9CM:656.03', 'ICD9CM:656.10', 'ICD9CM:656.11', 'ICD9CM:656.13', 'ICD9CM:656.20', 'ICD9CM:656.21', 'ICD9CM:656.23', 'ICD9CM:656.40', 'ICD9CM:656.41', 'ICD9CM:656.43', 'ICD9CM:656.50', 'ICD9CM:656.51', 'ICD9CM:656.53', 'ICD9CM:656.60', 'ICD9CM:656.61', 'ICD9CM:656.63', 'ICD9CM:656.70', 'ICD9CM:656.71', 'ICD9CM:656.73', 'ICD9CM:656.80', 'ICD9CM:656.81', 'ICD9CM:656.83', 'ICD9CM:656.90', 'ICD9CM:656.91', 'ICD9CM:656.93', 'ICD9CM:659.00', 'ICD9CM:659.01', 'ICD9CM:659.03', 'ICD9CM:659.10', 'ICD9CM:659.11', 'ICD9CM:659.13', 'ICD9CM:659.20', 'ICD9CM:659.21', 'ICD9CM:659.23', 'ICD9CM:659.30', 'ICD9CM:659.31', 'ICD9CM:659.33', 'ICD9CM:659.40', 'ICD9CM:659.41', 'ICD9CM:659.43', 'ICD9CM:659.50', 'ICD9CM:659.51', 'ICD9CM:659.53', 'ICD9CM:659.60', 'ICD9CM:659.61', 'ICD9CM:659.63', 'ICD9CM:659.70', 'ICD9CM:659.71', 'ICD9CM:659.73', 'ICD9CM:659.80', 'ICD9CM:659.81', 'ICD9CM:659.83', 'ICD9CM:659.90', 'ICD9CM:659.91', 'ICD9CM:659.93', 'ICD9CM:665.00', 'ICD9CM:665.01', 'ICD9CM:665.03', 'ICD9CM:665.10', 'ICD9CM:665.11', 'ICD9CM:665.12', 'ICD9CM:665.14', 'ICD9CM:665.20', 'ICD9CM:665.22', 'ICD9CM:665.24', 'ICD9CM:665.30', 'ICD9CM:665.31', 'ICD9CM:665.34', 'ICD9CM:665.40', 'ICD9CM:665.41', 'ICD9CM:665.44', 'ICD9CM:665.50', 'ICD9CM:665.51', 'ICD9CM:665.54', 'ICD9CM:665.60', 'ICD9CM:665.61', 'ICD9CM:665.64', 'ICD9CM:665.70', 'ICD9CM:665.71', 'ICD9CM:665.72', 'ICD9CM:665.74', 'ICD9CM:665.80', 'ICD9CM:665.81', 'ICD9CM:665.82', 'ICD9CM:665.83', 'ICD9CM:665.84', 'ICD9CM:665.90', 'ICD9CM:665.91', 'ICD9CM:665.92', 'ICD9CM:665.93', 'ICD9CM:665.94', 'ICD9CM:666.00', 'ICD9CM:666.02', 'ICD9CM:666.04', 'ICD9CM:666.10', 'ICD9CM:666.12', 'ICD9CM:666.14', 'ICD9CM:666.20', 'ICD9CM:666.22', 'ICD9CM:666.24', 'ICD9CM:666.30', 'ICD9CM:666.32', 'ICD9CM:666.34', 'ICD9CM:667.00', 'ICD9CM:667.02', 'ICD9CM:667.04', 'ICD9CM:667.10', 'ICD9CM:667.12', 'ICD9CM:667.14', 'ICD9CM:668.00', 'ICD9CM:668.01', 'ICD9CM:668.02', 'ICD9CM:668.03', 'ICD9CM:668.04', 'ICD9CM:668.10', 'ICD9CM:668.11', 'ICD9CM:668.12', 'ICD9CM:668.13', 'ICD9CM:668.14', 'ICD9CM:668.20', 'ICD9CM:668.21', 'ICD9CM:668.22', 'ICD9CM:668.23', 'ICD9CM:668.24', 'ICD9CM:668.80', 'ICD9CM:668.81', 'ICD9CM:668.82', 'ICD9CM:668.83', 'ICD9CM:668.84', 'ICD9CM:668.90', 'ICD9CM:668.91', 'ICD9CM:668.92', 'ICD9CM:668.93', 'ICD9CM:668.94', 'ICD9CM:669.00', 'ICD9CM:669.01', 'ICD9CM:669.02', 'ICD9CM:669.03', 'ICD9CM:669.04', 'ICD9CM:669.10', 'ICD9CM:669.11', 'ICD9CM:669.12', 'ICD9CM:669.13', 'ICD9CM:669.14', 'ICD9CM:669.20', 'ICD9CM:669.21', 'ICD9CM:669.22', 'ICD9CM:669.23', 'ICD9CM:669.24', 'ICD9CM:669.30', 'ICD9CM:669.32', 'ICD9CM:669.34', 'ICD9CM:669.40', 'ICD9CM:669.41', 'ICD9CM:669.42', 'ICD9CM:669.43', 'ICD9CM:669.44', 'ICD9CM:669.60', 'ICD9CM:669.61', 'ICD9CM:669.70', 'ICD9CM:669.71', 'ICD9CM:669.80', 'ICD9CM:669.81', 'ICD9CM:669.82', 'ICD9CM:669.83', 'ICD9CM:669.84', 'ICD9CM:669.90', 'ICD9CM:669.91', 'ICD9CM:669.92', 'ICD9CM:669.93', 'ICD9CM:669.94', 'ICD9CM:670.00', 'ICD9CM:670.02', 'ICD9CM:670.04', 'ICD9CM:670.10', 'ICD9CM:670.12', 'ICD9CM:670.14', 'ICD9CM:670.20', 'ICD9CM:670.22', 'ICD9CM:670.24', 'ICD9CM:670.30', 'ICD9CM:670.32', 'ICD9CM:670.34', 'ICD9CM:670.80', 'ICD9CM:670.82', 'ICD9CM:670.84', 'ICD9CM:671.00', 'ICD9CM:671.01', 'ICD9CM:671.02', 'ICD9CM:671.03', 'ICD9CM:671.04', 'ICD9CM:671.10', 'ICD9CM:671.11', 'ICD9CM:671.12', 'ICD9CM:671.13', 'ICD9CM:671.14', 'ICD9CM:671.20', 'ICD9CM:671.21', 'ICD9CM:671.22', 'ICD9CM:671.23', 'ICD9CM:671.24', 'ICD9CM:671.30', 'ICD9CM:671.31', 'ICD9CM:671.33', 'ICD9CM:671.40', 'ICD9CM:671.42', 'ICD9CM:671.44', 'ICD9CM:671.50', 'ICD9CM:671.51', 'ICD9CM:671.52', 'ICD9CM:671.53', 'ICD9CM:671.54', 'ICD9CM:671.80', 'ICD9CM:671.81', 'ICD9CM:671.82', 'ICD9CM:671.83', 'ICD9CM:671.84', 'ICD9CM:671.90', 'ICD9CM:671.91', 'ICD9CM:671.92', 'ICD9CM:671.93', 'ICD9CM:671.94', 'ICD9CM:672.00', 'ICD9CM:672.02', 'ICD9CM:672.04', 'ICD9CM:673.00', 'ICD9CM:673.01', 'ICD9CM:673.02', 'ICD9CM:673.03', 'ICD9CM:673.04', 'ICD9CM:673.10', 'ICD9CM:673.11', 'ICD9CM:673.12', 'ICD9CM:673.13', 'ICD9CM:673.14', 'ICD9CM:673.20', 'ICD9CM:673.21', 'ICD9CM:673.22', 'ICD9CM:673.23', 'ICD9CM:673.24', 'ICD9CM:673.30', 'ICD9CM:673.31', 'ICD9CM:673.32', 'ICD9CM:673.33', 'ICD9CM:673.34', 'ICD9CM:673.80', 'ICD9CM:673.81', 'ICD9CM:673.82', 'ICD9CM:673.83', 'ICD9CM:673.84', 'ICD9CM:674.00', 'ICD9CM:674.01', 'ICD9CM:674.02', 'ICD9CM:674.03', 'ICD9CM:674.04', 'ICD9CM:674.10', 'ICD9CM:674.12', 'ICD9CM:674.14', 'ICD9CM:674.20', 'ICD9CM:674.22', 'ICD9CM:674.24', 'ICD9CM:674.30', 'ICD9CM:674.32', 'ICD9CM:674.34', 'ICD9CM:674.40', 'ICD9CM:674.42', 'ICD9CM:674.44', 'ICD9CM:674.50', 'ICD9CM:674.51', 'ICD9CM:674.52', 'ICD9CM:674.53', 'ICD9CM:674.54', 'ICD9CM:674.80', 'ICD9CM:674.82', 'ICD9CM:674.84', 'ICD9CM:674.90', 'ICD9CM:674.92', 'ICD9CM:674.94', 'ICD9CM:675.00', 'ICD9CM:675.01', 'ICD9CM:675.02', 'ICD9CM:675.03', 'ICD9CM:675.04', 'ICD9CM:675.10', 'ICD9CM:675.11', 'ICD9CM:675.12', 'ICD9CM:675.13', 'ICD9CM:675.14', 'ICD9CM:675.20', 'ICD9CM:675.21', 'ICD9CM:675.22', 'ICD9CM:675.23', 'ICD9CM:675.24', 'ICD9CM:675.80', 'ICD9CM:675.81', 'ICD9CM:675.82', 'ICD9CM:675.83', 'ICD9CM:675.84', 'ICD9CM:675.90', 'ICD9CM:675.91', 'ICD9CM:675.92', 'ICD9CM:675.93', 'ICD9CM:675.94', 'ICD9CM:676.00', 'ICD9CM:676.01', 'ICD9CM:676.02', 'ICD9CM:676.03', 'ICD9CM:676.04', 'ICD9CM:676.10', 'ICD9CM:676.11', 'ICD9CM:676.12', 'ICD9CM:676.13', 'ICD9CM:676.14', 'ICD9CM:676.20', 'ICD9CM:676.21', 'ICD9CM:676.22', 'ICD9CM:676.23', 'ICD9CM:676.24', 'ICD9CM:676.30', 'ICD9CM:676.31', 'ICD9CM:676.32', 'ICD9CM:676.33', 'ICD9CM:676.34', 'ICD9CM:676.40', 'ICD9CM:676.41', 'ICD9CM:676.42', 'ICD9CM:676.43', 'ICD9CM:676.44', 'ICD9CM:676.50', 'ICD9CM:676.51', 'ICD9CM:676.52', 'ICD9CM:676.53', 'ICD9CM:676.54', 'ICD9CM:676.60', 'ICD9CM:676.61', 'ICD9CM:676.62', 'ICD9CM:676.63', 'ICD9CM:676.64', 'ICD9CM:676.80', 'ICD9CM:676.81', 'ICD9CM:676.82', 'ICD9CM:676.83', 'ICD9CM:676.84', 'ICD9CM:676.90', 'ICD9CM:676.91', 'ICD9CM:676.92', 'ICD9CM:676.93', 'ICD9CM:676.94', 'ICD9CM:677', 'ICD9CM:678.00', 'ICD9CM:678.01', 'ICD9CM:678.03', 'ICD9CM:679.00', 'ICD9CM:679.01', 'ICD9CM:679.02', 'ICD9CM:679.03', 'ICD9CM:679.04', 'ICD9CM:679.10', 'ICD9CM:679.11', 'ICD9CM:679.12', 'ICD9CM:679.13', 'ICD9CM:679.14', 'ICD9CM:V23.0', 'ICD9CM:V23.1', 'ICD9CM:V23.2', 'ICD9CM:V23.3', 'ICD9CM:V23.4', 'ICD9CM:V23.41', 'ICD9CM:V23.49', 'ICD9CM:V23.5', 'ICD9CM:V23.7', 'ICD9CM:V23.8', 'ICD9CM:V23.81', 'ICD9CM:V23.82', 'ICD9CM:V23.2', 'ICD9CM:V23.3', 'ICD9CM:V23.4', 'ICD9CM:V23.41', 'ICD9CM:V23.49', 'ICD9CM:V23.5', 'ICD9CM:V23.7', 'ICD9CM:V23.8', 'ICD9CM:V23.81', 'ICD9CM:V23.82', 'ICD9CM:V23.83', 'ICD9CM:V23.84', 'ICD9CM:V23.85', 'ICD9CM:V23.86', 'ICD9CM:V23.89', 'ICD9CM:V23.9'):
            results_ccs3["other_comp_birth"].append(1)
        else: results_ccs3["other_comp_birth"].append(0)
    print("Completed Binary Recode of: other_comp_birth")

    # Other_pregnancy_and_delivery_including_normal
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:650', 'ICD9CM:651.00', 'ICD9CM:651.01', 'ICD9CM:651.10', 'ICD9CM:651.11', 'ICD9CM:651.20', 'ICD9CM:651.21', 'ICD9CM:651.70', 'ICD9CM:651.71', 'ICD9CM:651.73', 'ICD9CM:651.80', 'ICD9CM:651.81', 'ICD9CM:651.90', 'ICD9CM:651.91', 'ICD9CM:V22.0', 'ICD9CM:V22.1', 'ICD9CM:V22.2', 'ICD9CM:V24.0', 'ICD9CM:V24.1', 'ICD9CM:V24.2', 'ICD9CM:V27.0', 'ICD9CM:V72.4', 'ICD9CM:V72.42', 'ICD9CM:V91.00', 'ICD9CM:V91.01', 'ICD9CM:V91.02', 'ICD9CM:V91.03', 'ICD9CM:V91.09', 'ICD9CM:V91.10', 'ICD9CM:V91.11', 'ICD9CM:V91.12', 'ICD9CM:V91.19', 'ICD9CM:V91.20', 'ICD9CM:V91.21', 'ICD9CM:V91.22', 'ICD9CM:V91.29', 'ICD9CM:V91.90', 'ICD9CM:V91.91', 'ICD9CM:V91.92', 'ICD9CM:V91.99'):
            results_ccs3["other_preg_deliv"].append(1)
        else: results_ccs3["other_preg_deliv"].append(0)
    print("Completed Binary Recode of: other_preg_deliv")

    # Skin_and_subcutaneous_tissue_infections
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:020.1', 'ICD9CM:021.0', 'ICD9CM:022.0', 'ICD9CM:031.1', 'ICD9CM:032.85', 'ICD9CM:035', 'ICD9CM:039.0', 'ICD9CM:680.0', 'ICD9CM:680.1', 'ICD9CM:680.2', 'ICD9CM:680.3', 'ICD9CM:680.4', 'ICD9CM:680.5', 'ICD9CM:680.6', 'ICD9CM:680.7', 'ICD9CM:680.8', 'ICD9CM:680.9', 'ICD9CM:681.00', 'ICD9CM:681.01', 'ICD9CM:681.02', 'ICD9CM:681.10', 'ICD9CM:681.11', 'ICD9CM:681.9', 'ICD9CM:682.0', 'ICD9CM:682.1', 'ICD9CM:682.2', 'ICD9CM:682.3', 'ICD9CM:682.4', 'ICD9CM:682.5', 'ICD9CM:682.6', 'ICD9CM:682.7', 'ICD9CM:682.8', 'ICD9CM:682.9', 'ICD9CM:684', 'ICD9CM:685.0', 'ICD9CM:685.1', 'ICD9CM:686.0', 'ICD9CM:686.00', 'ICD9CM:686.01', 'ICD9CM:686.09', 'ICD9CM:686.1', 'ICD9CM:686.8', 'ICD9CM:686.9'):
            results_ccs3["skin_tissue_infec"].append(1)
        else: results_ccs3["skin_tissue_infec"].append(0)
    print("Completed Binary Recode of: skin_tissue_infec")

    # Other_inflammatory_condition_of_skin
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:690', 'ICD9CM:690.10', 'ICD9CM:690.11', 'ICD9CM:690.12', 'ICD9CM:690.18', 'ICD9CM:690.8', 'ICD9CM:692.76', 'ICD9CM:692.77', 'ICD9CM:694.0', 'ICD9CM:694.1', 'ICD9CM:694.2', 'ICD9CM:694.3', 'ICD9CM:694.4', 'ICD9CM:694.5', 'ICD9CM:694.60', 'ICD9CM:694.61', 'ICD9CM:694.8', 'ICD9CM:694.9', 'ICD9CM:695.0', 'ICD9CM:695.1', 'ICD9CM:695.10', 'ICD9CM:695.11', 'ICD9CM:695.12', 'ICD9CM:695.13', 'ICD9CM:695.14', 'ICD9CM:695.15', 'ICD9CM:695.19', 'ICD9CM:695.2', 'ICD9CM:695.3', 'ICD9CM:695.4', 'ICD9CM:695.50', 'ICD9CM:695.51', 'ICD9CM:695.52', 'ICD9CM:695.53', 'ICD9CM:695.54', 'ICD9CM:695.55', 'ICD9CM:695.56', 'ICD9CM:695.57', 'ICD9CM:695.58', 'ICD9CM:695.59', 'ICD9CM:695.81', 'ICD9CM:695.89', 'ICD9CM:695.9', 'ICD9CM:696.0', 'ICD9CM:696.1', 'ICD9CM:696.2', 'ICD9CM:696.3', 'ICD9CM:696.4', 'ICD9CM:696.5', 'ICD9CM:696.8', 'ICD9CM:697.0', 'ICD9CM:697.1', 'ICD9CM:697.8', 'ICD9CM:697.9', 'ICD9CM:698.0', 'ICD9CM:698.1', 'ICD9CM:698.2', 'ICD9CM:698.3', 'ICD9CM:698.4', 'ICD9CM:698.8', 'ICD9CM:698.9'):
            results_ccs3["other_skin_inflam"].append(1)
        else: results_ccs3["other_skin_inflam"].append(0)
    print("Completed Binary Recode of: other_skin_inflam")

    # Chronic_ulcer_of_skin
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:707.0', 'ICD9CM:707.00', 'ICD9CM:707.01', 'ICD9CM:707.02', 'ICD9CM:707.03', 'ICD9CM:707.04', 'ICD9CM:707.05', 'ICD9CM:707.06', 'ICD9CM:707.07', 'ICD9CM:707.09', 'ICD9CM:707.1', 'ICD9CM:707.10', 'ICD9CM:707.11', 'ICD9CM:707.12', 'ICD9CM:707.13', 'ICD9CM:707.14', 'ICD9CM:707.15', 'ICD9CM:707.19', 'ICD9CM:707.20', 'ICD9CM:707.21', 'ICD9CM:707.22', 'ICD9CM:707.23', 'ICD9CM:707.24', 'ICD9CM:707.25', 'ICD9CM:707.8', 'ICD9CM:707.9'):
            results_ccs3["chronic_skin_ulcer"].append(1)
        else: results_ccs3["chronic_skin_ulcer"].append(0)
    print("Completed Binary Recode of: chronic_skin_ulcer")

    # Other_skin_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:692.75', 'ICD9CM:700', 'ICD9CM:701.0', 'ICD9CM:701.1', 'ICD9CM:701.2', 'ICD9CM:701.3', 'ICD9CM:701.4', 'ICD9CM:701.5', 'ICD9CM:701.8', 'ICD9CM:701.9', 'ICD9CM:702', 'ICD9CM:702.0', 'ICD9CM:702.1', 'ICD9CM:702.11', 'ICD9CM:702.19', 'ICD9CM:702.8', 'ICD9CM:703.0', 'ICD9CM:703.8', 'ICD9CM:703.9', 'ICD9CM:704.00', 'ICD9CM:704.01', 'ICD9CM:704.02', 'ICD9CM:704.09', 'ICD9CM:704.1', 'ICD9CM:704.2', 'ICD9CM:704.3', 'ICD9CM:704.41', 'ICD9CM:704.42', 'ICD9CM:704.8', 'ICD9CM:704.9', 'ICD9CM:705.0', 'ICD9CM:705.1', 'ICD9CM:705.21', 'ICD9CM:705.22', 'ICD9CM:705.81', 'ICD9CM:705.82', 'ICD9CM:705.83', 'ICD9CM:705.89', 'ICD9CM:705.9', 'ICD9CM:706.0', 'ICD9CM:706.1', 'ICD9CM:706.2', 'ICD9CM:706.3', 'ICD9CM:706.8', 'ICD9CM:706.9', 'ICD9CM:709.0', 'ICD9CM:709.00', 'ICD9CM:709.01', 'ICD9CM:709.09', 'ICD9CM:709.1', 'ICD9CM:709.2', 'ICD9CM:709.3', 'ICD9CM:709.4', 'ICD9CM:709.8', 'ICD9CM:709.9', 'ICD9CM:780.8', 'ICD9CM:782.1', 'ICD9CM:782.2', 'ICD9CM:V13.3', 'ICD9CM:V42.3'):
            results_ccs3["other_skin"].append(1)
        else: results_ccs3["other_skin"].append(0)
    print("Completed Binary Recode of: other_skin")

    # Infective_arthritis_and_osteomyelitis_(except_that_caused_by_tuberculosis_or_sexually_transmitted_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:003.23', 'ICD9CM:003.24', 'ICD9CM:026.1', 'ICD9CM:036.82', 'ICD9CM:056.71', 'ICD9CM:711.00', 'ICD9CM:711.01', 'ICD9CM:711.02', 'ICD9CM:711.03', 'ICD9CM:711.04', 'ICD9CM:711.05', 'ICD9CM:711.06', 'ICD9CM:711.07', 'ICD9CM:711.08', 'ICD9CM:711.09', 'ICD9CM:711.10', 'ICD9CM:711.11', 'ICD9CM:711.12', 'ICD9CM:711.13', 'ICD9CM:711.14', 'ICD9CM:711.15', 'ICD9CM:711.16', 'ICD9CM:711.17', 'ICD9CM:711.18', 'ICD9CM:711.19', 'ICD9CM:711.20', 'ICD9CM:711.21', 'ICD9CM:711.22', 'ICD9CM:711.23', 'ICD9CM:711.24', 'ICD9CM:711.25', 'ICD9CM:711.26', 'ICD9CM:711.27', 'ICD9CM:711.28', 'ICD9CM:711.29', 'ICD9CM:711.30', 'ICD9CM:711.31', 'ICD9CM:711.32', 'ICD9CM:711.33', 'ICD9CM:711.34', 'ICD9CM:711.35', 'ICD9CM:711.36', 'ICD9CM:711.37', 'ICD9CM:711.38', 'ICD9CM:711.39', 'ICD9CM:711.40', 'ICD9CM:711.41', 'ICD9CM:711.42', 'ICD9CM:711.43', 'ICD9CM:711.44', 'ICD9CM:711.45', 'ICD9CM:711.46', 'ICD9CM:711.47', 'ICD9CM:711.48', 'ICD9CM:711.49', 'ICD9CM:711.50', 'ICD9CM:711.51', 'ICD9CM:711.52', 'ICD9CM:711.53', 'ICD9CM:711.54', 'ICD9CM:711.55', 'ICD9CM:711.56', 'ICD9CM:711.57', 'ICD9CM:711.58', 'ICD9CM:711.59', 'ICD9CM:711.60', 'ICD9CM:711.61', 'ICD9CM:711.62', 'ICD9CM:711.63', 'ICD9CM:711.64', 'ICD9CM:711.65', 'ICD9CM:711.66', 'ICD9CM:711.67', 'ICD9CM:711.68', 'ICD9CM:711.69', 'ICD9CM:711.70', 'ICD9CM:711.71', 'ICD9CM:711.72', 'ICD9CM:711.73', 'ICD9CM:711.74', 'ICD9CM:711.75', 'ICD9CM:711.76', 'ICD9CM:711.77', 'ICD9CM:711.78', 'ICD9CM:711.79', 'ICD9CM:711.80', 'ICD9CM:711.81', 'ICD9CM:711.82', 'ICD9CM:711.83', 'ICD9CM:711.84', 'ICD9CM:711.85', 'ICD9CM:711.86', 'ICD9CM:711.87', 'ICD9CM:711.88', 'ICD9CM:711.89', 'ICD9CM:711.90', 'ICD9CM:711.91', 'ICD9CM:711.92', 'ICD9CM:711.93', 'ICD9CM:711.94', 'ICD9CM:711.95', 'ICD9CM:711.96', 'ICD9CM:711.97', 'ICD9CM:711.98', 'ICD9CM:711.99', 'ICD9CM:730.00', 'ICD9CM:730.01', 'ICD9CM:730.02', 'ICD9CM:730.03', 'ICD9CM:730.04', 'ICD9CM:730.05', 'ICD9CM:730.06', 'ICD9CM:730.07', 'ICD9CM:730.08', 'ICD9CM:730.09', 'ICD9CM:730.10', 'ICD9CM:730.11', 'ICD9CM:730.12', 'ICD9CM:730.13', 'ICD9CM:730.14', 'ICD9CM:730.15', 'ICD9CM:730.16', 'ICD9CM:730.17', 'ICD9CM:730.18', 'ICD9CM:730.19', 'ICD9CM:730.20', 'ICD9CM:730.21', 'ICD9CM:730.22', 'ICD9CM:730.23', 'ICD9CM:730.24', 'ICD9CM:730.25', 'ICD9CM:730.26', 'ICD9CM:730.27', 'ICD9CM:730.28', 'ICD9CM:730.29', 'ICD9CM:730.30', 'ICD9CM:730.31', 'ICD9CM:730.32', 'ICD9CM:730.33', 'ICD9CM:730.34', 'ICD9CM:730.35', 'ICD9CM:730.36', 'ICD9CM:730.37', 'ICD9CM:730.38', 'ICD9CM:730.39', 'ICD9CM:730.70', 'ICD9CM:730.71', 'ICD9CM:730.72', 'ICD9CM:730.73', 'ICD9CM:730.74', 'ICD9CM:730.75', 'ICD9CM:730.76', 'ICD9CM:730.77', 'ICD9CM:730.78', 'ICD9CM:730.79', 'ICD9CM:730.80', 'ICD9CM:730.81', 'ICD9CM:730.82', 'ICD9CM:730.83', 'ICD9CM:730.84', 'ICD9CM:730.85', 'ICD9CM:730.86', 'ICD9CM:730.87', 'ICD9CM:730.88', 'ICD9CM:730.89', 'ICD9CM:730.90', 'ICD9CM:730.91', 'ICD9CM:730.92', 'ICD9CM:730.93', 'ICD9CM:730.94', 'ICD9CM:730.95', 'ICD9CM:730.96', 'ICD9CM:730.97', 'ICD9CM:730.98', 'ICD9CM:730.99'):
            results_ccs3["infec_arthritis"].append(1)
        else: results_ccs3["infec_arthritis"].append(0)
    print("Completed Binary Recode of: infec_arthritis")

    # Rheumatoid_arthritis_and_related_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:714.0', 'ICD9CM:714.1', 'ICD9CM:714.2', 'ICD9CM:714.30', 'ICD9CM:714.31', 'ICD9CM:714.32', 'ICD9CM:714.33', 'ICD9CM:714.4', 'ICD9CM:714.81', 'ICD9CM:714.89', 'ICD9CM:714.9', 'ICD9CM:720.0'):
            results_ccs3["rheum_arth"].append(1)
        else: results_ccs3["rheum_arth"].append(0)
    print("Completed Binary Recode of: rheum_arth")

    # Osteoarthritis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:715.00', 'ICD9CM:715.04', 'ICD9CM:715.09', 'ICD9CM:715.10', 'ICD9CM:715.11', 'ICD9CM:715.12', 'ICD9CM:715.13', 'ICD9CM:715.14', 'ICD9CM:715.15', 'ICD9CM:715.16', 'ICD9CM:715.17', 'ICD9CM:715.18', 'ICD9CM:715.20', 'ICD9CM:715.21', 'ICD9CM:715.22', 'ICD9CM:715.23', 'ICD9CM:715.24', 'ICD9CM:715.25', 'ICD9CM:715.26', 'ICD9CM:715.27', 'ICD9CM:715.28', 'ICD9CM:715.30', 'ICD9CM:715.31', 'ICD9CM:715.32', 'ICD9CM:715.33', 'ICD9CM:715.34', 'ICD9CM:715.35', 'ICD9CM:715.36', 'ICD9CM:715.37', 'ICD9CM:715.38', 'ICD9CM:715.80', 'ICD9CM:715.89', 'ICD9CM:715.90', 'ICD9CM:715.91', 'ICD9CM:715.92', 'ICD9CM:715.93', 'ICD9CM:715.94', 'ICD9CM:715.95', 'ICD9CM:715.96', 'ICD9CM:715.97', 'ICD9CM:715.98', 'ICD9CM:V13.4'):
            results_ccs3["osteo_arth"].append(1)
        else: results_ccs3["osteo_arth"].append(0)
    print("Completed Binary Recode of: osteo_arth")

    # Other_non-_traumatic_joint_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:713.0', 'ICD9CM:713.1', 'ICD9CM:713.2', 'ICD9CM:713.3', 'ICD9CM:713.4', 'ICD9CM:713.5', 'ICD9CM:713.6', 'ICD9CM:713.7', 'ICD9CM:713.8', 'ICD9CM:716.00', 'ICD9CM:716.01', 'ICD9CM:716.02', 'ICD9CM:716.03', 'ICD9CM:716.04', 'ICD9CM:716.05', 'ICD9CM:716.06', 'ICD9CM:716.07', 'ICD9CM:716.08', 'ICD9CM:716.09', 'ICD9CM:716.20', 'ICD9CM:716.21', 'ICD9CM:716.22', 'ICD9CM:716.23', 'ICD9CM:716.24', 'ICD9CM:716.25', 'ICD9CM:716.26', 'ICD9CM:716.27', 'ICD9CM:716.28', 'ICD9CM:716.29', 'ICD9CM:716.30', 'ICD9CM:716.31', 'ICD9CM:716.32', 'ICD9CM:716.33', 'ICD9CM:716.34', 'ICD9CM:716.35', 'ICD9CM:716.36', 'ICD9CM:716.37', 'ICD9CM:716.38', 'ICD9CM:716.39', 'ICD9CM:716.40', 'ICD9CM:716.41', 'ICD9CM:716.42', 'ICD9CM:716.43', 'ICD9CM:716.44', 'ICD9CM:716.45', 'ICD9CM:716.46', 'ICD9CM:716.47', 'ICD9CM:716.48', 'ICD9CM:716.49', 'ICD9CM:716.50', 'ICD9CM:716.51', 'ICD9CM:716.52', 'ICD9CM:716.53', 'ICD9CM:716.54', 'ICD9CM:716.55', 'ICD9CM:716.56', 'ICD9CM:716.57', 'ICD9CM:716.58', 'ICD9CM:716.59', 'ICD9CM:716.60', 'ICD9CM:716.61', 'ICD9CM:716.62', 'ICD9CM:716.63', 'ICD9CM:716.64', 'ICD9CM:716.65', 'ICD9CM:716.66', 'ICD9CM:716.67', 'ICD9CM:716.68', 'ICD9CM:716.80', 'ICD9CM:716.81', 'ICD9CM:716.82', 'ICD9CM:716.83', 'ICD9CM:716.84', 'ICD9CM:716.85', 'ICD9CM:716.86', 'ICD9CM:716.87', 'ICD9CM:716.88', 'ICD9CM:716.89', 'ICD9CM:716.90', 'ICD9CM:716.91', 'ICD9CM:716.92', 'ICD9CM:716.93', 'ICD9CM:716.94', 'ICD9CM:716.95', 'ICD9CM:716.96', 'ICD9CM:716.97', 'ICD9CM:716.98', 'ICD9CM:716.99', 'ICD9CM:718.10', 'ICD9CM:718.11', 'ICD9CM:718.12', 'ICD9CM:718.13', 'ICD9CM:718.14', 'ICD9CM:718.15', 'ICD9CM:718.17', 'ICD9CM:718.18', 'ICD9CM:718.19', 'ICD9CM:718.20', 'ICD9CM:718.21', 'ICD9CM:718.22', 'ICD9CM:718.23', 'ICD9CM:718.24', 'ICD9CM:718.25', 'ICD9CM:718.26', 'ICD9CM:718.27', 'ICD9CM:718.28', 'ICD9CM:718.29', 'ICD9CM:718.50', 'ICD9CM:718.51', 'ICD9CM:718.52', 'ICD9CM:718.53', 'ICD9CM:718.54', 'ICD9CM:718.55', 'ICD9CM:718.56', 'ICD9CM:718.57', 'ICD9CM:718.58', 'ICD9CM:718.59', 'ICD9CM:718.60', 'ICD9CM:718.65', 'ICD9CM:718.70', 'ICD9CM:718.71', 'ICD9CM:718.72', 'ICD9CM:718.73', 'ICD9CM:718.74', 'ICD9CM:718.75', 'ICD9CM:718.76', 'ICD9CM:718.77', 'ICD9CM:718.78', 'ICD9CM:718.79', 'ICD9CM:718.80', 'ICD9CM:718.81', 'ICD9CM:718.82', 'ICD9CM:718.83', 'ICD9CM:718.84', 'ICD9CM:718.85', 'ICD9CM:718.86', 'ICD9CM:718.87', 'ICD9CM:718.88', 'ICD9CM:718.89', 'ICD9CM:718.90', 'ICD9CM:718.91', 'ICD9CM:718.92', 'ICD9CM:718.93', 'ICD9CM:718.94', 'ICD9CM:718.95', 'ICD9CM:718.97', 'ICD9CM:718.98', 'ICD9CM:718.99', 'ICD9CM:719.00', 'ICD9CM:719.01', 'ICD9CM:719.02', 'ICD9CM:719.03', 'ICD9CM:719.04', 'ICD9CM:719.05', 'ICD9CM:719.06', 'ICD9CM:719.07', 'ICD9CM:719.08', 'ICD9CM:719.09', 'ICD9CM:719.10', 'ICD9CM:719.11', 'ICD9CM:719.12', 'ICD9CM:719.13', 'ICD9CM:719.14', 'ICD9CM:719.15', 'ICD9CM:719.16', 'ICD9CM:719.17', 'ICD9CM:719.18', 'ICD9CM:719.19', 'ICD9CM:719.20', 'ICD9CM:719.21', 'ICD9CM:719.22', 'ICD9CM:719.23', 'ICD9CM:719.24', 'ICD9CM:719.25', 'ICD9CM:719.26', 'ICD9CM:719.27', 'ICD9CM:719.28', 'ICD9CM:719.29', 'ICD9CM:719.30', 'ICD9CM:719.31', 'ICD9CM:719.32', 'ICD9CM:719.33', 'ICD9CM:719.34', 'ICD9CM:719.35', 'ICD9CM:719.36', 'ICD9CM:719.37', 'ICD9CM:719.38', 'ICD9CM:719.39', 'ICD9CM:719.40', 'ICD9CM:719.41', 'ICD9CM:719.42', 'ICD9CM:719.43', 'ICD9CM:719.44', 'ICD9CM:719.45', 'ICD9CM:719.46', 'ICD9CM:719.47', 'ICD9CM:719.48', 'ICD9CM:719.49', 'ICD9CM:719.50', 'ICD9CM:719.51', 'ICD9CM:719.52', 'ICD9CM:719.53', 'ICD9CM:719.54', 'ICD9CM:719.55', 'ICD9CM:719.56', 'ICD9CM:719.57', 'ICD9CM:719.58', 'ICD9CM:719.59', 'ICD9CM:719.60', 'ICD9CM:719.61', 'ICD9CM:719.62', 'ICD9CM:719.63', 'ICD9CM:719.64', 'ICD9CM:719.65', 'ICD9CM:719.66', 'ICD9CM:719.67', 'ICD9CM:719.68', 'ICD9CM:719.69', 'ICD9CM:719.7', 'ICD9CM:719.70', 'ICD9CM:719.75', 'ICD9CM:719.76', 'ICD9CM:719.77', 'ICD9CM:719.78', 'ICD9CM:719.79', 'ICD9CM:719.80', 'ICD9CM:719.81', 'ICD9CM:719.82', 'ICD9CM:719.83', 'ICD9CM:719.84', 'ICD9CM:719.85', 'ICD9CM:719.86', 'ICD9CM:719.87', 'ICD9CM:719.88', 'ICD9CM:719.89', 'ICD9CM:719.90', 'ICD9CM:719.91', 'ICD9CM:719.92', 'ICD9CM:719.93', 'ICD9CM:719.94', 'ICD9CM:719.95', 'ICD9CM:719.96', 'ICD9CM:719.97', 'ICD9CM:719.98', 'ICD9CM:719.99'):
            results_ccs3["other_joint"].append(1)
        else: results_ccs3["other_joint"].append(0)
    print("Completed Binary Recode of: other_joint")

    # Spondylosis;_intervertebral_disc_disorders;_other_back_problems
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:720.1', 'ICD9CM:720.2', 'ICD9CM:720.81', 'ICD9CM:720.89', 'ICD9CM:720.9', 'ICD9CM:721.0', 'ICD9CM:721.1', 'ICD9CM:721.2', 'ICD9CM:721.3', 'ICD9CM:721.41', 'ICD9CM:721.42', 'ICD9CM:721.5', 'ICD9CM:721.6', 'ICD9CM:721.7', 'ICD9CM:721.8', 'ICD9CM:721.90', 'ICD9CM:721.91', 'ICD9CM:722.0', 'ICD9CM:722.10', 'ICD9CM:722.11', 'ICD9CM:722.2', 'ICD9CM:722.30', 'ICD9CM:722.31', 'ICD9CM:722.32', 'ICD9CM:722.39', 'ICD9CM:722.4', 'ICD9CM:722.51', 'ICD9CM:722.52', 'ICD9CM:722.6', 'ICD9CM:722.70', 'ICD9CM:722.71', 'ICD9CM:722.72', 'ICD9CM:722.73', 'ICD9CM:722.80', 'ICD9CM:722.81', 'ICD9CM:722.82', 'ICD9CM:722.83', 'ICD9CM:722.90', 'ICD9CM:722.91', 'ICD9CM:722.92', 'ICD9CM:722.93', 'ICD9CM:723.0', 'ICD9CM:723.1', 'ICD9CM:723.2', 'ICD9CM:723.3', 'ICD9CM:723.4', 'ICD9CM:723.5', 'ICD9CM:723.6', 'ICD9CM:723.7', 'ICD9CM:723.8', 'ICD9CM:723.9', 'ICD9CM:724.00', 'ICD9CM:724.01', 'ICD9CM:724.02', 'ICD9CM:724.03', 'ICD9CM:724.09', 'ICD9CM:724.1', 'ICD9CM:724.2', 'ICD9CM:724.3', 'ICD9CM:724.4', 'ICD9CM:724.5', 'ICD9CM:724.6', 'ICD9CM:724.70', 'ICD9CM:724.71', 'ICD9CM:724.79', 'ICD9CM:724.8', 'ICD9CM:724.9'):
            results_ccs3["spondylosis"].append(1)
        else: results_ccs3["spondylosis"].append(0)
    print("Completed Binary Recode of: spondylosis")

    # Osteoporosis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:733.00', 'ICD9CM:733.01', 'ICD9CM:733.02', 'ICD9CM:733.03', 'ICD9CM:733.09'):
            results_ccs3["osteoporosis"].append(1)
        else: results_ccs3["osteoporosis"].append(0)
    print("Completed Binary Recode of: osteoporosis")

    # Pathological_fracture
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:733.1', 'ICD9CM:733.10', 'ICD9CM:733.11', 'ICD9CM:733.12', 'ICD9CM:733.13', 'ICD9CM:733.14', 'ICD9CM:733.15', 'ICD9CM:733.16', 'ICD9CM:733.19', 'ICD9CM:733.93', 'ICD9CM:733.94', 'ICD9CM:733.95', 'ICD9CM:733.96', 'ICD9CM:733.97', 'ICD9CM:733.98', 'ICD9CM:V13.51'):
            results_ccs3["pathological_fract"].append(1)
        else: results_ccs3["pathological_fract"].append(0)
    print("Completed Binary Recode of: pathological_fract")

    # Acquired_foot_deformities
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:727.1', 'ICD9CM:734', 'ICD9CM:735.0', 'ICD9CM:735.1', 'ICD9CM:735.2', 'ICD9CM:735.3', 'ICD9CM:735.4', 'ICD9CM:735.5', 'ICD9CM:735.8', 'ICD9CM:735.9', 'ICD9CM:736.70', 'ICD9CM:736.71', 'ICD9CM:736.72', 'ICD9CM:736.73', 'ICD9CM:736.74', 'ICD9CM:736.75', 'ICD9CM:736.76', 'ICD9CM:736.79'):
            results_ccs3["acq_foot_deform"].append(1)
        else: results_ccs3["acq_foot_deform"].append(0)
    print("Completed Binary Recode of: acq_foot_deform")

    # Other_acquired_deformities
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:718.40', 'ICD9CM:718.41', 'ICD9CM:718.42', 'ICD9CM:718.43', 'ICD9CM:718.44', 'ICD9CM:718.45', 'ICD9CM:718.46', 'ICD9CM:718.47', 'ICD9CM:718.48', 'ICD9CM:718.49', 'ICD9CM:736.00', 'ICD9CM:736.01', 'ICD9CM:736.02', 'ICD9CM:736.03', 'ICD9CM:736.04', 'ICD9CM:736.05', 'ICD9CM:736.06', 'ICD9CM:736.07', 'ICD9CM:736.09', 'ICD9CM:736.1', 'ICD9CM:736.20', 'ICD9CM:736.21', 'ICD9CM:736.22', 'ICD9CM:736.29', 'ICD9CM:736.30', 'ICD9CM:736.31', 'ICD9CM:736.32', 'ICD9CM:736.39', 'ICD9CM:736.41', 'ICD9CM:736.42', 'ICD9CM:736.5', 'ICD9CM:736.6', 'ICD9CM:736.81', 'ICD9CM:736.89', 'ICD9CM:736.9', 'ICD9CM:737.0', 'ICD9CM:737.10', 'ICD9CM:737.11', 'ICD9CM:737.12', 'ICD9CM:737.19', 'ICD9CM:737.20', 'ICD9CM:737.21', 'ICD9CM:737.22', 'ICD9CM:737.29', 'ICD9CM:737.33', 'ICD9CM:737.34', 'ICD9CM:737.39', 'ICD9CM:737.40', 'ICD9CM:737.41', 'ICD9CM:737.42', 'ICD9CM:737.43', 'ICD9CM:737.8', 'ICD9CM:737.9', 'ICD9CM:738.0', 'ICD9CM:738.1', 'ICD9CM:738.10', 'ICD9CM:738.11', 'ICD9CM:738.12', 'ICD9CM:738.19', 'ICD9CM:738.2', 'ICD9CM:738.3', 'ICD9CM:738.4', 'ICD9CM:738.5', 'ICD9CM:738.6', 'ICD9CM:738.7', 'ICD9CM:738.8', 'ICD9CM:738.9'):
            results_ccs3["other_acq_deform"].append(1)
        else: results_ccs3["other_acq_deform"].append(0)
    print("Completed Binary Recode of: other_acq_deform")

    # Systemic_lupus_erythematosus_and_connective_tissue_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:710.0', 'ICD9CM:710.1', 'ICD9CM:710.2', 'ICD9CM:710.3', 'ICD9CM:710.4', 'ICD9CM:710.8', 'ICD9CM:710.9'):
            results_ccs3["systemic_lupus"].append(1)
        else: results_ccs3["systemic_lupus"].append(0)
    print("Completed Binary Recode of: systemic_lupus")

    # Other_connective_tissue_disease
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:327.52', 'ICD9CM:567.31', 'ICD9CM:710.5', 'ICD9CM:725', 'ICD9CM:726.0', 'ICD9CM:726.10', 'ICD9CM:726.11', 'ICD9CM:726.12', 'ICD9CM:726.13', 'ICD9CM:726.19', 'ICD9CM:726.2', 'ICD9CM:726.30', 'ICD9CM:726.31', 'ICD9CM:726.32', 'ICD9CM:726.33', 'ICD9CM:726.39', 'ICD9CM:726.4', 'ICD9CM:726.5', 'ICD9CM:726.60', 'ICD9CM:726.61', 'ICD9CM:726.62', 'ICD9CM:726.63', 'ICD9CM:726.64', 'ICD9CM:726.65', 'ICD9CM:726.69', 'ICD9CM:726.70', 'ICD9CM:726.71', 'ICD9CM:726.72', 'ICD9CM:726.73', 'ICD9CM:726.79', 'ICD9CM:726.8', 'ICD9CM:726.90', 'ICD9CM:726.91', 'ICD9CM:727.00', 'ICD9CM:727.01', 'ICD9CM:727.02', 'ICD9CM:727.03', 'ICD9CM:727.04', 'ICD9CM:727.05', 'ICD9CM:727.06', 'ICD9CM:727.09', 'ICD9CM:727.2', 'ICD9CM:727.3', 'ICD9CM:727.40', 'ICD9CM:727.41', 'ICD9CM:727.42', 'ICD9CM:727.43', 'ICD9CM:727.49', 'ICD9CM:727.50', 'ICD9CM:727.51', 'ICD9CM:727.59', 'ICD9CM:727.60', 'ICD9CM:727.61', 'ICD9CM:727.62', 'ICD9CM:727.63', 'ICD9CM:727.64', 'ICD9CM:727.65', 'ICD9CM:727.66', 'ICD9CM:727.67', 'ICD9CM:727.68', 'ICD9CM:727.69', 'ICD9CM:727.81', 'ICD9CM:727.82', 'ICD9CM:727.83', 'ICD9CM:727.89', 'ICD9CM:727.9', 'ICD9CM:728.0', 'ICD9CM:728.10', 'ICD9CM:728.11', 'ICD9CM:728.12', 'ICD9CM:728.13', 'ICD9CM:728.19', 'ICD9CM:728.2', 'ICD9CM:728.3', 'ICD9CM:728.4', 'ICD9CM:728.5', 'ICD9CM:728.6', 'ICD9CM:728.71', 'ICD9CM:728.79', 'ICD9CM:728.81', 'ICD9CM:728.82', 'ICD9CM:728.83', 'ICD9CM:728.84', 'ICD9CM:728.85', 'ICD9CM:728.86', 'ICD9CM:728.87', 'ICD9CM:728.88', 'ICD9CM:728.89', 'ICD9CM:728.9', 'ICD9CM:729.0', 'ICD9CM:729.1', 'ICD9CM:729.2', 'ICD9CM:729.30', 'ICD9CM:729.31', 'ICD9CM:729.39', 'ICD9CM:729.4', 'ICD9CM:729.5', 'ICD9CM:729.6', 'ICD9CM:729.71', 'ICD9CM:729.72', 'ICD9CM:729.73', 'ICD9CM:729.79', 'ICD9CM:729.81', 'ICD9CM:729.82', 'ICD9CM:729.89', 'ICD9CM:729.9', 'ICD9CM:729.90', 'ICD9CM:729.91', 'ICD9CM:729.92', 'ICD9CM:729.99', 'ICD9CM:781.9', 'ICD9CM:781.91', 'ICD9CM:781.92', 'ICD9CM:781.94', 'ICD9CM:781.99', 'ICD9CM:793.7', 'ICD9CM:V13.5', 'ICD9CM:V13.59', 'ICD9CM:V43.6', 'ICD9CM:V43.60', 'ICD9CM:V43.61', 'ICD9CM:V43.62', 'ICD9CM:V43.63', 'ICD9CM:V43.64', 'ICD9CM:V43.65', 'ICD9CM:V43.66', 'ICD9CM:V43.69', 'ICD9CM:V43.7', 'ICD9CM:V45.4', 'ICD9CM:V48.1', 'ICD9CM:V48.2', 'ICD9CM:V48.3', 'ICD9CM:V49.0', 'ICD9CM:V49.1', 'ICD9CM:V49.2', 'ICD9CM:V49.5', 'ICD9CM:V49.60', 'ICD9CM:V49.61', 'ICD9CM:V49.62', 'ICD9CM:V49.63', 'ICD9CM:V49.64', 'ICD9CM:V49.65', 'ICD9CM:V49.66', 'ICD9CM:V49.67', 'ICD9CM:V49.70', 'ICD9CM:V49.71', 'ICD9CM:V49.72', 'ICD9CM:V49.73', 'ICD9CM:V49.74', 'ICD9CM:V49.75', 'ICD9CM:V49.76', 'ICD9CM:V49.77', 'ICD9CM:V53.7'):
            results_ccs3["other_connective"].append(1)
        else: results_ccs3["other_connective"].append(0)
    print("Completed Binary Recode of: other_connective")

    # Other_bone_disease_and_musculoskeletal_deformities
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:731.0', 'ICD9CM:731.1', 'ICD9CM:731.2', 'ICD9CM:731.3', 'ICD9CM:731.8', 'ICD9CM:732.0', 'ICD9CM:732.1', 'ICD9CM:732.2', 'ICD9CM:732.3', 'ICD9CM:732.4', 'ICD9CM:732.5', 'ICD9CM:732.6', 'ICD9CM:732.7', 'ICD9CM:732.8', 'ICD9CM:732.9', 'ICD9CM:733.20', 'ICD9CM:733.21', 'ICD9CM:733.22', 'ICD9CM:733.29', 'ICD9CM:733.3', 'ICD9CM:733.40', 'ICD9CM:733.41', 'ICD9CM:733.42', 'ICD9CM:733.43', 'ICD9CM:733.44', 'ICD9CM:733.45', 'ICD9CM:733.49', 'ICD9CM:733.5', 'ICD9CM:733.6', 'ICD9CM:733.7', 'ICD9CM:733.81', 'ICD9CM:733.82', 'ICD9CM:733.90', 'ICD9CM:733.91', 'ICD9CM:733.92', 'ICD9CM:733.99', 'ICD9CM:737.30', 'ICD9CM:737.31', 'ICD9CM:737.32', 'ICD9CM:739.0', 'ICD9CM:739.1', 'ICD9CM:739.2', 'ICD9CM:739.3', 'ICD9CM:739.4', 'ICD9CM:739.5', 'ICD9CM:739.6', 'ICD9CM:739.7', 'ICD9CM:739.8', 'ICD9CM:739.9', 'ICD9CM:V42.4', 'ICD9CM:V48.6', 'ICD9CM:V48.7', 'ICD9CM:V49.4', 'ICD9CM:V88.21', 'ICD9CM:V88.22', 'ICD9CM:V88.29'):
            results_ccs3["other_bone_disease"].append(1)
        else: results_ccs3["other_bone_disease"].append(0)
    print("Completed Binary Recode of: other_bone_disease")

    # Cardiac_and_circulatory_congenital_anomalies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:745.0', 'ICD9CM:745.10', 'ICD9CM:745.11', 'ICD9CM:745.12', 'ICD9CM:745.19', 'ICD9CM:745.2', 'ICD9CM:745.3', 'ICD9CM:745.4', 'ICD9CM:745.5', 'ICD9CM:745.60', 'ICD9CM:745.61', 'ICD9CM:745.69', 'ICD9CM:745.7', 'ICD9CM:745.8', 'ICD9CM:745.9', 'ICD9CM:746.00', 'ICD9CM:746.01', 'ICD9CM:746.02', 'ICD9CM:746.09', 'ICD9CM:746.1', 'ICD9CM:746.2', 'ICD9CM:746.3', 'ICD9CM:746.4', 'ICD9CM:746.5', 'ICD9CM:746.6', 'ICD9CM:746.7', 'ICD9CM:746.81', 'ICD9CM:746.82', 'ICD9CM:746.83', 'ICD9CM:746.84', 'ICD9CM:746.85', 'ICD9CM:746.86', 'ICD9CM:746.87', 'ICD9CM:746.89', 'ICD9CM:746.9', 'ICD9CM:747.0', 'ICD9CM:747.10', 'ICD9CM:747.11', 'ICD9CM:747.20', 'ICD9CM:747.21', 'ICD9CM:747.22', 'ICD9CM:747.29', 'ICD9CM:747.3', 'ICD9CM:747.31', 'ICD9CM:747.32', 'ICD9CM:747.39', 'ICD9CM:747.40', 'ICD9CM:747.41', 'ICD9CM:747.42', 'ICD9CM:747.49', 'ICD9CM:747.5', 'ICD9CM:747.6', 'ICD9CM:747.60', 'ICD9CM:747.61', 'ICD9CM:747.62', 'ICD9CM:747.63', 'ICD9CM:747.64', 'ICD9CM:747.69', 'ICD9CM:747.81', 'ICD9CM:747.82', 'ICD9CM:747.83', 'ICD9CM:747.89', 'ICD9CM:747.9', 'ICD9CM:V13.65'):
            results_ccs3["cardiac_congen_anom"].append(1)
        else: results_ccs3["cardiac_congen_anom"].append(0)
    print("Completed Binary Recode of: cardiac_congen_anom")

    # Digestive_congenital_anomalies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:750.0', 'ICD9CM:750.10', 'ICD9CM:750.11', 'ICD9CM:750.12', 'ICD9CM:750.13', 'ICD9CM:750.15', 'ICD9CM:750.16', 'ICD9CM:750.19', 'ICD9CM:750.21', 'ICD9CM:750.22', 'ICD9CM:750.23', 'ICD9CM:750.24', 'ICD9CM:750.25', 'ICD9CM:750.26', 'ICD9CM:750.27', 'ICD9CM:750.29', 'ICD9CM:750.3', 'ICD9CM:750.4', 'ICD9CM:750.5', 'ICD9CM:750.6', 'ICD9CM:750.7', 'ICD9CM:750.8', 'ICD9CM:750.9', 'ICD9CM:751.0', 'ICD9CM:751.1', 'ICD9CM:751.2', 'ICD9CM:751.3', 'ICD9CM:751.4', 'ICD9CM:751.5', 'ICD9CM:751.60', 'ICD9CM:751.61', 'ICD9CM:751.62', 'ICD9CM:751.69', 'ICD9CM:751.7', 'ICD9CM:751.8', 'ICD9CM:751.9', 'ICD9CM:V13.67'):
            results_ccs3["digest_congen_anom"].append(1)
        else: results_ccs3["digest_congen_anom"].append(0)
    print("Completed Binary Recode of: digest_congen_anom")

    # Genitourinary_congenital_anomalies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:752.0', 'ICD9CM:752.10', 'ICD9CM:752.11', 'ICD9CM:752.19', 'ICD9CM:752.2', 'ICD9CM:752.3', 'ICD9CM:752.31', 'ICD9CM:752.32', 'ICD9CM:752.33', 'ICD9CM:752.34', 'ICD9CM:752.35', 'ICD9CM:752.36', 'ICD9CM:752.39', 'ICD9CM:752.40', 'ICD9CM:752.41', 'ICD9CM:752.42', 'ICD9CM:752.43', 'ICD9CM:752.44', 'ICD9CM:752.45', 'ICD9CM:752.46', 'ICD9CM:752.47', 'ICD9CM:752.49', 'ICD9CM:752.5', 'ICD9CM:752.51', 'ICD9CM:752.52', 'ICD9CM:752.6', 'ICD9CM:752.61', 'ICD9CM:752.62', 'ICD9CM:752.63', 'ICD9CM:752.64', 'ICD9CM:752.65', 'ICD9CM:752.69', 'ICD9CM:752.7', 'ICD9CM:752.8', 'ICD9CM:752.81', 'ICD9CM:752.89', 'ICD9CM:752.9', 'ICD9CM:753.0', 'ICD9CM:753.1', 'ICD9CM:753.10', 'ICD9CM:753.11', 'ICD9CM:753.12', 'ICD9CM:753.13', 'ICD9CM:753.14', 'ICD9CM:753.15', 'ICD9CM:753.16', 'ICD9CM:753.17', 'ICD9CM:753.19', 'ICD9CM:753.2', 'ICD9CM:753.20', 'ICD9CM:753.21', 'ICD9CM:753.22', 'ICD9CM:753.23', 'ICD9CM:753.29', 'ICD9CM:753.3', 'ICD9CM:753.4', 'ICD9CM:753.5', 'ICD9CM:753.6', 'ICD9CM:753.7', 'ICD9CM:753.8', 'ICD9CM:753.9', 'ICD9CM:V13.61', 'ICD9CM:V13.62'):
            results_ccs3["genito_congen_anom"].append(1)
        else: results_ccs3["genito_congen_anom"].append(0)
    print("Completed Binary Recode of: genito_congen_anom")

    # Nervous_system_congenital_anomalies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:740.0', 'ICD9CM:740.1', 'ICD9CM:740.2', 'ICD9CM:741.00', 'ICD9CM:741.01', 'ICD9CM:741.02', 'ICD9CM:741.03', 'ICD9CM:741.90', 'ICD9CM:741.91', 'ICD9CM:741.92', 'ICD9CM:741.93', 'ICD9CM:742.0', 'ICD9CM:742.1', 'ICD9CM:742.2', 'ICD9CM:742.3', 'ICD9CM:742.4', 'ICD9CM:742.51', 'ICD9CM:742.53', 'ICD9CM:742.59', 'ICD9CM:742.8', 'ICD9CM:742.9', 'ICD9CM:V13.63'):
            results_ccs3["ns_congen_anom"].append(1)
        else: results_ccs3["ns_congen_anom"].append(0)
    print("Completed Binary Recode of: ns_congen_anom")

    # Other_congenital_anomalies
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:743.00', 'ICD9CM:743.03', 'ICD9CM:743.06', 'ICD9CM:743.10', 'ICD9CM:743.11', 'ICD9CM:743.12', 'ICD9CM:743.20', 'ICD9CM:743.21', 'ICD9CM:743.22', 'ICD9CM:743.30', 'ICD9CM:743.31', 'ICD9CM:743.32', 'ICD9CM:743.33', 'ICD9CM:743.34', 'ICD9CM:743.35', 'ICD9CM:743.36', 'ICD9CM:743.37', 'ICD9CM:743.39', 'ICD9CM:743.41', 'ICD9CM:743.42', 'ICD9CM:743.43', 'ICD9CM:743.44', 'ICD9CM:743.45', 'ICD9CM:743.46', 'ICD9CM:743.47', 'ICD9CM:743.48', 'ICD9CM:743.49', 'ICD9CM:743.51', 'ICD9CM:743.52', 'ICD9CM:743.53', 'ICD9CM:743.54', 'ICD9CM:743.55', 'ICD9CM:743.56', 'ICD9CM:743.57', 'ICD9CM:743.58', 'ICD9CM:743.59', 'ICD9CM:743.61', 'ICD9CM:743.62', 'ICD9CM:743.63', 'ICD9CM:743.64', 'ICD9CM:743.65', 'ICD9CM:743.66', 'ICD9CM:743.69', 'ICD9CM:743.8', 'ICD9CM:743.9', 'ICD9CM:744.00', 'ICD9CM:744.01', 'ICD9CM:744.02', 'ICD9CM:744.03', 'ICD9CM:744.04', 'ICD9CM:744.05', 'ICD9CM:744.09', 'ICD9CM:744.1', 'ICD9CM:744.21', 'ICD9CM:744.22', 'ICD9CM:744.23', 'ICD9CM:744.24', 'ICD9CM:744.29', 'ICD9CM:744.3', 'ICD9CM:744.41', 'ICD9CM:744.42', 'ICD9CM:744.43', 'ICD9CM:744.46', 'ICD9CM:744.47', 'ICD9CM:744.49', 'ICD9CM:744.5', 'ICD9CM:744.81', 'ICD9CM:744.82', 'ICD9CM:744.83', 'ICD9CM:744.84', 'ICD9CM:744.89', 'ICD9CM:744.9', 'ICD9CM:748.0', 'ICD9CM:748.1', 'ICD9CM:748.2', 'ICD9CM:748.3', 'ICD9CM:748.4', 'ICD9CM:748.5', 'ICD9CM:748.60', 'ICD9CM:748.61', 'ICD9CM:748.69', 'ICD9CM:748.8', 'ICD9CM:748.9', 'ICD9CM:749.00', 'ICD9CM:749.01', 'ICD9CM:749.02', 'ICD9CM:749.03', 'ICD9CM:749.04', 'ICD9CM:749.10', 'ICD9CM:749.11', 'ICD9CM:749.12', 'ICD9CM:749.13', 'ICD9CM:749.14', 'ICD9CM:749.20', 'ICD9CM:749.21', 'ICD9CM:749.22', 'ICD9CM:749.23', 'ICD9CM:749.24', 'ICD9CM:749.25', 'ICD9CM:754.0', 'ICD9CM:754.1', 'ICD9CM:754.2', 'ICD9CM:754.30', 'ICD9CM:754.31', 'ICD9CM:754.32', 'ICD9CM:754.33', 'ICD9CM:754.35', 'ICD9CM:754.40', 'ICD9CM:754.41', 'ICD9CM:754.42', 'ICD9CM:754.43', 'ICD9CM:754.44', 'ICD9CM:754.50', 'ICD9CM:754.51', 'ICD9CM:754.52', 'ICD9CM:754.53', 'ICD9CM:754.59', 'ICD9CM:754.60', 'ICD9CM:754.61', 'ICD9CM:754.62', 'ICD9CM:754.69', 'ICD9CM:754.70', 'ICD9CM:754.71', 'ICD9CM:754.79', 'ICD9CM:754.81', 'ICD9CM:754.82', 'ICD9CM:754.89', 'ICD9CM:755.00', 'ICD9CM:755.01', 'ICD9CM:755.02', 'ICD9CM:755.10', 'ICD9CM:755.11', 'ICD9CM:755.12', 'ICD9CM:755.13', 'ICD9CM:755.14', 'ICD9CM:755.20', 'ICD9CM:755.21', 'ICD9CM:755.22', 'ICD9CM:755.23', 'ICD9CM:755.24', 'ICD9CM:755.25', 'ICD9CM:755.26', 'ICD9CM:755.27', 'ICD9CM:755.28', 'ICD9CM:755.29', 'ICD9CM:755.30', 'ICD9CM:755.31', 'ICD9CM:755.32', 'ICD9CM:755.33', 'ICD9CM:755.34', 'ICD9CM:755.35', 'ICD9CM:755.36', 'ICD9CM:755.37', 'ICD9CM:755.38', 'ICD9CM:755.39', 'ICD9CM:755.4', 'ICD9CM:755.50', 'ICD9CM:755.51', 'ICD9CM:755.52', 'ICD9CM:755.53', 'ICD9CM:755.54', 'ICD9CM:755.55', 'ICD9CM:755.56', 'ICD9CM:755.57', 'ICD9CM:755.58', 'ICD9CM:755.59', 'ICD9CM:755.60', 'ICD9CM:755.61', 'ICD9CM:755.62', 'ICD9CM:755.63', 'ICD9CM:755.64', 'ICD9CM:755.65', 'ICD9CM:755.66', 'ICD9CM:755.67', 'ICD9CM:755.69', 'ICD9CM:755.8', 'ICD9CM:755.9', 'ICD9CM:756.0', 'ICD9CM:756.10', 'ICD9CM:756.11', 'ICD9CM:756.12', 'ICD9CM:756.13', 'ICD9CM:756.14', 'ICD9CM:756.15', 'ICD9CM:756.16', 'ICD9CM:756.17', 'ICD9CM:756.19', 'ICD9CM:756.2', 'ICD9CM:756.3', 'ICD9CM:756.4', 'ICD9CM:756.50', 'ICD9CM:756.51', 'ICD9CM:756.52', 'ICD9CM:756.53', 'ICD9CM:756.54', 'ICD9CM:756.55', 'ICD9CM:756.56', 'ICD9CM:756.59', 'ICD9CM:756.6', 'ICD9CM:756.7', 'ICD9CM:756.70', 'ICD9CM:756.71', 'ICD9CM:756.72', 'ICD9CM:756.73', 'ICD9CM:756.79', 'ICD9CM:756.81', 'ICD9CM:756.82', 'ICD9CM:756.83', 'ICD9CM:756.89', 'ICD9CM:756.9', 'ICD9CM:757.0', 'ICD9CM:757.1', 'ICD9CM:757.2', 'ICD9CM:757.31', 'ICD9CM:757.32', 'ICD9CM:757.33', 'ICD9CM:757.39', 'ICD9CM:757.4', 'ICD9CM:757.5', 'ICD9CM:757.6', 'ICD9CM:757.8', 'ICD9CM:757.9', 'ICD9CM:758.0', 'ICD9CM:758.1', 'ICD9CM:758.2', 'ICD9CM:758.3', 'ICD9CM:758.31', 'ICD9CM:758.32', 'ICD9CM:758.33', 'ICD9CM:758.39', 'ICD9CM:758.4', 'ICD9CM:758.5', 'ICD9CM:758.6', 'ICD9CM:758.7', 'ICD9CM:758.8', 'ICD9CM:758.81', 'ICD9CM:758.89', 'ICD9CM:758.9', 'ICD9CM:759.0', 'ICD9CM:759.1', 'ICD9CM:759.2', 'ICD9CM:759.3', 'ICD9CM:759.4', 'ICD9CM:759.5', 'ICD9CM:759.6', 'ICD9CM:759.7', 'ICD9CM:759.8', 'ICD9CM:759.81', 'ICD9CM:759.82', 'ICD9CM:759.83', 'ICD9CM:759.89', 'ICD9CM:759.9', 'ICD9CM:795.2', 'ICD9CM:V13.6', 'ICD9CM:V13.64', 'ICD9CM:V13.66', 'ICD9CM:V13.68', 'ICD9CM:V13.69'):
            results_ccs3["other_congen_anom"].append(1)
        else: results_ccs3["other_congen_anom"].append(0)
    print("Completed Binary Recode of: other_congen_anom")

    # Liveborn
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:765.20', 'ICD9CM:765.29', 'ICD9CM:V30.0', 'ICD9CM:V30.00', 'ICD9CM:V30.01', 'ICD9CM:V30.1', 'ICD9CM:V30.2', 'ICD9CM:V31.0', 'ICD9CM:V31.00', 'ICD9CM:V31.01', 'ICD9CM:V31.1', 'ICD9CM:V31.2', 'ICD9CM:V32.0', 'ICD9CM:V32.00', 'ICD9CM:V32.01', 'ICD9CM:V32.1', 'ICD9CM:V32.2', 'ICD9CM:V33.0', 'ICD9CM:V33.00', 'ICD9CM:V33.01', 'ICD9CM:V33.1', 'ICD9CM:V33.2', 'ICD9CM:V34.0', 'ICD9CM:V34.00', 'ICD9CM:V34.01', 'ICD9CM:V34.1', 'ICD9CM:V34.2', 'ICD9CM:V35.0', 'ICD9CM:V35.00', 'ICD9CM:V35.01', 'ICD9CM:V35.1', 'ICD9CM:V35.2', 'ICD9CM:V36.0', 'ICD9CM:V36.00', 'ICD9CM:V36.01', 'ICD9CM:V36.1', 'ICD9CM:V36.2', 'ICD9CM:V37.0', 'ICD9CM:V37.00', 'ICD9CM:V37.01', 'ICD9CM:V37.1', 'ICD9CM:V37.2', 'ICD9CM:V39.0', 'ICD9CM:V39.00', 'ICD9CM:V39.01', 'ICD9CM:V39.1', 'ICD9CM:V39.2'):
            results_ccs3["liveborn"].append(1)
        else: results_ccs3["liveborn"].append(0)
    print("Completed Binary Recode of: liveborn")

    # Short_gestation;_low_birth_weight;_and_fetal_growth_retardation
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:764.0', 'ICD9CM:764.00', 'ICD9CM:764.01', 'ICD9CM:764.02', 'ICD9CM:764.03', 'ICD9CM:764.04', 'ICD9CM:764.05', 'ICD9CM:764.06', 'ICD9CM:764.07', 'ICD9CM:764.08', 'ICD9CM:764.09', 'ICD9CM:764.1', 'ICD9CM:764.10', 'ICD9CM:764.11', 'ICD9CM:764.12', 'ICD9CM:764.13', 'ICD9CM:764.14', 'ICD9CM:764.15', 'ICD9CM:764.16', 'ICD9CM:764.17', 'ICD9CM:764.18', 'ICD9CM:764.19', 'ICD9CM:764.2', 'ICD9CM:764.20', 'ICD9CM:764.21', 'ICD9CM:764.22', 'ICD9CM:764.23', 'ICD9CM:764.24', 'ICD9CM:764.25', 'ICD9CM:764.26', 'ICD9CM:764.27', 'ICD9CM:764.28', 'ICD9CM:764.29', 'ICD9CM:764.9', 'ICD9CM:764.90', 'ICD9CM:764.91', 'ICD9CM:764.92', 'ICD9CM:764.93', 'ICD9CM:764.94', 'ICD9CM:764.95', 'ICD9CM:764.96', 'ICD9CM:764.97', 'ICD9CM:764.98', 'ICD9CM:764.99', 'ICD9CM:765.0', 'ICD9CM:765.00', 'ICD9CM:765.01', 'ICD9CM:765.02', 'ICD9CM:765.03', 'ICD9CM:765.04', 'ICD9CM:765.05', 'ICD9CM:765.06', 'ICD9CM:765.07', 'ICD9CM:765.08', 'ICD9CM:765.09', 'ICD9CM:765.1', 'ICD9CM:765.10', 'ICD9CM:765.11', 'ICD9CM:765.12', 'ICD9CM:765.13', 'ICD9CM:765.14', 'ICD9CM:765.15', 'ICD9CM:765.16', 'ICD9CM:765.17', 'ICD9CM:765.18', 'ICD9CM:765.19', 'ICD9CM:765.21', 'ICD9CM:765.22', 'ICD9CM:765.23', 'ICD9CM:765.24', 'ICD9CM:765.25', 'ICD9CM:765.26', 'ICD9CM:765.27', 'ICD9CM:765.28', 'ICD9CM:V21.30', 'ICD9CM:V21.31', 'ICD9CM:V21.32', 'ICD9CM:V21.33', 'ICD9CM:V21.34', 'ICD9CM:V21.35'):
            results_ccs3["short_gest"].append(1)
        else: results_ccs3["short_gest"].append(0)
    print("Completed Binary Recode of: short_gest")

    # Intrauterine_hypoxia_and_birth_asphyxia
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:768.0', 'ICD9CM:768.1', 'ICD9CM:768.2', 'ICD9CM:768.3', 'ICD9CM:768.4', 'ICD9CM:768.5', 'ICD9CM:768.6', 'ICD9CM:768.7', 'ICD9CM:768.70', 'ICD9CM:768.71', 'ICD9CM:768.72', 'ICD9CM:768.73', 'ICD9CM:768.9', 'ICD9CM:770.88'):
            results_ccs3["intrauter_hypoxia"].append(1)
        else: results_ccs3["intrauter_hypoxia"].append(0)
    print("Completed Binary Recode of: intrauter_hypoxia")

    # Respiratory_distress_syndrome
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:769':
            results_ccs3["resp_distress_synd"].append(1)
        else: results_ccs3["resp_distress_synd"].append(0)
    print("Completed Binary Recode of: resp_distress_synd")

    # Hemolytic_jaundice_and_perinatal_jaundice
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:773.0', 'ICD9CM:773.1', 'ICD9CM:773.2', 'ICD9CM:773.3', 'ICD9CM:773.4', 'ICD9CM:773.5', 'ICD9CM:774.0', 'ICD9CM:774.1', 'ICD9CM:774.2', 'ICD9CM:774.30', 'ICD9CM:774.31', 'ICD9CM:774.39', 'ICD9CM:774.4', 'ICD9CM:774.5', 'ICD9CM:774.6', 'ICD9CM:774.7'):
            results_ccs3["hemolytic_jaundice"].append(1)
        else: results_ccs3["hemolytic_jaundice"].append(0)
    print("Completed Binary Recode of: hemolytic_jaundice")

    pd.DataFrame(results_ccs3).to_csv(output_filepath, encoding='utf-8')
    print("CDRN - CCS Dx Recode Part 3: Complete")
    print("")


###########################
###########################
###########################
###########################
###########################
###########################

def dx_convert4(df):

    output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccs_results4.csv'

    results_ccs4 = {"person_id":[],"condition_start_date":[], "birth_trauma": [], "other_perinatal": [], "joint_trauma": [], "fract_femur_neck": [],
                    "spinal_cord": [], "skull_face_fract": [], "upper_limb_fract": [], "lower_limb_fract": [],
                    "other_fract": [], "sprain_strain": [], "intracranial": [], "crush_injury": [],
                    "open_wound_head": [], "open_wound_extr": [], "comp_of_device": [], "comp_surg_proc": [],
                    "superficial_inj": [], "burns": [], "poison_psycho": [], "poison_other_med": [],
                    "poison_nonmed": [], "other_ext_injury": [], "syncope": [], "fever_unknown": [],
                    "lymphadenitis": [], "gangrene": [], "shock": [], "naus_vom": [], "abdominal_pain": [],
                    "malaise_fatigue": [], "allergy": [], "rehab_care": [], "admin_admiss": [], "medical_eval": [],
                    "other_aftercare": [], "other_screen": [], "residual_codes": [], "adjustment": [],
                    "anxiety": [], "adhd": [], "dementia": [], "develop_dis": [], "child_disorder": [],
                    "impule_control": [], "mood": [], "personality": [], "schizo": [], "alcohol": [],
                    "substance": [], "suicide": [], "mental_screen": [], "misc_mental": [], "e_cut_pierce": [],
                    "e_drown": [], "e_fall": [], "e_fire": [], "e_firearm": [], "e_machine": [], "e_mvt": [],
                    "e_cyclist": [], "e_pedestrian": [], "e_transport": [], "e_natural": [], "e_overexert": [],
                    "e_poison": [], "e_struckby": [], "e_suffocate": [], "e_ae_med_care": [], "e_ae_med_drug": [],
                    "e_other_class": [], "e_other_nec": [], "e_unspecified": [], "e_place": []}

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs4["person_id"].append(_)
    print("Number of person_id with missing dx history: ", len(results_ccs4["person_id"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs4["condition_start_date"].append(dt.datetime.strptime('12/31/13', "%m/%d/%y"))
    print("Number of start dates added for patients with missing dx history: ",
          len(results_ccs4["condition_start_date"]))

    for _ in cdrn_all_individual_visits_nodx['person_id']:
        results_ccs4["birth_trauma"].append(0)
        results_ccs4["other_perinatal"].append(0)
        results_ccs4["joint_trauma"].append(0)
        results_ccs4["fract_femur_neck"].append(0)
        results_ccs4["spinal_cord"].append(0)
        results_ccs4["skull_face_fract"].append(0)
        results_ccs4["upper_limb_fract"].append(0)
        results_ccs4["lower_limb_fract"].append(0)
        results_ccs4["other_fract"].append(0)
        results_ccs4["sprain_strain"].append(0)
        results_ccs4["intracranial"].append(0)
        results_ccs4["crush_injury"].append(0)
        results_ccs4["open_wound_head"].append(0)
        results_ccs4["open_wound_extr"].append(0)
        results_ccs4["comp_of_device"].append(0)
        results_ccs4["comp_surg_proc"].append(0)
        results_ccs4["superficial_inj"].append(0)
        results_ccs4["burns"].append(0)
        results_ccs4["poison_psycho"].append(0)
        results_ccs4["poison_other_med"].append(0)
        results_ccs4["poison_nonmed"].append(0)
        results_ccs4["other_ext_injury"].append(0)
        results_ccs4["syncope"].append(0)
        results_ccs4["fever_unknown"].append(0)
        results_ccs4["lymphadenitis"].append(0)
        results_ccs4["gangrene"].append(0)
        results_ccs4["shock"].append(0)
        results_ccs4["naus_vom"].append(0)
        results_ccs4["abdominal_pain"].append(0)
        results_ccs4["malaise_fatigue"].append(0)
        results_ccs4["allergy"].append(0)
        results_ccs4["rehab_care"].append(0)
        results_ccs4["admin_admiss"].append(0)
        results_ccs4["medical_eval"].append(0)
        results_ccs4["other_aftercare"].append(0)
        results_ccs4["other_screen"].append(0)
        results_ccs4["residual_codes"].append(0)
        results_ccs4["adjustment"].append(0)
        results_ccs4["anxiety"].append(0)
        results_ccs4["adhd"].append(0)
        results_ccs4["dementia"].append(0)
        results_ccs4["develop_dis"].append(0)
        results_ccs4["child_disorder"].append(0)
        results_ccs4["impule_control"].append(0)
        results_ccs4["mood"].append(0)
        results_ccs4["personality"].append(0)
        results_ccs4["schizo"].append(0)
        results_ccs4["alcohol"].append(0)
        results_ccs4["substance"].append(0)
        results_ccs4["suicide"].append(0)
        results_ccs4["mental_screen"].append(0)
        results_ccs4["misc_mental"].append(0)
        results_ccs4["e_cut_pierce"].append(0)
        results_ccs4["e_drown"].append(0)
        results_ccs4["e_fall"].append(0)
        results_ccs4["e_fire"].append(0)
        results_ccs4["e_firearm"].append(0)
        results_ccs4["e_machine"].append(0)
        results_ccs4["e_mvt"].append(0)
        results_ccs4["e_cyclist"].append(0)
        results_ccs4["e_pedestrian"].append(0)
        results_ccs4["e_transport"].append(0)
        results_ccs4["e_natural"].append(0)
        results_ccs4["e_overexert"].append(0)
        results_ccs4["e_poison"].append(0)
        results_ccs4["e_struckby"].append(0)
        results_ccs4["e_suffocate"].append(0)
        results_ccs4["e_ae_med_care"].append(0)
        results_ccs4["e_ae_med_drug"].append(0)
        results_ccs4["e_other_class"].append(0)
        results_ccs4["e_other_nec"].append(0)
        results_ccs4["e_unspecified"].append(0)
        results_ccs4["e_place"].append(0)
    print("Completed null dx recode for pts that are missing dx but meet visit criteria")

    for _ in df['person_id']:
        results_ccs4["person_id"].append(_)
    print("Number of patients in results_ccs4", len(results_ccs4["person_id"]))

    for _ in df['condition_start_date']:
        results_ccs4["condition_start_date"].append(_)
    print("Number of start dates in results_ccs4", len(results_ccs4["condition_start_date"]))

    # Birth_trauma
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:767.0', 'ICD9CM:767.1', 'ICD9CM:767.11', 'ICD9CM:767.19', 'ICD9CM:767.2', 'ICD9CM:767.3', 'ICD9CM:767.4', 'ICD9CM:767.5', 'ICD9CM:767.6', 'ICD9CM:767.7', 'ICD9CM:767.8', 'ICD9CM:767.9'):
            results_ccs4["birth_trauma"].append(1)
        else: results_ccs4["birth_trauma"].append(0)
    print("Completed Binary Recode of: birth_trauma")

    # Other_perinatal_conditions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:040.41', 'ICD9CM:760.0', 'ICD9CM:760.1', 'ICD9CM:760.2', 'ICD9CM:760.3', 'ICD9CM:760.4', 'ICD9CM:760.5', 'ICD9CM:760.6', 'ICD9CM:760.61', 'ICD9CM:760.62', 'ICD9CM:760.63', 'ICD9CM:760.64', 'ICD9CM:760.70', 'ICD9CM:760.74', 'ICD9CM:760.76', 'ICD9CM:760.77', 'ICD9CM:760.78', 'ICD9CM:760.79', 'ICD9CM:760.8', 'ICD9CM:760.9', 'ICD9CM:761.0', 'ICD9CM:761.1', 'ICD9CM:761.2', 'ICD9CM:761.3', 'ICD9CM:761.4', 'ICD9CM:761.5', 'ICD9CM:761.6', 'ICD9CM:761.7', 'ICD9CM:761.8', 'ICD9CM:761.9', 'ICD9CM:762.0', 'ICD9CM:762.1', 'ICD9CM:762.2', 'ICD9CM:762.3', 'ICD9CM:762.4', 'ICD9CM:762.5', 'ICD9CM:762.6', 'ICD9CM:762.7', 'ICD9CM:762.8', 'ICD9CM:762.9', 'ICD9CM:763.0', 'ICD9CM:763.1', 'ICD9CM:763.2', 'ICD9CM:763.3', 'ICD9CM:763.4', 'ICD9CM:763.5', 'ICD9CM:763.6', 'ICD9CM:763.7', 'ICD9CM:763.8', 'ICD9CM:763.81', 'ICD9CM:763.82', 'ICD9CM:763.83', 'ICD9CM:763.84', 'ICD9CM:763.89', 'ICD9CM:763.9', 'ICD9CM:766.0', 'ICD9CM:766.1', 'ICD9CM:766.2', 'ICD9CM:766.21', 'ICD9CM:766.22', 'ICD9CM:770.0', 'ICD9CM:770.1', 'ICD9CM:770.10', 'ICD9CM:770.11', 'ICD9CM:770.12', 'ICD9CM:770.13', 'ICD9CM:770.14', 'ICD9CM:770.15', 'ICD9CM:770.16', 'ICD9CM:770.17', 'ICD9CM:770.18', 'ICD9CM:770.2', 'ICD9CM:770.3', 'ICD9CM:770.4', 'ICD9CM:770.5', 'ICD9CM:770.6', 'ICD9CM:770.7', 'ICD9CM:770.8', 'ICD9CM:770.81', 'ICD9CM:770.82', 'ICD9CM:770.83', 'ICD9CM:770.84', 'ICD9CM:770.85', 'ICD9CM:770.86', 'ICD9CM:770.87', 'ICD9CM:770.89', 'ICD9CM:770.9', 'ICD9CM:771.0', 'ICD9CM:771.1', 'ICD9CM:771.2', 'ICD9CM:771.3', 'ICD9CM:771.4', 'ICD9CM:771.5', 'ICD9CM:771.6', 'ICD9CM:771.7', 'ICD9CM:771.8', 'ICD9CM:771.82', 'ICD9CM:771.83', 'ICD9CM:771.89', 'ICD9CM:772.0', 'ICD9CM:772.1', 'ICD9CM:772.10', 'ICD9CM:772.11', 'ICD9CM:772.12', 'ICD9CM:772.13', 'ICD9CM:772.14', 'ICD9CM:772.2', 'ICD9CM:772.3', 'ICD9CM:772.4', 'ICD9CM:772.5', 'ICD9CM:772.6', 'ICD9CM:772.8', 'ICD9CM:772.9', 'ICD9CM:775.0', 'ICD9CM:775.1', 'ICD9CM:775.2', 'ICD9CM:775.3', 'ICD9CM:775.4', 'ICD9CM:775.5', 'ICD9CM:775.6', 'ICD9CM:775.7', 'ICD9CM:775.8', 'ICD9CM:775.81', 'ICD9CM:775.89', 'ICD9CM:775.9', 'ICD9CM:776.0', 'ICD9CM:776.1', 'ICD9CM:776.2', 'ICD9CM:776.3', 'ICD9CM:776.4', 'ICD9CM:776.5', 'ICD9CM:776.6', 'ICD9CM:776.7', 'ICD9CM:776.8', 'ICD9CM:776.9', 'ICD9CM:777.1', 'ICD9CM:777.2', 'ICD9CM:777.3', 'ICD9CM:777.4', 'ICD9CM:777.5', 'ICD9CM:777.50', 'ICD9CM:777.51', 'ICD9CM:777.52', 'ICD9CM:777.53', 'ICD9CM:777.6', 'ICD9CM:777.8', 'ICD9CM:777.9', 'ICD9CM:778.0', 'ICD9CM:778.1', 'ICD9CM:778.2', 'ICD9CM:778.3', 'ICD9CM:778.4', 'ICD9CM:778.5', 'ICD9CM:778.6', 'ICD9CM:778.7', 'ICD9CM:778.8', 'ICD9CM:778.9', 'ICD9CM:779.0', 'ICD9CM:779.1', 'ICD9CM:779.2', 'ICD9CM:779.3', 'ICD9CM:779.31', 'ICD9CM:779.32', 'ICD9CM:779.33', 'ICD9CM:779.34', 'ICD9CM:779.4', 'ICD9CM:779.6', 'ICD9CM:779.7', 'ICD9CM:779.8', 'ICD9CM:779.81', 'ICD9CM:779.82', 'ICD9CM:779.83', 'ICD9CM:779.84', 'ICD9CM:779.85', 'ICD9CM:779.89', 'ICD9CM:779.9', 'ICD9CM:780.91', 'ICD9CM:780.92', 'ICD9CM:789.7', 'ICD9CM:V13.7', 'ICD9CM:V50.2'):
            results_ccs4["other_perinatal"].append(1)
        else: results_ccs4["other_perinatal"].append(0)
    print("Completed Binary Recode of: other_perinatal")

    # Joint_disorders_and_dislocations;_trauma-_related
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:716.10', 'ICD9CM:716.11', 'ICD9CM:716.12', 'ICD9CM:716.13', 'ICD9CM:716.14', 'ICD9CM:716.15', 'ICD9CM:716.16', 'ICD9CM:716.17', 'ICD9CM:716.18', 'ICD9CM:716.19', 'ICD9CM:717.0', 'ICD9CM:717.1', 'ICD9CM:717.2', 'ICD9CM:717.3', 'ICD9CM:717.40', 'ICD9CM:717.41', 'ICD9CM:717.42', 'ICD9CM:717.43', 'ICD9CM:717.49', 'ICD9CM:717.5', 'ICD9CM:717.6', 'ICD9CM:717.7', 'ICD9CM:717.81', 'ICD9CM:717.82', 'ICD9CM:717.83', 'ICD9CM:717.84', 'ICD9CM:717.85', 'ICD9CM:717.89', 'ICD9CM:717.9', 'ICD9CM:718.00', 'ICD9CM:718.01', 'ICD9CM:718.02', 'ICD9CM:718.03', 'ICD9CM:718.04', 'ICD9CM:718.05', 'ICD9CM:718.07', 'ICD9CM:718.08', 'ICD9CM:718.09', 'ICD9CM:718.30', 'ICD9CM:718.31', 'ICD9CM:718.32', 'ICD9CM:718.33', 'ICD9CM:718.34', 'ICD9CM:718.35', 'ICD9CM:718.36', 'ICD9CM:718.37', 'ICD9CM:718.38', 'ICD9CM:718.39', 'ICD9CM:830.0', 'ICD9CM:830.1', 'ICD9CM:831.00', 'ICD9CM:831.01', 'ICD9CM:831.02', 'ICD9CM:831.03', 'ICD9CM:831.04', 'ICD9CM:831.09', 'ICD9CM:831.10', 'ICD9CM:831.11', 'ICD9CM:831.12', 'ICD9CM:831.13', 'ICD9CM:831.14', 'ICD9CM:831.19', 'ICD9CM:832.00', 'ICD9CM:832.01', 'ICD9CM:832.02', 'ICD9CM:832.03', 'ICD9CM:832.04', 'ICD9CM:832.09', 'ICD9CM:832.10', 'ICD9CM:832.11', 'ICD9CM:832.12', 'ICD9CM:832.13', 'ICD9CM:832.14', 'ICD9CM:832.19', 'ICD9CM:832.2', 'ICD9CM:833.00', 'ICD9CM:833.01', 'ICD9CM:833.02', 'ICD9CM:833.03', 'ICD9CM:833.04', 'ICD9CM:833.05', 'ICD9CM:833.09', 'ICD9CM:833.10', 'ICD9CM:833.11', 'ICD9CM:833.12', 'ICD9CM:833.13', 'ICD9CM:833.14', 'ICD9CM:833.15', 'ICD9CM:833.19', 'ICD9CM:834.00', 'ICD9CM:834.01', 'ICD9CM:834.02', 'ICD9CM:834.10', 'ICD9CM:834.11', 'ICD9CM:834.12', 'ICD9CM:835.00', 'ICD9CM:835.01', 'ICD9CM:835.02', 'ICD9CM:835.03', 'ICD9CM:835.10', 'ICD9CM:835.11', 'ICD9CM:835.12', 'ICD9CM:835.13', 'ICD9CM:836.0', 'ICD9CM:836.1', 'ICD9CM:836.2', 'ICD9CM:836.3', 'ICD9CM:836.4', 'ICD9CM:836.50', 'ICD9CM:836.51', 'ICD9CM:836.52', 'ICD9CM:836.53', 'ICD9CM:836.54', 'ICD9CM:836.59', 'ICD9CM:836.60', 'ICD9CM:836.61', 'ICD9CM:836.62', 'ICD9CM:836.63', 'ICD9CM:836.64', 'ICD9CM:836.69', 'ICD9CM:837.0', 'ICD9CM:837.1', 'ICD9CM:838.00', 'ICD9CM:838.01', 'ICD9CM:838.02', 'ICD9CM:838.03', 'ICD9CM:838.04', 'ICD9CM:838.05', 'ICD9CM:838.06', 'ICD9CM:838.09', 'ICD9CM:838.10', 'ICD9CM:838.11', 'ICD9CM:838.12', 'ICD9CM:838.13', 'ICD9CM:838.14', 'ICD9CM:838.15', 'ICD9CM:838.16', 'ICD9CM:838.19', 'ICD9CM:839.00', 'ICD9CM:839.01', 'ICD9CM:839.02', 'ICD9CM:839.03', 'ICD9CM:839.04', 'ICD9CM:839.05', 'ICD9CM:839.06', 'ICD9CM:839.07', 'ICD9CM:839.08', 'ICD9CM:839.10', 'ICD9CM:839.11', 'ICD9CM:839.12', 'ICD9CM:839.13', 'ICD9CM:839.14', 'ICD9CM:839.15', 'ICD9CM:839.16', 'ICD9CM:839.17', 'ICD9CM:839.18', 'ICD9CM:839.20', 'ICD9CM:839.21', 'ICD9CM:839.30', 'ICD9CM:839.31', 'ICD9CM:839.40', 'ICD9CM:839.41', 'ICD9CM:839.42', 'ICD9CM:839.49', 'ICD9CM:839.50', 'ICD9CM:839.51', 'ICD9CM:839.52', 'ICD9CM:839.59', 'ICD9CM:839.61', 'ICD9CM:839.69', 'ICD9CM:839.71', 'ICD9CM:839.79', 'ICD9CM:839.8', 'ICD9CM:839.9', 'ICD9CM:905.6'):
            results_ccs4["joint_trauma"].append(1)
        else: results_ccs4["joint_trauma"].append(0)
    print("Completed Binary Recode of: joint_trauma")

    # Fracture_of_neck_of_femur_(_hip)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:820.00', 'ICD9CM:820.01', 'ICD9CM:820.02', 'ICD9CM:820.03', 'ICD9CM:820.09', 'ICD9CM:820.10', 'ICD9CM:820.11', 'ICD9CM:820.12', 'ICD9CM:820.13', 'ICD9CM:820.19', 'ICD9CM:820.20', 'ICD9CM:820.21', 'ICD9CM:820.22', 'ICD9CM:820.30', 'ICD9CM:820.31', 'ICD9CM:820.32', 'ICD9CM:820.8', 'ICD9CM:820.9', 'ICD9CM:905.3', 'ICD9CM:V54.13', 'ICD9CM:V54.23'):
            results_ccs4["fract_femur_neck"].append(1)
        else: results_ccs4["fract_femur_neck"].append(0)
    print("Completed Binary Recode of: fract_femur_neck")

    # Spinal_cord_injury
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:349.39', 'ICD9CM:806.00', 'ICD9CM:806.01', 'ICD9CM:806.02', 'ICD9CM:806.03', 'ICD9CM:806.04', 'ICD9CM:806.05', 'ICD9CM:806.06', 'ICD9CM:806.07', 'ICD9CM:806.08', 'ICD9CM:806.09', 'ICD9CM:806.10', 'ICD9CM:806.11', 'ICD9CM:806.12', 'ICD9CM:806.13', 'ICD9CM:806.14', 'ICD9CM:806.15', 'ICD9CM:806.16', 'ICD9CM:806.17', 'ICD9CM:806.18', 'ICD9CM:806.19', 'ICD9CM:806.20', 'ICD9CM:806.21', 'ICD9CM:806.22', 'ICD9CM:806.23', 'ICD9CM:806.24', 'ICD9CM:806.25', 'ICD9CM:806.26', 'ICD9CM:806.27', 'ICD9CM:806.28', 'ICD9CM:806.29', 'ICD9CM:806.30', 'ICD9CM:806.31', 'ICD9CM:806.32', 'ICD9CM:806.33', 'ICD9CM:806.34', 'ICD9CM:806.35', 'ICD9CM:806.36', 'ICD9CM:806.37', 'ICD9CM:806.38', 'ICD9CM:806.39', 'ICD9CM:806.4', 'ICD9CM:806.5', 'ICD9CM:806.60', 'ICD9CM:806.61', 'ICD9CM:806.62', 'ICD9CM:806.69', 'ICD9CM:806.70', 'ICD9CM:806.71', 'ICD9CM:806.72', 'ICD9CM:806.79', 'ICD9CM:806.8', 'ICD9CM:806.9', 'ICD9CM:907.2', 'ICD9CM:952.00', 'ICD9CM:952.01', 'ICD9CM:952.02', 'ICD9CM:952.03', 'ICD9CM:952.04', 'ICD9CM:952.05', 'ICD9CM:952.06', 'ICD9CM:952.07', 'ICD9CM:952.08', 'ICD9CM:952.09', 'ICD9CM:952.10', 'ICD9CM:952.11', 'ICD9CM:952.12', 'ICD9CM:952.13', 'ICD9CM:952.14', 'ICD9CM:952.15', 'ICD9CM:952.16', 'ICD9CM:952.17', 'ICD9CM:952.18', 'ICD9CM:952.19', 'ICD9CM:952.2', 'ICD9CM:952.3', 'ICD9CM:952.4', 'ICD9CM:952.8', 'ICD9CM:952.9'):
            results_ccs4["spinal_cord"].append(1)
        else: results_ccs4["spinal_cord"].append(0)
    print("Completed Binary Recode of: spinal_cord")

    # Skull_and_face_fractures
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:800.00', 'ICD9CM:800.01', 'ICD9CM:800.02', 'ICD9CM:800.03', 'ICD9CM:800.04', 'ICD9CM:800.05', 'ICD9CM:800.06', 'ICD9CM:800.09', 'ICD9CM:800.50', 'ICD9CM:800.51', 'ICD9CM:800.52', 'ICD9CM:800.53', 'ICD9CM:800.54', 'ICD9CM:800.55', 'ICD9CM:800.56', 'ICD9CM:800.59', 'ICD9CM:801.00', 'ICD9CM:801.01', 'ICD9CM:801.02', 'ICD9CM:801.03', 'ICD9CM:801.04', 'ICD9CM:801.05', 'ICD9CM:801.06', 'ICD9CM:801.09', 'ICD9CM:801.50', 'ICD9CM:801.51', 'ICD9CM:801.52', 'ICD9CM:801.53', 'ICD9CM:801.54', 'ICD9CM:801.55', 'ICD9CM:801.56', 'ICD9CM:801.59', 'ICD9CM:802.0', 'ICD9CM:802.1', 'ICD9CM:802.20', 'ICD9CM:802.21', 'ICD9CM:802.22', 'ICD9CM:802.23', 'ICD9CM:802.24', 'ICD9CM:802.25', 'ICD9CM:802.26', 'ICD9CM:802.27', 'ICD9CM:802.28', 'ICD9CM:802.29', 'ICD9CM:802.30', 'ICD9CM:802.31', 'ICD9CM:802.32', 'ICD9CM:802.33', 'ICD9CM:802.34', 'ICD9CM:802.35', 'ICD9CM:802.36', 'ICD9CM:802.37', 'ICD9CM:802.38', 'ICD9CM:802.39', 'ICD9CM:802.4', 'ICD9CM:802.5', 'ICD9CM:802.6', 'ICD9CM:802.7', 'ICD9CM:802.8', 'ICD9CM:802.9', 'ICD9CM:803.00', 'ICD9CM:803.01', 'ICD9CM:803.02', 'ICD9CM:803.03', 'ICD9CM:803.04', 'ICD9CM:803.05', 'ICD9CM:803.06', 'ICD9CM:803.09', 'ICD9CM:803.50', 'ICD9CM:803.51', 'ICD9CM:803.52', 'ICD9CM:803.53', 'ICD9CM:803.54', 'ICD9CM:803.55', 'ICD9CM:803.56', 'ICD9CM:803.59', 'ICD9CM:804.00', 'ICD9CM:804.01', 'ICD9CM:804.02', 'ICD9CM:804.03', 'ICD9CM:804.04', 'ICD9CM:804.05', 'ICD9CM:804.06', 'ICD9CM:804.09', 'ICD9CM:804.50', 'ICD9CM:804.51', 'ICD9CM:804.52', 'ICD9CM:804.53', 'ICD9CM:804.54', 'ICD9CM:804.55', 'ICD9CM:804.56', 'ICD9CM:804.59', 'ICD9CM:905.0'):
            results_ccs4["skull_face_fract"].append(1)
        else: results_ccs4["skull_face_fract"].append(0)
    print("Completed Binary Recode of: skull_face_fract")

    # Fracture_of_upper_limb
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:810.00', 'ICD9CM:810.01', 'ICD9CM:810.02', 'ICD9CM:810.03', 'ICD9CM:810.10', 'ICD9CM:810.11', 'ICD9CM:810.12', 'ICD9CM:810.13', 'ICD9CM:811.00', 'ICD9CM:811.01', 'ICD9CM:811.02', 'ICD9CM:811.03', 'ICD9CM:811.09', 'ICD9CM:811.10', 'ICD9CM:811.11', 'ICD9CM:811.12', 'ICD9CM:811.13', 'ICD9CM:811.19', 'ICD9CM:812.00', 'ICD9CM:812.01', 'ICD9CM:812.02', 'ICD9CM:812.03', 'ICD9CM:812.09', 'ICD9CM:812.10', 'ICD9CM:812.11', 'ICD9CM:812.12', 'ICD9CM:812.13', 'ICD9CM:812.19', 'ICD9CM:812.20', 'ICD9CM:812.21', 'ICD9CM:812.30', 'ICD9CM:812.31', 'ICD9CM:812.40', 'ICD9CM:812.41', 'ICD9CM:812.42', 'ICD9CM:812.43', 'ICD9CM:812.44', 'ICD9CM:812.49', 'ICD9CM:812.50', 'ICD9CM:812.51', 'ICD9CM:812.52', 'ICD9CM:812.53', 'ICD9CM:812.54', 'ICD9CM:812.59', 'ICD9CM:813.00', 'ICD9CM:813.01', 'ICD9CM:813.02', 'ICD9CM:813.03', 'ICD9CM:813.04', 'ICD9CM:813.05', 'ICD9CM:813.06', 'ICD9CM:813.07', 'ICD9CM:813.08', 'ICD9CM:813.10', 'ICD9CM:813.11', 'ICD9CM:813.12', 'ICD9CM:813.13', 'ICD9CM:813.14', 'ICD9CM:813.15', 'ICD9CM:813.16', 'ICD9CM:813.17', 'ICD9CM:813.18', 'ICD9CM:813.20', 'ICD9CM:813.21', 'ICD9CM:813.22', 'ICD9CM:813.23', 'ICD9CM:813.30', 'ICD9CM:813.31', 'ICD9CM:813.32', 'ICD9CM:813.33', 'ICD9CM:813.40', 'ICD9CM:813.41', 'ICD9CM:813.42', 'ICD9CM:813.43', 'ICD9CM:813.44', 'ICD9CM:813.45', 'ICD9CM:813.46', 'ICD9CM:813.47', 'ICD9CM:813.50', 'ICD9CM:813.51', 'ICD9CM:813.52', 'ICD9CM:813.53', 'ICD9CM:813.54', 'ICD9CM:813.80', 'ICD9CM:813.81', 'ICD9CM:813.82', 'ICD9CM:813.83', 'ICD9CM:813.90', 'ICD9CM:813.91', 'ICD9CM:813.92', 'ICD9CM:813.93', 'ICD9CM:814.00', 'ICD9CM:814.01', 'ICD9CM:814.02', 'ICD9CM:814.03', 'ICD9CM:814.04', 'ICD9CM:814.05', 'ICD9CM:814.06', 'ICD9CM:814.07', 'ICD9CM:814.08', 'ICD9CM:814.09', 'ICD9CM:814.10', 'ICD9CM:814.11', 'ICD9CM:814.12', 'ICD9CM:814.13', 'ICD9CM:814.14', 'ICD9CM:814.15', 'ICD9CM:814.16', 'ICD9CM:814.17', 'ICD9CM:814.18', 'ICD9CM:814.19', 'ICD9CM:815.00', 'ICD9CM:815.01', 'ICD9CM:815.02', 'ICD9CM:815.03', 'ICD9CM:815.04', 'ICD9CM:815.09', 'ICD9CM:815.10', 'ICD9CM:815.11', 'ICD9CM:815.12', 'ICD9CM:815.13', 'ICD9CM:815.14', 'ICD9CM:815.19', 'ICD9CM:816.00', 'ICD9CM:816.01', 'ICD9CM:816.02', 'ICD9CM:816.03', 'ICD9CM:816.10', 'ICD9CM:816.11', 'ICD9CM:816.12', 'ICD9CM:816.13', 'ICD9CM:817.0', 'ICD9CM:817.1', 'ICD9CM:818.0', 'ICD9CM:818.1', 'ICD9CM:819.0', 'ICD9CM:819.1', 'ICD9CM:905.2', 'ICD9CM:V54.10', 'ICD9CM:V54.11', 'ICD9CM:V54.12', 'ICD9CM:V54.20', 'ICD9CM:V54.21', 'ICD9CM:V54.22'):
            results_ccs4["upper_limb_fract"].append(1)
        else: results_ccs4["upper_limb_fract"].append(0)
    print("Completed Binary Recode of: upper_limb_fract")

    # Fracture_of_lower_limb
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:821.00', 'ICD9CM:821.01', 'ICD9CM:821.10', 'ICD9CM:821.11', 'ICD9CM:821.20', 'ICD9CM:821.21', 'ICD9CM:821.22', 'ICD9CM:821.23', 'ICD9CM:821.29', 'ICD9CM:821.30', 'ICD9CM:821.31', 'ICD9CM:821.32', 'ICD9CM:821.33', 'ICD9CM:821.39', 'ICD9CM:822.0', 'ICD9CM:822.1', 'ICD9CM:823.00', 'ICD9CM:823.01', 'ICD9CM:823.02', 'ICD9CM:823.10', 'ICD9CM:823.11', 'ICD9CM:823.12', 'ICD9CM:823.20', 'ICD9CM:823.21', 'ICD9CM:823.22', 'ICD9CM:823.30', 'ICD9CM:823.31', 'ICD9CM:823.32', 'ICD9CM:823.40', 'ICD9CM:823.41', 'ICD9CM:823.42', 'ICD9CM:823.80', 'ICD9CM:823.81', 'ICD9CM:823.82', 'ICD9CM:823.90', 'ICD9CM:823.91', 'ICD9CM:823.92', 'ICD9CM:824.0', 'ICD9CM:824.1', 'ICD9CM:824.2', 'ICD9CM:824.3', 'ICD9CM:824.4', 'ICD9CM:824.5', 'ICD9CM:824.6', 'ICD9CM:824.7', 'ICD9CM:824.8', 'ICD9CM:824.9', 'ICD9CM:825.0', 'ICD9CM:825.1', 'ICD9CM:825.20', 'ICD9CM:825.21', 'ICD9CM:825.22', 'ICD9CM:825.23', 'ICD9CM:825.24', 'ICD9CM:825.25', 'ICD9CM:825.29', 'ICD9CM:825.30', 'ICD9CM:825.31', 'ICD9CM:825.32', 'ICD9CM:825.33', 'ICD9CM:825.34', 'ICD9CM:825.35', 'ICD9CM:825.39', 'ICD9CM:826.0', 'ICD9CM:826.1', 'ICD9CM:827.0', 'ICD9CM:827.1', 'ICD9CM:905.4', 'ICD9CM:V54.14', 'ICD9CM:V54.15', 'ICD9CM:V54.16', 'ICD9CM:V54.24', 'ICD9CM:V54.25', 'ICD9CM:V54.26'):
            results_ccs4["lower_limb_fract"].append(1)
        else: results_ccs4["lower_limb_fract"].append(0)
    print("Completed Binary Recode of: lower_limb_fract")

    # Other_fractures
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:805.00', 'ICD9CM:805.01', 'ICD9CM:805.02', 'ICD9CM:805.03', 'ICD9CM:805.04', 'ICD9CM:805.05', 'ICD9CM:805.06', 'ICD9CM:805.07', 'ICD9CM:805.08', 'ICD9CM:805.10', 'ICD9CM:805.11', 'ICD9CM:805.12', 'ICD9CM:805.13', 'ICD9CM:805.14', 'ICD9CM:805.15', 'ICD9CM:805.16', 'ICD9CM:805.17', 'ICD9CM:805.18', 'ICD9CM:805.2', 'ICD9CM:805.3', 'ICD9CM:805.4', 'ICD9CM:805.5', 'ICD9CM:805.6', 'ICD9CM:805.7', 'ICD9CM:805.8', 'ICD9CM:805.9', 'ICD9CM:807.00', 'ICD9CM:807.01', 'ICD9CM:807.02', 'ICD9CM:807.03', 'ICD9CM:807.04', 'ICD9CM:807.05', 'ICD9CM:807.06', 'ICD9CM:807.07', 'ICD9CM:807.08', 'ICD9CM:807.09', 'ICD9CM:807.10', 'ICD9CM:807.11', 'ICD9CM:807.12', 'ICD9CM:807.13', 'ICD9CM:807.14', 'ICD9CM:807.15', 'ICD9CM:807.16', 'ICD9CM:807.17', 'ICD9CM:807.18', 'ICD9CM:807.19', 'ICD9CM:807.2', 'ICD9CM:807.3', 'ICD9CM:807.4', 'ICD9CM:807.5', 'ICD9CM:807.6', 'ICD9CM:808.0', 'ICD9CM:808.1', 'ICD9CM:808.2', 'ICD9CM:808.3', 'ICD9CM:808.41', 'ICD9CM:808.42', 'ICD9CM:808.43', 'ICD9CM:808.44', 'ICD9CM:808.49', 'ICD9CM:808.51', 'ICD9CM:808.52', 'ICD9CM:808.53', 'ICD9CM:808.54', 'ICD9CM:808.59', 'ICD9CM:808.8', 'ICD9CM:808.9', 'ICD9CM:809.0', 'ICD9CM:809.1', 'ICD9CM:828.0', 'ICD9CM:828.1', 'ICD9CM:829.0', 'ICD9CM:829.1', 'ICD9CM:905.1', 'ICD9CM:905.5', 'ICD9CM:V13.52', 'ICD9CM:V54.0', 'ICD9CM:V54.01', 'ICD9CM:V54.02', 'ICD9CM:V54.09', 'ICD9CM:V54.17', 'ICD9CM:V54.19', 'ICD9CM:V54.27', 'ICD9CM:V54.29', 'ICD9CM:V66.4', 'ICD9CM:V67.4'):
            results_ccs4["other_fract"].append(1)
        else: results_ccs4["other_fract"].append(0)
    print("Completed Binary Recode of: other_fract")

    # Sprains_and_strains
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:840.0', 'ICD9CM:840.1', 'ICD9CM:840.2', 'ICD9CM:840.3', 'ICD9CM:840.4', 'ICD9CM:840.5', 'ICD9CM:840.6', 'ICD9CM:840.7', 'ICD9CM:840.8', 'ICD9CM:840.9', 'ICD9CM:841.0', 'ICD9CM:841.1', 'ICD9CM:841.2', 'ICD9CM:841.3', 'ICD9CM:841.8', 'ICD9CM:841.9', 'ICD9CM:842.00', 'ICD9CM:842.01', 'ICD9CM:842.02', 'ICD9CM:842.09', 'ICD9CM:842.10', 'ICD9CM:842.11', 'ICD9CM:842.12', 'ICD9CM:842.13', 'ICD9CM:842.19', 'ICD9CM:843.0', 'ICD9CM:843.1', 'ICD9CM:843.8', 'ICD9CM:843.9', 'ICD9CM:844.0', 'ICD9CM:844.1', 'ICD9CM:844.2', 'ICD9CM:844.3', 'ICD9CM:844.8', 'ICD9CM:844.9', 'ICD9CM:845.00', 'ICD9CM:845.01', 'ICD9CM:845.02', 'ICD9CM:845.03', 'ICD9CM:845.09', 'ICD9CM:845.10', 'ICD9CM:845.11', 'ICD9CM:845.12', 'ICD9CM:845.13', 'ICD9CM:845.19', 'ICD9CM:846.0', 'ICD9CM:846.1', 'ICD9CM:846.2', 'ICD9CM:846.3', 'ICD9CM:846.8', 'ICD9CM:846.9', 'ICD9CM:847.0', 'ICD9CM:847.1', 'ICD9CM:847.2', 'ICD9CM:847.3', 'ICD9CM:847.4', 'ICD9CM:847.9', 'ICD9CM:848.0', 'ICD9CM:848.1', 'ICD9CM:848.2', 'ICD9CM:848.3', 'ICD9CM:848.40', 'ICD9CM:848.41', 'ICD9CM:848.42', 'ICD9CM:848.49', 'ICD9CM:848.5', 'ICD9CM:848.8', 'ICD9CM:848.9', 'ICD9CM:905.7'):
            results_ccs4["sprain_strain"].append(1)
        else: results_ccs4["sprain_strain"].append(0)
    print("Completed Binary Recode of: sprain_strain")

    # Intracranial_injury
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:800.10', 'ICD9CM:800.11', 'ICD9CM:800.12', 'ICD9CM:800.13', 'ICD9CM:800.14', 'ICD9CM:800.15', 'ICD9CM:800.16', 'ICD9CM:800.19', 'ICD9CM:800.20', 'ICD9CM:800.21', 'ICD9CM:800.22', 'ICD9CM:800.23', 'ICD9CM:800.24', 'ICD9CM:800.25', 'ICD9CM:800.26', 'ICD9CM:800.29', 'ICD9CM:800.30', 'ICD9CM:800.31', 'ICD9CM:800.32', 'ICD9CM:800.33', 'ICD9CM:800.34', 'ICD9CM:800.35', 'ICD9CM:800.36', 'ICD9CM:800.39', 'ICD9CM:800.40', 'ICD9CM:800.41', 'ICD9CM:800.42', 'ICD9CM:800.43', 'ICD9CM:800.44', 'ICD9CM:800.45', 'ICD9CM:800.46', 'ICD9CM:800.49', 'ICD9CM:800.60', 'ICD9CM:800.61', 'ICD9CM:800.62', 'ICD9CM:800.63', 'ICD9CM:800.64', 'ICD9CM:800.65', 'ICD9CM:800.66', 'ICD9CM:800.69', 'ICD9CM:800.70', 'ICD9CM:800.71', 'ICD9CM:800.72', 'ICD9CM:800.73', 'ICD9CM:800.74', 'ICD9CM:800.75', 'ICD9CM:800.76', 'ICD9CM:800.79', 'ICD9CM:800.80', 'ICD9CM:800.81', 'ICD9CM:800.82', 'ICD9CM:800.83', 'ICD9CM:800.84', 'ICD9CM:800.85', 'ICD9CM:800.86', 'ICD9CM:800.89', 'ICD9CM:800.90', 'ICD9CM:800.91', 'ICD9CM:800.92', 'ICD9CM:800.93', 'ICD9CM:800.94', 'ICD9CM:800.95', 'ICD9CM:800.96', 'ICD9CM:800.99', 'ICD9CM:801.10', 'ICD9CM:801.11', 'ICD9CM:801.12', 'ICD9CM:801.13', 'ICD9CM:801.14', 'ICD9CM:801.15', 'ICD9CM:801.16', 'ICD9CM:801.19', 'ICD9CM:801.20', 'ICD9CM:801.21', 'ICD9CM:801.22', 'ICD9CM:801.23', 'ICD9CM:801.24', 'ICD9CM:801.25', 'ICD9CM:801.26', 'ICD9CM:801.29', 'ICD9CM:801.30', 'ICD9CM:801.31', 'ICD9CM:801.32', 'ICD9CM:801.33', 'ICD9CM:801.34', 'ICD9CM:801.35', 'ICD9CM:801.36', 'ICD9CM:801.39', 'ICD9CM:801.40', 'ICD9CM:801.41', 'ICD9CM:801.42', 'ICD9CM:801.43', 'ICD9CM:801.44', 'ICD9CM:801.45', 'ICD9CM:801.46', 'ICD9CM:801.49', 'ICD9CM:801.60', 'ICD9CM:801.61', 'ICD9CM:801.62', 'ICD9CM:801.63', 'ICD9CM:801.64', 'ICD9CM:801.65', 'ICD9CM:801.66', 'ICD9CM:801.69', 'ICD9CM:801.70', 'ICD9CM:801.71', 'ICD9CM:801.72', 'ICD9CM:801.73', 'ICD9CM:801.74', 'ICD9CM:801.75', 'ICD9CM:801.76', 'ICD9CM:801.79', 'ICD9CM:801.80', 'ICD9CM:801.81', 'ICD9CM:801.82', 'ICD9CM:801.83', 'ICD9CM:801.84', 'ICD9CM:801.85', 'ICD9CM:801.86', 'ICD9CM:801.89', 'ICD9CM:801.90', 'ICD9CM:801.91', 'ICD9CM:801.92', 'ICD9CM:801.93', 'ICD9CM:801.94', 'ICD9CM:801.95', 'ICD9CM:801.96', 'ICD9CM:801.99', 'ICD9CM:803.10', 'ICD9CM:803.11', 'ICD9CM:803.12', 'ICD9CM:803.13', 'ICD9CM:803.14', 'ICD9CM:803.15', 'ICD9CM:803.16', 'ICD9CM:803.19', 'ICD9CM:803.20', 'ICD9CM:803.21', 'ICD9CM:803.22', 'ICD9CM:803.23', 'ICD9CM:803.24', 'ICD9CM:803.25', 'ICD9CM:803.26', 'ICD9CM:803.29', 'ICD9CM:803.30', 'ICD9CM:803.31', 'ICD9CM:803.32', 'ICD9CM:803.33', 'ICD9CM:803.34', 'ICD9CM:803.35', 'ICD9CM:803.36', 'ICD9CM:803.39', 'ICD9CM:803.40', 'ICD9CM:803.41', 'ICD9CM:803.42', 'ICD9CM:803.43', 'ICD9CM:803.44', 'ICD9CM:803.45', 'ICD9CM:803.46', 'ICD9CM:803.49', 'ICD9CM:803.60', 'ICD9CM:803.61', 'ICD9CM:803.62', 'ICD9CM:803.63', 'ICD9CM:803.64', 'ICD9CM:803.65', 'ICD9CM:803.66', 'ICD9CM:803.69', 'ICD9CM:803.70', 'ICD9CM:803.71', 'ICD9CM:803.72', 'ICD9CM:803.73', 'ICD9CM:803.74', 'ICD9CM:803.75', 'ICD9CM:803.76', 'ICD9CM:803.79', 'ICD9CM:803.80', 'ICD9CM:803.81', 'ICD9CM:803.82', 'ICD9CM:803.83', 'ICD9CM:803.84', 'ICD9CM:803.85', 'ICD9CM:803.86', 'ICD9CM:803.89', 'ICD9CM:803.90', 'ICD9CM:803.91', 'ICD9CM:803.92', 'ICD9CM:803.93', 'ICD9CM:803.94', 'ICD9CM:803.95', 'ICD9CM:803.96', 'ICD9CM:803.99', 'ICD9CM:804.10', 'ICD9CM:804.11', 'ICD9CM:804.12', 'ICD9CM:804.13', 'ICD9CM:804.14', 'ICD9CM:804.15', 'ICD9CM:804.16', 'ICD9CM:804.19', 'ICD9CM:804.20', 'ICD9CM:804.21', 'ICD9CM:804.22', 'ICD9CM:804.23', 'ICD9CM:804.24', 'ICD9CM:804.25', 'ICD9CM:804.26', 'ICD9CM:804.29', 'ICD9CM:804.30', 'ICD9CM:804.31', 'ICD9CM:804.32', 'ICD9CM:804.33', 'ICD9CM:804.34', 'ICD9CM:804.35', 'ICD9CM:804.36', 'ICD9CM:804.39', 'ICD9CM:804.40', 'ICD9CM:804.41', 'ICD9CM:804.42', 'ICD9CM:804.43', 'ICD9CM:804.44', 'ICD9CM:804.45', 'ICD9CM:804.46', 'ICD9CM:804.49', 'ICD9CM:804.60', 'ICD9CM:804.61', 'ICD9CM:804.62', 'ICD9CM:804.63', 'ICD9CM:804.64', 'ICD9CM:804.65', 'ICD9CM:804.66', 'ICD9CM:804.69', 'ICD9CM:804.70', 'ICD9CM:804.71', 'ICD9CM:804.72', 'ICD9CM:804.73', 'ICD9CM:804.74', 'ICD9CM:804.75', 'ICD9CM:804.76', 'ICD9CM:804.79', 'ICD9CM:804.80', 'ICD9CM:804.81', 'ICD9CM:804.82', 'ICD9CM:804.83', 'ICD9CM:804.84', 'ICD9CM:804.85', 'ICD9CM:804.86', 'ICD9CM:804.89', 'ICD9CM:804.90', 'ICD9CM:804.91', 'ICD9CM:804.92', 'ICD9CM:804.93', 'ICD9CM:804.94', 'ICD9CM:804.95', 'ICD9CM:804.96', 'ICD9CM:804.99', 'ICD9CM:850.0', 'ICD9CM:850.1', 'ICD9CM:850.11', 'ICD9CM:850.12', 'ICD9CM:850.2', 'ICD9CM:850.3', 'ICD9CM:850.4', 'ICD9CM:850.5', 'ICD9CM:850.9', 'ICD9CM:851.00', 'ICD9CM:851.01', 'ICD9CM:851.02', 'ICD9CM:851.03', 'ICD9CM:851.04', 'ICD9CM:851.05', 'ICD9CM:851.06', 'ICD9CM:851.09', 'ICD9CM:851.10', 'ICD9CM:851.11', 'ICD9CM:851.12', 'ICD9CM:851.13', 'ICD9CM:851.14', 'ICD9CM:851.15', 'ICD9CM:851.16', 'ICD9CM:851.19', 'ICD9CM:851.20', 'ICD9CM:851.21', 'ICD9CM:851.22', 'ICD9CM:851.23', 'ICD9CM:851.24', 'ICD9CM:851.25', 'ICD9CM:851.26', 'ICD9CM:851.29', 'ICD9CM:851.30', 'ICD9CM:851.31', 'ICD9CM:851.32', 'ICD9CM:851.33', 'ICD9CM:851.34', 'ICD9CM:851.35', 'ICD9CM:851.36', 'ICD9CM:851.39', 'ICD9CM:851.40', 'ICD9CM:851.41', 'ICD9CM:851.42', 'ICD9CM:851.43', 'ICD9CM:851.44', 'ICD9CM:851.45', 'ICD9CM:851.46', 'ICD9CM:851.49', 'ICD9CM:851.50', 'ICD9CM:851.51', 'ICD9CM:851.52', 'ICD9CM:851.53', 'ICD9CM:851.54', 'ICD9CM:851.55', 'ICD9CM:851.56', 'ICD9CM:851.59', 'ICD9CM:851.60', 'ICD9CM:851.61', 'ICD9CM:851.62', 'ICD9CM:851.63', 'ICD9CM:851.64', 'ICD9CM:851.65', 'ICD9CM:851.66', 'ICD9CM:851.69', 'ICD9CM:851.70', 'ICD9CM:851.71', 'ICD9CM:851.72', 'ICD9CM:851.73', 'ICD9CM:851.74', 'ICD9CM:851.75', 'ICD9CM:851.76', 'ICD9CM:851.79', 'ICD9CM:851.80', 'ICD9CM:851.81', 'ICD9CM:851.82', 'ICD9CM:851.83', 'ICD9CM:851.84', 'ICD9CM:851.85', 'ICD9CM:851.86', 'ICD9CM:851.89', 'ICD9CM:851.90', 'ICD9CM:851.91', 'ICD9CM:851.92', 'ICD9CM:851.93', 'ICD9CM:851.94', 'ICD9CM:851.95', 'ICD9CM:851.96', 'ICD9CM:851.99', 'ICD9CM:852.00', 'ICD9CM:852.01', 'ICD9CM:852.02', 'ICD9CM:852.03', 'ICD9CM:852.04', 'ICD9CM:852.05', 'ICD9CM:852.06', 'ICD9CM:852.09', 'ICD9CM:852.10', 'ICD9CM:852.11', 'ICD9CM:852.12', 'ICD9CM:852.13', 'ICD9CM:852.14', 'ICD9CM:852.15', 'ICD9CM:852.16', 'ICD9CM:852.19', 'ICD9CM:852.20', 'ICD9CM:852.21', 'ICD9CM:852.22', 'ICD9CM:852.23', 'ICD9CM:852.24', 'ICD9CM:852.25', 'ICD9CM:852.26', 'ICD9CM:852.29', 'ICD9CM:852.30', 'ICD9CM:852.31', 'ICD9CM:852.32', 'ICD9CM:852.33', 'ICD9CM:852.34', 'ICD9CM:852.35', 'ICD9CM:852.36', 'ICD9CM:852.39', 'ICD9CM:852.40', 'ICD9CM:852.41', 'ICD9CM:852.42', 'ICD9CM:852.43', 'ICD9CM:852.44', 'ICD9CM:852.45', 'ICD9CM:852.46', 'ICD9CM:852.49', 'ICD9CM:852.50', 'ICD9CM:852.51', 'ICD9CM:852.52', 'ICD9CM:852.53', 'ICD9CM:852.54', 'ICD9CM:852.55', 'ICD9CM:852.56', 'ICD9CM:852.59', 'ICD9CM:853.00', 'ICD9CM:853.01', 'ICD9CM:853.02', 'ICD9CM:853.03', 'ICD9CM:853.04', 'ICD9CM:853.05', 'ICD9CM:853.06', 'ICD9CM:853.09', 'ICD9CM:853.10', 'ICD9CM:853.11', 'ICD9CM:853.12', 'ICD9CM:853.13', 'ICD9CM:853.14', 'ICD9CM:853.15', 'ICD9CM:853.16', 'ICD9CM:853.19', 'ICD9CM:854.00', 'ICD9CM:854.01', 'ICD9CM:854.02', 'ICD9CM:854.03', 'ICD9CM:854.04', 'ICD9CM:854.05', 'ICD9CM:854.06', 'ICD9CM:854.09', 'ICD9CM:854.10', 'ICD9CM:854.11', 'ICD9CM:854.12', 'ICD9CM:854.13', 'ICD9CM:854.14', 'ICD9CM:854.15', 'ICD9CM:854.16', 'ICD9CM:854.19', 'ICD9CM:907.0', 'ICD9CM:V15.52'):
            results_ccs4["intracranial"].append(1)
        else: results_ccs4["intracranial"].append(0)
    print("Completed Binary Recode of: intracranial")

    # Crushing_injury_or_internal_injury
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:860.0', 'ICD9CM:860.1', 'ICD9CM:860.2', 'ICD9CM:860.3', 'ICD9CM:860.4', 'ICD9CM:860.5', 'ICD9CM:861.00', 'ICD9CM:861.01', 'ICD9CM:861.02', 'ICD9CM:861.03', 'ICD9CM:861.10', 'ICD9CM:861.11', 'ICD9CM:861.12', 'ICD9CM:861.13', 'ICD9CM:861.20', 'ICD9CM:861.21', 'ICD9CM:861.22', 'ICD9CM:861.30', 'ICD9CM:861.31', 'ICD9CM:861.32', 'ICD9CM:862.0', 'ICD9CM:862.1', 'ICD9CM:862.21', 'ICD9CM:862.22', 'ICD9CM:862.29', 'ICD9CM:862.31', 'ICD9CM:862.32', 'ICD9CM:862.39', 'ICD9CM:862.8', 'ICD9CM:862.9', 'ICD9CM:863.0', 'ICD9CM:863.1', 'ICD9CM:863.20', 'ICD9CM:863.21', 'ICD9CM:863.29', 'ICD9CM:863.30', 'ICD9CM:863.31', 'ICD9CM:863.39', 'ICD9CM:863.40', 'ICD9CM:863.41', 'ICD9CM:863.42', 'ICD9CM:863.43', 'ICD9CM:863.44', 'ICD9CM:863.45', 'ICD9CM:863.46', 'ICD9CM:863.49', 'ICD9CM:863.50', 'ICD9CM:863.51', 'ICD9CM:863.52', 'ICD9CM:863.53', 'ICD9CM:863.54', 'ICD9CM:863.55', 'ICD9CM:863.56', 'ICD9CM:863.59', 'ICD9CM:863.80', 'ICD9CM:863.81', 'ICD9CM:863.82', 'ICD9CM:863.83', 'ICD9CM:863.84', 'ICD9CM:863.85', 'ICD9CM:863.89', 'ICD9CM:863.90', 'ICD9CM:863.91', 'ICD9CM:863.92', 'ICD9CM:863.93', 'ICD9CM:863.94', 'ICD9CM:863.95', 'ICD9CM:863.99', 'ICD9CM:864.00', 'ICD9CM:864.01', 'ICD9CM:864.02', 'ICD9CM:864.03', 'ICD9CM:864.04', 'ICD9CM:864.05', 'ICD9CM:864.09', 'ICD9CM:864.10', 'ICD9CM:864.11', 'ICD9CM:864.12', 'ICD9CM:864.13', 'ICD9CM:864.14', 'ICD9CM:864.15', 'ICD9CM:864.19', 'ICD9CM:865.00', 'ICD9CM:865.01', 'ICD9CM:865.02', 'ICD9CM:865.03', 'ICD9CM:865.04', 'ICD9CM:865.09', 'ICD9CM:865.10', 'ICD9CM:865.11', 'ICD9CM:865.12', 'ICD9CM:865.13', 'ICD9CM:865.14', 'ICD9CM:865.19', 'ICD9CM:866.00', 'ICD9CM:866.01', 'ICD9CM:866.02', 'ICD9CM:866.03', 'ICD9CM:866.10', 'ICD9CM:866.11', 'ICD9CM:866.12', 'ICD9CM:866.13', 'ICD9CM:867.0', 'ICD9CM:867.1', 'ICD9CM:867.2', 'ICD9CM:867.3', 'ICD9CM:867.4', 'ICD9CM:867.5', 'ICD9CM:867.6', 'ICD9CM:867.7', 'ICD9CM:867.8', 'ICD9CM:867.9', 'ICD9CM:868.00', 'ICD9CM:868.01', 'ICD9CM:868.02', 'ICD9CM:868.03', 'ICD9CM:868.04', 'ICD9CM:868.09', 'ICD9CM:868.10', 'ICD9CM:868.11', 'ICD9CM:868.12', 'ICD9CM:868.13', 'ICD9CM:868.14', 'ICD9CM:868.19', 'ICD9CM:869.0', 'ICD9CM:869.1', 'ICD9CM:900.00', 'ICD9CM:900.01', 'ICD9CM:900.02', 'ICD9CM:900.03', 'ICD9CM:900.1', 'ICD9CM:900.81', 'ICD9CM:900.82', 'ICD9CM:900.89', 'ICD9CM:900.9', 'ICD9CM:901.0', 'ICD9CM:901.1', 'ICD9CM:901.2', 'ICD9CM:901.3', 'ICD9CM:901.40', 'ICD9CM:901.41', 'ICD9CM:901.42', 'ICD9CM:901.81', 'ICD9CM:901.82', 'ICD9CM:901.83', 'ICD9CM:901.89', 'ICD9CM:901.9', 'ICD9CM:902.0', 'ICD9CM:902.10', 'ICD9CM:902.11', 'ICD9CM:902.19', 'ICD9CM:902.20', 'ICD9CM:902.21', 'ICD9CM:902.22', 'ICD9CM:902.23', 'ICD9CM:902.24', 'ICD9CM:902.25', 'ICD9CM:902.26', 'ICD9CM:902.27', 'ICD9CM:902.29', 'ICD9CM:902.31', 'ICD9CM:902.32', 'ICD9CM:902.33', 'ICD9CM:902.34', 'ICD9CM:902.39', 'ICD9CM:902.40', 'ICD9CM:902.41', 'ICD9CM:902.42', 'ICD9CM:902.49', 'ICD9CM:902.50', 'ICD9CM:902.51', 'ICD9CM:902.52', 'ICD9CM:902.53', 'ICD9CM:902.54', 'ICD9CM:902.55', 'ICD9CM:902.56', 'ICD9CM:902.59', 'ICD9CM:902.81', 'ICD9CM:902.82', 'ICD9CM:902.87', 'ICD9CM:902.89', 'ICD9CM:902.9', 'ICD9CM:903.00', 'ICD9CM:903.01', 'ICD9CM:903.02', 'ICD9CM:903.1', 'ICD9CM:903.2', 'ICD9CM:903.3', 'ICD9CM:903.4', 'ICD9CM:903.5', 'ICD9CM:903.8', 'ICD9CM:903.9', 'ICD9CM:904.0', 'ICD9CM:904.1', 'ICD9CM:904.2', 'ICD9CM:904.3', 'ICD9CM:904.40', 'ICD9CM:904.41', 'ICD9CM:904.42', 'ICD9CM:904.50', 'ICD9CM:904.51', 'ICD9CM:904.52', 'ICD9CM:904.53', 'ICD9CM:904.54', 'ICD9CM:904.6', 'ICD9CM:904.7', 'ICD9CM:904.8', 'ICD9CM:904.9', 'ICD9CM:906.4', 'ICD9CM:908.0', 'ICD9CM:908.1', 'ICD9CM:908.2', 'ICD9CM:908.3', 'ICD9CM:908.4', 'ICD9CM:925', 'ICD9CM:925.1', 'ICD9CM:925.2', 'ICD9CM:926.0', 'ICD9CM:926.11', 'ICD9CM:926.12', 'ICD9CM:926.19', 'ICD9CM:926.8', 'ICD9CM:926.9', 'ICD9CM:927.00', 'ICD9CM:927.01', 'ICD9CM:927.02', 'ICD9CM:927.03', 'ICD9CM:927.09', 'ICD9CM:927.10', 'ICD9CM:927.11', 'ICD9CM:927.20', 'ICD9CM:927.21', 'ICD9CM:927.3', 'ICD9CM:927.8', 'ICD9CM:927.9', 'ICD9CM:928.00', 'ICD9CM:928.01', 'ICD9CM:928.10', 'ICD9CM:928.11', 'ICD9CM:928.20', 'ICD9CM:928.21', 'ICD9CM:928.3', 'ICD9CM:928.8', 'ICD9CM:928.9', 'ICD9CM:929.0', 'ICD9CM:929.9'):
            results_ccs4["crush_injury"].append(1)
        else: results_ccs4["crush_injury"].append(0)
    print("Completed Binary Recode of: crush_injury")

    # Open_wounds_of_head;_neck;_and_trunk
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:870.0', 'ICD9CM:870.1', 'ICD9CM:870.2', 'ICD9CM:870.3', 'ICD9CM:870.4', 'ICD9CM:870.8', 'ICD9CM:870.9', 'ICD9CM:871.0', 'ICD9CM:871.1', 'ICD9CM:871.2', 'ICD9CM:871.3', 'ICD9CM:871.4', 'ICD9CM:871.5', 'ICD9CM:871.6', 'ICD9CM:871.7', 'ICD9CM:871.9', 'ICD9CM:872.00', 'ICD9CM:872.01', 'ICD9CM:872.02', 'ICD9CM:872.10', 'ICD9CM:872.11', 'ICD9CM:872.12', 'ICD9CM:872.61', 'ICD9CM:872.62', 'ICD9CM:872.63', 'ICD9CM:872.64', 'ICD9CM:872.69', 'ICD9CM:872.71', 'ICD9CM:872.72', 'ICD9CM:872.73', 'ICD9CM:872.74', 'ICD9CM:872.79', 'ICD9CM:872.8', 'ICD9CM:872.9', 'ICD9CM:873.0', 'ICD9CM:873.1', 'ICD9CM:873.20', 'ICD9CM:873.21', 'ICD9CM:873.22', 'ICD9CM:873.23', 'ICD9CM:873.29', 'ICD9CM:873.30', 'ICD9CM:873.31', 'ICD9CM:873.32', 'ICD9CM:873.33', 'ICD9CM:873.39', 'ICD9CM:873.40', 'ICD9CM:873.41', 'ICD9CM:873.42', 'ICD9CM:873.43', 'ICD9CM:873.44', 'ICD9CM:873.49', 'ICD9CM:873.50', 'ICD9CM:873.51', 'ICD9CM:873.52', 'ICD9CM:873.53', 'ICD9CM:873.54', 'ICD9CM:873.59', 'ICD9CM:873.60', 'ICD9CM:873.61', 'ICD9CM:873.62', 'ICD9CM:873.63', 'ICD9CM:873.64', 'ICD9CM:873.65', 'ICD9CM:873.69', 'ICD9CM:873.70', 'ICD9CM:873.71', 'ICD9CM:873.72', 'ICD9CM:873.73', 'ICD9CM:873.74', 'ICD9CM:873.75', 'ICD9CM:873.79', 'ICD9CM:873.8', 'ICD9CM:873.9', 'ICD9CM:874.00', 'ICD9CM:874.01', 'ICD9CM:874.02', 'ICD9CM:874.10', 'ICD9CM:874.11', 'ICD9CM:874.12', 'ICD9CM:874.2', 'ICD9CM:874.3', 'ICD9CM:874.4', 'ICD9CM:874.5', 'ICD9CM:874.8', 'ICD9CM:874.9', 'ICD9CM:875.0', 'ICD9CM:875.1', 'ICD9CM:876.0', 'ICD9CM:876.1', 'ICD9CM:877.0', 'ICD9CM:877.1', 'ICD9CM:878.0', 'ICD9CM:878.1', 'ICD9CM:878.2', 'ICD9CM:878.3', 'ICD9CM:878.4', 'ICD9CM:878.5', 'ICD9CM:878.6', 'ICD9CM:878.7', 'ICD9CM:878.8', 'ICD9CM:878.9', 'ICD9CM:879.0', 'ICD9CM:879.1', 'ICD9CM:879.2', 'ICD9CM:879.3', 'ICD9CM:879.4', 'ICD9CM:879.5', 'ICD9CM:879.6', 'ICD9CM:879.7', 'ICD9CM:879.8', 'ICD9CM:879.9', 'ICD9CM:906.0'):
            results_ccs4["open_wound_head"].append(1)
        else: results_ccs4["open_wound_head"].append(0)
    print("Completed Binary Recode of: open_wound_head")

    # Open_wounds_of_extremities
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:880.00', 'ICD9CM:880.01', 'ICD9CM:880.02', 'ICD9CM:880.03', 'ICD9CM:880.09', 'ICD9CM:880.10', 'ICD9CM:880.11', 'ICD9CM:880.12', 'ICD9CM:880.13', 'ICD9CM:880.19', 'ICD9CM:880.20', 'ICD9CM:880.21', 'ICD9CM:880.22', 'ICD9CM:880.23', 'ICD9CM:880.29', 'ICD9CM:881.00', 'ICD9CM:881.01', 'ICD9CM:881.02', 'ICD9CM:881.10', 'ICD9CM:881.11', 'ICD9CM:881.12', 'ICD9CM:881.20', 'ICD9CM:881.21', 'ICD9CM:881.22', 'ICD9CM:882.0', 'ICD9CM:882.1', 'ICD9CM:882.2', 'ICD9CM:883.0', 'ICD9CM:883.1', 'ICD9CM:883.2', 'ICD9CM:884.0', 'ICD9CM:884.1', 'ICD9CM:884.2', 'ICD9CM:885.0', 'ICD9CM:885.1', 'ICD9CM:886.0', 'ICD9CM:886.1', 'ICD9CM:887.0', 'ICD9CM:887.1', 'ICD9CM:887.2', 'ICD9CM:887.3', 'ICD9CM:887.4', 'ICD9CM:887.5', 'ICD9CM:887.6', 'ICD9CM:887.7', 'ICD9CM:890.0', 'ICD9CM:890.1', 'ICD9CM:890.2', 'ICD9CM:891.0', 'ICD9CM:891.1', 'ICD9CM:891.2', 'ICD9CM:892.0', 'ICD9CM:892.1', 'ICD9CM:892.2', 'ICD9CM:893.0', 'ICD9CM:893.1', 'ICD9CM:893.2', 'ICD9CM:894.0', 'ICD9CM:894.1', 'ICD9CM:894.2', 'ICD9CM:895.0', 'ICD9CM:895.1', 'ICD9CM:896.0', 'ICD9CM:896.1', 'ICD9CM:896.2', 'ICD9CM:896.3', 'ICD9CM:897.0', 'ICD9CM:897.1', 'ICD9CM:897.2', 'ICD9CM:897.3', 'ICD9CM:897.4', 'ICD9CM:897.5', 'ICD9CM:897.6', 'ICD9CM:897.7', 'ICD9CM:905.8', 'ICD9CM:905.9', 'ICD9CM:906.1'):
            results_ccs4["open_wound_extr"].append(1)
        else: results_ccs4["open_wound_extr"].append(0)
    print("Completed Binary Recode of: open_wound_extr")

    # Complication_of_device;_implant_or_graft
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:279.50', 'ICD9CM:279.51', 'ICD9CM:279.52', 'ICD9CM:279.53', 'ICD9CM:414.02', 'ICD9CM:414.03', 'ICD9CM:414.04', 'ICD9CM:414.05', 'ICD9CM:414.07', 'ICD9CM:440.30', 'ICD9CM:440.31', 'ICD9CM:440.32', 'ICD9CM:569.60', 'ICD9CM:569.61', 'ICD9CM:569.69', 'ICD9CM:596.82', 'ICD9CM:596.83', 'ICD9CM:629.31', 'ICD9CM:629.32', 'ICD9CM:996.00', 'ICD9CM:996.01', 'ICD9CM:996.02', 'ICD9CM:996.03', 'ICD9CM:996.04', 'ICD9CM:996.09', 'ICD9CM:996.1', 'ICD9CM:996.2', 'ICD9CM:996.30', 'ICD9CM:996.31', 'ICD9CM:996.32', 'ICD9CM:996.39', 'ICD9CM:996.4', 'ICD9CM:996.40', 'ICD9CM:996.41', 'ICD9CM:996.42', 'ICD9CM:996.43', 'ICD9CM:996.44', 'ICD9CM:996.45', 'ICD9CM:996.46', 'ICD9CM:996.47', 'ICD9CM:996.49', 'ICD9CM:996.51', 'ICD9CM:996.52', 'ICD9CM:996.53', 'ICD9CM:996.54', 'ICD9CM:996.55', 'ICD9CM:996.56', 'ICD9CM:996.57', 'ICD9CM:996.59', 'ICD9CM:996.6', 'ICD9CM:996.60', 'ICD9CM:996.61', 'ICD9CM:996.62', 'ICD9CM:996.63', 'ICD9CM:996.64', 'ICD9CM:996.65', 'ICD9CM:996.66', 'ICD9CM:996.67', 'ICD9CM:996.68', 'ICD9CM:996.69', 'ICD9CM:996.7', 'ICD9CM:996.70', 'ICD9CM:996.71', 'ICD9CM:996.72', 'ICD9CM:996.73', 'ICD9CM:996.74', 'ICD9CM:996.75', 'ICD9CM:996.76', 'ICD9CM:996.77', 'ICD9CM:996.78', 'ICD9CM:996.79', 'ICD9CM:996.80', 'ICD9CM:996.81', 'ICD9CM:996.82', 'ICD9CM:996.83', 'ICD9CM:996.84', 'ICD9CM:996.85', 'ICD9CM:996.86', 'ICD9CM:996.87', 'ICD9CM:996.88', 'ICD9CM:996.89', 'ICD9CM:996.90', 'ICD9CM:996.91', 'ICD9CM:996.92', 'ICD9CM:996.93', 'ICD9CM:996.94', 'ICD9CM:996.95', 'ICD9CM:996.96', 'ICD9CM:996.99', 'ICD9CM:999.31', 'ICD9CM:999.32', 'ICD9CM:999.33'):
            results_ccs4["comp_of_device"].append(1)
        else: results_ccs4["comp_of_device"].append(0)
    print("Completed Binary Recode of: comp_of_device")

    # Complications_of_surgical_procedures_or_medical_care
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:276.61', 'ICD9CM:277.83', 'ICD9CM:277.88', 'ICD9CM:285.3', 'ICD9CM:287.41', 'ICD9CM:349.0', 'ICD9CM:349.1', 'ICD9CM:349.31', 'ICD9CM:415.11', 'ICD9CM:429.4', 'ICD9CM:458.2', 'ICD9CM:458.21', 'ICD9CM:458.29', 'ICD9CM:512.1', 'ICD9CM:512.2', 'ICD9CM:518.7', 'ICD9CM:519.0', 'ICD9CM:519.00', 'ICD9CM:519.01', 'ICD9CM:519.02', 'ICD9CM:519.09', 'ICD9CM:530.86', 'ICD9CM:530.87', 'ICD9CM:536.40', 'ICD9CM:536.41', 'ICD9CM:536.42', 'ICD9CM:536.49', 'ICD9CM:539.01', 'ICD9CM:539.09', 'ICD9CM:539.81', 'ICD9CM:539.89', 'ICD9CM:564.2', 'ICD9CM:564.3', 'ICD9CM:564.4', 'ICD9CM:569.6', 'ICD9CM:569.62', 'ICD9CM:569.71', 'ICD9CM:569.79', 'ICD9CM:579.3', 'ICD9CM:596.81', 'ICD9CM:780.62', 'ICD9CM:780.63', 'ICD9CM:780.66', 'ICD9CM:909.3', 'ICD9CM:995.24', 'ICD9CM:995.4', 'ICD9CM:995.86', 'ICD9CM:997.0', 'ICD9CM:997.00', 'ICD9CM:997.01', 'ICD9CM:997.02', 'ICD9CM:997.09', 'ICD9CM:997.1', 'ICD9CM:997.2', 'ICD9CM:997.3', 'ICD9CM:997.31', 'ICD9CM:997.32', 'ICD9CM:997.39', 'ICD9CM:997.4', 'ICD9CM:997.41', 'ICD9CM:997.49', 'ICD9CM:997.5', 'ICD9CM:997.60', 'ICD9CM:997.61', 'ICD9CM:997.62', 'ICD9CM:997.69', 'ICD9CM:997.71', 'ICD9CM:997.72', 'ICD9CM:997.79', 'ICD9CM:997.9', 'ICD9CM:997.91', 'ICD9CM:997.99', 'ICD9CM:998.0', 'ICD9CM:998.00', 'ICD9CM:998.01', 'ICD9CM:998.02', 'ICD9CM:998.09', 'ICD9CM:998.1', 'ICD9CM:998.11', 'ICD9CM:998.12', 'ICD9CM:998.13', 'ICD9CM:998.2', 'ICD9CM:998.3', 'ICD9CM:998.30', 'ICD9CM:998.31', 'ICD9CM:998.32', 'ICD9CM:998.33', 'ICD9CM:998.4', 'ICD9CM:998.5', 'ICD9CM:998.51', 'ICD9CM:998.59', 'ICD9CM:998.6', 'ICD9CM:998.7', 'ICD9CM:998.8', 'ICD9CM:998.81', 'ICD9CM:998.82', 'ICD9CM:998.83', 'ICD9CM:998.89', 'ICD9CM:998.9', 'ICD9CM:999.0', 'ICD9CM:999.1', 'ICD9CM:999.2', 'ICD9CM:999.3', 'ICD9CM:999.34', 'ICD9CM:999.39', 'ICD9CM:999.4', 'ICD9CM:999.41', 'ICD9CM:999.42', 'ICD9CM:999.49', 'ICD9CM:999.5', 'ICD9CM:999.51', 'ICD9CM:999.52', 'ICD9CM:999.59', 'ICD9CM:999.6', 'ICD9CM:999.60', 'ICD9CM:999.61', 'ICD9CM:999.62', 'ICD9CM:999.63', 'ICD9CM:999.69', 'ICD9CM:999.7', 'ICD9CM:999.70', 'ICD9CM:999.71', 'ICD9CM:999.72', 'ICD9CM:999.73', 'ICD9CM:999.74', 'ICD9CM:999.75', 'ICD9CM:999.76', 'ICD9CM:999.77', 'ICD9CM:999.78', 'ICD9CM:999.79', 'ICD9CM:999.8', 'ICD9CM:999.80', 'ICD9CM:999.81', 'ICD9CM:999.82', 'ICD9CM:999.83', 'ICD9CM:999.84', 'ICD9CM:999.85', 'ICD9CM:999.88', 'ICD9CM:999.89', 'ICD9CM:999.9', 'ICD9CM:V15.53', 'ICD9CM:V15.80', 'ICD9CM:V15.83', 'ICD9CM:V90.01', 'ICD9CM:V90.09'):
            results_ccs4["comp_surg_proc"].append(1)
        else: results_ccs4["comp_surg_proc"].append(0)
    print("Completed Binary Recode of: comp_surg_proc")

    # Superficial_injury;_contusion
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:906.2', 'ICD9CM:906.3', 'ICD9CM:910.0', 'ICD9CM:910.1', 'ICD9CM:910.2', 'ICD9CM:910.3', 'ICD9CM:910.4', 'ICD9CM:910.5', 'ICD9CM:910.6', 'ICD9CM:910.7', 'ICD9CM:910.8', 'ICD9CM:910.9', 'ICD9CM:911.0', 'ICD9CM:911.1', 'ICD9CM:911.2', 'ICD9CM:911.3', 'ICD9CM:911.4', 'ICD9CM:911.5', 'ICD9CM:911.6', 'ICD9CM:911.7', 'ICD9CM:911.8', 'ICD9CM:911.9', 'ICD9CM:912.0', 'ICD9CM:912.1', 'ICD9CM:912.2', 'ICD9CM:912.3', 'ICD9CM:912.4', 'ICD9CM:912.5', 'ICD9CM:912.6', 'ICD9CM:912.7', 'ICD9CM:912.8', 'ICD9CM:912.9', 'ICD9CM:913.0', 'ICD9CM:913.1', 'ICD9CM:913.2', 'ICD9CM:913.3', 'ICD9CM:913.4', 'ICD9CM:913.5', 'ICD9CM:913.6', 'ICD9CM:913.7', 'ICD9CM:913.8', 'ICD9CM:913.9', 'ICD9CM:914.0', 'ICD9CM:914.1', 'ICD9CM:914.2', 'ICD9CM:914.3', 'ICD9CM:914.4', 'ICD9CM:914.5', 'ICD9CM:914.6', 'ICD9CM:914.7', 'ICD9CM:914.8', 'ICD9CM:914.9', 'ICD9CM:915.0', 'ICD9CM:915.1', 'ICD9CM:915.2', 'ICD9CM:915.3', 'ICD9CM:915.4', 'ICD9CM:915.5', 'ICD9CM:915.6', 'ICD9CM:915.7', 'ICD9CM:915.8', 'ICD9CM:915.9', 'ICD9CM:916.0', 'ICD9CM:916.1', 'ICD9CM:916.2', 'ICD9CM:916.3', 'ICD9CM:916.4', 'ICD9CM:916.5', 'ICD9CM:916.6', 'ICD9CM:916.7', 'ICD9CM:916.8', 'ICD9CM:916.9', 'ICD9CM:917.0', 'ICD9CM:917.1', 'ICD9CM:917.2', 'ICD9CM:917.3', 'ICD9CM:917.4', 'ICD9CM:917.5', 'ICD9CM:917.6', 'ICD9CM:917.7', 'ICD9CM:917.8', 'ICD9CM:917.9', 'ICD9CM:918.0', 'ICD9CM:918.1', 'ICD9CM:918.2', 'ICD9CM:918.9', 'ICD9CM:919.0', 'ICD9CM:919.1', 'ICD9CM:919.2', 'ICD9CM:919.3', 'ICD9CM:919.4', 'ICD9CM:919.5', 'ICD9CM:919.6', 'ICD9CM:919.7', 'ICD9CM:919.8', 'ICD9CM:919.9', 'ICD9CM:920', 'ICD9CM:921.0', 'ICD9CM:921.1', 'ICD9CM:921.2', 'ICD9CM:921.3', 'ICD9CM:921.9', 'ICD9CM:922.0', 'ICD9CM:922.1', 'ICD9CM:922.2', 'ICD9CM:922.3', 'ICD9CM:922.31', 'ICD9CM:922.32', 'ICD9CM:922.33', 'ICD9CM:922.4', 'ICD9CM:922.8', 'ICD9CM:922.9', 'ICD9CM:923.00', 'ICD9CM:923.01', 'ICD9CM:923.02', 'ICD9CM:923.03', 'ICD9CM:923.09', 'ICD9CM:923.10', 'ICD9CM:923.11', 'ICD9CM:923.20', 'ICD9CM:923.21', 'ICD9CM:923.3', 'ICD9CM:923.8', 'ICD9CM:923.9', 'ICD9CM:924.00', 'ICD9CM:924.01', 'ICD9CM:924.10', 'ICD9CM:924.11', 'ICD9CM:924.20', 'ICD9CM:924.21', 'ICD9CM:924.3', 'ICD9CM:924.4', 'ICD9CM:924.5', 'ICD9CM:924.8', 'ICD9CM:924.9'):
            results_ccs4["superficial_inj"].append(1)
        else: results_ccs4["superficial_inj"].append(0)
    print("Completed Binary Recode of: superficial_inj")

    # Burns
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:906.5', 'ICD9CM:906.6', 'ICD9CM:906.7', 'ICD9CM:906.8', 'ICD9CM:906.9', 'ICD9CM:940.0', 'ICD9CM:940.1', 'ICD9CM:940.2', 'ICD9CM:940.3', 'ICD9CM:940.4', 'ICD9CM:940.5', 'ICD9CM:940.9', 'ICD9CM:941.00', 'ICD9CM:941.01', 'ICD9CM:941.02', 'ICD9CM:941.03', 'ICD9CM:941.04', 'ICD9CM:941.05', 'ICD9CM:941.06', 'ICD9CM:941.07', 'ICD9CM:941.08', 'ICD9CM:941.09', 'ICD9CM:941.10', 'ICD9CM:941.11', 'ICD9CM:941.12', 'ICD9CM:941.13', 'ICD9CM:941.14', 'ICD9CM:941.15', 'ICD9CM:941.16', 'ICD9CM:941.17', 'ICD9CM:941.18', 'ICD9CM:941.19', 'ICD9CM:941.20', 'ICD9CM:941.21', 'ICD9CM:941.22', 'ICD9CM:941.23', 'ICD9CM:941.24', 'ICD9CM:941.25', 'ICD9CM:941.26', 'ICD9CM:941.27', 'ICD9CM:941.28', 'ICD9CM:941.29', 'ICD9CM:941.30', 'ICD9CM:941.31', 'ICD9CM:941.32', 'ICD9CM:941.33', 'ICD9CM:941.34', 'ICD9CM:941.35', 'ICD9CM:941.36', 'ICD9CM:941.37', 'ICD9CM:941.38', 'ICD9CM:941.39', 'ICD9CM:941.40', 'ICD9CM:941.41', 'ICD9CM:941.42', 'ICD9CM:941.43', 'ICD9CM:941.44', 'ICD9CM:941.45', 'ICD9CM:941.46', 'ICD9CM:941.47', 'ICD9CM:941.48', 'ICD9CM:941.49', 'ICD9CM:941.50', 'ICD9CM:941.51', 'ICD9CM:941.52', 'ICD9CM:941.53', 'ICD9CM:941.54', 'ICD9CM:941.55', 'ICD9CM:941.56', 'ICD9CM:941.57', 'ICD9CM:941.58', 'ICD9CM:941.59', 'ICD9CM:942.00', 'ICD9CM:942.01', 'ICD9CM:942.02', 'ICD9CM:942.03', 'ICD9CM:942.04', 'ICD9CM:942.05', 'ICD9CM:942.09', 'ICD9CM:942.10', 'ICD9CM:942.11', 'ICD9CM:942.12', 'ICD9CM:942.13', 'ICD9CM:942.14', 'ICD9CM:942.15', 'ICD9CM:942.19', 'ICD9CM:942.20', 'ICD9CM:942.21', 'ICD9CM:942.22', 'ICD9CM:942.23', 'ICD9CM:942.24', 'ICD9CM:942.25', 'ICD9CM:942.29', 'ICD9CM:942.30', 'ICD9CM:942.31', 'ICD9CM:942.32', 'ICD9CM:942.33', 'ICD9CM:942.34', 'ICD9CM:942.35', 'ICD9CM:942.39', 'ICD9CM:942.40', 'ICD9CM:942.41', 'ICD9CM:942.42', 'ICD9CM:942.43', 'ICD9CM:942.44', 'ICD9CM:942.45', 'ICD9CM:942.49', 'ICD9CM:942.50', 'ICD9CM:942.51', 'ICD9CM:942.52', 'ICD9CM:942.53', 'ICD9CM:942.54', 'ICD9CM:942.55', 'ICD9CM:942.59', 'ICD9CM:943.00', 'ICD9CM:943.01', 'ICD9CM:943.02', 'ICD9CM:943.03', 'ICD9CM:943.04', 'ICD9CM:943.05', 'ICD9CM:943.06', 'ICD9CM:943.09', 'ICD9CM:943.10', 'ICD9CM:943.11', 'ICD9CM:943.12', 'ICD9CM:943.13', 'ICD9CM:943.14', 'ICD9CM:943.15', 'ICD9CM:943.16', 'ICD9CM:943.19', 'ICD9CM:943.20', 'ICD9CM:943.21', 'ICD9CM:943.22', 'ICD9CM:943.23', 'ICD9CM:943.24', 'ICD9CM:943.25', 'ICD9CM:943.26', 'ICD9CM:943.29', 'ICD9CM:943.30', 'ICD9CM:943.31', 'ICD9CM:943.32', 'ICD9CM:943.33', 'ICD9CM:943.34', 'ICD9CM:943.35', 'ICD9CM:943.36', 'ICD9CM:943.39', 'ICD9CM:943.40', 'ICD9CM:943.41', 'ICD9CM:943.42', 'ICD9CM:943.43', 'ICD9CM:943.44', 'ICD9CM:943.45', 'ICD9CM:943.46', 'ICD9CM:943.49', 'ICD9CM:943.50', 'ICD9CM:943.51', 'ICD9CM:943.52', 'ICD9CM:943.53', 'ICD9CM:943.54', 'ICD9CM:943.55', 'ICD9CM:943.56', 'ICD9CM:943.59', 'ICD9CM:944.00', 'ICD9CM:944.01', 'ICD9CM:944.02', 'ICD9CM:944.03', 'ICD9CM:944.04', 'ICD9CM:944.05', 'ICD9CM:944.06', 'ICD9CM:944.07', 'ICD9CM:944.08', 'ICD9CM:944.10', 'ICD9CM:944.11', 'ICD9CM:944.12', 'ICD9CM:944.13', 'ICD9CM:944.14', 'ICD9CM:944.15', 'ICD9CM:944.16', 'ICD9CM:944.17', 'ICD9CM:944.18', 'ICD9CM:944.20', 'ICD9CM:944.21', 'ICD9CM:944.22', 'ICD9CM:944.23', 'ICD9CM:944.24', 'ICD9CM:944.25', 'ICD9CM:944.26', 'ICD9CM:944.27', 'ICD9CM:944.28', 'ICD9CM:944.30', 'ICD9CM:944.31', 'ICD9CM:944.32', 'ICD9CM:944.33', 'ICD9CM:944.34', 'ICD9CM:944.35', 'ICD9CM:944.36', 'ICD9CM:944.37', 'ICD9CM:944.38', 'ICD9CM:944.40', 'ICD9CM:944.41', 'ICD9CM:944.42', 'ICD9CM:944.43', 'ICD9CM:944.44', 'ICD9CM:944.45', 'ICD9CM:944.46', 'ICD9CM:944.47', 'ICD9CM:944.48', 'ICD9CM:944.50', 'ICD9CM:944.51', 'ICD9CM:944.52', 'ICD9CM:944.53', 'ICD9CM:944.54', 'ICD9CM:944.55', 'ICD9CM:944.56', 'ICD9CM:944.57', 'ICD9CM:944.58', 'ICD9CM:945.00', 'ICD9CM:945.01', 'ICD9CM:945.02', 'ICD9CM:945.03', 'ICD9CM:945.04', 'ICD9CM:945.05', 'ICD9CM:945.06', 'ICD9CM:945.09', 'ICD9CM:945.10', 'ICD9CM:945.11', 'ICD9CM:945.12', 'ICD9CM:945.13', 'ICD9CM:945.14', 'ICD9CM:945.15', 'ICD9CM:945.16', 'ICD9CM:945.19', 'ICD9CM:945.20', 'ICD9CM:945.21', 'ICD9CM:945.22', 'ICD9CM:945.23', 'ICD9CM:945.24', 'ICD9CM:945.25', 'ICD9CM:945.26', 'ICD9CM:945.29', 'ICD9CM:945.30', 'ICD9CM:945.31', 'ICD9CM:945.32', 'ICD9CM:945.33', 'ICD9CM:945.34', 'ICD9CM:945.35', 'ICD9CM:945.36', 'ICD9CM:945.39', 'ICD9CM:945.40', 'ICD9CM:945.41', 'ICD9CM:945.42', 'ICD9CM:945.43', 'ICD9CM:945.44', 'ICD9CM:945.45', 'ICD9CM:945.46', 'ICD9CM:945.49', 'ICD9CM:945.50', 'ICD9CM:945.51', 'ICD9CM:945.52', 'ICD9CM:945.53', 'ICD9CM:945.54', 'ICD9CM:945.55', 'ICD9CM:945.56', 'ICD9CM:945.59', 'ICD9CM:946.0', 'ICD9CM:946.1', 'ICD9CM:946.2', 'ICD9CM:946.3', 'ICD9CM:946.4', 'ICD9CM:946.5', 'ICD9CM:947.0', 'ICD9CM:947.1', 'ICD9CM:947.2', 'ICD9CM:947.3', 'ICD9CM:947.4', 'ICD9CM:947.8', 'ICD9CM:947.9', 'ICD9CM:948.00', 'ICD9CM:948.10', 'ICD9CM:948.11', 'ICD9CM:948.20', 'ICD9CM:948.21', 'ICD9CM:948.22', 'ICD9CM:948.30', 'ICD9CM:948.31', 'ICD9CM:948.32', 'ICD9CM:948.33', 'ICD9CM:948.40', 'ICD9CM:948.41', 'ICD9CM:948.42', 'ICD9CM:948.43', 'ICD9CM:948.44', 'ICD9CM:948.50', 'ICD9CM:948.51', 'ICD9CM:948.52', 'ICD9CM:948.53', 'ICD9CM:948.54', 'ICD9CM:948.55', 'ICD9CM:948.60', 'ICD9CM:948.61', 'ICD9CM:948.62', 'ICD9CM:948.63', 'ICD9CM:948.64', 'ICD9CM:948.65', 'ICD9CM:948.66', 'ICD9CM:948.70', 'ICD9CM:948.71', 'ICD9CM:948.72', 'ICD9CM:948.73', 'ICD9CM:948.74', 'ICD9CM:948.75', 'ICD9CM:948.76', 'ICD9CM:948.77', 'ICD9CM:948.80', 'ICD9CM:948.81', 'ICD9CM:948.82', 'ICD9CM:948.83', 'ICD9CM:948.84', 'ICD9CM:948.85', 'ICD9CM:948.86', 'ICD9CM:948.87', 'ICD9CM:948.88', 'ICD9CM:948.90', 'ICD9CM:948.91', 'ICD9CM:948.92', 'ICD9CM:948.93', 'ICD9CM:948.94', 'ICD9CM:948.95', 'ICD9CM:948.96', 'ICD9CM:948.97', 'ICD9CM:948.98', 'ICD9CM:948.99', 'ICD9CM:949.0', 'ICD9CM:949.1', 'ICD9CM:949.2', 'ICD9CM:949.3', 'ICD9CM:949.4', 'ICD9CM:949.5'):
            results_ccs4["burns"].append(1)
        else: results_ccs4["burns"].append(0)
    print("Completed Binary Recode of: burns")

    # Poisoning_by_psychotropic_agents
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:969.0', 'ICD9CM:969.00', 'ICD9CM:969.01', 'ICD9CM:969.02', 'ICD9CM:969.03', 'ICD9CM:969.04', 'ICD9CM:969.05', 'ICD9CM:969.09', 'ICD9CM:969.1', 'ICD9CM:969.2', 'ICD9CM:969.3', 'ICD9CM:969.4', 'ICD9CM:969.5', 'ICD9CM:969.6', 'ICD9CM:969.7', 'ICD9CM:969.70', 'ICD9CM:969.71', 'ICD9CM:969.72', 'ICD9CM:969.73', 'ICD9CM:969.79', 'ICD9CM:969.8', 'ICD9CM:969.9'):
            results_ccs4["poison_psycho"].append(1)
        else: results_ccs4["poison_psycho"].append(0)
    print("Completed Binary Recode of: poison_psycho")

    # Poisoning_by_other_medications_and_drugs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:528.01', 'ICD9CM:528.02', 'ICD9CM:909.0', 'ICD9CM:909.5', 'ICD9CM:960.0', 'ICD9CM:960.1', 'ICD9CM:960.2', 'ICD9CM:960.3', 'ICD9CM:960.4', 'ICD9CM:960.5', 'ICD9CM:960.6', 'ICD9CM:960.7', 'ICD9CM:960.8', 'ICD9CM:960.9', 'ICD9CM:961.0', 'ICD9CM:961.1', 'ICD9CM:961.2', 'ICD9CM:961.3', 'ICD9CM:961.4', 'ICD9CM:961.5', 'ICD9CM:961.6', 'ICD9CM:961.7', 'ICD9CM:961.8', 'ICD9CM:961.9', 'ICD9CM:962.0', 'ICD9CM:962.1', 'ICD9CM:962.2', 'ICD9CM:962.3', 'ICD9CM:962.4', 'ICD9CM:962.5', 'ICD9CM:962.6', 'ICD9CM:962.7', 'ICD9CM:962.8', 'ICD9CM:962.9', 'ICD9CM:963.0', 'ICD9CM:963.1', 'ICD9CM:963.2', 'ICD9CM:963.3', 'ICD9CM:963.4', 'ICD9CM:963.5', 'ICD9CM:963.8', 'ICD9CM:963.9', 'ICD9CM:964.0', 'ICD9CM:964.1', 'ICD9CM:964.2', 'ICD9CM:964.3', 'ICD9CM:964.4', 'ICD9CM:964.5', 'ICD9CM:964.6', 'ICD9CM:964.7', 'ICD9CM:964.8', 'ICD9CM:964.9', 'ICD9CM:965.1', 'ICD9CM:965.4', 'ICD9CM:965.5', 'ICD9CM:965.6', 'ICD9CM:965.61', 'ICD9CM:965.69', 'ICD9CM:965.7', 'ICD9CM:965.8', 'ICD9CM:965.9', 'ICD9CM:966.0', 'ICD9CM:966.1', 'ICD9CM:966.2', 'ICD9CM:966.3', 'ICD9CM:966.4', 'ICD9CM:967.0', 'ICD9CM:967.1', 'ICD9CM:967.2', 'ICD9CM:967.3', 'ICD9CM:967.4', 'ICD9CM:967.5', 'ICD9CM:967.6', 'ICD9CM:967.8', 'ICD9CM:967.9', 'ICD9CM:968.0', 'ICD9CM:968.1', 'ICD9CM:968.2', 'ICD9CM:968.3', 'ICD9CM:968.4', 'ICD9CM:968.5', 'ICD9CM:968.6', 'ICD9CM:968.7', 'ICD9CM:968.9', 'ICD9CM:970.0', 'ICD9CM:970.1', 'ICD9CM:970.8', 'ICD9CM:970.81', 'ICD9CM:970.89', 'ICD9CM:970.9', 'ICD9CM:971.0', 'ICD9CM:971.1', 'ICD9CM:971.2', 'ICD9CM:971.3', 'ICD9CM:971.9', 'ICD9CM:972.0', 'ICD9CM:972.1', 'ICD9CM:972.2', 'ICD9CM:972.3', 'ICD9CM:972.4', 'ICD9CM:972.5', 'ICD9CM:972.6', 'ICD9CM:972.7', 'ICD9CM:972.8', 'ICD9CM:972.9', 'ICD9CM:973.0', 'ICD9CM:973.1', 'ICD9CM:973.2', 'ICD9CM:973.3', 'ICD9CM:973.4', 'ICD9CM:973.5', 'ICD9CM:973.6', 'ICD9CM:973.8', 'ICD9CM:973.9', 'ICD9CM:974.0', 'ICD9CM:974.1', 'ICD9CM:974.2', 'ICD9CM:974.3', 'ICD9CM:974.4', 'ICD9CM:974.5', 'ICD9CM:974.6', 'ICD9CM:974.7', 'ICD9CM:975.0', 'ICD9CM:975.1', 'ICD9CM:975.2', 'ICD9CM:975.3', 'ICD9CM:975.4', 'ICD9CM:975.5', 'ICD9CM:975.6', 'ICD9CM:975.7', 'ICD9CM:975.8', 'ICD9CM:976.0', 'ICD9CM:976.1', 'ICD9CM:976.2', 'ICD9CM:976.3', 'ICD9CM:976.4', 'ICD9CM:976.5', 'ICD9CM:976.6', 'ICD9CM:976.7', 'ICD9CM:976.8', 'ICD9CM:976.9', 'ICD9CM:977.0', 'ICD9CM:977.1', 'ICD9CM:977.2', 'ICD9CM:977.3', 'ICD9CM:977.4', 'ICD9CM:977.8', 'ICD9CM:977.9', 'ICD9CM:978.0', 'ICD9CM:978.1', 'ICD9CM:978.2', 'ICD9CM:978.3', 'ICD9CM:978.4', 'ICD9CM:978.5', 'ICD9CM:978.6', 'ICD9CM:978.8', 'ICD9CM:978.9', 'ICD9CM:979.0', 'ICD9CM:979.1', 'ICD9CM:979.2', 'ICD9CM:979.3', 'ICD9CM:979.4', 'ICD9CM:979.5', 'ICD9CM:979.6', 'ICD9CM:979.7', 'ICD9CM:979.9', 'ICD9CM:995.2', 'ICD9CM:995.20', 'ICD9CM:995.21', 'ICD9CM:995.22', 'ICD9CM:995.23', 'ICD9CM:995.27', 'ICD9CM:995.29'):
            results_ccs4["poison_other_med"].append(1)
        else: results_ccs4["poison_other_med"].append(0)
    print("Completed Binary Recode of: poison_other_med")

    # Poisoning_by_nonmedicinal_substances
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:909.1', 'ICD9CM:980.1', 'ICD9CM:980.2', 'ICD9CM:980.3', 'ICD9CM:980.8', 'ICD9CM:980.9', 'ICD9CM:981', 'ICD9CM:982.0', 'ICD9CM:982.1', 'ICD9CM:982.2', 'ICD9CM:982.3', 'ICD9CM:982.4', 'ICD9CM:982.8', 'ICD9CM:983.0', 'ICD9CM:983.1', 'ICD9CM:983.2', 'ICD9CM:983.9', 'ICD9CM:984.0', 'ICD9CM:984.1', 'ICD9CM:984.8', 'ICD9CM:984.9', 'ICD9CM:985.0', 'ICD9CM:985.1', 'ICD9CM:985.2', 'ICD9CM:985.3', 'ICD9CM:985.4', 'ICD9CM:985.5', 'ICD9CM:985.6', 'ICD9CM:985.8', 'ICD9CM:985.9', 'ICD9CM:986', 'ICD9CM:987.0', 'ICD9CM:987.1', 'ICD9CM:987.2', 'ICD9CM:987.3', 'ICD9CM:987.4', 'ICD9CM:987.5', 'ICD9CM:987.6', 'ICD9CM:987.7', 'ICD9CM:987.8', 'ICD9CM:987.9', 'ICD9CM:988.0', 'ICD9CM:988.1', 'ICD9CM:988.2', 'ICD9CM:988.8', 'ICD9CM:988.9', 'ICD9CM:989.0', 'ICD9CM:989.1', 'ICD9CM:989.2', 'ICD9CM:989.3', 'ICD9CM:989.4', 'ICD9CM:989.5', 'ICD9CM:989.6', 'ICD9CM:989.7', 'ICD9CM:989.8', 'ICD9CM:989.81', 'ICD9CM:989.82', 'ICD9CM:989.83', 'ICD9CM:989.84', 'ICD9CM:989.89', 'ICD9CM:989.9'):
            results_ccs4["poison_nonmed"].append(1)
        else: results_ccs4["poison_nonmed"].append(0)
    print("Completed Binary Recode of: poison_nonmed")

    # Other_injuries_and_conditions_due_to_external_causes
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:796.0', 'ICD9CM:799.0', 'ICD9CM:799.01', 'ICD9CM:799.02', 'ICD9CM:907.1', 'ICD9CM:907.3', 'ICD9CM:907.4', 'ICD9CM:907.5', 'ICD9CM:907.9', 'ICD9CM:908.5', 'ICD9CM:908.6', 'ICD9CM:908.9', 'ICD9CM:909.2', 'ICD9CM:909.4', 'ICD9CM:909.9', 'ICD9CM:930.0', 'ICD9CM:930.1', 'ICD9CM:930.2', 'ICD9CM:930.8', 'ICD9CM:930.9', 'ICD9CM:931', 'ICD9CM:932', 'ICD9CM:933.0', 'ICD9CM:933.1', 'ICD9CM:934.0', 'ICD9CM:934.1', 'ICD9CM:934.8', 'ICD9CM:934.9', 'ICD9CM:935.0', 'ICD9CM:935.1', 'ICD9CM:935.2', 'ICD9CM:936', 'ICD9CM:937', 'ICD9CM:938', 'ICD9CM:939.0', 'ICD9CM:939.1', 'ICD9CM:939.2', 'ICD9CM:939.3', 'ICD9CM:939.9', 'ICD9CM:950.0', 'ICD9CM:950.1', 'ICD9CM:950.2', 'ICD9CM:950.3', 'ICD9CM:950.9', 'ICD9CM:951.0', 'ICD9CM:951.1', 'ICD9CM:951.2', 'ICD9CM:951.3', 'ICD9CM:951.4', 'ICD9CM:951.5', 'ICD9CM:951.6', 'ICD9CM:951.7', 'ICD9CM:951.8', 'ICD9CM:951.9', 'ICD9CM:953.0', 'ICD9CM:953.1', 'ICD9CM:953.2', 'ICD9CM:953.3', 'ICD9CM:953.4', 'ICD9CM:953.5', 'ICD9CM:953.8', 'ICD9CM:953.9', 'ICD9CM:954.0', 'ICD9CM:954.1', 'ICD9CM:954.8', 'ICD9CM:954.9', 'ICD9CM:955.0', 'ICD9CM:955.1', 'ICD9CM:955.2', 'ICD9CM:955.3', 'ICD9CM:955.4', 'ICD9CM:955.5', 'ICD9CM:955.6', 'ICD9CM:955.7', 'ICD9CM:955.8', 'ICD9CM:955.9', 'ICD9CM:956.0', 'ICD9CM:956.1', 'ICD9CM:956.2', 'ICD9CM:956.3', 'ICD9CM:956.4', 'ICD9CM:956.5', 'ICD9CM:956.8', 'ICD9CM:956.9', 'ICD9CM:957.0', 'ICD9CM:957.1', 'ICD9CM:957.8', 'ICD9CM:957.9', 'ICD9CM:958.0', 'ICD9CM:958.1', 'ICD9CM:958.2', 'ICD9CM:958.3', 'ICD9CM:958.4', 'ICD9CM:958.5', 'ICD9CM:958.6', 'ICD9CM:958.7', 'ICD9CM:958.8', 'ICD9CM:958.90', 'ICD9CM:958.91', 'ICD9CM:958.92', 'ICD9CM:958.93', 'ICD9CM:958.99', 'ICD9CM:959.0', 'ICD9CM:959.01', 'ICD9CM:959.09', 'ICD9CM:959.1', 'ICD9CM:959.11', 'ICD9CM:959.12', 'ICD9CM:959.13', 'ICD9CM:959.14', 'ICD9CM:959.19', 'ICD9CM:959.2', 'ICD9CM:959.3', 'ICD9CM:959.4', 'ICD9CM:959.5', 'ICD9CM:959.6', 'ICD9CM:959.7', 'ICD9CM:959.8', 'ICD9CM:959.9', 'ICD9CM:990', 'ICD9CM:991.0', 'ICD9CM:991.1', 'ICD9CM:991.2', 'ICD9CM:991.3', 'ICD9CM:991.4', 'ICD9CM:991.5', 'ICD9CM:991.6', 'ICD9CM:991.8', 'ICD9CM:991.9', 'ICD9CM:992.0', 'ICD9CM:992.1', 'ICD9CM:992.2', 'ICD9CM:992.3', 'ICD9CM:992.4', 'ICD9CM:992.5', 'ICD9CM:992.6', 'ICD9CM:992.7', 'ICD9CM:992.8', 'ICD9CM:992.9', 'ICD9CM:993.0', 'ICD9CM:993.1', 'ICD9CM:993.2', 'ICD9CM:993.3', 'ICD9CM:993.4', 'ICD9CM:993.8', 'ICD9CM:993.9', 'ICD9CM:994.0', 'ICD9CM:994.1', 'ICD9CM:994.2', 'ICD9CM:994.3', 'ICD9CM:994.4', 'ICD9CM:994.5', 'ICD9CM:994.6', 'ICD9CM:994.7', 'ICD9CM:994.8', 'ICD9CM:994.9', 'ICD9CM:995.5', 'ICD9CM:995.50', 'ICD9CM:995.51', 'ICD9CM:995.52', 'ICD9CM:995.53', 'ICD9CM:995.54', 'ICD9CM:995.55', 'ICD9CM:995.59', 'ICD9CM:995.80', 'ICD9CM:995.81', 'ICD9CM:995.82', 'ICD9CM:995.83', 'ICD9CM:995.84', 'ICD9CM:995.85', 'ICD9CM:995.89', 'ICD9CM:995.90', 'ICD9CM:995.93', 'ICD9CM:995.94', 'ICD9CM:V15.5', 'ICD9CM:V15.51', 'ICD9CM:V15.59', 'ICD9CM:V15.6', 'ICD9CM:V15.88', 'ICD9CM:V71.3', 'ICD9CM:V71.4', 'ICD9CM:V71.6', 'ICD9CM:V90.10', 'ICD9CM:V90.11', 'ICD9CM:V90.12', 'ICD9CM:V90.2', 'ICD9CM:V90.31', 'ICD9CM:V90.32', 'ICD9CM:V90.33', 'ICD9CM:V90.39', 'ICD9CM:V90.81', 'ICD9CM:V90.83', 'ICD9CM:V90.89', 'ICD9CM:V90.9'):
            results_ccs4["other_ext_injury"].append(1)
        else: results_ccs4["other_ext_injury"].append(0)
    print("Completed Binary Recode of: other_ext_injury")

    # Syncope
    for _ in df['condition_source_value']:
        if _ in 'ICD9CM:780.2':
            results_ccs4["syncope"].append(1)
        else: results_ccs4["syncope"].append(0)
    print("Completed Binary Recode of: syncope")

    # Fever_of_unknown_origin
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:780.6', 'ICD9CM:780.60', 'ICD9CM:780.61'):
            results_ccs4["fever_unknown"].append(1)
        else: results_ccs4["fever_unknown"].append(0)
    print("Completed Binary Recode of: fever_unknown")

    # Lymphadenitis
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:289.1', 'ICD9CM:289.2', 'ICD9CM:289.3', 'ICD9CM:683', 'ICD9CM:785.6'):
            results_ccs4["lymphadenitis"].append(1)
        else: results_ccs4["lymphadenitis"].append(0)
    print("Completed Binary Recode of: lymphadenitis")

    # Gangrene
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:440.24', 'ICD9CM:785.4'):
            results_ccs4["gangrene"].append(1)
        else: results_ccs4["gangrene"].append(0)
    print("Completed Binary Recode of: gangrene")

    # Shock
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:785.50', 'ICD9CM:785.51', 'ICD9CM:785.52', 'ICD9CM:785.59'):
            results_ccs4["shock"].append(1)
        else: results_ccs4["shock"].append(0)
    print("Completed Binary Recode of: shock")

    # Nausea_and_vomiting
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:787.0', 'ICD9CM:787.01', 'ICD9CM:787.02', 'ICD9CM:787.03', 'ICD9CM:787.04'):
            results_ccs4["naus_vom"].append(1)
        else: results_ccs4["naus_vom"].append(0)
    print("Completed Binary Recode of: naus_vom")

    # Abdominal_pain
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:789.0', 'ICD9CM:789.00', 'ICD9CM:789.01', 'ICD9CM:789.02', 'ICD9CM:789.03', 'ICD9CM:789.04', 'ICD9CM:789.05', 'ICD9CM:789.06', 'ICD9CM:789.07', 'ICD9CM:789.09', 'ICD9CM:789.60', 'ICD9CM:789.61', 'ICD9CM:789.62', 'ICD9CM:789.63', 'ICD9CM:789.64', 'ICD9CM:789.65', 'ICD9CM:789.66', 'ICD9CM:789.67', 'ICD9CM:789.69'):
            results_ccs4["abdominal_pain"].append(1)
        else: results_ccs4["abdominal_pain"].append(0)
    print("Completed Binary Recode of: abdominal_pain")

    # Malaise_and_fatigue
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:780.7', 'ICD9CM:780.71', 'ICD9CM:780.79'):
            results_ccs4["malaise_fatigue"].append(1)
        else: results_ccs4["malaise_fatigue"].append(0)
    print("Completed Binary Recode of: malaise_fatigue")

    # Allergic_reactions
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:477.1', 'ICD9CM:518.6', 'ICD9CM:558.3', 'ICD9CM:691.0', 'ICD9CM:691.8', 'ICD9CM:692.0', 'ICD9CM:692.1', 'ICD9CM:692.2', 'ICD9CM:692.3', 'ICD9CM:692.4', 'ICD9CM:692.5', 'ICD9CM:692.6', 'ICD9CM:692.70', 'ICD9CM:692.71', 'ICD9CM:692.72', 'ICD9CM:692.73', 'ICD9CM:692.74', 'ICD9CM:692.79', 'ICD9CM:692.81', 'ICD9CM:692.82', 'ICD9CM:692.83', 'ICD9CM:692.84', 'ICD9CM:692.89', 'ICD9CM:692.9', 'ICD9CM:693.0', 'ICD9CM:693.1', 'ICD9CM:693.8', 'ICD9CM:693.9', 'ICD9CM:708.0', 'ICD9CM:708.1', 'ICD9CM:708.2', 'ICD9CM:708.3', 'ICD9CM:708.4', 'ICD9CM:708.5', 'ICD9CM:708.8', 'ICD9CM:708.9', 'ICD9CM:995.0', 'ICD9CM:995.3', 'ICD9CM:995.60', 'ICD9CM:995.61', 'ICD9CM:995.62', 'ICD9CM:995.63', 'ICD9CM:995.64', 'ICD9CM:995.65', 'ICD9CM:995.66', 'ICD9CM:995.67', 'ICD9CM:995.68', 'ICD9CM:995.69', 'ICD9CM:995.7', 'ICD9CM:V07.1', 'ICD9CM:V13.81', 'ICD9CM:V14.0', 'ICD9CM:V14.1', 'ICD9CM:V14.2', 'ICD9CM:V14.3', 'ICD9CM:V14.4', 'ICD9CM:V14.5', 'ICD9CM:V14.6', 'ICD9CM:V14.7', 'ICD9CM:V14.8', 'ICD9CM:V14.9', 'ICD9CM:V15.0', 'ICD9CM:V15.01', 'ICD9CM:V15.02', 'ICD9CM:V15.03', 'ICD9CM:V15.04', 'ICD9CM:V15.05', 'ICD9CM:V15.06', 'ICD9CM:V15.07', 'ICD9CM:V15.08', 'ICD9CM:V15.09', 'ICD9CM:V72.7'):
            results_ccs4["allergy"].append(1)
        else: results_ccs4["allergy"].append(0)
    print("Completed Binary Recode of: allergy")

    # Rehabilitation_care;_fitting_of_prostheses;_and_adjustment_of_devices
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V52.0', 'ICD9CM:V52.1', 'ICD9CM:V52.4', 'ICD9CM:V52.8', 'ICD9CM:V52.9', 'ICD9CM:V53.8', 'ICD9CM:V57.0', 'ICD9CM:V57.1', 'ICD9CM:V57.2', 'ICD9CM:V57.21', 'ICD9CM:V57.22', 'ICD9CM:V57.3', 'ICD9CM:V57.4', 'ICD9CM:V57.81', 'ICD9CM:V57.89', 'ICD9CM:V57.9', 'ICD9CM:V58.82'):
            results_ccs4["rehab_care"].append(1)
        else: results_ccs4["rehab_care"].append(0)
    print("Completed Binary Recode of: rehab_care")

    # Administrative/_social_admission
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V20.0', 'ICD9CM:V20.1', 'ICD9CM:V20.2', 'ICD9CM:V20.31', 'ICD9CM:V20.32', 'ICD9CM:V60.0', 'ICD9CM:V60.1', 'ICD9CM:V60.2', 'ICD9CM:V60.3', 'ICD9CM:V60.4', 'ICD9CM:V60.5', 'ICD9CM:V60.6', 'ICD9CM:V60.8', 'ICD9CM:V60.81', 'ICD9CM:V60.89', 'ICD9CM:V60.9', 'ICD9CM:V61.0', 'ICD9CM:V61.01', 'ICD9CM:V61.02', 'ICD9CM:V61.03', 'ICD9CM:V61.04', 'ICD9CM:V61.05', 'ICD9CM:V61.06', 'ICD9CM:V61.07', 'ICD9CM:V61.08', 'ICD9CM:V61.09', 'ICD9CM:V61.1', 'ICD9CM:V61.10', 'ICD9CM:V61.11', 'ICD9CM:V61.12', 'ICD9CM:V61.20', 'ICD9CM:V61.21', 'ICD9CM:V61.22', 'ICD9CM:V61.23', 'ICD9CM:V61.24', 'ICD9CM:V61.25', 'ICD9CM:V61.29', 'ICD9CM:V61.3', 'ICD9CM:V61.41', 'ICD9CM:V61.42', 'ICD9CM:V61.49', 'ICD9CM:V61.5', 'ICD9CM:V61.6', 'ICD9CM:V61.7', 'ICD9CM:V61.8', 'ICD9CM:V61.9', 'ICD9CM:V62.0', 'ICD9CM:V62.1', 'ICD9CM:V62.2', 'ICD9CM:V62.21', 'ICD9CM:V62.22', 'ICD9CM:V62.29', 'ICD9CM:V62.3', 'ICD9CM:V62.4', 'ICD9CM:V62.5', 'ICD9CM:V62.6', 'ICD9CM:V62.81', 'ICD9CM:V62.82', 'ICD9CM:V62.83', 'ICD9CM:V62.89', 'ICD9CM:V62.9', 'ICD9CM:V63.0', 'ICD9CM:V63.1', 'ICD9CM:V63.2', 'ICD9CM:V63.8', 'ICD9CM:V63.9', 'ICD9CM:V65.0', 'ICD9CM:V65.1', 'ICD9CM:V65.11', 'ICD9CM:V65.19', 'ICD9CM:V65.2', 'ICD9CM:V65.3', 'ICD9CM:V65.4', 'ICD9CM:V65.40', 'ICD9CM:V65.41', 'ICD9CM:V65.43', 'ICD9CM:V65.44', 'ICD9CM:V65.45', 'ICD9CM:V65.49', 'ICD9CM:V65.5', 'ICD9CM:V65.8', 'ICD9CM:V65.9', 'ICD9CM:V68.0', 'ICD9CM:V68.1', 'ICD9CM:V68.2', 'ICD9CM:V68.81', 'ICD9CM:V68.89', 'ICD9CM:V68.9'):
            results_ccs4["admin_admiss"].append(1)
        else: results_ccs4["admin_admiss"].append(0)
    print("Completed Binary Recode of: admin_admiss")

    # Medical_examination/_evaluation
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V29.0', 'ICD9CM:V29.1', 'ICD9CM:V29.2', 'ICD9CM:V29.3', 'ICD9CM:V29.8', 'ICD9CM:V29.9', 'ICD9CM:V68.01', 'ICD9CM:V68.09', 'ICD9CM:V70.0', 'ICD9CM:V70.3', 'ICD9CM:V70.4', 'ICD9CM:V70.5', 'ICD9CM:V70.6', 'ICD9CM:V70.7', 'ICD9CM:V70.8', 'ICD9CM:V70.9', 'ICD9CM:V71.8', 'ICD9CM:V71.9', 'ICD9CM:V72.31', 'ICD9CM:V72.32', 'ICD9CM:V72.5', 'ICD9CM:V72.6', 'ICD9CM:V72.60', 'ICD9CM:V72.61', 'ICD9CM:V72.62', 'ICD9CM:V72.63', 'ICD9CM:V72.69', 'ICD9CM:V72.8', 'ICD9CM:V72.81', 'ICD9CM:V72.82', 'ICD9CM:V72.83', 'ICD9CM:V72.84', 'ICD9CM:V72.85', 'ICD9CM:V72.86', 'ICD9CM:V72.9'):
            results_ccs4["medical_eval"].append(1)
        else: results_ccs4["medical_eval"].append(0)
    print("Completed Binary Recode of: medical_eval")

    # Other_aftercare
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:V51', 'ICD9CM:V51.0', 'ICD9CM:V51.8', 'ICD9CM:V53.9', 'ICD9CM:V53.90', 'ICD9CM:V53.99', 'ICD9CM:V54.8', 'ICD9CM:V54.81', 'ICD9CM:V54.82', 'ICD9CM:V54.89', 'ICD9CM:V54.9', 'ICD9CM:V55.8', 'ICD9CM:V55.9', 'ICD9CM:V58.3', 'ICD9CM:V58.30', 'ICD9CM:V58.31', 'ICD9CM:V58.32', 'ICD9CM:V58.4', 'ICD9CM:V58.41', 'ICD9CM:V58.42', 'ICD9CM:V58.43', 'ICD9CM:V58.44', 'ICD9CM:V58.49', 'ICD9CM:V58.61', 'ICD9CM:V58.62', 'ICD9CM:V58.63', 'ICD9CM:V58.64', 'ICD9CM:V58.65', 'ICD9CM:V58.66', 'ICD9CM:V58.67', 'ICD9CM:V58.68', 'ICD9CM:V58.69', 'ICD9CM:V58.71', 'ICD9CM:V58.72', 'ICD9CM:V58.73', 'ICD9CM:V58.74', 'ICD9CM:V58.75', 'ICD9CM:V58.76', 'ICD9CM:V58.77', 'ICD9CM:V58.78', 'ICD9CM:V58.8', 'ICD9CM:V58.81', 'ICD9CM:V58.83', 'ICD9CM:V58.89', 'ICD9CM:V58.9', 'ICD9CM:V66.0', 'ICD9CM:V66.5', 'ICD9CM:V66.6', 'ICD9CM:V66.7', 'ICD9CM:V66.9', 'ICD9CM:V67.0', 'ICD9CM:V67.00', 'ICD9CM:V67.01', 'ICD9CM:V67.09', 'ICD9CM:V67.51', 'ICD9CM:V67.59', 'ICD9CM:V67.6', 'ICD9CM:V67.9'):
            results_ccs4["other_aftercare"].append(1)
        else: results_ccs4["other_aftercare"].append(0)
    print("Completed Binary Recode of: other_aftercare")

    # Other_screening_for_suspected_conditions_(_not_mental_disorders_or_infectious_disease)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:792.9', 'ICD9CM:795.00', 'ICD9CM:795.07', 'ICD9CM:795.08', 'ICD9CM:795.18', 'ICD9CM:795.4', 'ICD9CM:796.77', 'ICD9CM:796.78', 'ICD9CM:V28.0', 'ICD9CM:V28.1', 'ICD9CM:V28.2', 'ICD9CM:V28.3', 'ICD9CM:V28.4', 'ICD9CM:V28.5', 'ICD9CM:V28.8', 'ICD9CM:V28.81', 'ICD9CM:V28.82', 'ICD9CM:V28.89', 'ICD9CM:V28.9', 'ICD9CM:V71.5', 'ICD9CM:V71.81', 'ICD9CM:V71.89', 'ICD9CM:V72.40', 'ICD9CM:V72.41', 'ICD9CM:V76.0', 'ICD9CM:V76.1', 'ICD9CM:V76.10', 'ICD9CM:V76.11', 'ICD9CM:V76.12', 'ICD9CM:V76.19', 'ICD9CM:V76.2', 'ICD9CM:V76.3', 'ICD9CM:V76.41', 'ICD9CM:V76.42', 'ICD9CM:V76.43', 'ICD9CM:V76.44', 'ICD9CM:V76.45', 'ICD9CM:V76.46', 'ICD9CM:V76.47', 'ICD9CM:V76.49', 'ICD9CM:V76.50', 'ICD9CM:V76.51', 'ICD9CM:V76.52', 'ICD9CM:V76.8', 'ICD9CM:V76.81', 'ICD9CM:V76.89', 'ICD9CM:V76.9', 'ICD9CM:V77.0', 'ICD9CM:V77.1', 'ICD9CM:V77.2', 'ICD9CM:V77.3', 'ICD9CM:V77.4', 'ICD9CM:V77.5', 'ICD9CM:V77.6', 'ICD9CM:V77.7', 'ICD9CM:V77.8', 'ICD9CM:V77.9', 'ICD9CM:V77.91', 'ICD9CM:V77.99', 'ICD9CM:V78.0', 'ICD9CM:V78.1', 'ICD9CM:V78.2', 'ICD9CM:V78.3', 'ICD9CM:V78.8', 'ICD9CM:V78.9', 'ICD9CM:V80.0', 'ICD9CM:V80.01', 'ICD9CM:V80.09', 'ICD9CM:V80.1', 'ICD9CM:V80.2', 'ICD9CM:V80.3', 'ICD9CM:V81.0', 'ICD9CM:V81.1', 'ICD9CM:V81.2', 'ICD9CM:V81.3', 'ICD9CM:V81.4', 'ICD9CM:V81.5', 'ICD9CM:V81.6', 'ICD9CM:V82.0', 'ICD9CM:V82.1', 'ICD9CM:V82.2', 'ICD9CM:V82.3', 'ICD9CM:V82.4', 'ICD9CM:V82.5', 'ICD9CM:V82.6', 'ICD9CM:V82.71', 'ICD9CM:V82.79', 'ICD9CM:V82.8', 'ICD9CM:V82.81', 'ICD9CM:V82.89', 'ICD9CM:V82.9'):
            results_ccs4["other_screen"].append(1)
        else: results_ccs4["other_screen"].append(0)
    print("Completed Binary Recode of: other_screen")

    # Residual_codes;_unclassified
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:302.0', 'ICD9CM:327.00', 'ICD9CM:327.01', 'ICD9CM:327.09', 'ICD9CM:327.10', 'ICD9CM:327.11', 'ICD9CM:327.12', 'ICD9CM:327.13', 'ICD9CM:327.14', 'ICD9CM:327.19', 'ICD9CM:327.20', 'ICD9CM:327.21', 'ICD9CM:327.22', 'ICD9CM:327.23', 'ICD9CM:327.24', 'ICD9CM:327.25', 'ICD9CM:327.26', 'ICD9CM:327.27', 'ICD9CM:327.29', 'ICD9CM:327.40', 'ICD9CM:327.41', 'ICD9CM:327.42', 'ICD9CM:327.43', 'ICD9CM:327.44', 'ICD9CM:327.49', 'ICD9CM:327.51', 'ICD9CM:327.59', 'ICD9CM:327.8', 'ICD9CM:780.02', 'ICD9CM:780.1', 'ICD9CM:780.50', 'ICD9CM:780.51', 'ICD9CM:780.52', 'ICD9CM:780.53', 'ICD9CM:780.54', 'ICD9CM:780.55', 'ICD9CM:780.56', 'ICD9CM:780.57', 'ICD9CM:780.58', 'ICD9CM:780.59', 'ICD9CM:780.64', 'ICD9CM:780.65', 'ICD9CM:780.9', 'ICD9CM:780.93', 'ICD9CM:780.94', 'ICD9CM:780.95', 'ICD9CM:780.96', 'ICD9CM:780.97', 'ICD9CM:780.99', 'ICD9CM:781.5', 'ICD9CM:781.6', 'ICD9CM:782.3', 'ICD9CM:782.61', 'ICD9CM:782.62', 'ICD9CM:782.8', 'ICD9CM:782.9', 'ICD9CM:783.0', 'ICD9CM:783.6', 'ICD9CM:784.2', 'ICD9CM:790.1', 'ICD9CM:790.6', 'ICD9CM:790.9', 'ICD9CM:790.91', 'ICD9CM:790.92', 'ICD9CM:790.93', 'ICD9CM:790.94', 'ICD9CM:790.95', 'ICD9CM:790.99', 'ICD9CM:793.2', 'ICD9CM:793.9', 'ICD9CM:793.99', 'ICD9CM:794.9', 'ICD9CM:795.81', 'ICD9CM:795.82', 'ICD9CM:795.89', 'ICD9CM:796.3', 'ICD9CM:796.4', 'ICD9CM:796.5', 'ICD9CM:796.6', 'ICD9CM:796.9', 'ICD9CM:798.0', 'ICD9CM:798.1', 'ICD9CM:798.2', 'ICD9CM:798.9', 'ICD9CM:799.2', 'ICD9CM:799.21', 'ICD9CM:799.22', 'ICD9CM:799.23', 'ICD9CM:799.24', 'ICD9CM:799.25', 'ICD9CM:799.29', 'ICD9CM:799.3', 'ICD9CM:799.8', 'ICD9CM:799.81', 'ICD9CM:799.82', 'ICD9CM:799.89', 'ICD9CM:799.9', 'ICD9CM:V07.0', 'ICD9CM:V07.2', 'ICD9CM:V07.3', 'ICD9CM:V07.31', 'ICD9CM:V07.39', 'ICD9CM:V07.51', 'ICD9CM:V07.52', 'ICD9CM:V07.59', 'ICD9CM:V07.8', 'ICD9CM:V07.9', 'ICD9CM:V13.1', 'ICD9CM:V13.8', 'ICD9CM:V13.89', 'ICD9CM:V13.9', 'ICD9CM:V15.2', 'ICD9CM:V15.21', 'ICD9CM:V15.22', 'ICD9CM:V15.29', 'ICD9CM:V15.3', 'ICD9CM:V15.81', 'ICD9CM:V15.84', 'ICD9CM:V15.85', 'ICD9CM:V15.86', 'ICD9CM:V15.87', 'ICD9CM:V15.89', 'ICD9CM:V15.9', 'ICD9CM:V16.0', 'ICD9CM:V16.1', 'ICD9CM:V16.2', 'ICD9CM:V16.3', 'ICD9CM:V16.4', 'ICD9CM:V16.40', 'ICD9CM:V16.41', 'ICD9CM:V16.42', 'ICD9CM:V16.43', 'ICD9CM:V16.49', 'ICD9CM:V16.5', 'ICD9CM:V16.51', 'ICD9CM:V16.52', 'ICD9CM:V16.59', 'ICD9CM:V16.6', 'ICD9CM:V16.7', 'ICD9CM:V16.8', 'ICD9CM:V16.9', 'ICD9CM:V17.0', 'ICD9CM:V17.1', 'ICD9CM:V17.2', 'ICD9CM:V17.3', 'ICD9CM:V17.4', 'ICD9CM:V17.41', 'ICD9CM:V17.49', 'ICD9CM:V17.5', 'ICD9CM:V17.6', 'ICD9CM:V17.7', 'ICD9CM:V17.8', 'ICD9CM:V17.81', 'ICD9CM:V17.89', 'ICD9CM:V18.0', 'ICD9CM:V18.1', 'ICD9CM:V18.11', 'ICD9CM:V18.19', 'ICD9CM:V18.2', 'ICD9CM:V18.3', 'ICD9CM:V18.4', 'ICD9CM:V18.5', 'ICD9CM:V18.51', 'ICD9CM:V18.59', 'ICD9CM:V18.6', 'ICD9CM:V18.61', 'ICD9CM:V18.69', 'ICD9CM:V18.7', 'ICD9CM:V18.8', 'ICD9CM:V18.9', 'ICD9CM:V19.0', 'ICD9CM:V19.1', 'ICD9CM:V19.11', 'ICD9CM:V19.19', 'ICD9CM:V19.2', 'ICD9CM:V19.3', 'ICD9CM:V19.4', 'ICD9CM:V19.5', 'ICD9CM:V19.6', 'ICD9CM:V19.7', 'ICD9CM:V19.8', 'ICD9CM:V21.0', 'ICD9CM:V21.1', 'ICD9CM:V21.2', 'ICD9CM:V21.8', 'ICD9CM:V21.9', 'ICD9CM:V41.8', 'ICD9CM:V41.9', 'ICD9CM:V42.8', 'ICD9CM:V42.81', 'ICD9CM:V42.82', 'ICD9CM:V42.83', 'ICD9CM:V42.84', 'ICD9CM:V42.89', 'ICD9CM:V42.9', 'ICD9CM:V43.8', 'ICD9CM:V43.81', 'ICD9CM:V43.82', 'ICD9CM:V43.83', 'ICD9CM:V43.89', 'ICD9CM:V44.7', 'ICD9CM:V44.8', 'ICD9CM:V44.9', 'ICD9CM:V45.71', 'ICD9CM:V45.72', 'ICD9CM:V45.73', 'ICD9CM:V45.74', 'ICD9CM:V45.75', 'ICD9CM:V45.76', 'ICD9CM:V45.77', 'ICD9CM:V45.78', 'ICD9CM:V45.79', 'ICD9CM:V45.83', 'ICD9CM:V45.84', 'ICD9CM:V45.86', 'ICD9CM:V45.87', 'ICD9CM:V45.88', 'ICD9CM:V45.89', 'ICD9CM:V46.0', 'ICD9CM:V46.3', 'ICD9CM:V46.8', 'ICD9CM:V46.9', 'ICD9CM:V47.0', 'ICD9CM:V47.1', 'ICD9CM:V47.2', 'ICD9CM:V47.9', 'ICD9CM:V48.0', 'ICD9CM:V48.8', 'ICD9CM:V48.9', 'ICD9CM:V49.8', 'ICD9CM:V49.81', 'ICD9CM:V49.82', 'ICD9CM:V49.83', 'ICD9CM:V49.84', 'ICD9CM:V49.86', 'ICD9CM:V49.87', 'ICD9CM:V49.89', 'ICD9CM:V49.9', 'ICD9CM:V50.0', 'ICD9CM:V50.1', 'ICD9CM:V50.3', 'ICD9CM:V50.41', 'ICD9CM:V50.42', 'ICD9CM:V50.49', 'ICD9CM:V50.8', 'ICD9CM:V50.9', 'ICD9CM:V59.0', 'ICD9CM:V59.01', 'ICD9CM:V59.02', 'ICD9CM:V59.09', 'ICD9CM:V59.1', 'ICD9CM:V59.2', 'ICD9CM:V59.3', 'ICD9CM:V59.4', 'ICD9CM:V59.5', 'ICD9CM:V59.6', 'ICD9CM:V59.70', 'ICD9CM:V59.71', 'ICD9CM:V59.72', 'ICD9CM:V59.73', 'ICD9CM:V59.74', 'ICD9CM:V59.8', 'ICD9CM:V59.9', 'ICD9CM:V64.0', 'ICD9CM:V64.00', 'ICD9CM:V64.01', 'ICD9CM:V64.02', 'ICD9CM:V64.03', 'ICD9CM:V64.04', 'ICD9CM:V64.05', 'ICD9CM:V64.06', 'ICD9CM:V64.07', 'ICD9CM:V64.08', 'ICD9CM:V64.09', 'ICD9CM:V64.1', 'ICD9CM:V64.2', 'ICD9CM:V64.3', 'ICD9CM:V64.4', 'ICD9CM:V64.41', 'ICD9CM:V64.42', 'ICD9CM:V64.43', 'ICD9CM:V69.0', 'ICD9CM:V69.1', 'ICD9CM:V69.2', 'ICD9CM:V69.3', 'ICD9CM:V69.4', 'ICD9CM:V69.5', 'ICD9CM:V69.8', 'ICD9CM:V69.9', 'ICD9CM:V83.01', 'ICD9CM:V83.02', 'ICD9CM:V83.81', 'ICD9CM:V83.89', 'ICD9CM:V84.01', 'ICD9CM:V84.02', 'ICD9CM:V84.03', 'ICD9CM:V84.04', 'ICD9CM:V84.09', 'ICD9CM:V84.8', 'ICD9CM:V84.81', 'ICD9CM:V84.89', 'ICD9CM:V85.1', 'ICD9CM:V85.52', 'ICD9CM:V86.0', 'ICD9CM:V86.1', 'ICD9CM:V87.01', 'ICD9CM:V87.02', 'ICD9CM:V87.09', 'ICD9CM:V87.11', 'ICD9CM:V87.12', 'ICD9CM:V87.19', 'ICD9CM:V87.2', 'ICD9CM:V87.31', 'ICD9CM:V87.32', 'ICD9CM:V87.39', 'ICD9CM:V87.41', 'ICD9CM:V87.42', 'ICD9CM:V87.43', 'ICD9CM:V87.44', 'ICD9CM:V87.45', 'ICD9CM:V87.46', 'ICD9CM:V87.49', 'ICD9CM:V88.01', 'ICD9CM:V88.02', 'ICD9CM:V88.03', 'ICD9CM:V88.11', 'ICD9CM:V88.12', 'ICD9CM:V89.01', 'ICD9CM:V89.02', 'ICD9CM:V89.03', 'ICD9CM:V89.04', 'ICD9CM:V89.05', 'ICD9CM:V89.09'):
            results_ccs4["residual_codes"].append(1)
        else: results_ccs4["residual_codes"].append(0)
    print("Completed Binary Recode of: residual_codes")

    # Adjustment_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:309.0', 'ICD9CM:309.1', 'ICD9CM:309.22', 'ICD9CM:309.23', 'ICD9CM:309.24', 'ICD9CM:309.28', 'ICD9CM:309.29', 'ICD9CM:309.3', 'ICD9CM:309.4', 'ICD9CM:309.82', 'ICD9CM:309.83', 'ICD9CM:309.89', 'ICD9CM:309.9'):
            results_ccs4["adjustment"].append(1)
        else: results_ccs4["adjustment"].append(0)
    print("Completed Binary Recode of: adjustment")

    # Anxiety_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:293.84', 'ICD9CM:300.00', 'ICD9CM:300.01', 'ICD9CM:300.02', 'ICD9CM:300.09', 'ICD9CM:300.10', 'ICD9CM:300.20', 'ICD9CM:300.21', 'ICD9CM:300.22', 'ICD9CM:300.23', 'ICD9CM:300.29', 'ICD9CM:300.3', 'ICD9CM:300.5', 'ICD9CM:300.89', 'ICD9CM:300.9', 'ICD9CM:308.0', 'ICD9CM:308.1', 'ICD9CM:308.2', 'ICD9CM:308.3', 'ICD9CM:308.4', 'ICD9CM:308.9', 'ICD9CM:309.81', 'ICD9CM:313.0', 'ICD9CM:313.1', 'ICD9CM:313.21', 'ICD9CM:313.22', 'ICD9CM:313.3', 'ICD9CM:313.82', 'ICD9CM:313.83'):
            results_ccs4["anxiety"].append(1)
        else: results_ccs4["anxiety"].append(0)
    print("Completed Binary Recode of: anxiety")

    # Attention-_deficit,_conduct,_and_disruptive_behavior_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:312.00', 'ICD9CM:312.01', 'ICD9CM:312.02', 'ICD9CM:312.03', 'ICD9CM:312.10', 'ICD9CM:312.11', 'ICD9CM:312.12', 'ICD9CM:312.13', 'ICD9CM:312.20', 'ICD9CM:312.21', 'ICD9CM:312.22', 'ICD9CM:312.23', 'ICD9CM:312.4', 'ICD9CM:312.8', 'ICD9CM:312.81', 'ICD9CM:312.82', 'ICD9CM:312.89', 'ICD9CM:312.9', 'ICD9CM:313.81', 'ICD9CM:314.00', 'ICD9CM:314.01', 'ICD9CM:314.1', 'ICD9CM:314.2', 'ICD9CM:314.8', 'ICD9CM:314.9'):
            results_ccs4["adhd"].append(1)
        else: results_ccs4["adhd"].append(0)
    print("Completed Binary Recode of: adhd")

    # Delirium,_dementia,_and_amnestic_and_other_cognitive_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:290.0', 'ICD9CM:290.10', 'ICD9CM:290.11', 'ICD9CM:290.12', 'ICD9CM:290.13', 'ICD9CM:290.20', 'ICD9CM:290.21', 'ICD9CM:290.3', 'ICD9CM:290.40', 'ICD9CM:290.41', 'ICD9CM:290.42', 'ICD9CM:290.43', 'ICD9CM:290.8', 'ICD9CM:290.9', 'ICD9CM:293.0', 'ICD9CM:293.1', 'ICD9CM:294.0', 'ICD9CM:294.1', 'ICD9CM:294.10', 'ICD9CM:294.11', 'ICD9CM:294.20', 'ICD9CM:294.21', 'ICD9CM:294.8', 'ICD9CM:294.9', 'ICD9CM:310.0', 'ICD9CM:310.2', 'ICD9CM:310.8', 'ICD9CM:310.81', 'ICD9CM:310.89', 'ICD9CM:310.9', 'ICD9CM:331.0', 'ICD9CM:331.1', 'ICD9CM:331.11', 'ICD9CM:331.19', 'ICD9CM:331.2', 'ICD9CM:331.82', 'ICD9CM:797'):
            results_ccs4["dementia"].append(1)
        else: results_ccs4["dementia"].append(0)
    print("Completed Binary Recode of: dementia")

    # Developmental_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:307.0', 'ICD9CM:307.9', 'ICD9CM:315.00', 'ICD9CM:315.01', 'ICD9CM:315.02', 'ICD9CM:315.09', 'ICD9CM:315.1', 'ICD9CM:315.2', 'ICD9CM:315.31', 'ICD9CM:315.32', 'ICD9CM:315.34', 'ICD9CM:315.35', 'ICD9CM:315.39', 'ICD9CM:315.4', 'ICD9CM:315.5', 'ICD9CM:315.8', 'ICD9CM:315.9', 'ICD9CM:317', 'ICD9CM:318.0', 'ICD9CM:318.1', 'ICD9CM:318.2', 'ICD9CM:319', 'ICD9CM:V40.0', 'ICD9CM:V40.1'):
            results_ccs4["develop_dis"].append(1)
        else: results_ccs4["develop_dis"].append(0)
    print("Completed Binary Recode of: develop_dis")

    # Disorders_usually_diagnosed_in_infancy,_childhood,_or_adolescence
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:299.00', 'ICD9CM:299.01', 'ICD9CM:299.10', 'ICD9CM:299.11', 'ICD9CM:299.80', 'ICD9CM:299.81', 'ICD9CM:299.90', 'ICD9CM:299.91', 'ICD9CM:307.20', 'ICD9CM:307.21', 'ICD9CM:307.22', 'ICD9CM:307.23', 'ICD9CM:307.3', 'ICD9CM:307.6', 'ICD9CM:307.7', 'ICD9CM:309.21', 'ICD9CM:313.23', 'ICD9CM:313.89', 'ICD9CM:313.9'):
            results_ccs4["child_disorder"].append(1)
        else: results_ccs4["child_disorder"].append(0)
    print("Completed Binary Recode of: child_disorder")

    # Impulse_control_disorders,_NEC
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:312.30', 'ICD9CM:312.31', 'ICD9CM:312.32', 'ICD9CM:312.33', 'ICD9CM:312.34', 'ICD9CM:312.35', 'ICD9CM:312.39'):
            results_ccs4["impule_control"].append(1)
        else: results_ccs4["impule_control"].append(0)
    print("Completed Binary Recode of: impule_control")

    # Mood_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:293.83', 'ICD9CM:296.00', 'ICD9CM:296.01', 'ICD9CM:296.02', 'ICD9CM:296.03', 'ICD9CM:296.04', 'ICD9CM:296.05', 'ICD9CM:296.06', 'ICD9CM:296.10', 'ICD9CM:296.11', 'ICD9CM:296.12', 'ICD9CM:296.13', 'ICD9CM:296.14', 'ICD9CM:296.15', 'ICD9CM:296.16', 'ICD9CM:296.20', 'ICD9CM:296.21', 'ICD9CM:296.22', 'ICD9CM:296.23', 'ICD9CM:296.24', 'ICD9CM:296.25', 'ICD9CM:296.26', 'ICD9CM:296.30', 'ICD9CM:296.31', 'ICD9CM:296.32', 'ICD9CM:296.33', 'ICD9CM:296.34', 'ICD9CM:296.35', 'ICD9CM:296.36', 'ICD9CM:296.40', 'ICD9CM:296.41', 'ICD9CM:296.42', 'ICD9CM:296.43', 'ICD9CM:296.44', 'ICD9CM:296.45', 'ICD9CM:296.46', 'ICD9CM:296.50', 'ICD9CM:296.51', 'ICD9CM:296.52', 'ICD9CM:296.53', 'ICD9CM:296.54', 'ICD9CM:296.55', 'ICD9CM:296.56', 'ICD9CM:296.60', 'ICD9CM:296.61', 'ICD9CM:296.62', 'ICD9CM:296.63', 'ICD9CM:296.64', 'ICD9CM:296.65', 'ICD9CM:296.66', 'ICD9CM:296.7', 'ICD9CM:296.80', 'ICD9CM:296.81', 'ICD9CM:296.82', 'ICD9CM:296.89', 'ICD9CM:296.90', 'ICD9CM:296.99', 'ICD9CM:300.4', 'ICD9CM:311'):
            results_ccs4["mood"].append(1)
        else: results_ccs4["mood"].append(0)
    print("Completed Binary Recode of: mood")


    # Personality_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:301.0', 'ICD9CM:301.10', 'ICD9CM:301.11', 'ICD9CM:301.12', 'ICD9CM:301.13', 'ICD9CM:301.20', 'ICD9CM:301.21', 'ICD9CM:301.22', 'ICD9CM:301.3', 'ICD9CM:301.4', 'ICD9CM:301.50', 'ICD9CM:301.51', 'ICD9CM:301.59', 'ICD9CM:301.6', 'ICD9CM:301.7', 'ICD9CM:301.81', 'ICD9CM:301.82', 'ICD9CM:301.83', 'ICD9CM:301.84', 'ICD9CM:301.89', 'ICD9CM:301.9'):
            results_ccs4["personality"].append(1)
        else: results_ccs4["personality"].append(0)
    print("Completed Binary Recode of: personality")


    # Schizophrenia_and_other_psychotic_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:293.81', 'ICD9CM:293.82', 'ICD9CM:295.00', 'ICD9CM:295.01', 'ICD9CM:295.02', 'ICD9CM:295.03', 'ICD9CM:295.04', 'ICD9CM:295.05', 'ICD9CM:295.10', 'ICD9CM:295.11', 'ICD9CM:295.12', 'ICD9CM:295.13', 'ICD9CM:295.14', 'ICD9CM:295.15', 'ICD9CM:295.20', 'ICD9CM:295.21', 'ICD9CM:295.22', 'ICD9CM:295.23', 'ICD9CM:295.24', 'ICD9CM:295.25', 'ICD9CM:295.30', 'ICD9CM:295.31', 'ICD9CM:295.32', 'ICD9CM:295.33', 'ICD9CM:295.34', 'ICD9CM:295.35', 'ICD9CM:295.40', 'ICD9CM:295.41', 'ICD9CM:295.42', 'ICD9CM:295.43', 'ICD9CM:295.44', 'ICD9CM:295.45', 'ICD9CM:295.50', 'ICD9CM:295.51', 'ICD9CM:295.52', 'ICD9CM:295.53', 'ICD9CM:295.54', 'ICD9CM:295.55', 'ICD9CM:295.60', 'ICD9CM:295.61', 'ICD9CM:295.62', 'ICD9CM:295.63', 'ICD9CM:295.64', 'ICD9CM:295.65', 'ICD9CM:295.70', 'ICD9CM:295.71', 'ICD9CM:295.72', 'ICD9CM:295.73', 'ICD9CM:295.74', 'ICD9CM:295.75', 'ICD9CM:295.80', 'ICD9CM:295.81', 'ICD9CM:295.82', 'ICD9CM:295.83', 'ICD9CM:295.84', 'ICD9CM:295.85', 'ICD9CM:295.90', 'ICD9CM:295.91', 'ICD9CM:295.92', 'ICD9CM:295.93', 'ICD9CM:295.94', 'ICD9CM:295.95', 'ICD9CM:297.0', 'ICD9CM:297.1', 'ICD9CM:297.2', 'ICD9CM:297.3', 'ICD9CM:297.8', 'ICD9CM:297.9', 'ICD9CM:298.0', 'ICD9CM:298.1', 'ICD9CM:298.2', 'ICD9CM:298.3', 'ICD9CM:298.4', 'ICD9CM:298.8', 'ICD9CM:298.9'):
            results_ccs4["schizo"].append(1)
        else: results_ccs4["schizo"].append(0)
    print("Completed Binary Recode of: schizo")


    # Alcohol-_related_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:291.0', 'ICD9CM:291.1', 'ICD9CM:291.2', 'ICD9CM:291.3', 'ICD9CM:291.4', 'ICD9CM:291.5', 'ICD9CM:291.8', 'ICD9CM:291.81', 'ICD9CM:291.82', 'ICD9CM:291.89', 'ICD9CM:291.9', 'ICD9CM:303.00', 'ICD9CM:303.01', 'ICD9CM:303.02', 'ICD9CM:303.03', 'ICD9CM:303.90', 'ICD9CM:303.91', 'ICD9CM:303.92', 'ICD9CM:303.93', 'ICD9CM:305.00', 'ICD9CM:305.01', 'ICD9CM:305.02', 'ICD9CM:305.03', 'ICD9CM:357.5', 'ICD9CM:425.5', 'ICD9CM:535.3', 'ICD9CM:535.30', 'ICD9CM:535.31', 'ICD9CM:571.0', 'ICD9CM:571.1', 'ICD9CM:571.2', 'ICD9CM:571.3', 'ICD9CM:760.71', 'ICD9CM:980.0'):
            results_ccs4["alcohol"].append(1)
        else: results_ccs4["alcohol"].append(0)
    print("Completed Binary Recode of: alcohol")


    # Substance-_related_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:292.0', 'ICD9CM:292.11', 'ICD9CM:292.12', 'ICD9CM:292.2', 'ICD9CM:292.81', 'ICD9CM:292.82', 'ICD9CM:292.83', 'ICD9CM:292.84', 'ICD9CM:292.85', 'ICD9CM:292.89', 'ICD9CM:292.9', 'ICD9CM:304.00', 'ICD9CM:304.01', 'ICD9CM:304.02', 'ICD9CM:304.03', 'ICD9CM:304.10', 'ICD9CM:304.11', 'ICD9CM:304.12', 'ICD9CM:304.13', 'ICD9CM:304.20', 'ICD9CM:304.21', 'ICD9CM:304.22', 'ICD9CM:304.23', 'ICD9CM:304.30', 'ICD9CM:304.31', 'ICD9CM:304.32', 'ICD9CM:304.33', 'ICD9CM:304.40', 'ICD9CM:304.41', 'ICD9CM:304.42', 'ICD9CM:304.43', 'ICD9CM:304.50', 'ICD9CM:304.51', 'ICD9CM:304.52', 'ICD9CM:304.53', 'ICD9CM:304.60', 'ICD9CM:304.61', 'ICD9CM:304.62', 'ICD9CM:304.63', 'ICD9CM:304.70', 'ICD9CM:304.71', 'ICD9CM:304.72', 'ICD9CM:304.73', 'ICD9CM:304.80', 'ICD9CM:304.81', 'ICD9CM:304.82', 'ICD9CM:304.83', 'ICD9CM:304.90', 'ICD9CM:304.91', 'ICD9CM:304.92', 'ICD9CM:304.93', 'ICD9CM:305.20', 'ICD9CM:305.21', 'ICD9CM:305.22', 'ICD9CM:305.23', 'ICD9CM:305.30', 'ICD9CM:305.31', 'ICD9CM:305.32', 'ICD9CM:305.33', 'ICD9CM:305.40', 'ICD9CM:305.41', 'ICD9CM:305.42', 'ICD9CM:305.43', 'ICD9CM:305.50', 'ICD9CM:305.51', 'ICD9CM:305.52', 'ICD9CM:305.53', 'ICD9CM:305.60', 'ICD9CM:305.61', 'ICD9CM:305.62', 'ICD9CM:305.63', 'ICD9CM:305.70', 'ICD9CM:305.71', 'ICD9CM:305.72', 'ICD9CM:305.73', 'ICD9CM:305.80', 'ICD9CM:305.81', 'ICD9CM:305.82', 'ICD9CM:305.83', 'ICD9CM:305.90', 'ICD9CM:305.91', 'ICD9CM:305.92', 'ICD9CM:305.93', 'ICD9CM:648.30', 'ICD9CM:648.31', 'ICD9CM:648.32', 'ICD9CM:648.33', 'ICD9CM:648.34', 'ICD9CM:655.50', 'ICD9CM:655.51', 'ICD9CM:655.53', 'ICD9CM:760.72', 'ICD9CM:760.73', 'ICD9CM:760.75', 'ICD9CM:779.5', 'ICD9CM:965.00', 'ICD9CM:965.01', 'ICD9CM:965.02', 'ICD9CM:965.09', 'ICD9CM:V65.42'):
            results_ccs4["substance"].append(1)
        else: results_ccs4["substance"].append(0)
    print("Completed Binary Recode of: substance")

    # Suicide_and_intentional_self-_inflicted_injury
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E95.00', 'ICD9CM:E95.01', 'ICD9CM:E95.02', 'ICD9CM:E95.03', 'ICD9CM:E95.04', 'ICD9CM:E95.05', 'ICD9CM:E95.06', 'ICD9CM:E95.07', 'ICD9CM:E95.08', 'ICD9CM:E95.09', 'ICD9CM:E95.10', 'ICD9CM:E95.11', 'ICD9CM:E95.18', 'ICD9CM:E95.20', 'ICD9CM:E95.21', 'ICD9CM:E95.28', 'ICD9CM:E95.29', 'ICD9CM:E95.30', 'ICD9CM:E95.31', 'ICD9CM:E95.38', 'ICD9CM:E95.39', 'ICD9CM:E95.4', 'ICD9CM:E95.50', 'ICD9CM:E95.51', 'ICD9CM:E95.52', 'ICD9CM:E95.53', 'ICD9CM:E95.54', 'ICD9CM:E95.55', 'ICD9CM:E95.56', 'ICD9CM:E95.57', 'ICD9CM:E95.59', 'ICD9CM:E95.6', 'ICD9CM:E95.70', 'ICD9CM:E95.71', 'ICD9CM:E95.72', 'ICD9CM:E95.79', 'ICD9CM:E95.80', 'ICD9CM:E95.81', 'ICD9CM:E95.82', 'ICD9CM:E95.83', 'ICD9CM:E95.84', 'ICD9CM:E95.85', 'ICD9CM:E95.86', 'ICD9CM:E95.87', 'ICD9CM:E95.88', 'ICD9CM:E95.89', 'ICD9CM:E95.9', 'ICD9CM:V62.84'):
            results_ccs4["suicide"].append(1)
        else: results_ccs4["suicide"].append(0)
    print("Completed Binary Recode of: suicide")

    # Screening_and_history_of_mental_health_and_substance_abuse_codes
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:305.1', 'ICD9CM:305.10', 'ICD9CM:305.11', 'ICD9CM:305.12', 'ICD9CM:305.13', 'ICD9CM:333.92', 'ICD9CM:790.3', 'ICD9CM:V11.0', 'ICD9CM:V11.1', 'ICD9CM:V11.2', 'ICD9CM:V11.3', 'ICD9CM:V11.4', 'ICD9CM:V11.8', 'ICD9CM:V11.9', 'ICD9CM:V15.4', 'ICD9CM:V15.41', 'ICD9CM:V15.42', 'ICD9CM:V15.49', 'ICD9CM:V15.82', 'ICD9CM:V62.85', 'ICD9CM:V66.3', 'ICD9CM:V70.1', 'ICD9CM:V70.2', 'ICD9CM:V71.01', 'ICD9CM:V71.02', 'ICD9CM:V71.09', 'ICD9CM:V79.0', 'ICD9CM:V79.1', 'ICD9CM:V79.2', 'ICD9CM:V79.3', 'ICD9CM:V79.8', 'ICD9CM:V79.9'):
            results_ccs4["mental_screen"].append(1)
        else: results_ccs4["mental_screen"].append(0)
    print("Completed Binary Recode of: mental_screen")


    # Miscellaneous_mental_health_disorders
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:293.89', 'ICD9CM:293.9', 'ICD9CM:300.11', 'ICD9CM:300.12', 'ICD9CM:300.13', 'ICD9CM:300.14', 'ICD9CM:300.15', 'ICD9CM:300.16', 'ICD9CM:300.19', 'ICD9CM:300.6', 'ICD9CM:300.7', 'ICD9CM:300.81', 'ICD9CM:300.82', 'ICD9CM:302.1', 'ICD9CM:302.2', 'ICD9CM:302.3', 'ICD9CM:302.4', 'ICD9CM:302.50', 'ICD9CM:302.51', 'ICD9CM:302.52', 'ICD9CM:302.53', 'ICD9CM:302.6', 'ICD9CM:302.70', 'ICD9CM:302.71', 'ICD9CM:302.72', 'ICD9CM:302.73', 'ICD9CM:302.74', 'ICD9CM:302.75', 'ICD9CM:302.76', 'ICD9CM:302.79', 'ICD9CM:302.81', 'ICD9CM:302.82', 'ICD9CM:302.83', 'ICD9CM:302.84', 'ICD9CM:302.85', 'ICD9CM:302.89', 'ICD9CM:302.9', 'ICD9CM:306.0', 'ICD9CM:306.1', 'ICD9CM:306.2', 'ICD9CM:306.3', 'ICD9CM:306.4', 'ICD9CM:306.50', 'ICD9CM:306.51', 'ICD9CM:306.52', 'ICD9CM:306.53', 'ICD9CM:306.59', 'ICD9CM:306.6', 'ICD9CM:306.7', 'ICD9CM:306.8', 'ICD9CM:306.9', 'ICD9CM:307.1', 'ICD9CM:307.40', 'ICD9CM:307.41', 'ICD9CM:307.42', 'ICD9CM:307.43', 'ICD9CM:307.44', 'ICD9CM:307.45', 'ICD9CM:307.46', 'ICD9CM:307.47', 'ICD9CM:307.48', 'ICD9CM:307.49', 'ICD9CM:307.50', 'ICD9CM:307.51', 'ICD9CM:307.52', 'ICD9CM:307.53', 'ICD9CM:307.54', 'ICD9CM:307.59', 'ICD9CM:307.80', 'ICD9CM:307.81', 'ICD9CM:307.89', 'ICD9CM:310.1', 'ICD9CM:316', 'ICD9CM:648.40', 'ICD9CM:648.41', 'ICD9CM:648.42', 'ICD9CM:648.43', 'ICD9CM:648.44', 'ICD9CM:V40.2', 'ICD9CM:V40.3', 'ICD9CM:V40.31', 'ICD9CM:V40.39', 'ICD9CM:V40.9', 'ICD9CM:V67.3'):
            results_ccs4["misc_mental"].append(1)
        else: results_ccs4["misc_mental"].append(0)
    print("Completed Binary Recode of: misc_mental")

    # E_Codes:_Cut/_pierceb
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E920.0','ICD9CM:E920.1','ICD9CM:E920.2','ICD9CM:E920.3','ICD9CM:E920.4','ICD9CM:E920.5','ICD9CM:E920.8','ICD9CM:E920.9','ICD9CM:E966','ICD9CM:E974','ICD9CM:E986'):
            results_ccs4["e_cut_pierce"].append(1)
        else: results_ccs4["e_cut_pierce"].append(0)
    print("Completed Binary Recode of: e_cut_pierce")

    # E_Codes:_Drowning/_submersion
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E830.0','ICD9CM:E830.1','ICD9CM:E830.2','ICD9CM:E830.3','ICD9CM:E830.4','ICD9CM:E830.5','ICD9CM:E830.6','ICD9CM:E830.7','ICD9CM:E830.8','ICD9CM:E830.9','ICD9CM:E831.7','ICD9CM:E832.0','ICD9CM:E832.1','ICD9CM:E832.2','ICD9CM:E832.3','ICD9CM:E832.4','ICD9CM:E832.5','ICD9CM:E832.6','ICD9CM:E832.7','ICD9CM:E832.8','ICD9CM:E832.9','ICD9CM:E910.0','ICD9CM:E910.1','ICD9CM:E910.2','ICD9CM:E910.3','ICD9CM:E910.4','ICD9CM:E910.8','ICD9CM:E910.9','ICD9CM:E964','ICD9CM:E984'):
            results_ccs4["e_drown"].append(1)
        else: results_ccs4["e_drown"].append(0)
    print("Completed Binary Recode of: e_drown")

    # E_Codes:_Fall
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E880.0','ICD9CM:E880.1','ICD9CM:E880.9','ICD9CM:E881.0','ICD9CM:E881.1','ICD9CM:E882','ICD9CM:E883.0','ICD9CM:E883.1','ICD9CM:E883.2','ICD9CM:E883.9','ICD9CM:E884.0','ICD9CM:E884.1','ICD9CM:E884.2','ICD9CM:E884.3','ICD9CM:E884.4','ICD9CM:E884.5','ICD9CM:E884.6','ICD9CM:E884.9','ICD9CM:E885','ICD9CM:E885.0','ICD9CM:E885.1','ICD9CM:E885.2','ICD9CM:E885.3','ICD9CM:E885.4','ICD9CM:E885.9','ICD9CM:E886.0','ICD9CM:E886.9','ICD9CM:E888','ICD9CM:E888.0','ICD9CM:E888.1','ICD9CM:E888.8','ICD9CM:E888.9','ICD9CM:E968.1','ICD9CM:E987.0','ICD9CM:E987.1','ICD9CM:E987.2','ICD9CM:E987.9'):
            results_ccs4["e_fall"].append(1)
        else: results_ccs4["e_fall"].append(0)
    print("Completed Binary Recode of: e_fall")

    # E_Codes:_Fire/_burn
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E890.0','ICD9CM:E890.1','ICD9CM:E890.2','ICD9CM:E890.3','ICD9CM:E890.8','ICD9CM:E890.9','ICD9CM:E891.0','ICD9CM:E891.1','ICD9CM:E891.2','ICD9CM:E891.3','ICD9CM:E891.8','ICD9CM:E891.9','ICD9CM:E892','ICD9CM:E893.0','ICD9CM:E893.1','ICD9CM:E893.2','ICD9CM:E893.8','ICD9CM:E893.9','ICD9CM:E894','ICD9CM:E895','ICD9CM:E896','ICD9CM:E897','ICD9CM:E898.0','ICD9CM:E898.1','ICD9CM:E899','ICD9CM:E924.0','ICD9CM:E924.1','ICD9CM:E924.2','ICD9CM:E924.8','ICD9CM:E924.9','ICD9CM:E961','ICD9CM:E968.0','ICD9CM:E968.3','ICD9CM:E979.3','ICD9CM:E988.1','ICD9CM:E988.2','ICD9CM:E988.7'):
            results_ccs4["e_fire"].append(1)
        else: results_ccs4["e_fire"].append(0)
    print("Completed Binary Recode of: e_fire")

    # E_Codes:_Firearm
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E922.0','ICD9CM:E922.1','ICD9CM:E922.2','ICD9CM:E922.3','ICD9CM:E922.8','ICD9CM:E922.9','ICD9CM:E928.7','ICD9CM:E965.0','ICD9CM:E965.1','ICD9CM:E965.2','ICD9CM:E965.3','ICD9CM:E965.4','ICD9CM:E970','ICD9CM:E979.4','ICD9CM:E985.0','ICD9CM:E985.1','ICD9CM:E985.2','ICD9CM:E985.3','ICD9CM:E985.4'):
            results_ccs4["e_firearm"].append(1)
        else: results_ccs4["e_firearm"].append(0)
    print("Completed Binary Recode of: e_firearm")

    # E_Codes:_Machinery
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E919.0','ICD9CM:E919.1','ICD9CM:E919.2','ICD9CM:E919.3','ICD9CM:E919.4','ICD9CM:E919.5','ICD9CM:E919.6','ICD9CM:E919.7','ICD9CM:E919.8','ICD9CM:E919.9'):
            results_ccs4["e_machine"].append(1)
        else: results_ccs4["e_machine"].append(0)
    print("Completed Binary Recode of: e_machine")

    # E_Codes:_Motor_vehicle_traffic_(_MVT)
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E810.0','ICD9CM:E810.1','ICD9CM:E810.2','ICD9CM:E810.3','ICD9CM:E810.4','ICD9CM:E810.5','ICD9CM:E810.6','ICD9CM:E810.7','ICD9CM:E810.8','ICD9CM:E810.9','ICD9CM:E811.0','ICD9CM:E811.1','ICD9CM:E811.2','ICD9CM:E811.3','ICD9CM:E811.4','ICD9CM:E811.5','ICD9CM:E811.6','ICD9CM:E811.7','ICD9CM:E811.8','ICD9CM:E811.9','ICD9CM:E812.0','ICD9CM:E812.1','ICD9CM:E812.2','ICD9CM:E812.3','ICD9CM:E812.4','ICD9CM:E812.5','ICD9CM:E812.6','ICD9CM:E812.7','ICD9CM:E812.8','ICD9CM:E812.9','ICD9CM:E813.0','ICD9CM:E813.1','ICD9CM:E813.2','ICD9CM:E813.3','ICD9CM:E813.4','ICD9CM:E813.5','ICD9CM:E813.6','ICD9CM:E813.7','ICD9CM:E813.8','ICD9CM:E813.9','ICD9CM:E814.0','ICD9CM:E814.1','ICD9CM:E814.2','ICD9CM:E814.3','ICD9CM:E814.4','ICD9CM:E814.5','ICD9CM:E814.6','ICD9CM:E814.7','ICD9CM:E814.8','ICD9CM:E814.9','ICD9CM:E815.0','ICD9CM:E815.1','ICD9CM:E815.2','ICD9CM:E815.3','ICD9CM:E815.4','ICD9CM:E815.5','ICD9CM:E815.6','ICD9CM:E815.7','ICD9CM:E815.8','ICD9CM:E815.9','ICD9CM:E816.0','ICD9CM:E816.1','ICD9CM:E816.2','ICD9CM:E816.3','ICD9CM:E816.4','ICD9CM:E816.5','ICD9CM:E816.6','ICD9CM:E816.7','ICD9CM:E816.8','ICD9CM:E816.9','ICD9CM:E817.0','ICD9CM:E817.1','ICD9CM:E817.2','ICD9CM:E817.3','ICD9CM:E817.4','ICD9CM:E817.5','ICD9CM:E817.6','ICD9CM:E817.7','ICD9CM:E817.8','ICD9CM:E817.9','ICD9CM:E818.0','ICD9CM:E818.1','ICD9CM:E818.2','ICD9CM:E818.3','ICD9CM:E818.4','ICD9CM:E818.5','ICD9CM:E818.6','ICD9CM:E818.7','ICD9CM:E818.8','ICD9CM:E818.9','ICD9CM:E819.0','ICD9CM:E819.1','ICD9CM:E819.2','ICD9CM:E819.3','ICD9CM:E819.4','ICD9CM:E819.5','ICD9CM:E819.6','ICD9CM:E819.7','ICD9CM:E819.8','ICD9CM:E819.9','ICD9CM:E968.5','ICD9CM:E988.5'):
            results_ccs4["e_mvt"].append(1)
        else: results_ccs4["e_mvt"].append(0)
    print("Completed Binary Recode of: e_mvt")

    # E_Codes:_Pedal_cyclist;_not_MVT
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E800.3','ICD9CM:E801.3','ICD9CM:E802.3','ICD9CM:E803.3','ICD9CM:E804.3','ICD9CM:E805.3','ICD9CM:E806.3','ICD9CM:E807.3','ICD9CM:E820.6','ICD9CM:E821.6','ICD9CM:E822.6','ICD9CM:E823.6','ICD9CM:E824.6','ICD9CM:E825.6','ICD9CM:E826.1','ICD9CM:E826.9'):
            results_ccs4["e_cyclist"].append(1)
        else: results_ccs4["e_cyclist"].append(0)
    print("Completed Binary Recode of: e_cyclist")

    # E_Codes:_Pedestrian;_not_MVT
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E800.2','ICD9CM:E801.2','ICD9CM:E802.2','ICD9CM:E803.2','ICD9CM:E804.2','ICD9CM:E805.2','ICD9CM:E806.2','ICD9CM:E807.2','ICD9CM:E820.7','ICD9CM:E821.7','ICD9CM:E822.7','ICD9CM:E823.7','ICD9CM:E824.7','ICD9CM:E825.7','ICD9CM:E826.0','ICD9CM:E827.0','ICD9CM:E828.0','ICD9CM:E829.0'):
            results_ccs4["e_pedestrian"].append(1)
        else: results_ccs4["e_pedestrian"].append(0)
    print("Completed Binary Recode of: e_pedestrian")

    # E_Codes:_Transport;_not_MVT
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E800.0','ICD9CM:E800.1','ICD9CM:E800.8','ICD9CM:E800.9','ICD9CM:E801.0','ICD9CM:E801.1','ICD9CM:E801.8','ICD9CM:E801.9','ICD9CM:E802.0','ICD9CM:E802.1','ICD9CM:E802.8','ICD9CM:E802.9','ICD9CM:E803.0','ICD9CM:E803.1','ICD9CM:E803.8','ICD9CM:E803.9','ICD9CM:E804.0','ICD9CM:E804.1','ICD9CM:E804.8','ICD9CM:E804.9','ICD9CM:E805.0','ICD9CM:E805.1','ICD9CM:E805.8','ICD9CM:E805.9','ICD9CM:E806.0','ICD9CM:E806.1','ICD9CM:E806.8','ICD9CM:E806.9','ICD9CM:E807.0','ICD9CM:E807.1','ICD9CM:E807.8','ICD9CM:E807.9','ICD9CM:E820.0','ICD9CM:E820.1','ICD9CM:E820.2','ICD9CM:E820.3','ICD9CM:E820.4','ICD9CM:E820.5','ICD9CM:E820.8','ICD9CM:E820.9','ICD9CM:E821.0','ICD9CM:E821.1','ICD9CM:E821.2','ICD9CM:E821.3','ICD9CM:E821.4','ICD9CM:E821.5','ICD9CM:E821.8','ICD9CM:E821.9','ICD9CM:E822.0','ICD9CM:E822.1','ICD9CM:E822.2','ICD9CM:E822.3','ICD9CM:E822.4','ICD9CM:E822.5','ICD9CM:E822.8','ICD9CM:E822.9','ICD9CM:E823.0','ICD9CM:E823.1','ICD9CM:E823.2','ICD9CM:E823.3','ICD9CM:E823.4','ICD9CM:E823.5','ICD9CM:E823.8','ICD9CM:E823.9','ICD9CM:E824.0','ICD9CM:E824.1','ICD9CM:E824.2','ICD9CM:E824.3','ICD9CM:E824.4','ICD9CM:E824.5','ICD9CM:E824.8','ICD9CM:E824.9','ICD9CM:E825.0','ICD9CM:E825.1','ICD9CM:E825.2','ICD9CM:E825.3','ICD9CM:E825.4','ICD9CM:E825.5','ICD9CM:E825.8','ICD9CM:E825.9','ICD9CM:E826.2','ICD9CM:E826.3','ICD9CM:E826.4','ICD9CM:E826.8','ICD9CM:E827.2','ICD9CM:E827.3','ICD9CM:E827.4','ICD9CM:E827.8','ICD9CM:E827.9','ICD9CM:E828.2','ICD9CM:E828.4','ICD9CM:E828.8','ICD9CM:E828.9','ICD9CM:E829.4','ICD9CM:E829.8','ICD9CM:E829.9','ICD9CM:E831.0','ICD9CM:E831.1','ICD9CM:E831.2','ICD9CM:E831.3','ICD9CM:E831.4','ICD9CM:E831.5','ICD9CM:E831.6','ICD9CM:E831.8','ICD9CM:E831.9','ICD9CM:E833.0','ICD9CM:E833.1','ICD9CM:E833.2','ICD9CM:E833.3','ICD9CM:E833.4','ICD9CM:E833.5','ICD9CM:E833.6','ICD9CM:E833.7','ICD9CM:E833.8','ICD9CM:E833.9','ICD9CM:E834.0','ICD9CM:E834.1','ICD9CM:E834.2','ICD9CM:E834.3','ICD9CM:E834.4','ICD9CM:E834.5','ICD9CM:E834.6','ICD9CM:E834.7','ICD9CM:E834.8','ICD9CM:E834.9','ICD9CM:E835.0','ICD9CM:E835.1','ICD9CM:E835.2','ICD9CM:E835.3','ICD9CM:E835.4','ICD9CM:E835.5','ICD9CM:E835.6','ICD9CM:E835.7','ICD9CM:E835.8','ICD9CM:E835.9','ICD9CM:E836.0','ICD9CM:E836.1','ICD9CM:E836.2','ICD9CM:E836.3','ICD9CM:E836.4','ICD9CM:E836.5','ICD9CM:E836.6','ICD9CM:E836.7','ICD9CM:E836.8','ICD9CM:E836.9','ICD9CM:E837.0','ICD9CM:E837.1','ICD9CM:E837.2','ICD9CM:E837.3','ICD9CM:E837.4','ICD9CM:E837.5','ICD9CM:E837.6','ICD9CM:E837.7','ICD9CM:E837.8','ICD9CM:E837.9','ICD9CM:E838.0','ICD9CM:E838.1','ICD9CM:E838.2','ICD9CM:E838.3','ICD9CM:E838.4','ICD9CM:E838.5','ICD9CM:E838.6','ICD9CM:E838.7','ICD9CM:E838.8','ICD9CM:E838.9','ICD9CM:E840.0','ICD9CM:E840.1','ICD9CM:E840.2','ICD9CM:E840.3','ICD9CM:E840.4','ICD9CM:E840.5','ICD9CM:E840.6','ICD9CM:E840.7','ICD9CM:E840.8','ICD9CM:E840.9','ICD9CM:E841.0','ICD9CM:E841.1','ICD9CM:E841.2','ICD9CM:E841.3','ICD9CM:E841.4','ICD9CM:E841.5','ICD9CM:E841.6','ICD9CM:E841.7','ICD9CM:E841.8','ICD9CM:E841.9','ICD9CM:E842.6','ICD9CM:E842.7','ICD9CM:E842.8','ICD9CM:E842.9','ICD9CM:E843.0','ICD9CM:E843.1','ICD9CM:E843.2','ICD9CM:E843.3','ICD9CM:E843.4','ICD9CM:E843.5','ICD9CM:E843.6','ICD9CM:E843.7','ICD9CM:E843.8','ICD9CM:E843.9','ICD9CM:E844.0','ICD9CM:E844.1','ICD9CM:E844.2','ICD9CM:E844.3','ICD9CM:E844.4','ICD9CM:E844.5','ICD9CM:E844.6','ICD9CM:E844.7','ICD9CM:E844.8','ICD9CM:E844.9','ICD9CM:E845.0','ICD9CM:E845.8','ICD9CM:E845.9','ICD9CM:E988.6'):
            results_ccs4["e_transport"].append(1)
        else: results_ccs4["e_transport"].append(0)
    print("Completed Binary Recode of: e_transport")

    # E_Codes:_Natural/_environment
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E900.0','ICD9CM:E900.1','ICD9CM:E900.9','ICD9CM:E901.0','ICD9CM:E901.1','ICD9CM:E901.8','ICD9CM:E901.9','ICD9CM:E902.0','ICD9CM:E902.1','ICD9CM:E902.2','ICD9CM:E902.8','ICD9CM:E902.9','ICD9CM:E903','ICD9CM:E904.0','ICD9CM:E904.1','ICD9CM:E904.2','ICD9CM:E904.3','ICD9CM:E904.9','ICD9CM:E905.0','ICD9CM:E905.1','ICD9CM:E905.2','ICD9CM:E905.3','ICD9CM:E905.4','ICD9CM:E905.5','ICD9CM:E905.6','ICD9CM:E905.7','ICD9CM:E905.8','ICD9CM:E905.9','ICD9CM:E906.0','ICD9CM:E906.1','ICD9CM:E906.2','ICD9CM:E906.3','ICD9CM:E906.4','ICD9CM:E906.5','ICD9CM:E906.8','ICD9CM:E906.9','ICD9CM:E907','ICD9CM:E908','ICD9CM:E908.0','ICD9CM:E908.1','ICD9CM:E908.2','ICD9CM:E908.3','ICD9CM:E908.4','ICD9CM:E908.8','ICD9CM:E908.9','ICD9CM:E909','ICD9CM:E909.0','ICD9CM:E909.1','ICD9CM:E909.2','ICD9CM:E909.3','ICD9CM:E909.4','ICD9CM:E909.8','ICD9CM:E909.9','ICD9CM:E928.0','ICD9CM:E928.1','ICD9CM:E928.2','ICD9CM:E988.3'):
            results_ccs4["e_natural"].append(1)
        else: results_ccs4["e_natural"].append(0)
    print("Completed Binary Recode of: e_natural")

    # E_Codes:_Overexertion
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E927','ICD9CM:E927.0','ICD9CM:E927.1','ICD9CM:E927.2','ICD9CM:E927.3','ICD9CM:E927.8','ICD9CM:E927.9'):
            results_ccs4["e_overexert"].append(1)
        else: results_ccs4["e_overexert"].append(0)
    print("Completed Binary Recode of: e_overexert")

    # E_Codes:_Poisoning
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E850.0','ICD9CM:E850.1','ICD9CM:E850.2','ICD9CM:E850.3','ICD9CM:E850.4','ICD9CM:E850.5','ICD9CM:E850.6','ICD9CM:E850.7','ICD9CM:E850.8','ICD9CM:E850.9','ICD9CM:E851','ICD9CM:E852.0','ICD9CM:E852.1','ICD9CM:E852.2','ICD9CM:E852.3','ICD9CM:E852.4','ICD9CM:E852.5','ICD9CM:E852.8','ICD9CM:E852.9','ICD9CM:E853.0','ICD9CM:E853.1','ICD9CM:E853.2','ICD9CM:E853.8','ICD9CM:E853.9','ICD9CM:E854.0','ICD9CM:E854.1','ICD9CM:E854.2','ICD9CM:E854.3','ICD9CM:E854.8','ICD9CM:E855.0','ICD9CM:E855.1','ICD9CM:E855.2','ICD9CM:E855.3','ICD9CM:E855.4','ICD9CM:E855.5','ICD9CM:E855.6','ICD9CM:E855.8','ICD9CM:E855.9','ICD9CM:E856','ICD9CM:E857','ICD9CM:E858.0','ICD9CM:E858.1','ICD9CM:E858.2','ICD9CM:E858.3','ICD9CM:E858.4','ICD9CM:E858.5','ICD9CM:E858.6','ICD9CM:E858.7','ICD9CM:E858.8','ICD9CM:E858.9','ICD9CM:E860.0','ICD9CM:E860.1','ICD9CM:E860.2','ICD9CM:E860.3','ICD9CM:E860.4','ICD9CM:E860.8','ICD9CM:E860.9','ICD9CM:E861.0','ICD9CM:E861.1','ICD9CM:E861.2','ICD9CM:E861.3','ICD9CM:E861.4','ICD9CM:E861.5','ICD9CM:E861.6','ICD9CM:E861.9','ICD9CM:E862.0','ICD9CM:E862.1','ICD9CM:E862.2','ICD9CM:E862.3','ICD9CM:E862.4','ICD9CM:E862.9','ICD9CM:E863.0','ICD9CM:E863.1','ICD9CM:E863.2','ICD9CM:E863.3','ICD9CM:E863.4','ICD9CM:E863.5','ICD9CM:E863.6','ICD9CM:E863.7','ICD9CM:E863.8','ICD9CM:E863.9','ICD9CM:E864.0','ICD9CM:E864.1','ICD9CM:E864.2','ICD9CM:E864.3','ICD9CM:E864.4','ICD9CM:E865.0','ICD9CM:E865.1','ICD9CM:E865.2','ICD9CM:E865.3','ICD9CM:E865.4','ICD9CM:E865.5','ICD9CM:E865.8','ICD9CM:E865.9','ICD9CM:E866.0','ICD9CM:E866.1','ICD9CM:E866.2','ICD9CM:E866.3','ICD9CM:E866.4','ICD9CM:E866.5','ICD9CM:E866.6','ICD9CM:E866.7','ICD9CM:E866.8','ICD9CM:E866.9','ICD9CM:E867','ICD9CM:E868.0','ICD9CM:E868.1','ICD9CM:E868.2','ICD9CM:E868.3','ICD9CM:E868.8','ICD9CM:E868.9','ICD9CM:E869.0','ICD9CM:E869.1','ICD9CM:E869.2','ICD9CM:E869.3','ICD9CM:E869.4','ICD9CM:E869.8','ICD9CM:E869.9','ICD9CM:E962.0','ICD9CM:E962.1','ICD9CM:E962.2','ICD9CM:E962.9','ICD9CM:E972','ICD9CM:E980.0','ICD9CM:E980.1','ICD9CM:E980.2','ICD9CM:E980.3','ICD9CM:E980.4','ICD9CM:E980.5','ICD9CM:E980.6','ICD9CM:E980.7','ICD9CM:E980.8','ICD9CM:E980.9','ICD9CM:E981.0','ICD9CM:E981.1','ICD9CM:E981.8','ICD9CM:E982.0','ICD9CM:E982.1','ICD9CM:E982.8','ICD9CM:E982.9'):
            results_ccs4["e_poison"].append(1)
        else: results_ccs4["e_poison"].append(0)
    print("Completed Binary Recode of: e_poison")

    # E_Codes:_Struck_by;_against
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E916','ICD9CM:E917.0','ICD9CM:E917.1','ICD9CM:E917.2','ICD9CM:E917.3','ICD9CM:E917.4','ICD9CM:E917.5','ICD9CM:E917.6','ICD9CM:E917.7','ICD9CM:E917.8','ICD9CM:E917.9','ICD9CM:E927.4','ICD9CM:E960.0','ICD9CM:E968.2','ICD9CM:E973','ICD9CM:E975'):
            results_ccs4["e_struckby"].append(1)
        else: results_ccs4["e_struckby"].append(0)
    print("Completed Binary Recode of: e_struckby")

    # E_Codes:_Suffocation
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E911','ICD9CM:E912','ICD9CM:E913.0','ICD9CM:E913.1','ICD9CM:E913.2','ICD9CM:E913.3','ICD9CM:E913.8','ICD9CM:E913.9','ICD9CM:E928.4','ICD9CM:E928.5','ICD9CM:E963','ICD9CM:E983.0','ICD9CM:E983.1','ICD9CM:E983.8','ICD9CM:E983.9'):
            results_ccs4["e_suffocate"].append(1)
        else: results_ccs4["e_suffocate"].append(0)
    print("Completed Binary Recode of: e_suffocate")

    # E_Codes:_Adverse_effects_of_medical_care
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E870.0','ICD9CM:E870.1','ICD9CM:E870.2','ICD9CM:E870.3','ICD9CM:E870.4','ICD9CM:E870.5','ICD9CM:E870.6','ICD9CM:E870.7','ICD9CM:E870.8','ICD9CM:E870.9','ICD9CM:E871.0','ICD9CM:E871.1','ICD9CM:E871.2','ICD9CM:E871.3','ICD9CM:E871.4','ICD9CM:E871.5','ICD9CM:E871.6','ICD9CM:E871.7','ICD9CM:E871.8','ICD9CM:E871.9','ICD9CM:E872.0','ICD9CM:E872.1','ICD9CM:E872.2','ICD9CM:E872.3','ICD9CM:E872.4','ICD9CM:E872.5','ICD9CM:E872.6','ICD9CM:E872.8','ICD9CM:E872.9','ICD9CM:E873.0','ICD9CM:E873.1','ICD9CM:E873.2','ICD9CM:E873.3','ICD9CM:E873.4','ICD9CM:E873.5','ICD9CM:E873.6','ICD9CM:E873.8','ICD9CM:E873.9','ICD9CM:E874.0','ICD9CM:E874.1','ICD9CM:E874.2','ICD9CM:E874.3','ICD9CM:E874.4','ICD9CM:E874.5','ICD9CM:E874.8','ICD9CM:E874.9','ICD9CM:E875.0','ICD9CM:E875.1','ICD9CM:E875.2','ICD9CM:E875.8','ICD9CM:E875.9','ICD9CM:E876.0','ICD9CM:E876.1','ICD9CM:E876.2','ICD9CM:E876.3','ICD9CM:E876.4','ICD9CM:E876.5','ICD9CM:E876.6','ICD9CM:E876.7','ICD9CM:E876.8','ICD9CM:E876.9','ICD9CM:E878.0','ICD9CM:E878.1','ICD9CM:E878.2','ICD9CM:E878.3','ICD9CM:E878.4','ICD9CM:E878.5','ICD9CM:E878.6','ICD9CM:E878.8','ICD9CM:E878.9','ICD9CM:E879.0','ICD9CM:E879.1','ICD9CM:E879.2','ICD9CM:E879.3','ICD9CM:E879.4','ICD9CM:E879.5','ICD9CM:E879.6','ICD9CM:E879.7','ICD9CM:E879.8','ICD9CM:E879.9'):
            results_ccs4["e_ae_med_care"].append(1)
        else: results_ccs4["e_ae_med_care"].append(0)
    print("Completed Binary Recode of: e_ae_med_care")

    # E_Codes:_Adverse_effects_of_medical_drugs
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E930.0','ICD9CM:E930.1','ICD9CM:E930.2','ICD9CM:E930.3','ICD9CM:E930.4','ICD9CM:E930.5','ICD9CM:E930.6','ICD9CM:E930.7','ICD9CM:E930.8','ICD9CM:E930.9','ICD9CM:E931.0','ICD9CM:E931.1','ICD9CM:E931.2','ICD9CM:E931.3','ICD9CM:E931.4','ICD9CM:E931.5','ICD9CM:E931.6','ICD9CM:E931.7','ICD9CM:E931.8','ICD9CM:E931.9','ICD9CM:E932.0','ICD9CM:E932.1','ICD9CM:E932.2','ICD9CM:E932.3','ICD9CM:E932.4','ICD9CM:E932.5','ICD9CM:E932.6','ICD9CM:E932.7','ICD9CM:E932.8','ICD9CM:E932.9','ICD9CM:E933.0','ICD9CM:E933.1','ICD9CM:E933.2','ICD9CM:E933.3','ICD9CM:E933.4','ICD9CM:E933.5','ICD9CM:E933.6','ICD9CM:E933.7','ICD9CM:E933.8','ICD9CM:E933.9','ICD9CM:E934.0','ICD9CM:E934.1','ICD9CM:E934.2','ICD9CM:E934.3','ICD9CM:E934.4','ICD9CM:E934.5','ICD9CM:E934.6','ICD9CM:E934.7','ICD9CM:E934.8','ICD9CM:E934.9','ICD9CM:E935.0','ICD9CM:E935.1','ICD9CM:E935.2','ICD9CM:E935.3','ICD9CM:E935.4','ICD9CM:E935.5','ICD9CM:E935.6','ICD9CM:E935.7','ICD9CM:E935.8','ICD9CM:E935.9','ICD9CM:E936.0','ICD9CM:E936.1','ICD9CM:E936.2','ICD9CM:E936.3','ICD9CM:E936.4','ICD9CM:E937.0','ICD9CM:E937.1','ICD9CM:E937.2','ICD9CM:E937.3','ICD9CM:E937.4','ICD9CM:E937.5','ICD9CM:E937.6','ICD9CM:E937.8','ICD9CM:E937.9','ICD9CM:E938.0','ICD9CM:E938.1','ICD9CM:E938.2','ICD9CM:E938.3','ICD9CM:E938.4','ICD9CM:E938.5','ICD9CM:E938.6','ICD9CM:E938.7','ICD9CM:E938.9','ICD9CM:E939.0','ICD9CM:E939.1','ICD9CM:E939.2','ICD9CM:E939.3','ICD9CM:E939.4','ICD9CM:E939.5','ICD9CM:E939.6','ICD9CM:E939.7','ICD9CM:E939.8','ICD9CM:E939.9','ICD9CM:E940.0','ICD9CM:E940.1','ICD9CM:E940.8','ICD9CM:E940.9','ICD9CM:E941.0','ICD9CM:E941.1','ICD9CM:E941.2','ICD9CM:E941.3','ICD9CM:E941.9','ICD9CM:E942.0','ICD9CM:E942.1','ICD9CM:E942.2','ICD9CM:E942.3','ICD9CM:E942.4','ICD9CM:E942.5','ICD9CM:E942.6','ICD9CM:E942.7','ICD9CM:E942.8','ICD9CM:E942.9','ICD9CM:E943.0','ICD9CM:E943.1','ICD9CM:E943.2','ICD9CM:E943.3','ICD9CM:E943.4','ICD9CM:E943.5','ICD9CM:E943.6','ICD9CM:E943.8','ICD9CM:E943.9','ICD9CM:E944.0','ICD9CM:E944.1','ICD9CM:E944.2','ICD9CM:E944.3','ICD9CM:E944.4','ICD9CM:E944.5','ICD9CM:E944.6','ICD9CM:E944.7','ICD9CM:E945.0','ICD9CM:E945.1','ICD9CM:E945.2','ICD9CM:E945.3','ICD9CM:E945.4','ICD9CM:E945.5','ICD9CM:E945.6','ICD9CM:E945.7','ICD9CM:E945.8','ICD9CM:E946.0','ICD9CM:E946.1','ICD9CM:E946.2','ICD9CM:E946.3','ICD9CM:E946.4','ICD9CM:E946.5','ICD9CM:E946.6','ICD9CM:E946.7','ICD9CM:E946.8','ICD9CM:E946.9','ICD9CM:E947.0','ICD9CM:E947.1','ICD9CM:E947.2','ICD9CM:E947.3','ICD9CM:E947.4','ICD9CM:E947.8','ICD9CM:E947.9','ICD9CM:E948.0','ICD9CM:E948.1','ICD9CM:E948.2','ICD9CM:E948.3','ICD9CM:E948.4','ICD9CM:E948.5','ICD9CM:E948.6','ICD9CM:E948.8','ICD9CM:E948.9','ICD9CM:E949.0','ICD9CM:E949.1','ICD9CM:E949.2','ICD9CM:E949.3','ICD9CM:E949.4','ICD9CM:E949.5','ICD9CM:E949.6','ICD9CM:E949.7','ICD9CM:E949.9'):
            results_ccs4["e_ae_med_drug"].append(1)
        else: results_ccs4["e_ae_med_drug"].append(0)
    print("Completed Binary Recode of: e_ae_med_drug")

    # E_Codes:_Other_specified_and_classifiable
    for _ in df['condition_source_value']:
        if _ in (
        'ICD9CM:E846','ICD9CM:E847','ICD9CM:E848','ICD9CM:E914','ICD9CM:E915','ICD9CM:E918','ICD9CM:E921.0','ICD9CM:E921.1','ICD9CM:E921.8','ICD9CM:E921.9','ICD9CM:E922.4','ICD9CM:E922.5','ICD9CM:E923.0','ICD9CM:E923.1','ICD9CM:E923.2','ICD9CM:E923.8','ICD9CM:E923.9','ICD9CM:E925.0','ICD9CM:E925.1','ICD9CM:E925.2','ICD9CM:E925.8','ICD9CM:E925.9','ICD9CM:E926.0','ICD9CM:E926.1','ICD9CM:E926.2','ICD9CM:E926.3','ICD9CM:E926.4','ICD9CM:E926.5','ICD9CM:E926.8','ICD9CM:E926.9','ICD9CM:E928.3','ICD9CM:E929.0','ICD9CM:E929.1','ICD9CM:E929.2','ICD9CM:E929.3','ICD9CM:E929.4','ICD9CM:E929.5','ICD9CM:E960.1','ICD9CM:E965.5','ICD9CM:E965.6','ICD9CM:E965.7','ICD9CM:E965.8','ICD9CM:E965.9','ICD9CM:E967.0','ICD9CM:E967.1','ICD9CM:E967.2','ICD9CM:E967.3','ICD9CM:E967.4','ICD9CM:E967.5','ICD9CM:E967.6','ICD9CM:E967.7','ICD9CM:E967.8','ICD9CM:E967.9','ICD9CM:E968.4','ICD9CM:E968.6','ICD9CM:E968.7','ICD9CM:E971','ICD9CM:E978','ICD9CM:E979.0','ICD9CM:E979.1','ICD9CM:E979.2','ICD9CM:E979.5','ICD9CM:E979.6','ICD9CM:E979.7','ICD9CM:E979.8','ICD9CM:E979.9','ICD9CM:E985.5','ICD9CM:E985.6','ICD9CM:E985.7','ICD9CM:E988.0','ICD9CM:E988.4','ICD9CM:E990.0','ICD9CM:E990.1','ICD9CM:E990.2','ICD9CM:E990.3','ICD9CM:E990.9','ICD9CM:E991.0','ICD9CM:E991.1','ICD9CM:E991.2','ICD9CM:E991.3','ICD9CM:E991.4','ICD9CM:E991.5','ICD9CM:E991.6','ICD9CM:E991.7','ICD9CM:E991.8','ICD9CM:E991.9','ICD9CM:E992','ICD9CM:E992.0','ICD9CM:E992.1','ICD9CM:E992.2','ICD9CM:E992.3','ICD9CM:E992.8','ICD9CM:E992.9','ICD9CM:E993','ICD9CM:E993.0','ICD9CM:E993.1','ICD9CM:E993.2','ICD9CM:E993.3','ICD9CM:E993.4','ICD9CM:E993.5','ICD9CM:E993.6','ICD9CM:E993.7','ICD9CM:E993.8','ICD9CM:E993.9','ICD9CM:E994','ICD9CM:E994.0','ICD9CM:E994.1','ICD9CM:E994.2','ICD9CM:E994.3','ICD9CM:E994.8','ICD9CM:E994.9','ICD9CM:E995.0','ICD9CM:E995.1','ICD9CM:E995.2','ICD9CM:E995.3','ICD9CM:E995.4','ICD9CM:E995.8','ICD9CM:E995.9','ICD9CM:E996','ICD9CM:E996.0','ICD9CM:E996.1','ICD9CM:E996.2','ICD9CM:E996.3','ICD9CM:E996.8','ICD9CM:E996.9','ICD9CM:E997.0','ICD9CM:E997.1','ICD9CM:E997.2','ICD9CM:E997.3','ICD9CM:E998.0','ICD9CM:E998.1','ICD9CM:E998.8','ICD9CM:E998.9','ICD9CM:E999.0','ICD9CM:E999.1'):
            results_ccs4["e_other_class"].append(1)
        else: results_ccs4["e_other_class"].append(0)
    print("Completed Binary Recode of: e_other_class")

    # E_Codes:_Other_specified;_NEC
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E928.6','ICD9CM:E928.8','ICD9CM:E929.8','ICD9CM:E968.8','ICD9CM:E969','ICD9CM:E977','ICD9CM:E988.8','ICD9CM:E989','ICD9CM:E995','ICD9CM:E997.8','ICD9CM:E998','ICD9CM:E999'):
            results_ccs4["e_other_nec"].append(1)
        else: results_ccs4["e_other_nec"].append(0)
    print("Completed Binary Recode of: e_other_nec")

    # E_Codes:_Unspecified
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E000.0','ICD9CM:E000.1','ICD9CM:E000.2','ICD9CM:E000.8','ICD9CM:E000.9','ICD9CM:E001.0','ICD9CM:E001.1','ICD9CM:E002.0','ICD9CM:E002.1','ICD9CM:E002.2','ICD9CM:E002.3','ICD9CM:E002.4','ICD9CM:E002.5','ICD9CM:E002.6','ICD9CM:E002.7','ICD9CM:E002.8','ICD9CM:E002.9','ICD9CM:E003.0','ICD9CM:E003.1','ICD9CM:E003.2','ICD9CM:E003.3','ICD9CM:E003.9','ICD9CM:E004.0','ICD9CM:E004.1','ICD9CM:E004.2','ICD9CM:E004.3','ICD9CM:E004.4','ICD9CM:E004.9','ICD9CM:E005.0','ICD9CM:E005.1','ICD9CM:E005.2','ICD9CM:E005.3','ICD9CM:E005.4','ICD9CM:E005.9','ICD9CM:E006.0','ICD9CM:E006.1','ICD9CM:E006.2','ICD9CM:E006.3','ICD9CM:E006.4','ICD9CM:E006.5','ICD9CM:E006.6','ICD9CM:E006.9','ICD9CM:E007.0','ICD9CM:E007.1','ICD9CM:E007.2','ICD9CM:E007.3','ICD9CM:E007.4','ICD9CM:E007.5','ICD9CM:E007.6','ICD9CM:E007.7','ICD9CM:E007.8','ICD9CM:E007.9','ICD9CM:E008.0','ICD9CM:E008.1','ICD9CM:E008.2','ICD9CM:E008.3','ICD9CM:E008.4','ICD9CM:E008.9','ICD9CM:E009.0','ICD9CM:E009.1','ICD9CM:E009.2','ICD9CM:E009.3','ICD9CM:E009.4','ICD9CM:E009.5','ICD9CM:E009.9','ICD9CM:E010.0','ICD9CM:E010.1','ICD9CM:E010.2','ICD9CM:E010.3','ICD9CM:E010.9','ICD9CM:E011.0','ICD9CM:E011.1','ICD9CM:E011.9','ICD9CM:E012.0','ICD9CM:E012.1','ICD9CM:E012.2','ICD9CM:E012.9','ICD9CM:E013.0','ICD9CM:E013.1','ICD9CM:E013.2','ICD9CM:E013.3','ICD9CM:E013.4','ICD9CM:E013.5','ICD9CM:E013.8','ICD9CM:E013.9','ICD9CM:E014.0','ICD9CM:E014.1','ICD9CM:E014.9','ICD9CM:E015.0','ICD9CM:E015.1','ICD9CM:E015.2','ICD9CM:E015.9','ICD9CM:E016.0','ICD9CM:E016.1','ICD9CM:E016.2','ICD9CM:E016.9','ICD9CM:E017.0','ICD9CM:E017.9','ICD9CM:E018.0','ICD9CM:E018.1','ICD9CM:E018.2','ICD9CM:E018.3','ICD9CM:E019.0','ICD9CM:E019.1','ICD9CM:E019.2','ICD9CM:E019.9','ICD9CM:E029.0','ICD9CM:E029.1','ICD9CM:E029.2','ICD9CM:E029.9','ICD9CM:E030','ICD9CM:E887','ICD9CM:E928.9','ICD9CM:E929.9','ICD9CM:E968.9','ICD9CM:E976','ICD9CM:E988.9','ICD9CM:E997.9'):
            results_ccs4["e_unspecified"].append(1)
        else: results_ccs4["e_unspecified"].append(0)
    print("Completed Binary Recode of: e_unspecified")

    # E_Codes:_Place_of_occurrence
    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:E849.0','ICD9CM:E849.1','ICD9CM:E849.2','ICD9CM:E849.3','ICD9CM:E849.4','ICD9CM:E849.5','ICD9CM:E849.6','ICD9CM:E849.7','ICD9CM:E849.8','ICD9CM:E849.9'):
            results_ccs4["e_place"].append(1)
        else: results_ccs4["e_place"].append(0)
    print("Completed Binary Recode of: e_place")

    pd.DataFrame(results_ccs4).to_csv(output_filepath, encoding='utf-8')
    print("CDRN - CCS Dx Recode Part 4: Complete")
    print("")



dx_convert1(cdrn_dx)

dx_convert2(cdrn_dx)

dx_convert3(cdrn_dx)

dx_convert4(cdrn_dx)