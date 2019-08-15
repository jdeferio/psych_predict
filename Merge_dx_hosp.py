import pandas as pd

output_filepath = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_dx_hosp.csv'

cdrn_dx = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_individual_dx.csv',encoding='utf-8',names=["person_id","condition_start_date","condition_source_value"])

cdrn_hosp = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014.csv', encoding='utf-8', names=["person_id", "condition_start_date", "condition_source_value"])
cdrn_hosp["condition_source_value"] = cdrn_hosp["condition_source_value"].astype(str)

cdrn_dx_hosp = cdrn_dx.append(cdrn_hosp, sort=False)


pd.DataFrame(cdrn_dx_hosp).to_csv(output_filepath, encoding='utf-8')
print(cdrn_dx_hosp.head())
print(cdrn_dx_hosp.info())
print(cdrn_dx_hosp.describe())
print(len(cdrn_dx_hosp['person_id']))
print(len(cdrn_dx_hosp['condition_start_date']))
print(len(cdrn_dx_hosp['condition_source_value']))