import pandas as pd
import datetime as dt


cdrn_prevent_hosp_2014_sql = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_2014_3.csv', encoding='utf-8', names=['person_id', 'visit_start_date', 'visit_concept_id', 'visit_occurrence_id', 'condition_source_value', 'condition_type_concept_id', 'procedure_source_value'])

cdrn_prevent_hosp_bef_2014_sql = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_bef_2014_3.csv', encoding='utf-8', names=['person_id', 'visit_start_date', 'visit_concept_id', 'visit_occurrence_id', 'condition_source_value', 'condition_type_concept_id', 'procedure_source_value'])

# ============================================= #
#
# START CREATION OF 1ST PREVENTABLE HOSP IN 2014 FILE
#
# ============================================= #

# Sorts df by 'person_id' and 'visit_start_date'
cdrn_prevent_hosp_2014_sql = cdrn_prevent_hosp_2014_sql.sort_values(by=['person_id','visit_occurrence_id'])
print("Length and Number of unique person_id's with any preventable hospitalization in 2014: ", len(cdrn_prevent_hosp_2014_sql),", ",cdrn_prevent_hosp_2014_sql.person_id.nunique())
print("Number of potential preventable visits during 2014: ", cdrn_prevent_hosp_2014_sql.visit_occurrence_id.nunique())

# Sorts df by 'person_id' and 'visit_start_date'
cdrn_prevent_hosp_bef_2014_sql = cdrn_prevent_hosp_bef_2014_sql.sort_values(by=['person_id','visit_occurrence_id'])
print("Length and Number of unique person_id's with any preventable hospitalization in 2014: ", len(cdrn_prevent_hosp_bef_2014_sql),", ",cdrn_prevent_hosp_bef_2014_sql.person_id.nunique())
print("Number of potential preventable visits before 2014: ", cdrn_prevent_hosp_bef_2014_sql.visit_occurrence_id.nunique())

# Composite PQI
pqi_results1 = {"visit_occurrence_id":[], "dm_comp_st":[], "appendix":[], "dm_comp_lt":[], "htn":[], "hf":[],  "dm_no_comp":[], "lower_amputate":[], "diabetes":[], "asthma":[], "uti":[], "bact_pneu":[], "dehydration":[], "copd":[], "htn_exclude":[], "amp_exclude":[], "asth_exclude":[], "uti_exclude":[], "bac_exclude":[], "dehyd_exclude":[], "copd_exclude":[], "immunocomp":[], "immuno_proc":[], "cardiac_proc":[], "dialysis_access":[]}

pqi_results2 = {"visit_occurrence_id":[], "dm_comp_st":[], "appendix":[], "dm_comp_lt":[], "htn":[], "hf":[], "dm_no_comp":[], "lower_amputate":[], "diabetes":[], "asthma":[], "uti":[], "bact_pneu":[], "dehydration":[], "copd":[], "htn_exclude":[], "amp_exclude":[], "asth_exclude":[], "uti_exclude":[], "bac_exclude":[], "dehyd_exclude":[], "copd_exclude":[], "immunocomp":[], "immuno_proc":[], "cardiac_proc":[], "dialysis_access":[]}


# Reset Index
cdrn_prevent_hosp_2014_sql = cdrn_prevent_hosp_2014_sql.reset_index(drop=True)
cdrn_prevent_hosp_bef_2014_sql = cdrn_prevent_hosp_bef_2014_sql.reset_index(drop=True)


#####################
#####################
print("")
#####################
#####################

# This function will establish the PQI variables and define the rules
def pqi(df):
    output_filepath =  '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/pqi_results_1.csv'

    for _ in df['visit_occurrence_id']:
        pqi_results1["visit_occurrence_id"].append(_)
    print("Length visit_occurrence:", len(pqi_results1["visit_occurrence_id"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:250.10', 'ICD9CM:250.11', 'ICD9CM:250.12', 'ICD9CM:250.13', 'ICD9CM:250.20', 'ICD9CM:250.21',
                 'ICD9CM:250.22', 'ICD9CM:250.23', 'ICD9CM:250.30', 'ICD9CM:250.31', 'ICD9CM:250.32', 'ICD9CM:250.33'):
            pqi_results1["dm_comp_st"].append(1)
        else:
            pqi_results1["dm_comp_st"].append(0)
    print("Completed Binary Recoding of: Short-term Diabetes Complications,", len(pqi_results1["dm_comp_st"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:540.0', 'ICD9CM:540.1', 'ICD9CM:540.9', 'ICD9CM:541'):
            pqi_results1["appendix"].append(1)
        else:
            pqi_results1["appendix"].append(0)
    print("Completed Binary Recoding of: Appendix,", len(pqi_results1["appendix"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:250.40', 'ICD9CM:250.41', 'ICD9CM:250.42', 'ICD9CM:250.43', 'ICD9CM:250.50', 'ICD9CM:250.51',
                 'ICD9CM:250.52', 'ICD9CM:250.53', 'ICD9CM:250.60', 'ICD9CM:250.61', 'ICD9CM:250.62', 'ICD9CM:250.63',
                 'ICD9CM:250.70', 'ICD9CM:250.71', 'ICD9CM:250.72', 'ICD9CM:250.73', 'ICD9CM:250.80', 'ICD9CM:250.81',
                 'ICD9CM:250.82', 'ICD9CM:250.83', 'ICD9CM:250.90', 'ICD9CM:250.91', 'ICD9CM:250.92', 'ICD9CM:250.93'):
            pqi_results1["dm_comp_lt"].append(1)
        else:
            pqi_results1["dm_comp_lt"].append(0)
    print("Completed Binary Recoding of: Long-term Diabetes Complications,", len(pqi_results1["dm_comp_lt"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:401.0', 'ICD9CM:401.9', 'ICD9CM:402.00', 'ICD9CM:402.10', 'ICD9CM:402.90', 'ICD9CM:403.00', 'ICD9CM:403.10', 'ICD9CM:403.90', 'ICD9CM:404.00', 'ICD9CM:404.10', 'ICD9CM:404.90') and row.condition_type_concept_id == 44786627:
            pqi_results1["htn"].append(1)
        else: pqi_results1["htn"].append(0)
    print("Completed Binary Recoding of: Preventable Hypertension,", len(pqi_results1["htn"]))

    for index, row in df.iterrows():
        if row.condition_source_value in ('ICD9CM:398.91', 'ICD9CM:402.01', 'ICD9CM:402.11', 'ICD9CM:402.91', 'ICD9CM:404.01', 'ICD9CM:404.03', 'ICD9CM:404.11', 'ICD9CM:404.13', 'ICD9CM:404.91', 'ICD9CM:404.93', 'ICD9CM:428.0', 'ICD9CM:428.1', 'ICD9CM:428.20', 'ICD9CM:428.21', 'ICD9CM:428.22', 'ICD9CM:428.23', 'ICD9CM:428.30', 'ICD9CM:428.31', 'ICD9CM:428.32', 'ICD9CM:428.33', 'ICD9CM:428.40', 'ICD9CM:428.41', 'ICD9CM:428.42', 'ICD9CM:428.43', 'ICD9CM:428.9') and row.condition_type_concept_id == 44786627:
            pqi_results1["hf"].append(1)
        else: pqi_results1["hf"].append(0)
    print("Completed Binary Recoding of: Heart Failure,", len(pqi_results1["hf"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:250.02', 'ICD9CM:250.03'):
            pqi_results1["dm_no_comp"].append(1)
        else: pqi_results1["dm_no_comp"].append(0)
    print("Completed Binary Recoding of: DM No Complications,", len(pqi_results1["dm_no_comp"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:841.0', 'ICD9CM:841.2', 'ICD9CM:841.3', 'ICD9CM:841.4', 'ICD9CM:841.5', 'ICD9CM:841.6', 'ICD9CM:841.7', 'ICD9CM:841.8', 'ICD9CM:841.9'):
            pqi_results1["lower_amputate"].append(1)
        else: pqi_results1["lower_amputate"].append(0)
    print("Completed Binary Recoding of: Preventable Lower Extremity Amputation,", len(pqi_results1["lower_amputate"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:250.00', 'ICD9CM:250.01', 'ICD9CM:250.02', 'ICD9CM:250.03', 'ICD9CM:250.10', 'ICD9CM:250.11', 'ICD9CM:250.12', 'ICD9CM:250.13', 'ICD9CM:250.20', 'ICD9CM:250.21', 'ICD9CM:250.22', 'ICD9CM:250.23', 'ICD9CM:250.30', 'ICD9CM:250.31', 'ICD9CM:250.32', 'ICD9CM:250.33', 'ICD9CM:250.40', 'ICD9CM:250.41', 'ICD9CM:250.42', 'ICD9CM:250.43', 'ICD9CM:250.50', 'ICD9CM:250.51', 'ICD9CM:250.52', 'ICD9CM:250.53', 'ICD9CM:250.60', 'ICD9CM:250.61', 'ICD9CM:250.62', 'ICD9CM:250.63', 'ICD9CM:250.70', 'ICD9CM:250.71', 'ICD9CM:250.72', 'ICD9CM:250.73', 'ICD9CM:250.80', 'ICD9CM:250.81', 'ICD9CM:250.82', 'ICD9CM:250.83', 'ICD9CM:250.90', 'ICD9CM:250.91', 'ICD9CM:250.92', 'ICD9CM:250.93'):
            pqi_results1["diabetes"].append(1)
        else: pqi_results1["diabetes"].append(0)
    print("Completed Binary Recoding of: Diabetes,", len(pqi_results1["diabetes"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:493.00', 'ICD9CM:493.01', 'ICD9CM:493.02', 'ICD9CM:493.10', 'ICD9CM:493.11', 'ICD9CM:493.12', 'ICD9CM:493.20', 'ICD9CM:493.21', 'ICD9CM:493.22', 'ICD9CM:493.81', 'ICD9CM:493.82', 'ICD9CM:493.90', 'ICD9CM:493.91', 'ICD9CM:493.92') and row.condition_type_concept_id == 44786627:
            pqi_results1["asthma"].append(1)
        else: pqi_results1["asthma"].append(0)
    print("Completed Binary Recoding of: Preventable Asthma,", len(pqi_results1["asthma"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:590.10', 'ICD9CM:590.11', 'ICD9CM:590.2', 'ICD9CM:590.3', 'ICD9CM:590.80', 'ICD9CM:590.81', 'ICD9CM:590.9', 'ICD9CM:595.0', 'ICD9CM:595.9', 'ICD9CM:599.0') and row.condition_type_concept_id == 44786627:
            pqi_results1["uti"].append(1)
        else: pqi_results1["uti"].append(0)
    print("Completed Binary Recoding of: Preventable Urinary Tract Infection,", len(pqi_results1["uti"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:481', 'ICD9CM:482.2', 'ICD9CM:482.30', 'ICD9CM:482.31', 'ICD9CM:482.32', 'ICD9CM:482.39', 'ICD9CM:482.40', 'ICD9CM:482.41', 'ICD9CM:482.42', 'ICD9CM:482.49', 'ICD9CM:482.9', 'ICD9CM:483.0', 'ICD9CM:483.1', 'ICD9CM:483.8', 'ICD9CM:485', 'ICD9CM:486') and row.condition_type_concept_id == 44786627:
            pqi_results1["bact_pneu"].append(1)
        else: pqi_results1["bact_pneu"].append(0)
    print("Completed Binary Recoding of: Preventable Bacterial Pneumonia,", len(pqi_results1["bact_pneu"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:276.5', 'ICD9CM:276.50', 'ICD9CM:276.51', 'ICD9CM:276.52') and row.condition_type_concept_id == 44786627:
            pqi_results1["dehydration"].append(1)
        elif row.condition_source_value in('ICD9CM:276.0', 'ICD9CM:008.61', 'ICD9CM:008.62', 'ICD9CM:008.63', 'ICD9CM:008.64', 'ICD9CM:008.65', 'ICD9CM:008.66', 'ICD9CM:008.67', 'ICD9CM:008.69', 'ICD9CM:008.8', 'ICD9CM:009.0', 'ICD9CM:009.1', 'ICD9CM:009.2', 'ICD9CM:009.3', 'ICD9CM:558.9', 'ICD9CM:584.5', 'ICD9CM:584.6', 'ICD9CM:584.7', 'ICD9CM:584.8', 'ICD9CM:584.9', 'ICD9CM:586', 'ICD9CM:997.5') and row.condition_type_concept_id == 44786627:
            pqi_results1["dehydration"].append(1)
        elif row.condition_source_value in('ICD9CM:276.5', 'ICD9CM:276.50', 'ICD9CM:276.51', 'ICD9CM:276.52') and row.condition_type_concept_id == 44786629:
            pqi_results1["dehydration"].append(1)
        else: pqi_results1["dehydration"].append(0)
    print("Completed Binary Recoding of: Preventable Dehydration,", len(pqi_results1["dehydration"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:491.0', 'ICD9CM:491.1', 'ICD9CM:491.20', 'ICD9CM:491.21', 'ICD9CM:491.22', 'ICD9CM:491.8', 'ICD9CM:491.9', 'ICD9CM:492.0', 'ICD9CM:492.8', 'ICD9CM:494', 'ICD9CM:494.0', 'ICD9CM:494.1', 'ICD9CM:496', 'ICD9CM:493.00', 'ICD9CM:493.01', 'ICD9CM:493.02', 'ICD9CM:493.10', 'ICD9CM:493.11', 'ICD9CM:493.12', 'ICD9CM:493.20', 'ICD9CM:493.21', 'ICD9CM:493.22', 'ICD9CM:493.81', 'ICD9CM:493.82', 'ICD9CM:493.90', 'ICD9CM:493.91', 'ICD9CM:493.92') and row.condition_type_concept_id == 44786627:
            pqi_results1["copd"].append(1)
        else: pqi_results1["copd"].append(0)
    print("Completed Binary Recoding of: Preventable COPD,", len(pqi_results1["copd"]))

    ##
    ## Begin Exclusions
    ##

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:403.00', 'ICD9CM:403.10', 'ICD9CM:403.90', 'ICD9CM:404.00', 'ICD9CM:404.10', 'ICD9CM:404.90'):
            pqi_results1["htn_exclude"].append(1)
        else: pqi_results1["htn_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Hypertension EXCLUSION,", len(pqi_results1["htn_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:895.0', 'ICD9CM:895.1', 'ICD9CM:896.0', 'ICD9CM:896.1', 'ICD9CM:896.2', 'ICD9CM:896.3', 'ICD9CM:897.0', 'ICD9CM:897.1', 'ICD9CM:897.2', 'ICD9CM:897.3', 'ICD9CM:897.4', 'ICD9CM:897.5', 'ICD9CM:897.6', 'ICD9CM:897.7'):
            pqi_results1["amp_exclude"].append(1)
        else: pqi_results1["amp_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Lower Extremity Amputation EXCLUSION,", len(pqi_results1["amp_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09', 'ICD9CM:516.61', 'ICD9CM:516.62', 'ICD9CM:516.63', 'ICD9CM:516.64', 'ICD9CM:516.69', 'ICD9CM:747.21', 'ICD9CM:748.3', 'ICD9CM:748.4', 'ICD9CM:748.5', 'ICD9CM:748.60', 'ICD9CM:748.61', 'ICD9CM:748.69', 'ICD9CM:748.8', 'ICD9CM:748.9', 'ICD9CM:750.3', 'ICD9CM:759.3', 'ICD9CM:770.7'):
            pqi_results1["asth_exclude"].append(1)
        else: pqi_results1["asth_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Asthma EXCLUSION,", len(pqi_results1["asth_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:590.00', 'ICD9CM:590.01', 'ICD9CM:593.70', 'ICD9CM:593.71', 'ICD9CM:593.72', 'ICD9CM:593.73', 'ICD9CM:753.0', 'ICD9CM:753.10', 'ICD9CM:753.11', 'ICD9CM:753.12', 'ICD9CM:753.13', 'ICD9CM:753.14', 'ICD9CM:753.15', 'ICD9CM:753.16', 'ICD9CM:753.17', 'ICD9CM:753.19', 'ICD9CM:753.20', 'ICD9CM:753.21', 'ICD9CM:753.22', 'ICD9CM:753.23', 'ICD9CM:753.29', 'ICD9CM:753.3', 'ICD9CM:753.4', 'ICD9CM:753.5', 'ICD9CM:753.6', 'ICD9CM:753.8', 'ICD9CM:753.9'):
            pqi_results1["uti_exclude"].append(1)
        else: pqi_results1["uti_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Urinary Tract Infection EXCLUSION,", len(pqi_results1["uti_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:282.41', 'ICD9CM:282.42', 'ICD9CM:282.60', 'ICD9CM:282.61', 'ICD9CM:282.62', 'ICD9CM:282.63', 'ICD9CM:282.64', 'ICD9CM:282.68', 'ICD9CM:282.69'):
            pqi_results1["bac_exclude"].append(1)
        else: pqi_results1["bac_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Bacterial Pneumonia EXCLUSION,", len(pqi_results1["bac_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:403.01', 'ICD9CM:403.11', 'ICD9CM:403.91', 'ICD9CM:404.02', 'ICD9CM:404.03', 'ICD9CM:404.12', 'ICD9CM:404.13', 'ICD9CM:404.92', 'ICD9CM:404.93', 'ICD9CM:585.5', 'ICD9CM:585.6'):
            pqi_results1["dehyd_exclude"].append(1)
        else: pqi_results1["dehyd_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Dehydration EXCLUSION,", len(pqi_results1["dehyd_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09', 'ICD9CM:516.61', 'ICD9CM:516.62', 'ICD9CM:516.63', 'ICD9CM:516.64', 'ICD9CM:516.69', 'ICD9CM:747.21', 'ICD9CM:748.3', 'ICD9CM:748.4', 'ICD9CM:748.5', 'ICD9CM:748.60', 'ICD9CM:748.61', 'ICD9CM:748.69', 'ICD9CM:748.8', 'ICD9CM:748.9', 'ICD9CM:750.3', 'ICD9CM:759.3', 'ICD9CM:770.7'):
            pqi_results1["copd_exclude"].append(1)
        else: pqi_results1["copd_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable COPD EXCLUSION,", len(pqi_results1["copd_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:042', 'ICD9CM:136.3', 'ICD9CM:199.2', 'ICD9CM:238.76', 'ICD9CM:238.77', 'ICD9CM:238.79', 'ICD9CM:260', 'ICD9CM:261', 'ICD9CM:262', 'ICD9CM:279.00', 'ICD9CM:279.01', 'ICD9CM:279.02', 'ICD9CM:279.03', 'ICD9CM:279.04', 'ICD9CM:279.05', 'ICD9CM:279.06', 'ICD9CM:279.09', 'ICD9CM:279.10', 'ICD9CM:279.11', 'ICD9CM:279.12', 'ICD9CM:279.13', 'ICD9CM:279.19', 'ICD9CM:279.2', 'ICD9CM:279.3', 'ICD9CM:279.4', 'ICD9CM:279.41', 'ICD9CM:279.49', 'ICD9CM:279.50', 'ICD9CM:279.51', 'ICD9CM:279.52', 'ICD9CM:279.53', 'ICD9CM:279.8', 'ICD9CM:279.9', 'ICD9CM:284.09', 'ICD9CM:284.1', 'ICD9CM:284.11', 'ICD9CM:284.12', 'ICD9CM:284.19', 'ICD9CM:288.0', 'ICD9CM:288.00', 'ICD9CM:288.01', 'ICD9CM:288.02', 'ICD9CM:288.03', 'ICD9CM:288.09', 'ICD9CM:288.1', 'ICD9CM:288.2', 'ICD9CM:288.4', 'ICD9CM:288.50', 'ICD9CM:288.51', 'ICD9CM:288.59', 'ICD9CM:289.53', 'ICD9CM:289.83', 'ICD9CM:403.01', 'ICD9CM:403.11', 'ICD9CM:403.91', 'ICD9CM:404.02', 'ICD9CM:404.03', 'ICD9CM:404.12', 'ICD9CM:404.13', 'ICD9CM:404.92', 'ICD9CM:404.93', 'ICD9CM:579.3', 'ICD9CM:585', 'ICD9CM:585.5', 'ICD9CM:585.6', 'ICD9CM:996.8', 'ICD9CM:996.80', 'ICD9CM:996.81', 'ICD9CM:996.82', 'ICD9CM:996.83', 'ICD9CM:996.84', 'ICD9CM:996.85', 'ICD9CM:996.86', 'ICD9CM:996.87', 'ICD9CM:996.88', 'ICD9CM:996.89', 'ICD9CM:V42.0', 'ICD9CM:V42.1', 'ICD9CM:V42.6', 'ICD9CM:V42.7', 'ICD9CM:V42.8', 'ICD9CM:V42.81', 'ICD9CM:V42.82', 'ICD9CM:V42.83', 'ICD9CM:V42.84', 'ICD9CM:V42.89', 'ICD9CM:V45.1', 'ICD9CM:V45.11', 'ICD9CM:V56.0', 'ICD9CM:V56.1', 'ICD9CM:V56.2'):
            pqi_results1["immunocomp"].append(1)
        else: pqi_results1["immunocomp"].append(0)
    print("Completed Binary Recoding of: Immunocompromised EXCLUSION,", len(pqi_results1["immunocomp"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:00.18', 'ICD9Proc:33.5', 'ICD9Proc:33.50', 'ICD9Proc:33.51', 'ICD9Proc:33.52', 'ICD9Proc:33.6', 'ICD9Proc:37.5', 'ICD9Proc:37.51', 'ICD9Proc:41.0', 'ICD9Proc:41.00', 'ICD9Proc:41.01', 'ICD9Proc:41.02', 'ICD9Proc:41.03', 'ICD9Proc:41.04', 'ICD9Proc:41.05', 'ICD9Proc:41.06', 'ICD9Proc:41.07', 'ICD9Proc:41.08', 'ICD9Proc:41.09', 'ICD9Proc:46.97', 'ICD9Proc:50.51', 'ICD9Proc:50.59', 'ICD9Proc:52.80', 'ICD9Proc:52.81', 'ICD9Proc:52.82', 'ICD9Proc:52.83', 'ICD9Proc:52.85', 'ICD9Proc:52.86', 'ICD9Proc:55.69'):
            pqi_results1["immuno_proc"].append(1)
        else: pqi_results1["immuno_proc"].append(0)
    print("Completed Binary Recoding of: Immunocompromised Procedure EXCLUSION,", len(pqi_results1["immuno_proc"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:00.50', 'ICD9Proc:00.51', 'ICD9Proc:00.52', 'ICD9Proc:00.53', 'ICD9Proc:00.54', 'ICD9Proc:00.56', 'ICD9Proc:00.57', 'ICD9Proc:00.66', 'ICD9Proc:17.51', 'ICD9Proc:17.52', 'ICD9Proc:17.55', 'ICD9Proc:35.00', 'ICD9Proc:35.01', 'ICD9Proc:35.02', 'ICD9Proc:35.03', 'ICD9Proc:35.04', 'ICD9Proc:35.05', 'ICD9Proc:35.06', 'ICD9Proc:35.07', 'ICD9Proc:35.08', 'ICD9Proc:35.09', 'ICD9Proc:35.10', 'ICD9Proc:35.11', 'ICD9Proc:35.12', 'ICD9Proc:35.13', 'ICD9Proc:35.14', 'ICD9Proc:35.20', 'ICD9Proc:35.21', 'ICD9Proc:35.22', 'ICD9Proc:35.23', 'ICD9Proc:35.24', 'ICD9Proc:35.25', 'ICD9Proc:35.26', 'ICD9Proc:35.27', 'ICD9Proc:35.28', 'ICD9Proc:35.31', 'ICD9Proc:35.32', 'ICD9Proc:35.33', 'ICD9Proc:35.34', 'ICD9Proc:35.35', 'ICD9Proc:35.39', 'ICD9Proc:35.41', 'ICD9Proc:35.42', 'ICD9Proc:35.50', 'ICD9Proc:35.51', 'ICD9Proc:35.52', 'ICD9Proc:35.53', 'ICD9Proc:35.54', 'ICD9Proc:35.55', 'ICD9Proc:35.60', 'ICD9Proc:35.61', 'ICD9Proc:35.62', 'ICD9Proc:35.63', 'ICD9Proc:35.70', 'ICD9Proc:35.71', 'ICD9Proc:35.72', 'ICD9Proc:35.73', 'ICD9Proc:35.81', 'ICD9Proc:35.82', 'ICD9Proc:35.83', 'ICD9Proc:35.84', 'ICD9Proc:35.91', 'ICD9Proc:35.92', 'ICD9Proc:35.93', 'ICD9Proc:35.94', 'ICD9Proc:35.95', 'ICD9Proc:35.96', 'ICD9Proc:35.97', 'ICD9Proc:35.98', 'ICD9Proc:35.99', 'ICD9Proc:36.01', 'ICD9Proc:36.02', 'ICD9Proc:36.03', 'ICD9Proc:36.04', 'ICD9Proc:36.05', 'ICD9Proc:36.06', 'ICD9Proc:36.07', 'ICD9Proc:36.09', 'ICD9Proc:36.10', 'ICD9Proc:36.11', 'ICD9Proc:36.12', 'ICD9Proc:36.13', 'ICD9Proc:36.14', 'ICD9Proc:36.15', 'ICD9Proc:36.16', 'ICD9Proc:36.17', 'ICD9Proc:36.19', 'ICD9Proc:36.2', 'ICD9Proc:36.3', 'ICD9Proc:36.31', 'ICD9Proc:36.32', 'ICD9Proc:36.33', 'ICD9Proc:36.34', 'ICD9Proc:36.39', 'ICD9Proc:36.91', 'ICD9Proc:36.99', 'ICD9Proc:37.31', 'ICD9Proc:37.32', 'ICD9Proc:37.33', 'ICD9Proc:37.34', 'ICD9Proc:37.35', 'ICD9Proc:37.36', 'ICD9Proc:37.37', 'ICD9Proc:37.41', 'ICD9Proc:37.5', 'ICD9Proc:37.51', 'ICD9Proc:37.52', 'ICD9Proc:37.53', 'ICD9Proc:37.54', 'ICD9Proc:37.55', 'ICD9Proc:37.60', 'ICD9Proc:37.61', 'ICD9Proc:37.62', 'ICD9Proc:37.63', 'ICD9Proc:37.64', 'ICD9Proc:37.65', 'ICD9Proc:37.66', 'ICD9Proc:37.70', 'ICD9Proc:37.71', 'ICD9Proc:37.72', 'ICD9Proc:37.73', 'ICD9Proc:37.74', 'ICD9Proc:37.75', 'ICD9Proc:37.76', 'ICD9Proc:37.77', 'ICD9Proc:37.78', 'ICD9Proc:37.79', 'ICD9Proc:37.80', 'ICD9Proc:37.81', 'ICD9Proc:37.82', 'ICD9Proc:37.83', 'ICD9Proc:37.85', 'ICD9Proc:37.86', 'ICD9Proc:37.87', 'ICD9Proc:37.89', 'ICD9Proc:37.94', 'ICD9Proc:37.95', 'ICD9Proc:37.96', 'ICD9Proc:37.97', 'ICD9Proc:37.98', 'ICD9Proc:38.26'):
            pqi_results1["cardiac_proc"].append(1)
        else: pqi_results1["cardiac_proc"].append(0)
    print("Completed Binary Recoding of: Cardiac Procedure EXCLUSION,", len(pqi_results1["cardiac_proc"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:38.95', 'ICD9Proc:39.27', 'ICD9Proc:39.29', 'ICD9Proc:39.42', 'ICD9Proc:39.43', 'ICD9Proc:39.93', 'ICD9Proc:39.94'):
            pqi_results1["dialysis_access"].append(1)
        else: pqi_results1["dialysis_access"].append(0)
    print("Completed Binary Recoding of: Dialysis Access Procedure EXCLUSION,", len(pqi_results1["dialysis_access"]))

    pd.DataFrame(pqi_results1).to_csv(output_filepath, encoding='utf-8')

pqi(cdrn_prevent_hosp_2014_sql)



#####################
#####################
print("")
#####################
#####################


# This function will establish the PQI variables and define the rules
def pqi(df):

    output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/pqi_results_2.csv'


    for _ in df['visit_occurrence_id']:
        pqi_results2["visit_occurrence_id"].append(_)
    print("Length visit_occurrence:", len(pqi_results2["visit_occurrence_id"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:250.10', 'ICD9CM:250.11', 'ICD9CM:250.12', 'ICD9CM:250.13', 'ICD9CM:250.20', 'ICD9CM:250.21',
                 'ICD9CM:250.22', 'ICD9CM:250.23', 'ICD9CM:250.30', 'ICD9CM:250.31', 'ICD9CM:250.32', 'ICD9CM:250.33'):
            pqi_results2["dm_comp_st"].append(1)
        else:
            pqi_results2["dm_comp_st"].append(0)
    print("Completed Binary Recoding of: Short-term Diabetes Complications,", len(pqi_results2["dm_comp_st"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:540.0', 'ICD9CM:540.1', 'ICD9CM:540.9', 'ICD9CM:541'):
            pqi_results2["appendix"].append(1)
        else:
            pqi_results2["appendix"].append(0)
    print("Completed Binary Recoding of: Appendix,", len(pqi_results2["appendix"]))

    for _ in df['condition_source_value']:
        if _ in ('ICD9CM:250.40', 'ICD9CM:250.41', 'ICD9CM:250.42', 'ICD9CM:250.43', 'ICD9CM:250.50', 'ICD9CM:250.51',
                 'ICD9CM:250.52', 'ICD9CM:250.53', 'ICD9CM:250.60', 'ICD9CM:250.61', 'ICD9CM:250.62', 'ICD9CM:250.63',
                 'ICD9CM:250.70', 'ICD9CM:250.71', 'ICD9CM:250.72', 'ICD9CM:250.73', 'ICD9CM:250.80', 'ICD9CM:250.81',
                 'ICD9CM:250.82', 'ICD9CM:250.83', 'ICD9CM:250.90', 'ICD9CM:250.91', 'ICD9CM:250.92', 'ICD9CM:250.93'):
            pqi_results2["dm_comp_lt"].append(1)
        else:
            pqi_results2["dm_comp_lt"].append(0)
    print("Completed Binary Recoding of: Long-term Diabetes Complications,", len(pqi_results2["dm_comp_lt"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:401.0', 'ICD9CM:401.9', 'ICD9CM:402.00', 'ICD9CM:402.10', 'ICD9CM:402.90', 'ICD9CM:403.00', 'ICD9CM:403.10', 'ICD9CM:403.90', 'ICD9CM:404.00', 'ICD9CM:404.10', 'ICD9CM:404.90') and row.condition_type_concept_id == 44786627:
            pqi_results2["htn"].append(1)
        else: pqi_results2["htn"].append(0)
    print("Completed Binary Recoding of: Preventable Hypertension,", len(pqi_results2["htn"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:398.91', 'ICD9CM:402.01', 'ICD9CM:402.11', 'ICD9CM:402.91', 'ICD9CM:404.01', 'ICD9CM:404.03', 'ICD9CM:404.11', 'ICD9CM:404.13', 'ICD9CM:404.91', 'ICD9CM:404.93', 'ICD9CM:428.0', 'ICD9CM:428.1', 'ICD9CM:428.20', 'ICD9CM:428.21', 'ICD9CM:428.22', 'ICD9CM:428.23', 'ICD9CM:428.30', 'ICD9CM:428.31', 'ICD9CM:428.32', 'ICD9CM:428.33', 'ICD9CM:428.40', 'ICD9CM:428.41', 'ICD9CM:428.42', 'ICD9CM:428.43', 'ICD9CM:428.9') and row.condition_type_concept_id == 44786627:
            pqi_results2["hf"].append(1)
        else: pqi_results2["hf"].append(0)
    print("Completed Binary Recoding of: Heart Failure,", len(pqi_results2["hf"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:250.02', 'ICD9CM:250.03'):
            pqi_results2["dm_no_comp"].append(1)
        else: pqi_results2["dm_no_comp"].append(0)
    print("Completed Binary Recoding of: DM No Complications,", len(pqi_results2["dm_no_comp"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:841.0', 'ICD9CM:841.2', 'ICD9CM:841.3', 'ICD9CM:841.4', 'ICD9CM:841.5', 'ICD9CM:841.6', 'ICD9CM:841.7', 'ICD9CM:841.8', 'ICD9CM:841.9'):
            pqi_results2["lower_amputate"].append(1)
        else: pqi_results2["lower_amputate"].append(0)
    print("Completed Binary Recoding of: Preventable Lower Extremity Amputation,", len(pqi_results2["lower_amputate"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:250.00', 'ICD9CM:250.01', 'ICD9CM:250.02', 'ICD9CM:250.03', 'ICD9CM:250.10', 'ICD9CM:250.11', 'ICD9CM:250.12', 'ICD9CM:250.13', 'ICD9CM:250.20', 'ICD9CM:250.21', 'ICD9CM:250.22', 'ICD9CM:250.23', 'ICD9CM:250.30', 'ICD9CM:250.31', 'ICD9CM:250.32', 'ICD9CM:250.33', 'ICD9CM:250.40', 'ICD9CM:250.41', 'ICD9CM:250.42', 'ICD9CM:250.43', 'ICD9CM:250.50', 'ICD9CM:250.51', 'ICD9CM:250.52', 'ICD9CM:250.53', 'ICD9CM:250.60', 'ICD9CM:250.61', 'ICD9CM:250.62', 'ICD9CM:250.63', 'ICD9CM:250.70', 'ICD9CM:250.71', 'ICD9CM:250.72', 'ICD9CM:250.73', 'ICD9CM:250.80', 'ICD9CM:250.81', 'ICD9CM:250.82', 'ICD9CM:250.83', 'ICD9CM:250.90', 'ICD9CM:250.91', 'ICD9CM:250.92', 'ICD9CM:250.93'):
            pqi_results2["diabetes"].append(1)
        else: pqi_results2["diabetes"].append(0)
    print("Completed Binary Recoding of: Diabetes,", len(pqi_results2["diabetes"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:493.00', 'ICD9CM:493.01', 'ICD9CM:493.02', 'ICD9CM:493.10', 'ICD9CM:493.11', 'ICD9CM:493.12', 'ICD9CM:493.20', 'ICD9CM:493.21', 'ICD9CM:493.22', 'ICD9CM:493.81', 'ICD9CM:493.82', 'ICD9CM:493.90', 'ICD9CM:493.91', 'ICD9CM:493.92') and row.condition_type_concept_id == 44786627:
            pqi_results2["asthma"].append(1)
        else: pqi_results2["asthma"].append(0)
    print("Completed Binary Recoding of: Preventable Asthma,", len(pqi_results2["asthma"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:590.10', 'ICD9CM:590.11', 'ICD9CM:590.2', 'ICD9CM:590.3', 'ICD9CM:590.80', 'ICD9CM:590.81', 'ICD9CM:590.9', 'ICD9CM:595.0', 'ICD9CM:595.9', 'ICD9CM:599.0') and row.condition_type_concept_id == 44786627:
            pqi_results2["uti"].append(1)
        else: pqi_results2["uti"].append(0)
    print("Completed Binary Recoding of: Preventable Urinary Tract Infection,", len(pqi_results2["uti"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:481', 'ICD9CM:482.2', 'ICD9CM:482.30', 'ICD9CM:482.31', 'ICD9CM:482.32', 'ICD9CM:482.39', 'ICD9CM:482.40', 'ICD9CM:482.41', 'ICD9CM:482.42', 'ICD9CM:482.49', 'ICD9CM:482.9', 'ICD9CM:483.0', 'ICD9CM:483.1', 'ICD9CM:483.8', 'ICD9CM:485', 'ICD9CM:486') and row.condition_type_concept_id == 44786627:
            pqi_results2["bact_pneu"].append(1)
        else: pqi_results2["bact_pneu"].append(0)
    print("Completed Binary Recoding of: Preventable Bacterial Pneumonia,", len(pqi_results2["bact_pneu"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:276.5', 'ICD9CM:276.50', 'ICD9CM:276.51', 'ICD9CM:276.52') and row.condition_type_concept_id == 44786627:
            pqi_results2["dehydration"].append(1)
        elif row.condition_source_value in('ICD9CM:276.0', 'ICD9CM:008.61', 'ICD9CM:008.62', 'ICD9CM:008.63', 'ICD9CM:008.64', 'ICD9CM:008.65', 'ICD9CM:008.66', 'ICD9CM:008.67', 'ICD9CM:008.69', 'ICD9CM:008.8', 'ICD9CM:009.0', 'ICD9CM:009.1', 'ICD9CM:009.2', 'ICD9CM:009.3', 'ICD9CM:558.9', 'ICD9CM:584.5', 'ICD9CM:584.6', 'ICD9CM:584.7', 'ICD9CM:584.8', 'ICD9CM:584.9', 'ICD9CM:586', 'ICD9CM:997.5') and row.condition_type_concept_id == 44786627:
            pqi_results2["dehydration"].append(1)
        elif row.condition_source_value in('ICD9CM:276.5', 'ICD9CM:276.50', 'ICD9CM:276.51', 'ICD9CM:276.52') and row.condition_type_concept_id == 44786629:
            pqi_results2["dehydration"].append(1)
        else: pqi_results2["dehydration"].append(0)
    print("Completed Binary Recoding of: Preventable Dehydration,", len(pqi_results2["dehydration"]))

    for index, row in df.iterrows():
        if row.condition_source_value in('ICD9CM:491.0', 'ICD9CM:491.1', 'ICD9CM:491.20', 'ICD9CM:491.21', 'ICD9CM:491.22', 'ICD9CM:491.8', 'ICD9CM:491.9', 'ICD9CM:492.0', 'ICD9CM:492.8', 'ICD9CM:494', 'ICD9CM:494.0', 'ICD9CM:494.1', 'ICD9CM:496', 'ICD9CM:493.00', 'ICD9CM:493.01', 'ICD9CM:493.02', 'ICD9CM:493.10', 'ICD9CM:493.11', 'ICD9CM:493.12', 'ICD9CM:493.20', 'ICD9CM:493.21', 'ICD9CM:493.22', 'ICD9CM:493.81', 'ICD9CM:493.82', 'ICD9CM:493.90', 'ICD9CM:493.91', 'ICD9CM:493.92') and row.condition_type_concept_id == 44786627:
            pqi_results2["copd"].append(1)
        else: pqi_results2["copd"].append(0)
    print("Completed Binary Recoding of: Preventable COPD,", len(pqi_results2["copd"]))

    ##
    ## Begin Exclusions
    ##

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:403.00', 'ICD9CM:403.10', 'ICD9CM:403.90', 'ICD9CM:404.00', 'ICD9CM:404.10', 'ICD9CM:404.90'):
            pqi_results2["htn_exclude"].append(1)
        else: pqi_results2["htn_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Hypertension EXCLUSION,", len(pqi_results2["htn_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:895.0', 'ICD9CM:895.1', 'ICD9CM:896.0', 'ICD9CM:896.1', 'ICD9CM:896.2', 'ICD9CM:896.3', 'ICD9CM:897.0', 'ICD9CM:897.1', 'ICD9CM:897.2', 'ICD9CM:897.3', 'ICD9CM:897.4', 'ICD9CM:897.5', 'ICD9CM:897.6', 'ICD9CM:897.7'):
            pqi_results2["amp_exclude"].append(1)
        else: pqi_results2["amp_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Lower Extremity Amputation EXCLUSION,", len(pqi_results2["amp_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09', 'ICD9CM:516.61', 'ICD9CM:516.62', 'ICD9CM:516.63', 'ICD9CM:516.64', 'ICD9CM:516.69', 'ICD9CM:747.21', 'ICD9CM:748.3', 'ICD9CM:748.4', 'ICD9CM:748.5', 'ICD9CM:748.60', 'ICD9CM:748.61', 'ICD9CM:748.69', 'ICD9CM:748.8', 'ICD9CM:748.9', 'ICD9CM:750.3', 'ICD9CM:759.3', 'ICD9CM:770.7'):
            pqi_results2["asth_exclude"].append(1)
        else: pqi_results2["asth_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Asthma EXCLUSION,", len(pqi_results2["asth_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:590.00', 'ICD9CM:590.01', 'ICD9CM:593.70', 'ICD9CM:593.71', 'ICD9CM:593.72', 'ICD9CM:593.73', 'ICD9CM:753.0', 'ICD9CM:753.10', 'ICD9CM:753.11', 'ICD9CM:753.12', 'ICD9CM:753.13', 'ICD9CM:753.14', 'ICD9CM:753.15', 'ICD9CM:753.16', 'ICD9CM:753.17', 'ICD9CM:753.19', 'ICD9CM:753.20', 'ICD9CM:753.21', 'ICD9CM:753.22', 'ICD9CM:753.23', 'ICD9CM:753.29', 'ICD9CM:753.3', 'ICD9CM:753.4', 'ICD9CM:753.5', 'ICD9CM:753.6', 'ICD9CM:753.8', 'ICD9CM:753.9'):
            pqi_results2["uti_exclude"].append(1)
        else: pqi_results2["uti_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Urinary Tract Infection EXCLUSION,", len(pqi_results2["uti_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:282.41', 'ICD9CM:282.42', 'ICD9CM:282.60', 'ICD9CM:282.61', 'ICD9CM:282.62', 'ICD9CM:282.63', 'ICD9CM:282.64', 'ICD9CM:282.68', 'ICD9CM:282.69'):
            pqi_results2["bac_exclude"].append(1)
        else: pqi_results2["bac_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Bacterial Pneumonia EXCLUSION,", len(pqi_results2["bac_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:403.01', 'ICD9CM:403.11', 'ICD9CM:403.91', 'ICD9CM:404.02', 'ICD9CM:404.03', 'ICD9CM:404.12', 'ICD9CM:404.13', 'ICD9CM:404.92', 'ICD9CM:404.93', 'ICD9CM:585.5', 'ICD9CM:585.6'):
            pqi_results2["dehyd_exclude"].append(1)
        else: pqi_results2["dehyd_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable Dehydration EXCLUSION,", len(pqi_results2["dehyd_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09', 'ICD9CM:516.61', 'ICD9CM:516.62', 'ICD9CM:516.63', 'ICD9CM:516.64', 'ICD9CM:516.69', 'ICD9CM:747.21', 'ICD9CM:748.3', 'ICD9CM:748.4', 'ICD9CM:748.5', 'ICD9CM:748.60', 'ICD9CM:748.61', 'ICD9CM:748.69', 'ICD9CM:748.8', 'ICD9CM:748.9', 'ICD9CM:750.3', 'ICD9CM:759.3', 'ICD9CM:770.7'):
            pqi_results2["copd_exclude"].append(1)
        else: pqi_results2["copd_exclude"].append(0)
    print("Completed Binary Recoding of: Preventable COPD EXCLUSION,", len(pqi_results2["copd_exclude"]))

    for _ in df['condition_source_value']:
        if _ in('ICD9CM:042', 'ICD9CM:136.3', 'ICD9CM:199.2', 'ICD9CM:238.76', 'ICD9CM:238.77', 'ICD9CM:238.79', 'ICD9CM:260', 'ICD9CM:261', 'ICD9CM:262', 'ICD9CM:279.00', 'ICD9CM:279.01', 'ICD9CM:279.02', 'ICD9CM:279.03', 'ICD9CM:279.04', 'ICD9CM:279.05', 'ICD9CM:279.06', 'ICD9CM:279.09', 'ICD9CM:279.10', 'ICD9CM:279.11', 'ICD9CM:279.12', 'ICD9CM:279.13', 'ICD9CM:279.19', 'ICD9CM:279.2', 'ICD9CM:279.3', 'ICD9CM:279.4', 'ICD9CM:279.41', 'ICD9CM:279.49', 'ICD9CM:279.50', 'ICD9CM:279.51', 'ICD9CM:279.52', 'ICD9CM:279.53', 'ICD9CM:279.8', 'ICD9CM:279.9', 'ICD9CM:284.09', 'ICD9CM:284.1', 'ICD9CM:284.11', 'ICD9CM:284.12', 'ICD9CM:284.19', 'ICD9CM:288.0', 'ICD9CM:288.00', 'ICD9CM:288.01', 'ICD9CM:288.02', 'ICD9CM:288.03', 'ICD9CM:288.09', 'ICD9CM:288.1', 'ICD9CM:288.2', 'ICD9CM:288.4', 'ICD9CM:288.50', 'ICD9CM:288.51', 'ICD9CM:288.59', 'ICD9CM:289.53', 'ICD9CM:289.83', 'ICD9CM:403.01', 'ICD9CM:403.11', 'ICD9CM:403.91', 'ICD9CM:404.02', 'ICD9CM:404.03', 'ICD9CM:404.12', 'ICD9CM:404.13', 'ICD9CM:404.92', 'ICD9CM:404.93', 'ICD9CM:579.3', 'ICD9CM:585', 'ICD9CM:585.5', 'ICD9CM:585.6', 'ICD9CM:996.8', 'ICD9CM:996.80', 'ICD9CM:996.81', 'ICD9CM:996.82', 'ICD9CM:996.83', 'ICD9CM:996.84', 'ICD9CM:996.85', 'ICD9CM:996.86', 'ICD9CM:996.87', 'ICD9CM:996.88', 'ICD9CM:996.89', 'ICD9CM:V42.0', 'ICD9CM:V42.1', 'ICD9CM:V42.6', 'ICD9CM:V42.7', 'ICD9CM:V42.8', 'ICD9CM:V42.81', 'ICD9CM:V42.82', 'ICD9CM:V42.83', 'ICD9CM:V42.84', 'ICD9CM:V42.89', 'ICD9CM:V45.1', 'ICD9CM:V45.11', 'ICD9CM:V56.0', 'ICD9CM:V56.1', 'ICD9CM:V56.2'):
            pqi_results2["immunocomp"].append(1)
        else: pqi_results2["immunocomp"].append(0)
    print("Completed Binary Recoding of: Immunocompromised EXCLUSION,", len(pqi_results2["immunocomp"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:00.18', 'ICD9Proc:33.5', 'ICD9Proc:33.50', 'ICD9Proc:33.51', 'ICD9Proc:33.52', 'ICD9Proc:33.6', 'ICD9Proc:37.5', 'ICD9Proc:37.51', 'ICD9Proc:41.0', 'ICD9Proc:41.00', 'ICD9Proc:41.01', 'ICD9Proc:41.02', 'ICD9Proc:41.03', 'ICD9Proc:41.04', 'ICD9Proc:41.05', 'ICD9Proc:41.06', 'ICD9Proc:41.07', 'ICD9Proc:41.08', 'ICD9Proc:41.09', 'ICD9Proc:46.97', 'ICD9Proc:50.51', 'ICD9Proc:50.59', 'ICD9Proc:52.80', 'ICD9Proc:52.81', 'ICD9Proc:52.82', 'ICD9Proc:52.83', 'ICD9Proc:52.85', 'ICD9Proc:52.86', 'ICD9Proc:55.69'):
            pqi_results2["immuno_proc"].append(1)
        else: pqi_results2["immuno_proc"].append(0)
    print("Completed Binary Recoding of: Immunocompromised Procedure EXCLUSION,", len(pqi_results2["immuno_proc"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:00.50', 'ICD9Proc:00.51', 'ICD9Proc:00.52', 'ICD9Proc:00.53', 'ICD9Proc:00.54', 'ICD9Proc:00.56', 'ICD9Proc:00.57', 'ICD9Proc:00.66', 'ICD9Proc:17.51', 'ICD9Proc:17.52', 'ICD9Proc:17.55', 'ICD9Proc:35.00', 'ICD9Proc:35.01', 'ICD9Proc:35.02', 'ICD9Proc:35.03', 'ICD9Proc:35.04', 'ICD9Proc:35.05', 'ICD9Proc:35.06', 'ICD9Proc:35.07', 'ICD9Proc:35.08', 'ICD9Proc:35.09', 'ICD9Proc:35.10', 'ICD9Proc:35.11', 'ICD9Proc:35.12', 'ICD9Proc:35.13', 'ICD9Proc:35.14', 'ICD9Proc:35.20', 'ICD9Proc:35.21', 'ICD9Proc:35.22', 'ICD9Proc:35.23', 'ICD9Proc:35.24', 'ICD9Proc:35.25', 'ICD9Proc:35.26', 'ICD9Proc:35.27', 'ICD9Proc:35.28', 'ICD9Proc:35.31', 'ICD9Proc:35.32', 'ICD9Proc:35.33', 'ICD9Proc:35.34', 'ICD9Proc:35.35', 'ICD9Proc:35.39', 'ICD9Proc:35.41', 'ICD9Proc:35.42', 'ICD9Proc:35.50', 'ICD9Proc:35.51', 'ICD9Proc:35.52', 'ICD9Proc:35.53', 'ICD9Proc:35.54', 'ICD9Proc:35.55', 'ICD9Proc:35.60', 'ICD9Proc:35.61', 'ICD9Proc:35.62', 'ICD9Proc:35.63', 'ICD9Proc:35.70', 'ICD9Proc:35.71', 'ICD9Proc:35.72', 'ICD9Proc:35.73', 'ICD9Proc:35.81', 'ICD9Proc:35.82', 'ICD9Proc:35.83', 'ICD9Proc:35.84', 'ICD9Proc:35.91', 'ICD9Proc:35.92', 'ICD9Proc:35.93', 'ICD9Proc:35.94', 'ICD9Proc:35.95', 'ICD9Proc:35.96', 'ICD9Proc:35.97', 'ICD9Proc:35.98', 'ICD9Proc:35.99', 'ICD9Proc:36.01', 'ICD9Proc:36.02', 'ICD9Proc:36.03', 'ICD9Proc:36.04', 'ICD9Proc:36.05', 'ICD9Proc:36.06', 'ICD9Proc:36.07', 'ICD9Proc:36.09', 'ICD9Proc:36.10', 'ICD9Proc:36.11', 'ICD9Proc:36.12', 'ICD9Proc:36.13', 'ICD9Proc:36.14', 'ICD9Proc:36.15', 'ICD9Proc:36.16', 'ICD9Proc:36.17', 'ICD9Proc:36.19', 'ICD9Proc:36.2', 'ICD9Proc:36.3', 'ICD9Proc:36.31', 'ICD9Proc:36.32', 'ICD9Proc:36.33', 'ICD9Proc:36.34', 'ICD9Proc:36.39', 'ICD9Proc:36.91', 'ICD9Proc:36.99', 'ICD9Proc:37.31', 'ICD9Proc:37.32', 'ICD9Proc:37.33', 'ICD9Proc:37.34', 'ICD9Proc:37.35', 'ICD9Proc:37.36', 'ICD9Proc:37.37', 'ICD9Proc:37.41', 'ICD9Proc:37.5', 'ICD9Proc:37.51', 'ICD9Proc:37.52', 'ICD9Proc:37.53', 'ICD9Proc:37.54', 'ICD9Proc:37.55', 'ICD9Proc:37.60', 'ICD9Proc:37.61', 'ICD9Proc:37.62', 'ICD9Proc:37.63', 'ICD9Proc:37.64', 'ICD9Proc:37.65', 'ICD9Proc:37.66', 'ICD9Proc:37.70', 'ICD9Proc:37.71', 'ICD9Proc:37.72', 'ICD9Proc:37.73', 'ICD9Proc:37.74', 'ICD9Proc:37.75', 'ICD9Proc:37.76', 'ICD9Proc:37.77', 'ICD9Proc:37.78', 'ICD9Proc:37.79', 'ICD9Proc:37.80', 'ICD9Proc:37.81', 'ICD9Proc:37.82', 'ICD9Proc:37.83', 'ICD9Proc:37.85', 'ICD9Proc:37.86', 'ICD9Proc:37.87', 'ICD9Proc:37.89', 'ICD9Proc:37.94', 'ICD9Proc:37.95', 'ICD9Proc:37.96', 'ICD9Proc:37.97', 'ICD9Proc:37.98', 'ICD9Proc:38.26'):
            pqi_results2["cardiac_proc"].append(1)
        else: pqi_results2["cardiac_proc"].append(0)
    print("Completed Binary Recoding of: Cardiac Procedure EXCLUSION,", len(pqi_results2["cardiac_proc"]))

    for _ in df['procedure_source_value']:
        if _ in('ICD9Proc:38.95', 'ICD9Proc:39.27', 'ICD9Proc:39.29', 'ICD9Proc:39.42', 'ICD9Proc:39.43', 'ICD9Proc:39.93', 'ICD9Proc:39.94'):
            pqi_results2["dialysis_access"].append(1)
        else: pqi_results2["dialysis_access"].append(0)
    print("Completed Binary Recoding of: Dialysis Access Procedure EXCLUSION,", len(pqi_results2["dialysis_access"]))

    pd.DataFrame(pqi_results2).to_csv(output_filepath2, encoding='utf-8')

pqi(cdrn_prevent_hosp_bef_2014_sql)

#####################
#####################
print("")
#####################
#####################

# Loads the PQI Results DFs
pqi_results_1 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/pqi_results_1.csv', encoding='utf-8')
pqi_results_2 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/pqi_results_2.csv', encoding ='utf-8')


# Converts Longitudinal Data to Aggregate Counts Per Patient Visit
pqi_results1_group = pqi_results_1.groupby('visit_occurrence_id').agg({"dm_comp_st":sum, "appendix":sum, "dm_comp_lt":sum,"htn":sum, "hf":sum, "dm_no_comp":sum,"lower_amputate":sum, "diabetes":sum, "asthma":sum, "uti":sum, "bact_pneu":sum, "dehydration":sum, "copd":sum, "htn_exclude":sum, "amp_exclude":sum, "asth_exclude":sum, "uti_exclude":sum, "bac_exclude":sum, "dehyd_exclude":sum, "copd_exclude":sum, "immunocomp":sum, "immuno_proc":sum, "cardiac_proc":sum, "dialysis_access":sum})
print("Number of potential preventable visits during 2014:", len(pqi_results1_group))

# Converts Longitudinal Data to Aggregate Counts Per Patient Visit
pqi_results2_group = pqi_results_2.groupby('visit_occurrence_id').agg({"dm_comp_st":sum, "appendix":sum, "dm_comp_lt":sum,"htn":sum, "hf":sum, "dm_no_comp":sum,"lower_amputate":sum, "diabetes":sum, "asthma":sum, "uti":sum, "bact_pneu":sum, "dehydration":sum, "copd":sum, "htn_exclude":sum, "amp_exclude":sum, "asth_exclude":sum, "uti_exclude":sum, "bac_exclude":sum, "dehyd_exclude":sum, "copd_exclude":sum, "immunocomp":sum, "immuno_proc":sum, "cardiac_proc":sum, "dialysis_access":sum})
print("Number of potential preventable visits before 2014:", len(pqi_results2_group))


#####################
#####################
print("")
#####################
#####################

cdrn_prevent_hosp_2014_sql_ = cdrn_prevent_hosp_2014_sql.drop(cdrn_prevent_hosp_2014_sql.columns[4:], axis =1).drop_duplicates()
print(cdrn_prevent_hosp_2014_sql_.nunique())

cdrn_prevent_hosp_bef_2014_sql_ = cdrn_prevent_hosp_bef_2014_sql.drop(cdrn_prevent_hosp_bef_2014_sql.columns[4:], axis =1).drop_duplicates()
print(cdrn_prevent_hosp_bef_2014_sql_.nunique())


#####################
#####################
print("")
#####################
#####################

# Joins the PQI Results with the SQL outputs based on the Reset Index from before
cdrn_prevent_hosp_2014_sql_pqi = pd.merge(cdrn_prevent_hosp_2014_sql_,pqi_results1_group, how='inner', on='visit_occurrence_id')
print("Number of unique individuals and visits in cdrn_prevent_hosp_2014_2_pqi:", cdrn_prevent_hosp_2014_sql_pqi.person_id.nunique(), "&", cdrn_prevent_hosp_2014_sql_pqi.visit_occurrence_id.nunique())

cdrn_prevent_hosp_bef_2014_sql_pqi = pd.merge(cdrn_prevent_hosp_bef_2014_sql_,pqi_results2_group, how='inner', on='visit_occurrence_id')
print("Number of unique individuals and visits in cdrn_prevent_hosp_bef_2014_2_pqi:", cdrn_prevent_hosp_bef_2014_sql_pqi.person_id.nunique(), "&", cdrn_prevent_hosp_bef_2014_sql_pqi.visit_occurrence_id.nunique())


# Creates a new dictionary of exclusion categories
exclusion_rules1 = {"exclude":[]}
exclusion_rules2 = {"exclude":[]}

# Reset Index
cdrn_prevent_hosp_2014_sql_pqi = cdrn_prevent_hosp_2014_sql_pqi.reset_index(drop=True)
cdrn_prevent_hosp_bef_2014_sql_pqi = cdrn_prevent_hosp_bef_2014_sql_pqi.reset_index(drop=True)

# This function will employ the exclusion rules for each category
def exclusion(df):

    output_filepath1 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/exclusion_results1.csv'

    # Start Exclusion Rules
    for index, row in df.iterrows():
        if (row.htn >= 1 and row.cardiac_proc >= 1) or (row.htn >= 1 and row.htn_exclude >= 1 and row.dialysis_access >=1):
            exclusion_rules1["exclude"].append(1)

        elif row.hf >= 1 and row.cardiac_proc >= 1:
            exclusion_rules1["exclude"].append(1)

        elif row.lower_amputate >= 1 and row.diabetes >= 1 and row.amp_exclude >= 1:
            exclusion_rules1["exclude"].append(1)

        elif row.asthma >= 1 and row.asth_exclude >= 1:
            exclusion_rules1["exclude"].append(1)

        elif row.uti >= 1 and (row.uti_exclude >= 1 or row.immunocomp >= 1 or row.immuno_proc >= 1):
            exclusion_rules1["exclude"].append(1)

        elif row.copd >= 1 and row.copd_exclude >= 1:
            exclusion_rules1["exclude"].append(1)

        elif row.dehydration >= 1 and row.dehyd_exclude >= 1:
            exclusion_rules1["exclude"].append(1)

        elif row.bact_pneu >= 1 and (row.bac_exclude >= 1 or row.immunocomp >= 1 or row.immuno_proc >= 1):
            exclusion_rules1["exclude"].append(1)

        else: exclusion_rules1["exclude"].append(0)

    pd.DataFrame(exclusion_rules1).to_csv(output_filepath1, encoding='utf-8')

exclusion(cdrn_prevent_hosp_2014_sql_pqi)

########################################
########################################
########################################
########################################

# This function will employ the exclusion rules for each category
def exclusion(df):

    output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/exclusion_results2.csv'

    # Start Exclusion Rules
    for index, row in df.iterrows():
        if (row.htn >= 1 and row.cardiac_proc >= 1) or (row.htn >= 1 and row.htn_exclude >= 1 and row.dialysis_access >=1):
            exclusion_rules2["exclude"].append(1)

        elif row.hf >= 1 and row.cardiac_proc >= 1:
            exclusion_rules2["exclude"].append(1)

        elif row.lower_amputate >= 1 and row.diabetes >= 1 and row.amp_exclude >= 1:
            exclusion_rules2["exclude"].append(1)

        elif row.asthma >= 1 and row.asth_exclude >= 1:
            exclusion_rules2["exclude"].append(1)

        elif row.uti >= 1 and (row.uti_exclude >= 1 or row.immunocomp >= 1 or row.immuno_proc >= 1):
            exclusion_rules2["exclude"].append(1)

        elif row.copd >= 1 and row.copd_exclude >= 1:
            exclusion_rules2["exclude"].append(1)

        elif row.dehydration >= 1 and row.dehyd_exclude >= 1:
            exclusion_rules2["exclude"].append(1)

        elif row.bact_pneu >= 1 and (row.bac_exclude >= 1 or row.immunocomp >= 1 or row.immuno_proc >= 1):
            exclusion_rules2["exclude"].append(1)

        else: exclusion_rules2["exclude"].append(0)

    pd.DataFrame(exclusion_rules2).to_csv(output_filepath2, encoding='utf-8')

exclusion(cdrn_prevent_hosp_bef_2014_sql_pqi)


exclusion_results_1 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/exclusion_results1.csv', encoding='utf-8')
exclusion_results_2 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/exclusion_results2.csv', encoding ='utf-8')

cdrn_prevent_hosp_2014_sql_pqi_ = pd.merge(cdrn_prevent_hosp_2014_sql_pqi,exclusion_results_1, left_index=True, right_index=True)
cdrn_prevent_hosp_bef_2014_sql_pqi_ = pd.merge(cdrn_prevent_hosp_bef_2014_sql_pqi,exclusion_results_2, left_index=True, right_index=True)

#####################
print("")
#####################


# Removes unnecessary classifier (Dx) variables and reports the number of unique values in each remaining column
cdrn_prevent_hosp_2014_sql_pqi_edit = cdrn_prevent_hosp_2014_sql_pqi_.drop(cdrn_prevent_hosp_2014_sql_pqi_.columns[4:29], axis =1)
print("Number of unique individuals and visits in cdrn_prevent_hosp_2014_sql_pqi_edit:", cdrn_prevent_hosp_2014_sql_pqi_edit.person_id.nunique(), "&", cdrn_prevent_hosp_2014_sql_pqi_edit.visit_occurrence_id.nunique())

# Removes unnecessary classifier (Dx) variables and reports the number of unique values in each remaining column
cdrn_prevent_hosp_bef_2014_sql_pqi_edit = cdrn_prevent_hosp_bef_2014_sql_pqi_.drop(cdrn_prevent_hosp_bef_2014_sql_pqi_.columns[4:29], axis =1)
print("Number of unique individuals and visits in cdrn_prevent_hosp_bef_2014_sql_pqi_edit:", cdrn_prevent_hosp_bef_2014_sql_pqi_edit.person_id.nunique(), "&", cdrn_prevent_hosp_bef_2014_sql_pqi_edit.visit_occurrence_id.nunique())


#####################
print("")
#####################

cdrn_prevent_hosp_2014 = cdrn_prevent_hosp_2014_sql_pqi_edit[cdrn_prevent_hosp_2014_sql_pqi_edit['exclude'] == 0]
print("Number of unique individuals and visits in cdrn_prevent_hosp_2014:", cdrn_prevent_hosp_2014.person_id.nunique(), "&", cdrn_prevent_hosp_2014.visit_occurrence_id.nunique())

cdrn_prevent_hosp_bef_2014 = cdrn_prevent_hosp_bef_2014_sql_pqi_edit[cdrn_prevent_hosp_bef_2014_sql_pqi_edit['exclude'] == 0]
print("Number of unique individuals and visits in cdrn_prevent_hosp_bef_2014:", cdrn_prevent_hosp_bef_2014.person_id.nunique(), "&", cdrn_prevent_hosp_bef_2014.visit_occurrence_id.nunique())

cdrn_prevent_hosp_2014 = cdrn_prevent_hosp_2014.drop(cdrn_prevent_hosp_2014.columns[3:], axis =1)
cdrn_prevent_hosp_bef_2014 = cdrn_prevent_hosp_bef_2014.drop(cdrn_prevent_hosp_bef_2014.columns[1:], axis =1).drop_duplicates()

pd.DataFrame(cdrn_prevent_hosp_2014).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_2014.csv', encoding ='utf-8')
pd.DataFrame(cdrn_prevent_hosp_bef_2014).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_bef_2014.csv', encoding ='utf-8')