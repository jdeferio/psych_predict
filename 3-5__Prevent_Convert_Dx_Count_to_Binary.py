import pandas as pd

cdrn_ccw_grouped = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_grouped_prevent.csv',encoding='utf-8')
print("cdrn_ccw_grouped length: ", len(cdrn_ccw_grouped))

cdrn_all_demographics = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_demographics.csv',encoding='utf-8', names=['person_id', 'gender', 'birth_date','age_1_jan_2014'])

loc = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_dedup_loc_all.csv',encoding='utf-8')

nta = pd.read_csv('/Users/jdeferio/Documents/Work/Cornell/Social Behavior R01/Projects/SDH/NYC Neighborhood Data/nyc_nta_sdoh.csv', encoding='utf-8')

ccw_modified = {"person_id":[], "acq_hypo_thy":[], "acute_mi":[], "alzheimers":[], "anemia":[], "asthma":[], "a_fib":[], "ben_prost_hyp":[], "cataract":[], "ckd":[], "copd":[], "depression":[], "diabetes":[], "glaucoma":[], "heart_fail":[], "hip_pelv_frac":[], "hyperlipid":[], "htn":[], "ischemic_hd":[], "osteoporosis":[], "ra_oa":[], "stroke_tia":[], "breast_ca":[], "colorectal_ca":[], "prostate_ca":[], "lung_ca":[], "endometrial_ca":[], "adhd":[], "anxiety":[], "autism":[], "bipolar":[], "cerebral_p":[], "cystic_f":[], "epilepsy":[], "chronic_pain":[], "hiv_aids":[], "iq_disable":[], "learn_disable":[], "leukemia":[], "liver":[], "migraine":[], "mobility":[], "ms_tm":[], "muscular_dys":[], "obesity":[], "develop_delay":[], "pvd":[], "personality":[], "ptsd":[], "ulcers":[], "schizo":[], "visual_imp":[], "hearing_imp":[], "spina_bifida":[], "spinal_cord":[], "tobacco":[], "trauma_brain":[], "hepatitis":[], "injury_frm_others":[], "suicide":[], "drug_dep":[], "alc_dep":[], "other_dx":[]}


# ========================================================= #


output_filepath2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_prevent_demo.csv'

output_filepath3 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_prevent_loc.csv'


# ========================================================= #


def dx_convert(df):

    output_filepath =  '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_prevent.csv'


    for _ in df['person_id']:
        ccw_modified["person_id"].append(_)
    print(len(ccw_modified["person_id"]))


# Acquired Hypothyroidism
    for _ in df['acq_hypo_thy']:
        if _ >= 1:
            ccw_modified["acq_hypo_thy"].append(1)
        else: ccw_modified["acq_hypo_thy"].append(0)
    print("Completed Binary Recoding of: Acquired Hypothyroidism")

# Acute Myocardial Infarction
    for _ in df['acute_mi']:
        if _ >= 1:
            ccw_modified["acute_mi"].append(1)
        else:  ccw_modified["acute_mi"].append(0)
    print("Completed Binary Recoding of: Acute Myocardial Infarction")

# Alzheimer's Disease and Related Disorders or Senile Dementia
    for _ in df['alzheimers']:
        if _ >= 1:
            ccw_modified["alzheimers"].append(1)
        else: ccw_modified["alzheimers"].append(0)
    print("Completed Binary Recoding of: Alzheimer's Disease and Related Disorders or Senile Dementia")

# Anemia
    for _ in df['anemia']:
        if _ >= 1:
            ccw_modified["anemia"].append(1)
        else: ccw_modified["anemia"].append(0)
    print("Completed Binary Recoding of: Anemia")

# Asthma
    for _ in df['asthma']:
        if _ >= 1:
            ccw_modified["asthma"].append(1)
        else: ccw_modified["asthma"].append(0)
    print("Completed Binary Recoding of: Asthma")

# Atrial Fibrillation
    for _ in df['a_fib']:
        if _ >= 1:
            ccw_modified["a_fib"].append(1)
        else: ccw_modified["a_fib"].append(0)
    print("Completed Binary Recoding of: Atrial Fibrillation")

# Benign Prostatic Hyperplasia
    for _ in df['ben_prost_hyp']:
        if _ >= 1:
            ccw_modified["ben_prost_hyp"].append(1)
        else: ccw_modified["ben_prost_hyp"].append(0)
    print("Completed Binary Recoding of: Benign Prostatic Hyperplasia")

# Cataract
    for _ in df['cataract']:
        if _ >= 1:
            ccw_modified["cataract"].append(1)
        else: ccw_modified["cataract"].append(0)
    print("Completed Binary Recoding of: Cataract")

# Chronic Kidney Disease
    for _ in df['ckd']:
        if _ >= 1:
            ccw_modified["ckd"].append(1)
        else: ccw_modified["ckd"].append(0)
    print("Completed Binary Recoding of: Chronic Kidney Disease")

# Chronic Obstructive Pulmonary Disease
    for _ in df['copd']:
        if _ >= 1:
            ccw_modified["copd"].append(1)
        else: ccw_modified["copd"].append(0)
    print("Completed Binary Recoding of: Chronic Obstructive Pulmonary Disease")

# Depression
    for _ in df['depression']:
        if _ >= 1:
            ccw_modified["depression"].append(1)
        else: ccw_modified["depression"].append(0)
    print("Completed Binary Recoding of: Depression")

# Diabetes
    for _ in df['diabetes']:
        if _ >= 1:
            ccw_modified["diabetes"].append(1)
        else: ccw_modified["diabetes"].append(0)
    print("Completed Binary Recoding of: Diabetes")

# Glaucoma
    for _ in df['glaucoma']:
        if _ >= 1:
            ccw_modified["glaucoma"].append(1)
        else: ccw_modified["glaucoma"].append(0)
    print("Completed Binary Recoding of: Glaucoma")

# Heart Failure
    for _ in df['heart_fail']:
        if _ >= 1:
            ccw_modified["heart_fail"].append(1)
        else: ccw_modified["heart_fail"].append(0)
    print("Completed Binary Recoding of: Heart Failure")

# Hip / Pelvic Fracture
    for _ in df['hip_pelv_frac']:
        if _ >= 1:
            ccw_modified["hip_pelv_frac"].append(1)
        else: ccw_modified["hip_pelv_frac"].append(0)
    print("Completed Binary Recoding of: Hip / Pelvic Fracture")

# Hyperlipidemia
    for _ in df['hyperlipid']:
        if _ >= 1:
            ccw_modified["hyperlipid"].append(1)
        else: ccw_modified["hyperlipid"].append(0)
    print("Completed Binary Recoding of: Hyperlipidemia")

# Hypertension
    for _ in df['htn']:
        if _ >= 1:
            ccw_modified["htn"].append(1)
        else: ccw_modified["htn"].append(0)
    print("Completed Binary Recoding of: Hypertension")

# Ischemic Heart Disease
    for _ in df['ischemic_hd']:
        if _ >= 1:
            ccw_modified["ischemic_hd"].append(1)
        else: ccw_modified["ischemic_hd"].append(0)
    print("Completed Binary Recoding of: Ischemic Heart Disease")

# Osteoporosis
    for _ in df['osteoporosis']:
        if _ >= 1:
            ccw_modified["osteoporosis"].append(1)
        else: ccw_modified["osteoporosis"].append(0)
    print("Completed Binary Recoding of: Osteoporosis")

# Rheumatoid Arthritis / Osteoarthritis
    for _ in df['ra_oa']:
        if _ >= 1:
            ccw_modified["ra_oa"].append(1)
        else: ccw_modified["ra_oa"].append(0)
    print("Completed Binary Recoding of: Rheumatoid Arthritis / Osteoarthritis")

# Stroke / Trans-Ischemic Attack
    for _ in df['stroke_tia']:
        if _ >= 1:
            ccw_modified["stroke_tia"].append(1)
        else: ccw_modified["stroke_tia"].append(0)
    print("Completed Binary Recoding of: Stroke / Trans-Ischemic Attack")

# Breast Cancer
    for _ in df['breast_ca']:
        if _ >= 1:
            ccw_modified["breast_ca"].append(1)
        else: ccw_modified["breast_ca"].append(0)
    print("Completed Binary Recoding of: Breast Cancer")

# Colorectal Cancer
    for _ in df['colorectal_ca']:
        if _ >= 1:
            ccw_modified["colorectal_ca"].append(1)
        else: ccw_modified["colorectal_ca"].append(0)
    print("Completed Binary Recoding of: Colorectal Cancer")

# Prostate Cancer
    for _ in df['prostate_ca']:
        if _ >= 1:
            ccw_modified["prostate_ca"].append(1)
        else: ccw_modified["prostate_ca"].append(0)
    print("Completed Binary Recoding of: Prostate Cancer")

# Lung Cancer
    for _ in df['lung_ca']:
        if _ >= 1:
            ccw_modified["lung_ca"].append(1)
        else: ccw_modified["lung_ca"].append(0)
    print("Completed Binary Recoding of: Lung Cancer")

# Endometrial Cancer
    for _ in df['endometrial_ca']:
        if _ >= 1:
            ccw_modified["endometrial_ca"].append(1)
        else: ccw_modified["endometrial_ca"].append(0)
    print("Completed Binary Recoding of: Endometrial Cancer")

# ==================================================== #
#
#    START OTHER CHRONIC OR POTENTIALLY DISABLING
#
# ==================================================== #

# ADHD Conduct Disorders and Hyperkinetic Syndrome
    for _ in df['adhd']:
        if _ >= 1:
            ccw_modified["adhd"].append(1)
        else: ccw_modified["adhd"].append(0)
    print("Completed Binary Recoding of: ADHD Conduct Disorders and Hyperkinetic Syndrome")

# Anxiety
    for _ in df['anxiety']:
        if _ >= 1:
            ccw_modified["anxiety"].append(1)
        else: ccw_modified["anxiety"].append(0)
    print("Completed Binary Recoding of: Anxiety")

# Autism Spectrum
    for _ in df['autism']:
        if _ >= 1:
            ccw_modified["autism"].append(1)
        else: ccw_modified["autism"].append(0)
    print("Completed Binary Recoding of: Autism Spectrum")

# Bipolar Disorder
    for _ in df['bipolar']:
        if _ >= 1:
            ccw_modified["bipolar"].append(1)
        else: ccw_modified["bipolar"].append(0)
    print("Completed Binary Recoding of: Bipolar Disorder")

# Cerebral Palsy
    for _ in df['cerebral_p']:
        if _ >= 1:
            ccw_modified["cerebral_p"].append(1)
        else: ccw_modified["cerebral_p"].append(0)
    print("Completed Binary Recoding of: Cerebral Palsy")

# Cystic Fibrosis or Other Metabolic Developmental Disorders
    for _ in df['cystic_f']:
        if _ >= 1:
            ccw_modified["cystic_f"].append(1)
        else: ccw_modified["cystic_f"].append(0)
    print("Completed Binary Recoding of: Cystic Fibrosis or Other Metabolic Developmental Disorders")

# Epilepsy
    for _ in df['epilepsy']:
        if _ >= 1:
            ccw_modified["epilepsy"].append(1)
        else: ccw_modified["epilepsy"].append(0)
    print("Completed Binary Recoding of: Epilepsy")

# Fibromyalgia, Chronic Pain, and Fatigue
    for _ in df['chronic_pain']:
        if _ >= 1:
            ccw_modified["chronic_pain"].append(1)
        else: ccw_modified["chronic_pain"].append(0)
    print("Completed Binary Recoding of: Fibromyalgia, Chronic Pain, and Fatigue")

# HIV / AIDS
    for _ in df['hiv_aids']:
        if _ >= 1:
            ccw_modified["hiv_aids"].append(1)
        else: ccw_modified["hiv_aids"].append(0)
    print("Completed Binary Recoding of: HIV / AIDS")

# Intellectual Disabilities
    for _ in df['iq_disable']:
        if _ >= 1:
            ccw_modified["iq_disable"].append(1)
        else: ccw_modified["iq_disable"].append(0)
    print("Completed Binary Recoding of: Intellectual Disabilities")

# Learning Disabilities
    for _ in df['learn_disable']:
        if _ >= 1:
            ccw_modified["learn_disable"].append(1)
        else: ccw_modified["learn_disable"].append(0)
    print("Completed Binary Recoding of: Learning Disabilities")

# Leukemias and Lymphomas
    for _ in df['leukemia']:
        if _ >= 1:
            ccw_modified["leukemia"].append(1)
        else: ccw_modified["leukemia"].append(0)
    print("Completed Binary Recoding of: Leukemias and Lymphomas")

# Liver Disease, Cirrhosis, and Other Liver Conditions
    for _ in df['liver']:
        if _ >= 1:
            ccw_modified["liver"].append(1)
        else: ccw_modified["liver"].append(0)
    print("Completed Binary Recoding of: Liver Disease, Cirrhosis, and Other Liver Conditions")

# Migraine and Headache
    for _ in df['migraine']:
        if _ >= 1:
            ccw_modified["migraine"].append(1)
        else: ccw_modified["migraine"].append(0)
    print("Completed Binary Recoding of: Migraine and Headache")

# Mobility Impairment
    for _ in df['mobility']:
        if _ >= 1:
            ccw_modified["mobility"].append(1)
        else: ccw_modified["mobility"].append(0)
    print("Completed Binary Recoding of: Mobility Impairment")

# Multiple Sclerosis and Transverse Myelitis
    for _ in df['ms_tm']:
        if _ >= 1:
            ccw_modified["ms_tm"].append(1)
        else: ccw_modified["ms_tm"].append(0)
    print("Completed Binary Recoding of: Multiple Sclerosis and Transverse Myelitis")

# Muscular Dystrophy
    for _ in df['muscular_dys']:
        if _ >= 1:
            ccw_modified["muscular_dys"].append(1)
        else: ccw_modified["muscular_dys"].append(0)
    print("Completed Binary Recoding of: Muscular Dystrophy")

# Obesity
    for _ in df['obesity']:
        if _ >= 1:
            ccw_modified["obesity"].append(1)
        else: ccw_modified["obesity"].append(0)
    print("Completed Binary Recoding of: Obesity")

# Other Developmental Delays
    for _ in df['develop_delay']:
        if _ >= 1:
            ccw_modified["develop_delay"].append(1)
        else: ccw_modified["develop_delay"].append(0)
    print("Completed Binary Recoding of: Other Developmental Delays")

# Peripheral Vascular Disease
    for _ in df['pvd']:
        if _ >= 1:
            ccw_modified["pvd"].append(1)
        else: ccw_modified["pvd"].append(0)
    print("Completed Binary Recoding of: Peripheral Vascular Disease")

# Personality Disorders
    for _ in df['personality']:
        if _ >= 1:
            ccw_modified["personality"].append(1)
        else: ccw_modified["personality"].append(0)
    print("Completed Binary Recoding of: Personality Disorders")

# Post-Traumatic Stress Disorder
    for _ in df['ptsd']:
        if _ >= 1:
            ccw_modified["ptsd"].append(1)
        else: ccw_modified["ptsd"].append(0)
    print("Completed Binary Recoding of: Post-Traumatic Stress Disorder")

# Pressure and Chronic Ulcers
    for _ in df['ulcers']:
        if _ >= 1:
            ccw_modified["ulcers"].append(1)
        else: ccw_modified["ulcers"].append(0)
    print("Completed Binary Recoding of: Pressure and Chronic Ulcers")

# Schizophrenia and Other Psychotic Disorders
    for _ in df['schizo']:
        if _ >= 1:
            ccw_modified["schizo"].append(1)
        else: ccw_modified["schizo"].append(0)
    print("Completed Binary Recoding of: Schizophrenia and Other Psychotic Disorders")

# Sensory – Blindness and Visual Impairment
    for _ in df['visual_imp']:
        if _ >= 1:
            ccw_modified["visual_imp"].append(1)
        else: ccw_modified["visual_imp"].append(0)
    print("Completed Binary Recoding of: Sensory – Blindness and Visual Impairment")

# Sensory – Deafness and Hearing Impairment
    for _ in df['hearing_imp']:
        if _ >= 1:
            ccw_modified["hearing_imp"].append(1)
        else: ccw_modified["hearing_imp"].append(0)
    print("Completed Binary Recoding of: Sensory – Deafness and Hearing Impairment")

# Spina Bifida and Other Congenital Anomalies of the NS
    for _ in df['spina_bifida']:
        if _ >= 1:
            ccw_modified["spina_bifida"].append(1)
        else: ccw_modified["spina_bifida"].append(0)
    print("Completed Binary Recoding of: Spina Bifida and Other Congenital Anomalies of the NS")

# Spinal Cord Injury
    for _ in df['spinal_cord']:
        if _ >= 1:
            ccw_modified["spinal_cord"].append(1)
        else: ccw_modified["spinal_cord"].append(0)
    print("Completed Binary Recoding of: Spinal Cord Injury")

# Tobacco Use
    for _ in df['tobacco']:
        if _ >= 1:
            ccw_modified["tobacco"].append(1)
        else: ccw_modified["tobacco"].append(0)
    print("Completed Binary Recoding of: Tobacco Use")

# Traumatic Brain Injury
    for _ in df['trauma_brain']:
        if _ >= 1:
            ccw_modified["trauma_brain"].append(1)
        else: ccw_modified["trauma_brain"].append(0)
    print("Completed Binary Recoding of: Traumatic Brain Injury")

# Viral Hepatitis
    for _ in df['hepatitis']:
        if _ >= 1:
            ccw_modified["hepatitis"].append(1)
        else: ccw_modified["hepatitis"].append(0)
    print("Completed Binary Recoding of: Viral Hepatitis")


# ============================================= #
#
#      START ASSAULT, HOMICIDE, SUICIDE
#
# ============================================= #

# Homicide and Injury Purposely Inflicted By Others
    for _ in df['injury_frm_others']:
        ccw_modified["injury_frm_others"].append(_)
    print("Completed Binary Recoding of: Homicide and Injury Purposely Inflicted By Others")


# Suicide Attempt / Ideation
    for _ in df['suicide']:
        ccw_modified["suicide"].append(_)
    print("Completed Binary Recoding of: Suicide Attempt / Ideation")

# ============================================= #
#
#    START DRUG & ALCOHOL ABUSE / DEPENDENCE
#
# ============================================= #

    for _ in df['drug_dep']:
        ccw_modified["drug_dep"].append(_)
    print("Completed Binary Recoding of: Drug Abuse / Dependence - Not in Remission")

    for _ in df['alc_dep']:
        ccw_modified["alc_dep"].append(_)
    print("Completed Binary Recoding of: Alcohol Abuse / Dependence - Not in Remission")

    for _ in df['other_dx']:
        ccw_modified["other_dx"].append(_)
    print("Completed Binary Recoding of: Other Dx")

# ============================================= #
#
#      START PSYCH HOSPITALIZATION
#
# ============================================= #

    #for _ in df['psych_hosp']:
     #   ccw_modified["psych_hosp"].append(_)
    #print("Completed Binary Recoding of: Psychiatric Hospitalizations")


    pd.DataFrame(ccw_modified).to_csv(output_filepath, encoding='utf-8')



dx_convert(cdrn_ccw_grouped)

cdrn_ccw_modified = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_prevent.csv',encoding='utf-8')

cdrn_ccw_modified_demo = pd.merge(cdrn_ccw_modified, cdrn_all_demographics, how='inner', on='person_id')

cdrn_ccw_modified_demo = cdrn_ccw_modified_demo.drop(cdrn_ccw_modified_demo.columns[[0,65]], axis =1)

person_list = []
for _ in cdrn_ccw_modified_demo['person_id']:
    person_list.append(_)

gender_list = []
for _ in cdrn_ccw_modified_demo['gender']:
    if _ == 8532:
        gender_list.append(1)
    else: gender_list.append(0)

person_gender = pd.DataFrame({"person_id":person_list,"sex":gender_list})
cdrn_ccw_modified_demo_ = pd.merge(cdrn_ccw_modified_demo,person_gender, how='left', on='person_id')

cdrn_ccw_modified_demo_ = cdrn_ccw_modified_demo_.drop(cdrn_ccw_modified_demo_.columns[[63]], axis =1)

pd.DataFrame(cdrn_ccw_modified_demo_).to_csv(output_filepath2, encoding='utf-8')
print("cdrn_ccw_modified_demo unique patients: ", cdrn_ccw_modified_demo_.person_id.nunique())



cdrn_ccw_modified_loc = pd.merge(cdrn_ccw_modified_demo_, loc, how='inner', on='person_id')
print("cdrn_ccw_modified_loc unique patients: ", cdrn_ccw_modified_loc.person_id.nunique())

cdrn_prevent_hosp_2014_1st_ = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_2014_1st_.csv',encoding='utf-8')

person_list2 = []
for _ in cdrn_ccw_modified_loc['person_id']:
    person_list2.append(_)

prevent_hosp_list_final = []
for _ in cdrn_ccw_modified_loc['person_id']:
    if _ in (list(cdrn_prevent_hosp_2014_1st_['person_id'])):
        prevent_hosp_list_final.append(1)
    else: prevent_hosp_list_final.append(0)

person_hosp = pd.DataFrame({"person_id":person_list2,"hosp_any":prevent_hosp_list_final})
cdrn_ccw_modified_loc = pd.merge(cdrn_ccw_modified_loc,person_hosp, how='left', on='person_id')

# Reset Index
cdrn_ccw_modified_loc = cdrn_ccw_modified_loc.reset_index(drop=True)

dx_cols = list(cdrn_ccw_modified_loc.columns[1:63])
cdrn_ccw_modified_loc['no_dx'] = cdrn_ccw_modified_loc[dx_cols].sum(axis=1)

no_dx_flag = []
for _ in cdrn_ccw_modified_loc['no_dx']:
    if _ == 0:
        no_dx_flag.append(1)
    else: no_dx_flag.append(0)
no_dx_flag_ = pd.DataFrame({"no_dx_flag":no_dx_flag})

cdrn_ccw_modified_loc = pd.merge(cdrn_ccw_modified_loc,no_dx_flag_, left_index=True, right_index=True)

cdrn_ccw_modified_loc = cdrn_ccw_modified_loc.drop(cdrn_ccw_modified_loc.columns[[65,66,68,71,72,73,74,75,76,77,78,80]], axis =1)

pd.DataFrame(cdrn_ccw_modified_loc).to_csv(output_filepath3, encoding='utf-8')

cdrn_ccw_modified_nta = pd.merge(cdrn_ccw_modified_loc, nta, how='left', on='nta_code')
print(len(cdrn_ccw_modified_nta))

pd.DataFrame(cdrn_ccw_modified_nta).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_nta_prevent.csv',encoding='utf-8')