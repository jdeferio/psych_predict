import pandas as pd
import datetime as dt


output_filepath =  '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_grouped_all.csv'

# ============================================= #
#
#            IMPORT DATA SETS
#
# ============================================= #

cdrn_ccw_results = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_results.csv', encoding='utf-8')
print("Number of unique person_id in cdrn_ccw_results: ", cdrn_ccw_results.person_id.nunique())

cdrn_all_hosp_bef_2014 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_hosp_bef_2014.csv', encoding='utf-8', names=['person_id'])

cdrn_all_hosp_2014 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_hosp_2014.csv', encoding='utf-8', names=['person_id', 'visit_start_date', 'visit_concept_id'])

cdrn_all_visits_2014 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_visits_2014.csv', encoding='utf-8', names=['person_id', 'condition_start_date', 'visit_type'])



# ============================================= #
#
# START CREATION OF 1ST HOSP IN 2014 FILE
#
# ============================================= #

# Sorts df by 'person_id' and 'visit_start_date'
cdrn_all_hosp_2014 = cdrn_all_hosp_2014.sort_values(by=['person_id','visit_start_date'])
print("Length and Number of unique person_id's with any hospitalization in 2014: ", len(cdrn_all_hosp_2014),", ",cdrn_all_hosp_2014.person_id.nunique())

# Creates var 'hosp_num' which is a successive count of hospitalizations per 'person_id' (ascending order by date)
# Identifies the first hospitalization in 2014, but is not necessarily the first hosp ever
cdrn_all_hosp_2014['hosp_num'] = cdrn_all_hosp_2014.groupby('person_id').visit_start_date.apply(pd.Series.rank)

# Creates new df where only the first hospitalization in 2014 is retained
cdrn_all_hosp_2014_1st = cdrn_all_hosp_2014[cdrn_all_hosp_2014['hosp_num'] == 1.0]
print("Length of all hospitalizations in 2014: ", len(cdrn_all_hosp_2014_1st))

# Reset Index
cdrn_all_hosp_2014_1st = cdrn_all_hosp_2014_1st.reset_index(drop=True)

# Creates a filters patients who had a previous hospitalization
# id_list = []
# for _ in cdrn_all_hosp_2014_1st['person_id']:
#     id_list.append(_)
# print("Length id_list:", len(id_list))

prev_hosp = []
for _ in cdrn_all_hosp_2014_1st['person_id']:
    if _ in(set(list(cdrn_all_hosp_bef_2014['person_id']))):
        prev_hosp.append(1)
    else: prev_hosp.append(0)
print("Length prev_hosp:", len(prev_hosp))

first_hosp_id = pd.DataFrame({"id":prev_hosp})

# Join the filter first_hosp_id['id'] with the analysis file
cdrn_hosp_flag = pd.merge(cdrn_all_hosp_2014_1st,first_hosp_id, left_index=True, right_index=True)
print("Length cdrn_hosp flag:",len(cdrn_hosp_flag))


# Remove Patients that had a previous hospitalization
cdrn_all_hosp_2014_1st_ = cdrn_hosp_flag[cdrn_hosp_flag['id'] == 0]

# cdrn_all_hosp_2014_1st_ = cdrn_all_hosp_2014_1st_.drop(cdrn_all_hosp_2014_1st_.columns[[1,2,3,4]], axis =1).drop_duplicates()
print("Number of unique persons who do NOT have a hospitalization prior to 2014: ", len(cdrn_all_hosp_2014_1st_), cdrn_all_hosp_2014_1st_.person_id.nunique())
pd.DataFrame(cdrn_all_hosp_2014_1st_).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_hosp_2014_1st_.csv', encoding='utf-8')

# Merges the 2014 hospitalization file with the CCW results
cdrn_1st_hosp_dx = pd.merge(cdrn_all_hosp_2014_1st_, cdrn_ccw_results, how='inner', on='person_id')
print("Number of unique persons with a hospitalization and dx / visit history:", cdrn_1st_hosp_dx.person_id.nunique())
print("Length of cdrn_1st_hosp_dx:", len(cdrn_1st_hosp_dx))


# Filters the resultant df so that only the dx that occurred on or before the first hospitalization are present
cdrn_1st_hosp_dx = cdrn_1st_hosp_dx[(cdrn_1st_hosp_dx.condition_start_date < cdrn_1st_hosp_dx.visit_start_date)]
print("Number of unique persons with a hospitalization and dx history < hospitalization date:", cdrn_1st_hosp_dx.person_id.nunique())


# # Reset the Index
# cdrn_all_hosp_2014_1st_ = cdrn_all_hosp_2014_1st_.reset_index(drop=True)
#
# hosp_included = list(cdrn_all_individual_visits.person_id.values)
# hosp_missing_dict = {"psych_missing":[]}
# for _ in cdrn_psych_hosp_2014_1st_['person_id']:
#     if _ in set(psych_included):
#         psych_missing_dict["psych_missing"].append(0)
#     else: psych_missing_dict["psych_missing"].append(1)
#
# print("psych_missing length: ", len(psych_missing_dict["psych_missing"]))
# print("cdrn_psych_hosp_2014_1st_ length: ", len(cdrn_psych_hosp_2014_1st_))
#
# # Creates DataFrame of the List
# psych_missing_df = pd.DataFrame({"psych_missing":psych_missing_dict["psych_missing"]})
#
# # Merges df psych_missing with the psych hospitalizations
# cdrn_psych_hosp_2014_1st_edit = pd.merge(cdrn_psych_hosp_2014_1st_, psych_missing_df, left_index=True, right_index=True)
#
# cdrn_psych_hosp_2014_1st_edit = cdrn_psych_hosp_2014_1st_edit[cdrn_psych_hosp_2014_1st_edit['psych_missing'] == 1]
# print("Missing psych hospitalizations: ", len(cdrn_psych_hosp_2014_1st_edit))
#
# psych_results_ccw = {"person_id":[], "condition_start_date":[], "acq_hypo_thy":[], "acute_mi":[], "alzheimers":[], "anemia":[], "asthma":[], "a_fib":[], "ben_prost_hyp":[], "cataract":[], "ckd":[], "copd":[], "depression":[], "diabetes":[], "glaucoma":[], "heart_fail":[], "hip_pelv_frac":[], "hyperlipid":[], "htn":[], "ischemic_hd":[], "osteoporosis":[], "ra_oa":[], "stroke_tia":[], "breast_ca":[], "colorectal_ca":[], "prostate_ca":[], "lung_ca":[], "endometrial_ca":[], "adhd":[], "anxiety":[], "autism":[], "bipolar":[], "cerebral_p":[], "cystic_f":[], "epilepsy":[], "chronic_pain":[], "hiv_aids":[], "iq_disable":[], "learn_disable":[], "leukemia":[], "liver":[], "migraine":[], "mobility":[], "ms_tm":[], "muscular_dys":[], "obesity":[], "develop_delay":[], "pvd":[], "personality":[], "ptsd":[], "ulcers":[], "schizo":[], "visual_imp":[], "hearing_imp":[], "spina_bifida":[], "spinal_cord":[], "tobacco":[], "trauma_brain":[], "hepatitis":[], "injury_frm_others":[], "suicide":[], "drug_dep":[], "alc_dep":[], "other_dx":[]}


# output_filepath5 =  '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_ccw_results.csv'
#
# for _ in cdrn_psych_hosp_2014_1st_edit['person_id']:
#     psych_results_ccw["person_id"].append(_)
# print(len(psych_results_ccw["person_id"]))
#
# for _ in cdrn_psych_hosp_2014_1st_edit['visit_start_date']:
#     psych_results_ccw["condition_start_date"].append(_)
# print(len(psych_results_ccw["condition_start_date"]))
#
#
# for _ in cdrn_psych_hosp_2014_1st_edit['person_id']:
#     psych_results_ccw["acq_hypo_thy"].append(0)
#     psych_results_ccw["acute_mi"].append(0)
#     psych_results_ccw["alzheimers"].append(0)
#     psych_results_ccw["anemia"].append(0)
#     psych_results_ccw["asthma"].append(0)
#     psych_results_ccw["a_fib"].append(0)
#     psych_results_ccw["ben_prost_hyp"].append(0)
#     psych_results_ccw["cataract"].append(0)
#     psych_results_ccw["ckd"].append(0)
#     psych_results_ccw["copd"].append(0)
#     psych_results_ccw["depression"].append(0)
#     psych_results_ccw["diabetes"].append(0)
#     psych_results_ccw["glaucoma"].append(0)
#     psych_results_ccw["heart_fail"].append(0)
#     psych_results_ccw["hip_pelv_frac"].append(0)
#     psych_results_ccw["hyperlipid"].append(0)
#     psych_results_ccw["htn"].append(0)
#     psych_results_ccw["ischemic_hd"].append(0)
#     psych_results_ccw["osteoporosis"].append(0)
#     psych_results_ccw["ra_oa"].append(0)
#     psych_results_ccw["stroke_tia"].append(0)
#     psych_results_ccw["breast_ca"].append(0)
#     psych_results_ccw["colorectal_ca"].append(0)
#     psych_results_ccw["prostate_ca"].append(0)
#     psych_results_ccw["lung_ca"].append(0)
#     psych_results_ccw["endometrial_ca"].append(0)
#     psych_results_ccw["adhd"].append(0)
#     psych_results_ccw["anxiety"].append(0)
#     psych_results_ccw["autism"].append(0)
#     psych_results_ccw["bipolar"].append(0)
#     psych_results_ccw["cerebral_p"].append(0)
#     psych_results_ccw["cystic_f"].append(0)
#     psych_results_ccw["epilepsy"].append(0)
#     psych_results_ccw["chronic_pain"].append(0)
#     psych_results_ccw["hiv_aids"].append(0)
#     psych_results_ccw["iq_disable"].append(0)
#     psych_results_ccw["learn_disable"].append(0)
#     psych_results_ccw["leukemia"].append(0)
#     psych_results_ccw["liver"].append(0)
#     psych_results_ccw["migraine"].append(0)
#     psych_results_ccw["mobility"].append(0)
#     psych_results_ccw["ms_tm"].append(0)
#     psych_results_ccw["muscular_dys"].append(0)
#     psych_results_ccw["obesity"].append(0)
#     psych_results_ccw["develop_delay"].append(0)
#     psych_results_ccw["pvd"].append(0)
#     psych_results_ccw["personality"].append(0)
#     psych_results_ccw["ptsd"].append(0)
#     psych_results_ccw["ulcers"].append(0)
#     psych_results_ccw["schizo"].append(0)
#     psych_results_ccw["visual_imp"].append(0)
#     psych_results_ccw["hearing_imp"].append(0)
#     psych_results_ccw["spina_bifida"].append(0)
#     psych_results_ccw["spinal_cord"].append(0)
#     psych_results_ccw["tobacco"].append(0)
#     psych_results_ccw["trauma_brain"].append(0)
#     psych_results_ccw["hepatitis"].append(0)
#     psych_results_ccw["injury_frm_others"].append(0)
#     psych_results_ccw["suicide"].append(0)
#     psych_results_ccw["drug_dep"].append(0)
#     psych_results_ccw["alc_dep"].append(0)
#     psych_results_ccw["other_dx"].append(0)
#
# pd.DataFrame(psych_results_ccw).to_csv(output_filepath5, encoding='utf-8')


# merge cdrn_psych_hosp_2014_1st id and condition start date with the utilization file where the visit_start_date is less than the hospitalization date
# Convert the different visit codes into variables ED, Inpt, Outpt, Other Ambulatory, Other in 2014 with the same convert method used in __4__



# ============================================= #
#
#     START CREATION OF NO HOSP FILE
#
# ============================================= #


# Creates a df of 'person_id' for people who had a hospitalization before end of 2014
cdrn_all_hosp = cdrn_all_hosp_2014.person_id.append(cdrn_all_hosp_bef_2014.person_id).drop_duplicates()

all_hosp_list = []
for _ in cdrn_all_hosp:
    all_hosp_list.append(_)

ids = [1 for i in range(len(all_hosp_list))]
hosp_id = pd.DataFrame({"person_id":all_hosp_list,"id":ids})
cdrn_no_hosp_flag = pd.merge(cdrn_ccw_results,hosp_id, how='left', on='person_id')


# Removes patients with a previous hospitalization
cdrn_no_hosp_dx = cdrn_no_hosp_flag[cdrn_no_hosp_flag['id'] != 1]
print("Number of patients with no hospitalizations: ", cdrn_no_hosp_dx.person_id.nunique())

feat = ['person_id']
no_allcause = cdrn_no_hosp_dx.loc[:,feat]
no_allcause = no_allcause.drop_duplicates()
print(len(no_allcause))
pd.DataFrame(no_allcause).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/no_allcause_hosp.csv', encoding='utf-8')



# cdrn_all_hosp_missing = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_ccw_results.csv', encoding='utf-8')

cdrn_no_hosp_dx = cdrn_no_hosp_dx.drop(cdrn_no_hosp_dx.columns[[0,65]], axis=1)

cdrn_1st_hosp_dx = cdrn_1st_hosp_dx.drop(cdrn_1st_hosp_dx.columns[[1,2,3,4,5]], axis=1)

# cdrn_all_hosp_missing = cdrn_all_hosp_missing.drop(cdrn_all_hosp_missing.columns[[0]], axis = 1)

cdrn_hosp_dx_all = cdrn_no_hosp_dx.append(cdrn_1st_hosp_dx, sort=False)
print("Length cdrn_hosp_dx_all: ",len(cdrn_hosp_dx_all))

# cdrn_all_dx_all = cdrn_all_dx_all.append(cdrn_all_hosp_missing, sort=False)
# print("Length cdrn_all_dx_all: ",len(cdrn_all_dx_all_))


# Converts Longitudinal Data to Aggregate Counts Per Patient
cdrn_ccw_grouped = cdrn_hosp_dx_all.groupby('person_id').agg({"acq_hypo_thy":sum, "acute_mi":sum, "alzheimers":sum, "anemia":sum, "asthma":sum, "a_fib":sum, "ben_prost_hyp":sum, "cataract":sum, "ckd":sum, "copd":sum, "depression":sum, "diabetes":sum, "glaucoma":sum, "heart_fail":sum, "hip_pelv_frac":sum, "hyperlipid":sum, "htn":sum, "ischemic_hd":sum, "osteoporosis":sum, "ra_oa":sum, "stroke_tia":sum, "breast_ca":sum, "colorectal_ca":sum, "prostate_ca":sum, "lung_ca":sum, "endometrial_ca":sum, "adhd":sum, "anxiety":sum, "autism":sum, "bipolar":sum, "cerebral_p":sum, "cystic_f":sum, "epilepsy":sum, "chronic_pain":sum, "hiv_aids":sum, "iq_disable":sum, "learn_disable":sum, "leukemia":sum, "liver":sum, "migraine":sum, "mobility":sum, "ms_tm":sum, "muscular_dys":sum, "obesity":sum, "develop_delay":sum, "pvd":sum, "personality":sum, "ptsd":sum, "ulcers":sum, "schizo":sum, "visual_imp":sum, "hearing_imp":sum, "spina_bifida":sum, "spinal_cord":sum, "tobacco":sum, "trauma_brain":sum, "hepatitis":sum, "injury_frm_others":sum, "suicide":sum, "drug_dep":sum, "alc_dep":sum, "other_dx":sum})

pd.DataFrame(cdrn_ccw_grouped).to_csv(output_filepath, encoding='utf-8')

# ========================================================================= #
#
#     START CREATION OF 2014 UTILIZATION METRICS FOR HOSP PTS
#
# ========================================================================= #

cdrn_hosp_util_2014 = pd.merge(cdrn_all_hosp_2014_1st_.drop(cdrn_all_hosp_2014_1st_.columns[[2,3,4]], axis=1),cdrn_all_visits_2014, how='left', on='person_id')

cdrn_hosp_util_2014 = cdrn_hosp_util_2014[(cdrn_hosp_util_2014.condition_start_date < cdrn_hosp_util_2014.visit_start_date)]

cdrn_no_hosp_util_2014 = pd.merge(cdrn_no_hosp_dx.drop(cdrn_no_hosp_dx.columns[1:], axis =1).drop_duplicates(), cdrn_all_visits_2014, how='left', on='person_id').fillna(0)

util2014 = {"person_id": [], "ed2014": [], "inpt_2014":[], "outpt_2014": [], "amb_2014": [], "other_2014": []}


def util_convert(df):
    output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_2014_util_vars_allcause.csv'

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

util2014_ = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_2014_util_vars_allcause.csv', encoding='utf-8')

# Converts Longitudinal Data to Aggregate Counts Per Patient
cdrn_util2014_grouped = util2014_.groupby('person_id').agg({"ed2014":sum, "inpt_2014":sum, "outpt_2014":sum, "amb_2014":sum, "other_2014":sum})

pd.DataFrame(cdrn_util2014_grouped).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_util2014_allcause_grouped.csv', encoding='utf-8')
