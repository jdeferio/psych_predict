import pandas as pd

# Psych Hospitalizations
cdrn = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ccw_modified_nta.csv', encoding='utf-8')

cdrn_util2014_grouped = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_util2014_psych_grouped.csv', encoding='utf-8')

ed2012 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ED_visit_2012.csv', encoding='utf-8', names=["ed_2012","person_id"])
ed2013 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_ED_visit_2013.csv', encoding='utf-8', names=["ed_2013","person_id"])

inpt_2012 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_inpt_visit_2012.csv', encoding='utf-8', names=["inpt_2012","person_id"])
inpt_2013 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_inpt_visit_2013.csv', encoding='utf-8', names=["inpt_2013","person_id"])

outpt_2012 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_outpt_ct2012.csv', encoding='utf-8', names=["outpt_2012","person_id"])
outpt_2013 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_outpt_ct2013.csv', encoding='utf-8', names=["outpt_2013","person_id"])

amb_2012 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_amb_visit_2012.csv', encoding='utf-8', names=["amb_2012","person_id"])
amb_2013 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_amb_visit_2013.csv', encoding='utf-8', names=["amb_2013","person_id"])

other_2012 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_other_visit_2012.csv', encoding='utf-8', names=["other_2012","person_id"])
other_2013 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_other_visit_2013.csv', encoding='utf-8', names=["other_2013","person_id"])


cdrn1 = pd.merge(cdrn,ed2012, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,ed2013, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,inpt_2012, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,inpt_2013, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,outpt_2012, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,outpt_2013, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,amb_2012, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,amb_2013, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,other_2012, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,other_2013, how='left',on='person_id').fillna(0)
cdrn1 = pd.merge(cdrn1,cdrn_util2014_grouped, how='left', on='person_id').fillna(0)

print("cdrn1 length: ", len(cdrn1))

# Psych Hospitalizations
pd.DataFrame(cdrn1).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_clin_util_all_nta.csv', encoding='utf-8')



