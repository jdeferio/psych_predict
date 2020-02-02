import pandas as pd

cdrn_dx_hosp = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_dx_hosp.csv',encoding='utf-8')
cdrn_dx_hosp = cdrn_dx_hosp.drop(cdrn_dx_hosp.columns[[0]], axis=1)


results_ccw = {"person_id":[], "condition_start_date":[], "acq_hypo_thy":[], "acute_mi":[], "alzheimers":[], "anemia":[], "asthma":[], "a_fib":[], "ben_prost_hyp":[], "cataract":[], "ckd":[], "copd":[], "depression":[], "diabetes":[], "glaucoma":[], "heart_fail":[], "hip_pelv_frac":[], "hyperlipid":[], "htn":[], "ischemic_hd":[], "osteoporosis":[], "ra_oa":[], "stroke_tia":[], "breast_ca":[], "colorectal_ca":[], "prostate_ca":[], "lung_ca":[], "endometrial_ca":[], "adhd":[], "anxiety":[], "autism":[], "bipolar":[], "cerebral_p":[], "cystic_f":[], "epilepsy":[], "chronic_pain":[], "hiv_aids":[], "iq_disable":[], "learn_disable":[], "leukemia":[], "liver":[], "migraine":[], "mobility":[], "ms_tm":[], "muscular_dys":[], "obesity":[], "develop_delay":[], "pvd":[], "personality":[], "ptsd":[], "ulcers":[], "schizo":[], "visual_imp":[], "hearing_imp":[], "spina_bifida":[], "spinal_cord":[], "tobacco":[], "trauma_brain":[], "hepatitis":[], "injury_frm_others":[], "suicide":[], "psych_hosp":[]}



def dx_convert(cdrn_dx_hosp):

    output_filepath =  '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_results.csv'

    for _ in cdrn_dx_hosp['person_id']:
        results_ccw["person_id"].append(_)
    print(len(results_ccw["person_id"]))

    for _ in cdrn_dx_hosp['condition_start_date']:
        results_ccw["condition_start_date"].append(_)
    print(len(results_ccw["condition_start_date"]))


# Acquired Hypothyroidism
    for index,_ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:244.0','ICD9CM:244.1','ICD9CM:244.2','ICD9CM:244.3','ICD9CM:244.8','ICD9CM:244.9'):
            results_ccw["acq_hypo_thy"].append(1)
        else: results_ccw["acq_hypo_thy"].append(0)
    print("Completed Binary Recoding of: Acquired Hypothyroidism")

# Acute Myocardial Infarction
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:410.01','ICD9CM:410.11','ICD9CM:410.21','ICD9CM:410.31','ICD9CM:410.41','ICD9CM:410.51','ICD9CM:410.61','ICD9CM:410.71','ICD9CM:410.81','ICD9CM:410.91'):
            results_ccw["acute_mi"].append(1)
        else:  results_ccw["acute_mi"].append(0)
    print("Completed Binary Recoding of: Acute Myocardial Infarction")

# Alzheimer's Disease and Related Disorders or Senile Dementia
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:331.0','ICD9CM:331.11','ICD9CM:331.19','ICD9CM:331.2','ICD9CM:331.7','ICD9CM:290.0','ICD9CM:290.10','ICD9CM:290.11','ICD9CM:290.12','ICD9CM:290.13','ICD9CM:290.20','ICD9CM:290.21','ICD9CM:290.3','ICD9CM:290.40','ICD9CM:290.41','ICD9CM:290.42','ICD9CM:290.43','ICD9CM:294.0','ICD9CM:294.10','ICD9CM:294.11','ICD9CM:294.20','ICD9CM:294.21','ICD9CM:294.8','ICD9CM:797'):
            results_ccw["alzheimers"].append(1)
        else: results_ccw["alzheimers"].append(0)
    print("Completed Binary Recoding of: Alzheimer's Disease and Related Disorders or Senile Dementia")

# Anemia
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:280.0','ICD9CM:280.1','ICD9CM:280.8','ICD9CM:280.9','ICD9CM:281.0','ICD9CM:281.1','ICD9CM:281.2','ICD9CM:281.3','ICD9CM:281.4','ICD9CM:281.8','ICD9CM:281.9','ICD9CM:282.0','ICD9CM:282.1','ICD9CM:282.2','ICD9CM:282.3','ICD9CM:282.40','ICD9CM:282.41','ICD9CM:282.42','ICD9CM:282.43','ICD9CM:282.44','ICD9CM:282.45','ICD9CM:282.46','ICD9CM:282.47','ICD9CM:282.49','ICD9CM:282.5','ICD9CM:282.60','ICD9CM:282.61','ICD9CM:282.62','ICD9CM:282.63','ICD9CM:282.64','ICD9CM:282.68','ICD9CM:282.69','ICD9CM:282.7','ICD9CM:282.8','ICD9CM:282.9','ICD9CM:283.0','ICD9CM:283.10','ICD9CM:283.11','ICD9CM:283.19','ICD9CM:283.2','ICD9CM:283.9','ICD9CM:284.01','ICD9CM:284.09','ICD9CM:284.11','ICD9CM:284.12','ICD9CM:284.19','ICD9CM:284.2','ICD9CM:284.81','ICD9CM:284.89','ICD9CM:284.9','ICD9CM:285.0','ICD9CM:285.1','ICD9CM:285.21','ICD9CM:285.22','ICD9CM:285.29','ICD9CM:285.3','ICD9CM:285.8','ICD9CM:285.9'):
            results_ccw["anemia"].append(1)
        else: results_ccw["anemia"].append(0)
    print("Completed Binary Recoding of: Anemia")

# Asthma
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:493.00','ICD9CM:493.01','ICD9CM:493.02','ICD9CM:493.10','ICD9CM:493.11','ICD9CM:493.12','ICD9CM:493.20','ICD9CM:493.21','ICD9CM:493.22','ICD9CM:493.81','ICD9CM:493.82','ICD9CM:493.90','ICD9CM:493.91','ICD9CM:493.92'):
            results_ccw["asthma"].append(1)
        else: results_ccw["asthma"].append(0)
    print("Completed Binary Recoding of: Asthma")

# Atrial Fibrillation
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in 'ICD9CM:427.31':
            results_ccw["a_fib"].append(1)
        else: results_ccw["a_fib"].append(0)
    print("Completed Binary Recoding of: Atrial Fibrillation")

# Benign Prostatic Hyperplasia
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:600.00','ICD9CM:600.01','ICD9CM:600.10','ICD9CM:600.11','ICD9CM:600.20','ICD9CM:600.21','ICD9CM:600.3','ICD9CM:600.90','ICD9CM:600.91'):
            results_ccw["ben_prost_hyp"].append(1)
        else: results_ccw["ben_prost_hyp"].append(0)
    print("Completed Binary Recoding of: Benign Prostatic Hyperplasia")

# Cataract
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:366.01','ICD9CM:366.02','ICD9CM:366.03','ICD9CM:366.04','ICD9CM:366.09','ICD9CM:366.10','ICD9CM:366.12','ICD9CM:366.13','ICD9CM:366.14','ICD9CM:366.15','ICD9CM:366.16','ICD9CM:366.17','ICD9CM:366.18','ICD9CM:366.19','ICD9CM:366.20','ICD9CM:366.21','ICD9CM:366.22','ICD9CM:366.23','ICD9CM:366.30','ICD9CM:366.45','ICD9CM:366.46','ICD9CM:366.50','ICD9CM:366.51','ICD9CM:366.52','ICD9CM:366.53','ICD9CM:366.8','ICD9CM:366.9','ICD9CM:379.26','ICD9CM:379.31','ICD9CM:379.39','ICD9CM:743.30','ICD9CM:743.31','ICD9CM:743.32','ICD9CM:743.33'):
            results_ccw["cataract"].append(1)
        else: results_ccw["cataract"].append(0)
    print("Completed Binary Recoding of: Cataract")

# Chronic Kidney Disease
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:016.00','ICD9CM:016.01','ICD9CM:016.02','ICD9CM:016.03','ICD9CM:016.04','ICD9CM:016.05','ICD9CM:016.06','ICD9CM:095.4','ICD9CM:189.0','ICD9CM:189.9','ICD9CM:223.0','ICD9CM:236.91','ICD9CM:249.40','ICD9CM:249.41','ICD9CM:250.40','ICD9CM:250.41','ICD9CM:250.42','ICD9CM:250.43','ICD9CM:271.4','ICD9CM:274.10','ICD9CM:283.11','ICD9CM:403.01','ICD9CM:403.11','ICD9CM:403.91','ICD9CM:404.02','ICD9CM:404.03','ICD9CM:404.12','ICD9CM:404.13','ICD9CM:404.92','ICD9CM:404.93','ICD9CM:440.1','ICD9CM:442.1','ICD9CM:572.4','ICD9CM:580.0','ICD9CM:580.4','ICD9CM:580.81','ICD9CM:580.89','ICD9CM:580.9','ICD9CM:581.0','ICD9CM:581.1','ICD9CM:581.2','ICD9CM:581.3','ICD9CM:581.81','ICD9CM:581.89','ICD9CM:581.9','ICD9CM:582.0','ICD9CM:582.1','ICD9CM:582.2','ICD9CM:582.4','ICD9CM:582.81','ICD9CM:582.89','ICD9CM:582.9','ICD9CM:583.0','ICD9CM:583.1','ICD9CM:583.2','ICD9CM:583.4','ICD9CM:583.6','ICD9CM:583.7','ICD9CM:583.81','ICD9CM:583.89','ICD9CM:583.9','ICD9CM:584.5','ICD9CM:584.6','ICD9CM:584.7','ICD9CM:584.8','ICD9CM:584.9','ICD9CM:585.1','ICD9CM:585.2','ICD9CM:585.3','ICD9CM:585.4','ICD9CM:585.5','ICD9CM:585.6','ICD9CM:585.9','ICD9CM:586','ICD9CM:587','ICD9CM:588.0','ICD9CM:588.1','ICD9CM:588.81','ICD9CM:588.89','ICD9CM:588.9','ICD9CM:591','ICD9CM:753.12','ICD9CM:753.13','ICD9CM:753.14','ICD9CM:753.15','ICD9CM:753.16','ICD9CM:753.17','ICD9CM:753.19','ICD9CM:753.20','ICD9CM:753.21','ICD9CM:753.22','ICD9CM:753.23','ICD9CM:753.29','ICD9CM:794.4'):
            results_ccw["ckd"].append(1)
        else: results_ccw["ckd"].append(0)
    print("Completed Binary Recoding of: Chronic Kidney Disease")

# Chronic Obstructive Pulmonary Disease
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:490','ICD9CM:491.0','ICD9CM:491.1','ICD9CM:491.8','ICD9CM:491.9','ICD9CM:492.0','ICD9CM:492.8','ICD9CM:491.20','ICD9CM:491.21','ICD9CM:491.22','ICD9CM:494.0','ICD9CM:494.1','ICD9CM:496'):
            results_ccw["copd"].append(1)
        else: results_ccw["copd"].append(0)
    print("Completed Binary Recoding of: Chronic Obstructive Pulmonary Disease")

# Depression
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:296.20','ICD9CM:296.21','ICD9CM:296.22','ICD9CM:296.23','ICD9CM:296.24','ICD9CM:296.25','ICD9CM:296.26','ICD9CM:296.30','ICD9CM:296.31','ICD9CM:296.32','ICD9CM:296.33','ICD9CM:296.34','ICD9CM:296.35','ICD9CM:296.36','ICD9CM:296.51','ICD9CM:296.52','ICD9CM:296.53','ICD9CM:296.54','ICD9CM:296.55','ICD9CM:296.56','ICD9CM:296.60','ICD9CM:296.61','ICD9CM:296.62','ICD9CM:296.63','ICD9CM:296.64','ICD9CM:296.65','ICD9CM:296.66','ICD9CM:296.89','ICD9CM:298.0','ICD9CM:300.4','ICD9CM:311'):
            results_ccw["depression"].append(1)
        else: results_ccw["depression"].append(0)
    print("Completed Binary Recoding of: Depression")

# Diabetes
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:249.00','ICD9CM:249.01','ICD9CM:249.10','ICD9CM:249.11','ICD9CM:249.20','ICD9CM:249.21','ICD9CM:249.30','ICD9CM:249.31','ICD9CM:249.40','ICD9CM:249.41','ICD9CM:249.50','ICD9CM:249.51','ICD9CM:249.60','ICD9CM:249.61','ICD9CM:249.70','ICD9CM:249.71','ICD9CM:249.80','ICD9CM:249.81','ICD9CM:249.90','ICD9CM:249.91','ICD9CM:250.00','ICD9CM:250.01','ICD9CM:250.02','ICD9CM:250.03','ICD9CM:250.10','ICD9CM:250.11','ICD9CM:250.12','ICD9CM:250.13','ICD9CM:250.20','ICD9CM:250.21','ICD9CM:250.22','ICD9CM:250.23','ICD9CM:250.30','ICD9CM:250.31','ICD9CM:250.32','ICD9CM:250.33','ICD9CM:250.40','ICD9CM:250.41','ICD9CM:250.42','ICD9CM:250.43','ICD9CM:250.50','ICD9CM:250.51','ICD9CM:250.52','ICD9CM:250.53','ICD9CM:250.60','ICD9CM:250.61','ICD9CM:250.62','ICD9CM:250.63','ICD9CM:250.70','ICD9CM:250.71','ICD9CM:250.72','ICD9CM:250.73','ICD9CM:250.80','ICD9CM:250.81','ICD9CM:250.82','ICD9CM:250.83','ICD9CM:250.90','ICD9CM:250.91','ICD9CM:250.92','ICD9CM:250.93','ICD9CM:357.2','ICD9CM:362.01','ICD9CM:362.02','ICD9CM:362.03','ICD9CM:362.04','ICD9CM:362.05','ICD9CM:362.06','ICD9CM:366.41'):
            results_ccw["diabetes"].append(1)
        else: results_ccw["diabetes"].append(0)
    print("Completed Binary Recoding of: Diabetes")

# Glaucoma
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:362.85','ICD9CM:365.00','ICD9CM:365.01','ICD9CM:365.02','ICD9CM:365.03','ICD9CM:365.04','ICD9CM:365.10','ICD9CM:365.11','ICD9CM:365.12','ICD9CM:365.13','ICD9CM:365.15','ICD9CM:365.20','ICD9CM:365.21','ICD9CM:365.22','ICD9CM:365.23','ICD9CM:365.24','ICD9CM:365.31','ICD9CM:365.32','ICD9CM:365.41','ICD9CM:365.42','ICD9CM:365.43','ICD9CM:365.51','ICD9CM:365.52','ICD9CM:365.59','ICD9CM:365.60','ICD9CM:365.61','ICD9CM:365.62','ICD9CM:365.63','ICD9CM:365.64','ICD9CM:365.65','ICD9CM:365.81','ICD9CM:365.82','ICD9CM:365.83','ICD9CM:365.89','ICD9CM:365.9','ICD9CM:377.14'):
            results_ccw["glaucoma"].append(1)
        else: results_ccw["glaucoma"].append(0)
    print("Completed Binary Recoding of: Glaucoma")

# Heart Failure
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:398.91','ICD9CM:402.01','ICD9CM:402.11','ICD9CM:402.91','ICD9CM:404.01','ICD9CM:404.03','ICD9CM:404.11','ICD9CM:404.13','ICD9CM:404.91','ICD9CM:404.93','ICD9CM:428.0','ICD9CM:428.1','ICD9CM:428.20','ICD9CM:428.21','ICD9CM:428.22','ICD9CM:428.23','ICD9CM:428.30','ICD9CM:428.31','ICD9CM:428.32','ICD9CM:428.33','ICD9CM:428.40','ICD9CM:428.41','ICD9CM:428.42','ICD9CM:428.43','ICD9CM:428.9'):
            results_ccw["heart_fail"].append(1)
        else: results_ccw["heart_fail"].append(0)
    print("Completed Binary Recoding of: Heart Failure")

# Hip / Pelvic Fracture
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:733.14','ICD9CM:733.15','ICD9CM:733.96','ICD9CM:733.97','ICD9CM:733.98','ICD9CM:808.0','ICD9CM:808.1','ICD9CM:808.2','ICD9CM:808.3','ICD9CM:808.41','ICD9CM:808.42','ICD9CM:808.43','ICD9CM:808.44','ICD9CM:808.49','ICD9CM:808.51','ICD9CM:808.52','ICD9CM:808.53','ICD9CM:808.54','ICD9CM:808.59','ICD9CM:808.8','ICD9CM:808.9','ICD9CM:820.00','ICD9CM:820.01','ICD9CM:820.02','ICD9CM:820.03','ICD9CM:820.09','ICD9CM:820.10','ICD9CM:820.11','ICD9CM:820.12','ICD9CM:820.13','ICD9CM:820.19','ICD9CM:820.20','ICD9CM:820.21','ICD9CM:820.22','ICD9CM:820.30','ICD9CM:820.31','ICD9CM:820.32','ICD9CM:820.8','ICD9CM:820.9 '):
            results_ccw["hip_pelv_frac"].append(1)
        else: results_ccw["hip_pelv_frac"].append(0)
    print("Completed Binary Recoding of: Hip / Pelvic Fracture")

# Hyperlipidemia
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:272.0','ICD9CM:272.1','ICD9CM:272.2','ICD9CM:272.3','ICD9CM:272.4'):
            results_ccw["hyperlipid"].append(1)
        else: results_ccw["hyperlipid"].append(0)
    print("Completed Binary Recoding of: Hyperlipidemia")

# Hypertension
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:362.11','ICD9CM:401.0','ICD9CM:401.1','ICD9CM:401.9','ICD9CM:402.00','ICD9CM:402.01','ICD9CM:402.10','ICD9CM:402.11','ICD9CM:402.90','ICD9CM:402.91','ICD9CM:403.00','ICD9CM:403.01','ICD9CM:403.10','ICD9CM:403.11','ICD9CM:403.90','ICD9CM:403.91','ICD9CM:404.00','ICD9CM:404.01','ICD9CM:404.02','ICD9CM:404.03','ICD9CM:404.10','ICD9CM:404.11','ICD9CM:404.12','ICD9CM:404.13','ICD9CM:404.90','ICD9CM:404.91','ICD9CM:404.92','ICD9CM:404.93','ICD9CM:405.01','ICD9CM:405.09','ICD9CM:405.11','ICD9CM:405.19','ICD9CM:405.91','ICD9CM:405.99','ICD9CM:437.2'):
            results_ccw["htn"].append(1)
        else: results_ccw["htn"].append(0)
    print("Completed Binary Recoding of: Hypertension")

# Ischemic Heart Disease
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:410.00','ICD9CM:410.01','ICD9CM:410.02','ICD9CM:410.10','ICD9CM:410.11','ICD9CM:410.12','ICD9CM:410.20','ICD9CM:410.21','ICD9CM:410.22','ICD9CM:410.30','ICD9CM:410.31','ICD9CM:410.32','ICD9CM:410.40','ICD9CM:410.41','ICD9CM:410.42','ICD9CM:410.50','ICD9CM:410.51','ICD9CM:410.52','ICD9CM:410.60','ICD9CM:410.61','ICD9CM:410.62','ICD9CM:410.70','ICD9CM:410.71','ICD9CM:410.72','ICD9CM:410.80','ICD9CM:410.81','ICD9CM:410.82','ICD9CM:410.90','ICD9CM:410.91','ICD9CM:410.92','ICD9CM:411.0','ICD9CM:411.1','ICD9CM:411.81','ICD9CM:411.89','ICD9CM:412','ICD9CM:413.0','ICD9CM:413.1','ICD9CM:413.9','ICD9CM:414.00','ICD9CM:414.01','ICD9CM:414.02','ICD9CM:414.03','ICD9CM:414.04','ICD9CM:414.05','ICD9CM:414.06','ICD9CM:414.07','ICD9CM:414.12','ICD9CM:414.2','ICD9CM:414.3','ICD9CM:414.4','ICD9CM:414.8','ICD9CM:414.9'):
            results_ccw["ischemic_hd"].append(1)
        else: results_ccw["ischemic_hd"].append(0)
    print("Completed Binary Recoding of: Ischemic Heart Disease")

# Osteoporosis
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:733.00','ICD9CM:733.01','ICD9CM:733.02','ICD9CM:733.03','ICD9CM:733.09'):
            results_ccw["osteoporosis"].append(1)
        else: results_ccw["osteoporosis"].append(0)
    print("Completed Binary Recoding of: Osteoporosis")

# Rheumatoid Arthritis / Osteoarthritis
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:714.0','ICD9CM:714.1','ICD9CM:714.2','ICD9CM:714.30','ICD9CM:714.31','ICD9CM:714.32','ICD9CM:714.33','ICD9CM:715.00','ICD9CM:715.04','ICD9CM:715.09','ICD9CM:715.10','ICD9CM:715.11','ICD9CM:715.12','ICD9CM:715.13','ICD9CM:715.14','ICD9CM:715.15','ICD9CM:715.16','ICD9CM:715.17','ICD9CM:715.18','ICD9CM:715.20','ICD9CM:715.21','ICD9CM:715.22','ICD9CM:715.23','ICD9CM:715.24','ICD9CM:715.25','ICD9CM:715.26','ICD9CM:715.27','ICD9CM:715.28','ICD9CM:715.30','ICD9CM:715.31','ICD9CM:715.32','ICD9CM:715.33','ICD9CM:715.34','ICD9CM:715.35','ICD9CM:715.36','ICD9CM:715.37','ICD9CM:715.38','ICD9CM:715.80','ICD9CM:715.89','ICD9CM:715.90','ICD9CM:715.91','ICD9CM:715.92','ICD9CM:715.93','ICD9CM:715.94','ICD9CM:715.95','ICD9CM:715.96','ICD9CM:715.97','ICD9CM:715.98','ICD9CM:720.0','ICD9CM:721.0','ICD9CM:721.1','ICD9CM:721.2','ICD9CM:721.3','ICD9CM:721.90','ICD9CM:721.91'):
            results_ccw["ra_oa"].append(1)
        else: results_ccw["ra_oa"].append(0)
    print("Completed Binary Recoding of: Rheumatoid Arthritis / Osteoarthritis")

# Stroke / Trans-Ischemic Attack
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:430','ICD9CM:431','ICD9CM:433.01','ICD9CM:433.11','ICD9CM:433.21','ICD9CM:433.31','ICD9CM:433.81','ICD9CM:433.91','ICD9CM:434.00','ICD9CM:434.01','ICD9CM:434.10','ICD9CM:434.11','ICD9CM:434.90','ICD9CM:434.91','ICD9CM:435.0','ICD9CM:435.1','ICD9CM:435.3','ICD9CM:435.8','ICD9CM:435.9','ICD9CM:436','ICD9CM:997.02'):
            results_ccw["stroke_tia"].append(1)
        else: results_ccw["stroke_tia"].append(0)
    print("Completed Binary Recoding of: Stroke / Trans-Ischemic Attack")

# Breast Cancer
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:174.0','ICD9CM:174.1','ICD9CM:174.2','ICD9CM:174.3','ICD9CM:174.4','ICD9CM:174.5','ICD9CM:174.6','ICD9CM:174.8','ICD9CM:174.9','ICD9CM:175.0','ICD9CM:175.9','ICD9CM:233.0'):
            results_ccw["breast_ca"].append(1)
        else: results_ccw["breast_ca"].append(0)
    print("Completed Binary Recoding of: Breast Cancer")

# Colorectal Cancer
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:153.0','ICD9CM:153.1','ICD9CM:153.2','ICD9CM:153.3','ICD9CM:153.4','ICD9CM:153.5','ICD9CM:153.6','ICD9CM:153.7','ICD9CM:153.8','ICD9CM:153.9,154.0,154.1','ICD9CM:230.3','ICD9CM:230.4'):
            results_ccw["colorectal_ca"].append(1)
        else: results_ccw["colorectal_ca"].append(0)
    print("Completed Binary Recoding of: Colorectal Cancer")

# Prostate Cancer
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:185','ICD9CM:233.4'):
            results_ccw["prostate_ca"].append(1)
        else: results_ccw["prostate_ca"].append(0)
    print("Completed Binary Recoding of: Prostate Cancer")

# Lung Cancer
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:162.2','ICD9CM:162.3','ICD9CM:162.4','ICD9CM:162.5','ICD9CM:162.8','ICD9CM:162.9','ICD9CM:231.2'):
            results_ccw["lung_ca"].append(1)
        else: results_ccw["lung_ca"].append(0)
    print("Completed Binary Recoding of: Lung Cancer")

# Endometrial Cancer
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:182.0','ICD9CM:233.2'):
            results_ccw["endometrial_ca"].append(1)
        else: results_ccw["endometrial_ca"].append(0)
    print("Completed Binary Recoding of: Endometrial Cancer")

# ==================================================== #
#
#    START OTHER CHRONIC OR POTENTIALLY DISABLING
#
# ==================================================== #

# ADHD Conduct Disorders and Hyperkinetic Syndrome
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:312.00', 'ICD9CM:312.01', 'ICD9CM:312.02', 'ICD9CM:312.03', 'ICD9CM:312.10', 'ICD9CM:312.11', 'ICD9CM:312.12', 'ICD9CM:312.13', 'ICD9CM:312.20', 'ICD9CM:312.21', 'ICD9CM:312.22', 'ICD9CM:312.23', 'ICD9CM:312.30', 'ICD9CM:312.31', 'ICD9CM:312.32', 'ICD9CM:312.33', 'ICD9CM:312.34', 'ICD9CM:312.35', 'ICD9CM:312.39', 'ICD9CM:312.4', 'ICD9CM:312.81', 'ICD9CM:312.82', 'ICD9CM:312.89', 'ICD9CM:312.9', 'ICD9CM:314.00', 'ICD9CM:314.01', 'ICD9CM:314.1', 'ICD9CM:314.2', 'ICD9CM:314.8', 'ICD9CM:314.9'):
            results_ccw["adhd"].append(1)
        else: results_ccw["adhd"].append(0)
    print("Completed Binary Recoding of: ADHD Conduct Disorders and Hyperkinetic Syndrome")

# Anxiety
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:293.84', 'ICD9CM:300.00', 'ICD9CM:300.01','ICD9CM:300.10', 'ICD9CM:300.20', 'ICD9CM:300.21', 'ICD9CM:300.22', 'ICD9CM:300.23', 'ICD9CM:300.29', 'ICD9CM:300.3', 'ICD9CM:300.5', 'ICD9CM:300.89', 'ICD9CM:300.9', 'ICD9CM:308.0', 'ICD9CM:308.1', 'ICD9CM:308.2', 'ICD9CM:308.3', 'ICD9CM:308.4', 'ICD9CM:308.9', 'ICD9CM:309.81', 'ICD9CM:313.0', 'ICD9CM:313.1', 'ICD9CM:313.21', 'ICD9CM:313.22', 'ICD9CM:313.3', 'ICD9CM:313.82', 'ICD9CM:313.83'):
            results_ccw["anxiety"].append(1)
        else: results_ccw["anxiety"].append(0)
    print("Completed Binary Recoding of: Anxiety")

# Autism Spectrum
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:299.0', 'ICD9CM:299.00', 'ICD9CM:299.01', 'ICD9CM:299.1', 'ICD9CM:299.11', 'ICD9CM:299.8', 'ICD9CM:299.80', 'ICD9CM:299.81', 'ICD9CM:299.9', 'ICD9CM:299.90', 'ICD9CM:299.91'):
            results_ccw["autism"].append(1)
        else: results_ccw["autism"].append(0)
    print("Completed Binary Recoding of: Autism Spectrum")

# Bipolar Disorder
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:296.00', 'ICD9CM:296.01', 'ICD9CM:296.02', 'ICD9CM:296.03', 'ICD9CM:296.04', 'ICD9CM:296.05', 'ICD9CM:296.06', 'ICD9CM:296.10', 'ICD9CM:296.11', 'ICD9CM:296.12', 'ICD9CM:296.13', 'ICD9CM:296.14', 'ICD9CM:296.15', 'ICD9CM:296.16', 'ICD9CM:296.40', 'ICD9CM:296.41', 'ICD9CM:296.42', 'ICD9CM:296.43', 'ICD9CM:296.44', 'ICD9CM:296.45', 'ICD9CM:296.46', 'ICD9CM:296.50', 'ICD9CM:296.51', 'ICD9CM:296.52', 'ICD9CM:296.53', 'ICD9CM:296.54', 'ICD9CM:296.55', 'ICD9CM:296.56', 'ICD9CM:296.60', 'ICD9CM:296.61', 'ICD9CM:296.62', 'ICD9CM:296.63', 'ICD9CM:296.64', 'ICD9CM:296.65', 'ICD9CM:296.66', 'ICD9CM:296.7', 'ICD9CM:296.80', 'ICD9CM:296.81', 'ICD9CM:296.82', 'ICD9CM:296.89', 'ICD9CM:296.90', 'ICD9CM:296.99'):
            results_ccw["bipolar"].append(1)
        else: results_ccw["bipolar"].append(0)
    print("Completed Binary Recoding of: Bipolar Disorder")

# Cerebral Palsy
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:333.71', 'ICD9CM:343', 'ICD9CM:343.0', 'ICD9CM:343.1', 'ICD9CM:343.2', 'ICD9CM:343.3', 'ICD9CM:343.4', 'ICD9CM:343.8', 'ICD9CM:343.9'):
            results_ccw["cerebral_p"].append(1)
        else: results_ccw["cerebral_p"].append(0)
    print("Completed Binary Recoding of: Cerebral Palsy")

# Cystic Fibrosis or Other Metabolic Developmental Disorders
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:243', 'ICD9CM:255.2', 'ICD9CM:269.2', 'ICD9CM:270.1', 'ICD9CM:270.2', 'ICD9CM:270.3', 'ICD9CM:270.4', 'ICD9CM:270.6', 'ICD9CM:270.7', 'ICD9CM:271.1', 'ICD9CM:277.0', 'ICD9CM:277.00', 'ICD9CM:277.01', 'ICD9CM:277.02', 'ICD9CM:277.03', 'ICD9CM:277.09', 'ICD9CM:277.6', 'ICD9CM:277.81', 'ICD9CM:277.85'):
            results_ccw["cystic_f"].append(1)
        else: results_ccw["cystic_f"].append(0)
    print("Completed Binary Recoding of: Cystic Fibrosis or Other Metabolic Developmental Disorders")

# Epilepsy
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:345', 'ICD9CM:345.0', 'ICD9CM:345.00', 'ICD9CM:345.01', 'ICD9CM:345.1', 'ICD9CM:345.10', 'ICD9CM:345.11', 'ICD9CM:345.2', 'ICD9CM:345.3', 'ICD9CM:345.4', 'ICD9CM:345.40', 'ICD9CM:345.41', 'ICD9CM:345.5', 'ICD9CM:345.50', 'ICD9CM:345.51', 'ICD9CM:345.6', 'ICD9CM:345.60', 'ICD9CM:345.61', 'ICD9CM:345.7', 'ICD9CM:345.70', 'ICD9CM:345.71', 'ICD9CM:345.8', 'ICD9CM:345.80', 'ICD9CM:345.81', 'ICD9CM:345.9', 'ICD9CM:345.90', 'ICD9CM:345.91'):
            results_ccw["epilepsy"].append(1)
        else: results_ccw["epilepsy"].append(0)
    print("Completed Binary Recoding of: Epilepsy")

# Fibromyalgia, Chronic Pain, and Fatigue
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:338.2', 'ICD9CM:338.21', 'ICD9CM:338.22', 'ICD9CM:338.23', 'ICD9CM:338.29', 'ICD9CM:338.3', 'ICD9CM:338.4', 'ICD9CM:780.7', 'ICD9CM:780.71', 'ICD9CM:729.1', 'ICD9CM:729.2'):
            results_ccw["chronic_pain"].append(1)
        else: results_ccw["chronic_pain"].append(0)
    print("Completed Binary Recoding of: Fibromyalgia, Chronic Pain, and Fatigue")

# HIV / AIDS
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:042', 'ICD9CM:042.0', 'ICD9CM:042.1', 'ICD9CM:042.2', 'ICD9CM:042.9', 'ICD9CM:043', 'ICD9CM:043.1', 'ICD9CM:043.2', 'ICD9CM:043.3', 'ICD9CM:043.9', 'ICD9CM:044', 'ICD9CM:044.0', 'ICD9CM:044.9', 'ICD9CM:079.53', 'ICD9CM:795.71'):
            results_ccw["hiv_aids"].append(1)
        else: results_ccw["hiv_aids"].append(0)
    print("Completed Binary Recoding of: HIV / AIDS")

# Intellectual Disabilities
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:317', 'ICD9CM:318', 'ICD9CM:318.0', 'ICD9CM:318.1', 'ICD9CM:318.2', 'ICD9CM:319', 'ICD9CM:758', 'ICD9CM:758.0', 'ICD9CM:758.1', 'ICD9CM:758.2', 'ICD9CM:758.3', 'ICD9CM:758.31', 'ICD9CM:758.32', 'ICD9CM:758.33', 'ICD9CM:758.39', 'ICD9CM:758.5', 'ICD9CM:759.7', 'ICD9CM:759.81', 'ICD9CM:759.83', 'ICD9CM:759.89', 'ICD9CM:760.71'):
            results_ccw["iq_disable"].append(1)
        else: results_ccw["iq_disable"].append(0)
    print("Completed Binary Recoding of: Intellectual Disabilities")

# Learning Disabilities
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:315', 'ICD9CM:315.01', 'ICD9CM:315.02', 'ICD9CM:315.09', 'ICD9CM:315.1', 'ICD9CM:315.2', 'ICD9CM:315.31', 'ICD9CM:315.32', 'ICD9CM:315.34', 'ICD9CM:315.35', 'ICD9CM:315.39', 'ICD9CM:315.4'):
            results_ccw["learn_disable"].append(1)
        else: results_ccw["learn_disable"].append(0)
    print("Completed Binary Recoding of: Learning Disabilities")

# Leukemias and Lymphomas
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:200.0', 'ICD9CM:200.00', 'ICD9CM:200.01', 'ICD9CM:200.02', 'ICD9CM:200.03', 'ICD9CM:200.04', 'ICD9CM:200.05', 'ICD9CM:200.06', 'ICD9CM:200.07', 'ICD9CM:200.08', 'ICD9CM:200.1', 'ICD9CM:200.10', 'ICD9CM:200.11', 'ICD9CM:200.12', 'ICD9CM:200.13', 'ICD9CM:200.14', 'ICD9CM:200.15', 'ICD9CM:200.16', 'ICD9CM:200.17', 'ICD9CM:200.18', 'ICD9CM:200.2', 'ICD9CM:200.20', 'ICD9CM:200.21', 'ICD9CM:200.22', 'ICD9CM:200.23', 'ICD9CM:200.24', 'ICD9CM:200.25', 'ICD9CM:200.26', 'ICD9CM:200.27', 'ICD9CM:200.28', 'ICD9CM:200.3', 'ICD9CM:200.30', 'ICD9CM:200.31', 'ICD9CM:200.32', 'ICD9CM:200.33', 'ICD9CM:200.34', 'ICD9CM:200.35', 'ICD9CM:200.36', 'ICD9CM:200.37', 'ICD9CM:200.38', 'ICD9CM:200.4', 'ICD9CM:200.40', 'ICD9CM:200.41', 'ICD9CM:200.42', 'ICD9CM:200.43', 'ICD9CM:200.44', 'ICD9CM:200.45', 'ICD9CM:200.46', 'ICD9CM:200.47', 'ICD9CM:200.48', 'ICD9CM:200.5', 'ICD9CM:200.50', 'ICD9CM:200.51', 'ICD9CM:200.52', 'ICD9CM:200.53', 'ICD9CM:200.54', 'ICD9CM:200.55', 'ICD9CM:200.56', 'ICD9CM:200.57', 'ICD9CM:200.58', 'ICD9CM:200.6', 'ICD9CM:200.60', 'ICD9CM:200.61', 'ICD9CM:200.62', 'ICD9CM:200.63', 'ICD9CM:200.64', 'ICD9CM:200.65', 'ICD9CM:200.66', 'ICD9CM:200.67', 'ICD9CM:200.68', 'ICD9CM:200.7', 'ICD9CM:200.70', 'ICD9CM:200.71', 'ICD9CM:200.72', 'ICD9CM:200.73', 'ICD9CM:200.74', 'ICD9CM:200.75', 'ICD9CM:200.76', 'ICD9CM:200.77', 'ICD9CM:200.78', 'ICD9CM:200.8', 'ICD9CM:200.80', 'ICD9CM:200.81', 'ICD9CM:200.82', 'ICD9CM:200.83', 'ICD9CM:200.84', 'ICD9CM:200.85', 'ICD9CM:200.86', 'ICD9CM:200.87', 'ICD9CM:200.88', 'ICD9CM:201.0', 'ICD9CM:201.00', 'ICD9CM:201.01', 'ICD9CM:201.02', 'ICD9CM:201.03', 'ICD9CM:201.04','ICD9CM:201.05', 'ICD9CM:201.06', 'ICD9CM:201.07', 'ICD9CM:201.08', 'ICD9CM:201.1', 'ICD9CM:201.10', 'ICD9CM:201.11', 'ICD9CM:201.12', 'ICD9CM:201.13', 'ICD9CM:201.14', 'ICD9CM:201.15', 'ICD9CM:201.16', 'ICD9CM:201.17', 'ICD9CM:201.18', 'ICD9CM:201.2', 'ICD9CM:201.20', 'ICD9CM:201.21', 'ICD9CM:201.22', 'ICD9CM:201.23', 'ICD9CM:201.24', 'ICD9CM:201.25', 'ICD9CM:201.26', 'ICD9CM:201.27', 'ICD9CM:201.28', 'ICD9CM:201.4', 'ICD9CM:201.40', 'ICD9CM:201.41', 'ICD9CM:201.42', 'ICD9CM:201.43', 'ICD9CM:201.44', 'ICD9CM:201.45', 'ICD9CM:201.46', 'ICD9CM:201.47', 'ICD9CM:201.48', 'ICD9CM:201.5', 'ICD9CM:201.50', 'ICD9CM:201.51', 'ICD9CM:201.52', 'ICD9CM:201.53', 'ICD9CM:201.54', 'ICD9CM:201.55', 'ICD9CM:201.56', 'ICD9CM:201.57', 'ICD9CM:201.58', 'ICD9CM:201.6', 'ICD9CM:201.60', 'ICD9CM:201.61', 'ICD9CM:201.62', 'ICD9CM:201.63', 'ICD9CM:201.64', 'ICD9CM:201.65', 'ICD9CM:201.66', 'ICD9CM:201.67', 'ICD9CM:201.68', 'ICD9CM:201.7', 'ICD9CM:201.70', 'ICD9CM:201.71', 'ICD9CM:201.72', 'ICD9CM:201.73', 'ICD9CM:201.74', 'ICD9CM:201.75', 'ICD9CM:201.76', 'ICD9CM:201.77', 'ICD9CM:201.78', 'ICD9CM:201.9', 'ICD9CM:201.90', 'ICD9CM:201.91', 'ICD9CM:201.92', 'ICD9CM:201.93', 'ICD9CM:201.94', 'ICD9CM:201.95', 'ICD9CM:201.96', 'ICD9CM:201.97', 'ICD9CM:201.98', 'ICD9CM:202.0', 'ICD9CM:202.00', 'ICD9CM:202.01', 'ICD9CM:202.02', 'ICD9CM:202.03', 'ICD9CM:202.04', 'ICD9CM:202.05', 'ICD9CM:202.06', 'ICD9CM:202.07', 'ICD9CM:202.08', 'ICD9CM:202.1', 'ICD9CM:202.10', 'ICD9CM:202.11', 'ICD9CM:202.12', 'ICD9CM:202.13', 'ICD9CM:202.14', 'ICD9CM:202.15', 'ICD9CM:202.16', 'ICD9CM:202.17', 'ICD9CM:202.18', 'ICD9CM:202.2', 'ICD9CM:202.20', 'ICD9CM:202.21', 'ICD9CM:202.22', 'ICD9CM:202.23', 'ICD9CM:202.24', 'ICD9CM:202.25', 'ICD9CM:202.26', 'ICD9CM:202.27', 'ICD9CM:202.28', 'ICD9CM:202.4', 'ICD9CM:202.40', 'ICD9CM:202.41', 'ICD9CM:202.42', 'ICD9CM:202.43', 'ICD9CM:202.44', 'ICD9CM:202.45', 'ICD9CM:202.46', 'ICD9CM:202.47', 'ICD9CM:202.48', 'ICD9CM:202.7', 'ICD9CM:202.70', 'ICD9CM:202.71', 'ICD9CM:202.72', 'ICD9CM:202.73', 'ICD9CM:202.74', 'ICD9CM:202.75', 'ICD9CM:202.76', 'ICD9CM:202.77', 'ICD9CM:202.78', 'ICD9CM:202.8', 'ICD9CM:202.80', 'ICD9CM:202.81', 'ICD9CM:202.82', 'ICD9CM:202.83', 'ICD9CM:202.84', 'ICD9CM:202.85', 'ICD9CM:202.86', 'ICD9CM:202.87', 'ICD9CM:202.88', 'ICD9CM:202.9', 'ICD9CM:202.90', 'ICD9CM:202.91', 'ICD9CM:202.92', 'ICD9CM:202.93', 'ICD9CM:202.94', 'ICD9CM:202.95', 'ICD9CM:202.96', 'ICD9CM:202.97', 'ICD9CM:202.98', 'ICD9CM:203.1', 'ICD9CM:203.10', 'ICD9CM:203.11', 'ICD9CM:203.12', 'ICD9CM:204.0', 'ICD9CM:204.00', 'ICD9CM:204.01', 'ICD9CM:204.02', 'ICD9CM:204.1', 'ICD9CM:204.10', 'ICD9CM:204.11', 'ICD9CM:204.12', 'ICD9CM:204.2', 'ICD9CM:204.20', 'ICD9CM:204.21', 'ICD9CM:204.22', 'ICD9CM:204.8', 'ICD9CM:204.80', 'ICD9CM:204.81', 'ICD9CM:204.82', 'ICD9CM:204.9', 'ICD9CM:204.90', 'ICD9CM:204.91', 'ICD9CM:204.92', 'ICD9CM:205.0', 'ICD9CM:205.01', 'ICD9CM:205.02', 'ICD9CM:205.1', 'ICD9CM:205.10', 'ICD9CM:205.11', 'ICD9CM:205.12', 'ICD9CM:205.2', 'ICD9CM:205.20', 'ICD9CM:205.21', 'ICD9CM:205.22', 'ICD9CM:205.3', 'ICD9CM:205.30', 'ICD9CM:205.31', 'ICD9CM:205.32', 'ICD9CM:205.8', 'ICD9CM:205.80', 'ICD9CM:205.81', 'ICD9CM:205.82', 'ICD9CM:205.9', 'ICD9CM:205.90', 'ICD9CM:205.91', 'ICD9CM:205.92', 'ICD9CM:206.0', 'ICD9CM:206.00', 'ICD9CM:206.01', 'ICD9CM:206.02', 'ICD9CM:206.1', 'ICD9CM:206.10', 'ICD9CM:206.11', 'ICD9CM:206.12', 'ICD9CM:206.2', 'ICD9CM:206.20', 'ICD9CM:206.21', 'ICD9CM:206.22', 'ICD9CM:206.2', 'ICD9CM:206.20', 'ICD9CM:206.21', 'ICD9CM:206.22', 'ICD9CM:206.8', 'ICD9CM:206.80', 'ICD9CM:206.81', 'ICD9CM:206.82', 'ICD9CM:206.9', 'ICD9CM:206.90', 'ICD9CM:206.91', 'ICD9CM:206.92', 'ICD9CM:207.0', 'ICD9CM:207.00', 'ICD9CM:207.01', 'ICD9CM:207.02', 'ICD9CM:207.1', 'ICD9CM:207.10', 'ICD9CM:207.11', 'ICD9CM:207.12', 'ICD9CM:207.2', 'ICD9CM:207.20', 'ICD9CM:207.21', 'ICD9CM:207.22', 'ICD9CM:207.8', 'ICD9CM:207.80', 'ICD9CM:207.81', 'ICD9CM:207.82', 'ICD9CM:208.0', 'ICD9CM:208.00', 'ICD9CM:208.01', 'ICD9CM:208.02', 'ICD9CM:208.1', 'ICD9CM:208.10', 'ICD9CM:208.11', 'ICD9CM:208.12', 'ICD9CM:208.2', 'ICD9CM:208.20', 'ICD9CM:208.21', 'ICD9CM:208.22', 'ICD9CM:208.8', 'ICD9CM:208.80', 'ICD9CM:208.81', 'ICD9CM:208.82', 'ICD9CM:208.9', 'ICD9CM:208.90', 'ICD9CM:208.91', 'ICD9CM:208.92'):
            results_ccw["leukemia"].append(1)
        else: results_ccw["leukemia"].append(0)
    print("Completed Binary Recoding of: Leukemias and Lymphomas")

# Liver Disease, Cirrhosis, and Other Liver Conditions
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:570', 'ICD9CM:571', 'ICD9CM:571.0', 'ICD9CM:571.1', 'ICD9CM:571.2', 'ICD9CM:571.3', 'ICD9CM:571.5', 'ICD9CM:571.6', 'ICD9CM:571.8', 'ICD9CM:571.9', 'ICD9CM:572', 'ICD9CM:572.0', 'ICD9CM:572.1', 'ICD9CM:572.2', 'ICD9CM:572.3', 'ICD9CM:572.4', 'ICD9CM:572.8', 'ICD9CM:573', 'ICD9CM:573.0', 'ICD9CM:573.4', 'ICD9CM:573.5', 'ICD9CM:573.8', 'ICD9CM:573.9', 'ICD9CM:576.1', 'ICD9CM:789.1'):
            results_ccw["liver"].append(1)
        else: results_ccw["liver"].append(0)
    print("Completed Binary Recoding of: Liver Disease, Cirrhosis, and Other Liver Conditions")

# Migraine and Headache
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:339', 'ICD9CM:339.0', 'ICD9CM:339.00', 'ICD9CM:339.01', 'ICD9CM:339.02', 'ICD9CM:339.03', 'ICD9CM:339.04', 'ICD9CM:339.05', 'ICD9CM:339.09', 'ICD9CM:339.1', 'ICD9CM:339.10', 'ICD9CM:339.11', 'ICD9CM:339.12', 'ICD9CM:339.2', 'ICD9CM:339.20', 'ICD9CM:339.21', 'ICD9CM:339.22', 'ICD9CM:339.3', 'ICD9CM:339.4', 'ICD9CM:339.41', 'ICD9CM:339.42', 'ICD9CM:339.43', 'ICD9CM:339.44', 'ICD9CM:339.8', 'ICD9CM:339.81', 'ICD9CM:339.82', 'ICD9CM:339.83', 'ICD9CM:339.84', 'ICD9CM:339.85', 'ICD9CM:339.89', 'ICD9CM:346', 'ICD9CM:346.0', 'ICD9CM:346.00', 'ICD9CM:346.01', 'ICD9CM:346.02', 'ICD9CM:346.03', 'ICD9CM:346.1', 'ICD9CM:346.10', 'ICD9CM:346.11', 'ICD9CM:346.12', 'ICD9CM:346.13', 'ICD9CM:346.2', 'ICD9CM:346.20', 'ICD9CM:346.21', 'ICD9CM:346.22', 'ICD9CM:346.23', 'ICD9CM:346.3', 'ICD9CM:346.30', 'ICD9CM:346.31', 'ICD9CM:346.32', 'ICD9CM:346.33', 'ICD9CM:346.4', 'ICD9CM:346.40', 'ICD9CM:346.41', 'ICD9CM:346.42', 'ICD9CM:346.43', 'ICD9CM:346.5', 'ICD9CM:346.50', 'ICD9CM:346.51', 'ICD9CM:346.52', 'ICD9CM:346.53', 'ICD9CM:346.6', 'ICD9CM:346.60', 'ICD9CM:346.61', 'ICD9CM:346.62', 'ICD9CM:346.63', 'ICD9CM:346.7', 'ICD9CM:346.70', 'ICD9CM:346.71', 'ICD9CM:346.72', 'ICD9CM:346.73', 'ICD9CM:346.8', 'ICD9CM:346.80', 'ICD9CM:346.81', 'ICD9CM:346.82', 'ICD9CM:346.83', 'ICD9CM:346.9', 'ICD9CM:346.90', 'ICD9CM:346.91', 'ICD9CM:346.92', 'ICD9CM:346.93'):
            results_ccw["migraine"].append(1)
        else: results_ccw["migraine"].append(0)
    print("Completed Binary Recoding of: Migraine and Headache")

# Mobility Impairment
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:334.1', 'ICD9CM:342.00', 'ICD9CM:342.01', 'ICD9CM:342.02', 'ICD9CM:342.10', 'ICD9CM:342.11', 'ICD9CM:342.12', 'ICD9CM:342.80', 'ICD9CM:342.81', 'ICD9CM:342.82', 'ICD9CM:342.90', 'ICD9CM:342.91', 'ICD9CM:342.92', 'ICD9CM:344', 'ICD9CM:344.0', 'ICD9CM:344.00', 'ICD9CM:344.01', 'ICD9CM:344.02', 'ICD9CM:344.03', 'ICD9CM:344.04', 'ICD9CM:344.09', 'ICD9CM:344.1', 'ICD9CM:344.2', 'ICD9CM:344.3', 'ICD9CM:344.30', 'ICD9CM:344.31', 'ICD9CM:344.32', 'ICD9CM:344.4', 'ICD9CM:344.40', 'ICD9CM:344.41', 'ICD9CM:344.42', 'ICD9CM:344.5', 'ICD9CM:344.6', 'ICD9CM:344.60', 'ICD9CM:344.61', 'ICD9CM:344.8', 'ICD9CM:344.81', 'ICD9CM:344.89', 'ICD9CM:344.9', 'ICD9CM:438.20', 'ICD9CM:438.21', 'ICD9CM:438.22', 'ICD9CM:438.30', 'ICD9CM:438.31', 'ICD9CM:438.32', 'ICD9CM:438.40', 'ICD9CM:438.41', 'ICD9CM:438.42', 'ICD9CM:438.50', 'ICD9CM:438.51', 'ICD9CM:438.52', 'ICD9CM:438.53'):
            results_ccw["mobility"].append(1)
        else: results_ccw["mobility"].append(0)
    print("Completed Binary Recoding of: Mobility Impairment")

# Multiple Sclerosis and Transverse Myelitis
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:340', 'ICD9CM:341', 'ICD9CM:341.0', 'ICD9CM:341.2', 'ICD9CM:341.20', 'ICD9CM:341.21', 'ICD9CM:341.22', 'ICD9CM:341.8', 'ICD9CM:341.9'):
            results_ccw["ms_tm"].append(1)
        else: results_ccw["ms_tm"].append(0)
    print("Completed Binary Recoding of: Multiple Sclerosis and Transverse Myelitis")

# Muscular Dystrophy
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:359', 'ICD9CM:359.0', 'ICD9CM:359.1'):
            results_ccw["muscular_dys"].append(1)
        else: results_ccw["muscular_dys"].append(0)
    print("Completed Binary Recoding of: Muscular Dystrophy")

# Obesity
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:278.0', 'ICD9CM:278.00', 'ICD9CM:278.01', 'ICD9CM:278.03'):
            results_ccw["obesity"].append(1)
        else: results_ccw["obesity"].append(0)
    print("Completed Binary Recoding of: Obesity")

# Other Developmental Delays
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:315.5', 'ICD9CM:315.8', 'ICD9CM:315.9'):
            results_ccw["develop_delay"].append(1)
        else: results_ccw["develop_delay"].append(0)
    print("Completed Binary Recoding of: Other Developmental Delays")

# Peripheral Vascular Disease
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:440', 'ICD9CM:440.1', 'ICD9CM:440.2', 'ICD9CM:440.20', 'ICD9CM:440.21', 'ICD9CM:440.22', 'ICD9CM:440.23', 'ICD9CM:440.29', 'ICD9CM:440.4', 'ICD9CM:443.8', 'ICD9CM:443.81', 'ICD9CM:443.82', 'ICD9CM:442.89', 'ICD9CM:443.9'):
            results_ccw["pvd"].append(1)
        else: results_ccw["pvd"].append(0)
    print("Completed Binary Recoding of: Peripheral Vascular Disease")

# Personality Disorders
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:301.0', 'ICD9CM:301.10', 'ICD9CM:301.11', 'ICD9CM:301.12', 'ICD9CM:301.13', 'ICD9CM:301.20', 'ICD9CM:301.21', 'ICD9CM:301.22', 'ICD9CM:301.3', 'ICD9CM:301.4', 'ICD9CM:301.50', 'ICD9CM:301.51', 'ICD9CM:301.59', 'ICD9CM:301.6', 'ICD9CM:301.7', 'ICD9CM:301.81', 'ICD9CM:301.82', 'ICD9CM:301.83', 'ICD9CM:301.84', 'ICD9CM:301.89', 'ICD9CM:301.9'):
            results_ccw["personality"].append(1)
        else: results_ccw["personality"].append(0)
    print("Completed Binary Recoding of: Personality Disorders")

# Post-Traumatic Stress Disorder
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in 'ICD9CM:309.81':
            results_ccw["ptsd"].append(1)
        else: results_ccw["ptsd"].append(0)
    print("Completed Binary Recoding of: Post-Traumatic Stress Disorder")

# Pressure and Chronic Ulcers
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:707.0', 'ICD9CM:707.00', 'ICD9CM:707.01', 'ICD9CM:707.02', 'ICD9CM:707.03', 'ICD9CM:707.04', 'ICD9CM:707.05', 'ICD9CM:707.06', 'ICD9CM:707.07', 'ICD9CM:707.09', 'ICD9CM:707.1', 'ICD9CM:707.10', 'ICD9CM:707.11', 'ICD9CM:707.12', 'ICD9CM:707.13', 'ICD9CM:707.14', 'ICD9CM:707.15', 'ICD9CM:707.19', 'ICD9CM:707.2', 'ICD9CM:707.22', 'ICD9CM:707.23', 'ICD9CM:707.24', 'ICD9CM:707.25', 'ICD9CM:707.8', 'ICD9CM:707.9'):
            results_ccw["ulcers"].append(1)
        else: results_ccw["ulcers"].append(0)
    print("Completed Binary Recoding of: Pressure and Chronic Ulcers")

# Schizophrenia and Other Psychotic Disorders
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:293.81', 'ICD9CM:293.82', 'ICD9CM:295.00', 'ICD9CM:295.01', 'ICD9CM:295.02', 'ICD9CM:295.03', 'ICD9CM:295.04', 'ICD9CM:295.05', 'ICD9CM:295.10', 'ICD9CM:295.11', 'ICD9CM:295.12', 'ICD9CM:295.13', 'ICD9CM:295.14', 'ICD9CM:295.15', 'ICD9CM:295.20', 'ICD9CM:295.21', 'ICD9CM:295.22', 'ICD9CM:295.23', 'ICD9CM:295.24', 'ICD9CM:295.25', 'ICD9CM:295.30', 'ICD9CM:295.31', 'ICD9CM:295.32', 'ICD9CM:295.33', 'ICD9CM:295.34', 'ICD9CM:295.35', 'ICD9CM:295.40', 'ICD9CM:295.41', 'ICD9CM:295.42', 'ICD9CM:295.43', 'ICD9CM:295.44', 'ICD9CM:295.45', 'ICD9CM:295.50', 'ICD9CM:295.51', 'ICD9CM:295.52', 'ICD9CM:295.53', 'ICD9CM:295.54', 'ICD9CM:295.55', 'ICD9CM:295.60', 'ICD9CM:295.61', 'ICD9CM:295.62', 'ICD9CM:295.63', 'ICD9CM:295.64', 'ICD9CM:295.65', 'ICD9CM:295.70', 'ICD9CM:295.71', 'ICD9CM:295.72', 'ICD9CM:295.73', 'ICD9CM:295.74', 'ICD9CM:295.75', 'ICD9CM:295.80', 'ICD9CM:295.81', 'ICD9CM:295.82', 'ICD9CM:295.83', 'ICD9CM:295.84', 'ICD9CM:295.85', 'ICD9CM:295.90', 'ICD9CM:295.91', 'ICD9CM:295.92', 'ICD9CM:295.93', 'ICD9CM:295.94', 'ICD9CM:295.95', 'ICD9CM:297.0', 'ICD9CM:297.1', 'ICD9CM:297.2', 'ICD9CM:297.3', 'ICD9CM:297.8', 'ICD9CM:297.9', 'ICD9CM:298.0', 'ICD9CM:298.1', 'ICD9CM:298.2', 'ICD9CM:298.3', 'ICD9CM:298.4', 'ICD9CM:298.8', 'ICD9CM:298.9'):
            results_ccw["schizo"].append(1)
        else: results_ccw["schizo"].append(0)
    print("Completed Binary Recoding of: Schizophrenia and Other Psychotic Disorders")

# Sensory – Blindness and Visual Impairment
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:369', 'ICD9CM:369.0', 'ICD9CM:369.00', 'ICD9CM:369.01', 'ICD9CM:369.02', 'ICD9CM:369.03', 'ICD9CM:369.04', 'ICD9CM:369.05', 'ICD9CM:369.06', 'ICD9CM:369.07', 'ICD9CM:369.08', 'ICD9CM:369.1', 'ICD9CM:369.10', 'ICD9CM:369.11', 'ICD9CM:369.12', 'ICD9CM:369.13', 'ICD9CM:369.14', 'ICD9CM:369.15', 'ICD9CM:369.16', 'ICD9CM:369.17', 'ICD9CM:369.18', 'ICD9CM:369.2', 'ICD9CM:369.20', 'ICD9CM:369.21', 'ICD9CM:369.22', 'ICD9CM:369.23', 'ICD9CM:369.24', 'ICD9CM:369.25', 'ICD9CM:369.3', 'ICD9CM:369.4'):
            results_ccw["visual_imp"].append(1)
        else: results_ccw["visual_imp"].append(0)
    print("Completed Binary Recoding of: Sensory – Blindness and Visual Impairment")

# Sensory – Deafness and Hearing Impairment
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:389', 'ICD9CM:389.1', 'ICD9CM:389.10', 'ICD9CM:389.11', 'ICD9CM:389.12', 'ICD9CM:389.13', 'ICD9CM:389.14', 'ICD9CM:389.15', 'ICD9CM:389.16', 'ICD9CM:389.17', 'ICD9CM:389.18', 'ICD9CM:389.2', 'ICD9CM:389.20', 'ICD9CM:389.21', 'ICD9CM:389.22', 'ICD9CM:389.7', 'ICD9CM:389.8', 'ICD9CM:389.9'):
            results_ccw["hearing_imp"].append(1)
        else: results_ccw["hearing_imp"].append(0)
    print("Completed Binary Recoding of: Sensory – Deafness and Hearing Impairment")

# Spina Bifida and Other Congenital Anomalies of the NS
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:740.0', 'ICD9CM:740.1', 'ICD9CM:740.2', 'ICD9CM:741', 'ICD9CM:741.0', 'ICD9CM:741.00. 741.01', 'ICD9CM:741.02', 'ICD9CM:741.03', 'ICD9CM:741.9', 'ICD9CM:741.90', 'ICD9CM:741.91. 741.92', 'ICD9CM:741.93', 'ICD9CM:742.0', 'ICD9CM:742.1', 'ICD9CM:742.2', 'ICD9CM:742.3', 'ICD9CM:742.4', 'ICD9CM:742.5', 'ICD9CM:742.51', 'ICD9CM:742.53', 'ICD9CM:742.59', 'ICD9CM:742.8', 'ICD9CM:742.9'):
            results_ccw["spina_bifida"].append(1)
        else: results_ccw["spina_bifida"].append(0)
    print("Completed Binary Recoding of: Spina Bifida and Other Congenital Anomalies of the NS")

# Spinal Cord Injury
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:349.39', 'ICD9CM:806.00. 806.01', 'ICD9CM:806.02', 'ICD9CM:806.03', 'ICD9CM:806.04', 'ICD9CM:806.05', 'ICD9CM:806.06', 'ICD9CM:806.07', 'ICD9CM:806.08', 'ICD9CM:806.09', 'ICD9CM:806.10', 'ICD9CM:806.11', 'ICD9CM:806.12', 'ICD9CM:806.13', 'ICD9CM:806.14', 'ICD9CM:806.15', 'ICD9CM:806.16', 'ICD9CM:806.17', 'ICD9CM:806.18', 'ICD9CM:806.19', 'ICD9CM:806.20', 'ICD9CM:806.21', 'ICD9CM:806.22', 'ICD9CM:806.23', 'ICD9CM:806.24', 'ICD9CM:806.25', 'ICD9CM:806.26', 'ICD9CM:806.27', 'ICD9CM:806.28', 'ICD9CM:806.29', 'ICD9CM:806.30', 'ICD9CM:806.31', 'ICD9CM:806.32', 'ICD9CM:806.33', 'ICD9CM:806.34', 'ICD9CM:806.35', 'ICD9CM:806.36', 'ICD9CM:806.37', 'ICD9CM:806.38', 'ICD9CM:806.39', 'ICD9CM:806.4', 'ICD9CM:806.5', 'ICD9CM:806.60', 'ICD9CM:806.61', 'ICD9CM:806.62', 'ICD9CM:806.69', 'ICD9CM:806.70', 'ICD9CM:806.71', 'ICD9CM:806.72', 'ICD9CM:806.79', 'ICD9CM:806.8', 'ICD9CM:806.9', 'ICD9CM:907.2', 'ICD9CM:952.00', 'ICD9CM:952.01', 'ICD9CM:952.02', 'ICD9CM:952.03', 'ICD9CM:952.04', 'ICD9CM:952.05', 'ICD9CM:952.06', 'ICD9CM:952.07', 'ICD9CM:952.08', 'ICD9CM:952.09', 'ICD9CM:952.10', 'ICD9CM:952.11', 'ICD9CM:952.12', 'ICD9CM:952.13', 'ICD9CM:952.14', 'ICD9CM:952,15', 'ICD9CM:952.16', 'ICD9CM:952.17', 'ICD9CM:952.18', 'ICD9CM:952.19', 'ICD9CM:952.2', 'ICD9CM:952.3', 'ICD9CM:952.4', 'ICD9CM:952.8', 'ICD9CM:952.9'):
            results_ccw["spinal_cord"].append(1)
        else: results_ccw["spinal_cord"].append(0)
    print("Completed Binary Recoding of: Spinal Cord Injury")

# Tobacco Use
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:305.1', 'ICD9CM:649.00', 'ICD9CM:649.01', 'ICD9CM:649.02', 'ICD9CM:649.03', 'ICD9CM:649.04', 'ICD9CM:989.84'):
            results_ccw["tobacco"].append(1)
        else: results_ccw["tobacco"].append(0)
    print("Completed Binary Recoding of: Tobacco Use")

# Traumatic Brain Injury
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:310', 'ICD9CM:310.0', 'ICD9CM:310.1', 'ICD9CM:310.2', 'ICD9CM:310.8', 'ICD9CM:310.81', 'ICD9CM:310.89', 'ICD9CM:907', 'ICD9CM:907.0', 'ICD9CM:907.1'):
            results_ccw["trauma_brain"].append(1)
        else: results_ccw["trauma_brain"].append(0)
    print("Completed Binary Recoding of: Traumatic Brain Injury")

# Viral Hepatitis
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:070.0', 'ICD9CM:070.1', 'ICD9CM:070.2', 'ICD9CM:070.20', 'ICD9CM:070.21', 'ICD9CM:070.22', 'ICD9CM:070.23', 'ICD9CM:070.3,070.30', 'ICD9CM:070.31', 'ICD9CM:070.32', 'ICD9CM:070.33', 'ICD9CM:070.4', 'ICD9CM:070.41', 'ICD9CM:070.42', 'ICD9CM:070.43', 'ICD9CM:070.49', 'ICD9CM:070.5', 'ICD9CM:070.51', 'ICD9CM:070.52', 'ICD9CM:070.53', 'ICD9CM:070.54', 'ICD9CM:070.59', 'ICD9CM:070.6', 'ICD9CM:070.7', 'ICD9CM:070.70', 'ICD9CM:070.71', 'ICD9CM:070.9'):
            results_ccw["hepatitis"].append(1)
        else: results_ccw["hepatitis"].append(0)
    print("Completed Binary Recoding of: Viral Hepatitis")


# ============================================= #
#
#      START ASSAULT, HOMICIDE, SUICIDE
#
# ============================================= #

# Homicide and Injury Purposely Inflicted By Others
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:E963','ICD9CM:E967.7','ICD9CM:E968.2','ICD9CM:E967.2','ICD9CM:E965.8','ICD9CM:E968.6','ICD9CM:E962.1','ICD9CM:E965.4','ICD9CM:E967.4','ICD9CM:E960.1','ICD9CM:E968.8','ICD9CM:E968.3','ICD9CM:E967.8','ICD9CM:E968.1','ICD9CM:E968.9','ICD9CM:E965.0','ICD9CM:E965.1','ICD9CM:E967.3','ICD9CM:E967.6','ICD9CM:E960.0','ICD9CM:E969','ICD9CM:E960','ICD9CM:E962.9','ICD9CM:E967.5','ICD9CM:E961','ICD9CM:E968.7','ICD9CM:E962.0','ICD9CM:E967.1','ICD9CM:E967.9','ICD9CM:E968.0','ICD9CM:E968.5','ICD9CM:E965.7','ICD9CM:E962.2','ICD9CM:E966','ICD9CM:E967.0'):
            results_ccw["injury_frm_others"].append(1)
        else: results_ccw["injury_frm_others"].append(0)
    print("Completed Binary Recoding of: Homicide and Injury Purposely Inflicted By Others")


# Suicide Attempt / Ideation
    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in ('ICD9CM:E958.0','ICD9CM:E950.3','ICD9CM:E955.7','ICD9CM:E955.6','ICD9CM:E958.7','ICD9CM:E958.8','ICD9CM:E950.8','ICD9CM:E958.1','ICD9CM:E958.3','ICD9CM:E955.0','ICD9CM:E950.9','ICD9CM:E959','ICD9CM:E958.9','ICD9CM:E954','ICD9CM:E953.9','ICD9CM:E950.4','ICD9CM:E957.0','ICD9CM:E953.1','ICD9CM:E952.1','ICD9CM:E950.7','ICD9CM:E950.6','ICD9CM:E950.2','ICD9CM:E955.9','ICD9CM:E955.5','ICD9CM:E957.2','ICD9CM:E950.5','ICD9CM:E957.1','ICD9CM:E956','ICD9CM:E950.1','ICD9CM:E955.4','ICD9CM:E951.8','ICD9CM:E953.0','ICD9CM:E951.0','ICD9CM:E952.8','ICD9CM:E950.0','ICD9CM:E953.8','ICD9CM:E957.9','ICD9CM:V62.84'):
            results_ccw["suicide"].append(1)
        else: results_ccw["suicide"].append(0)
    print("Completed Binary Recoding of: Suicide Attempt / Ideation")

# ============================================= #
#
#      START PSYCH HOSPITALIZATION
#
# ============================================= #

    for index, _ in enumerate(cdrn_dx_hosp['condition_source_value']):
        if _ in '9201':
            results_ccw["psych_hosp"].append(1)
        else: results_ccw["psych_hosp"].append(0)
    print("Completed Binary Recoding of: Psychiatric Hospitalizations")


    pd.DataFrame(results_ccw).to_csv(output_filepath, encoding='utf-8')



dx_convert(cdrn_dx_hosp)