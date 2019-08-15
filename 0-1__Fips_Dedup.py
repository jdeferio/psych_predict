import pandas as pd
import datetime as dt
import requests
import logging
import time
# from dateutil.parser import parse

logger = logging.getLogger("root")
logger.setLevel(logging.DEBUG)
# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

cdrn_loc = pd.read_csv('/Users/jdeferio/Documents/Work/Cornell/Social Behavior R01/Projects/CDRN/Zipcode/cdrn_fips_nta_nyc.csv', encoding='utf-8')
print("cdrn_loc length: ",len(cdrn_loc))
print(cdrn_loc.nunique())

# Drops Column ['Unnamed']
cdrn_loc = cdrn_loc.drop(cdrn_loc.columns[[0]],axis=1)


# Create column ['dup'] which identifies duplicate ['person_id'] and ['fips_census_code'] combos
cdrn_loc['dup_id_fips'] = cdrn_loc[['person_id','fips_census_code']].duplicated(keep=False)
cdrn_loc['zip_date'] = cdrn_loc['zip_date'].fillna('12/31/18')

# Converts string to a date
zip_date_2 = []
for _ in cdrn_loc['zip_date']:
    zip_date_2.append(dt.datetime.strptime(_,"%m/%d/%y"))
print("Finished zip_date_2")

# Merge new dates with df
person_dt = pd.DataFrame({"zip_date_2":zip_date_2})
print("person_dt length: ",len(person_dt))
print("cdrn_loc length: ", len(cdrn_loc))
cdrn_loc = pd.merge(cdrn_loc,person_dt, left_index=True, right_index=True)

# Sort by 'person_id' and  'zip_date_2'
cdrn_loc = cdrn_loc.sort_values(by=['person_id','zip_date_2'])

# Reset the Index
cdrn_loc = cdrn_loc.reset_index(drop=True)

# Identifies the number of addresses per patient
cdrn_loc['dup_id_count'] = cdrn_loc.groupby('person_id').zip_date_2.apply(pd.Series.rank)

# pat_id = []
# for _ in cdrn_loc['person_id']:
#    pat_id.append(_)
#    if len(pat_id) % 50000 == 0:
#        logger.info("Completed {} of {} records".format(len(pat_id), len(cdrn_loc)))
# print("Finished pat_id")

# Identifies all occurrences after first of duplicate 'person_id' and 'fips_census_code'
delete_dup2 = []
for index, row in cdrn_loc.iterrows():
    if row.dup_id_fips == True and row.dup_id_count > 1:
        delete_dup2.append(1)
    else: delete_dup2.append(0)
    if len(delete_dup2) % 50000 == 0:
        logger.info("Completed {} of {} records".format(len(delete_dup2), len(cdrn_loc)))
print("Finished delete_dup2")

# Identifies ADDRESSES that were listed before the end of 2014
date_bf_end2014 = []
for index, row in cdrn_loc.iterrows():
    if row.zip_date_2 <= dt.datetime(2014,12,31,00,00,00):
        date_bf_end2014.append(1)
    else: date_bf_end2014.append(0)
    if len(date_bf_end2014) % 50000 == 0:
        logger.info("Completed {} of {} records".format(len(date_bf_end2014), len(cdrn_loc)))
print("Finished date_bf_end2014")

person_dups = pd.DataFrame({"delete_dup_2":delete_dup2,"date_bf_end2014":date_bf_end2014})

print("person_dups length: ", len(person_dups))
print("cdrn_loc length: ", len(cdrn_loc))
cdrn_loc = pd.merge(cdrn_loc, person_dups, left_index=True, right_index=True)


person_dt_bf2014 = []
for index, row in cdrn_loc.iterrows():
    if row.date_bf_end2014 == 1:
        person_dt_bf2014.append(row.person_id)
    if len(person_dt_bf2014) % 10000 == 0:
        logger.info("Completed {} records".format(len(person_dt_bf2014)))
print("Finished person_dt_bf2014, length: ",len(person_dt_bf2014))

delete_dict = {"person2014":[], "date2015":[]}

# for _ in cdrn_loc['person_id']:
#    delete_dict['person_id'].append(_)
#    if len(delete_dict['person_id']) % 50000 == 0:
#        logger.info("Completed {} of {} records".format(len(delete_dict['person_id']), len(cdrn_loc)))
# print("Finished delete_dict.person_id")

# Identifies PEOPLE with dates before end of 2014
for _ in cdrn_loc['person_id']:
    if _ in set(person_dt_bf2014):
        delete_dict['person2014'].append(1)
    else: delete_dict['person2014'].append(0)
    if len(delete_dict['person2014']) % 50000 == 0:
        logger.info("Completed {} of {} records".format(len(delete_dict['person2014']), len(cdrn_loc)))
print("Finished delete_dict.person2014")

# Identifies ADDRESSES that were listed AFTER 2014
for _ in cdrn_loc['zip_date_2']:
    if _ > dt.datetime(2014,12,31,00,00,00):
        delete_dict['date2015'].append(1)
    else: delete_dict['date2015'].append(0)
    if len(delete_dict['date2015']) % 50000 == 0:
        logger.info("Completed {} of {} records".format(len(delete_dict['date2015']), len(cdrn_loc)))
print("Finished delete_dict.date2015")

print("delete_dict: 'person2014', 'date2015' length: ", len(delete_dict['person2014']), len(delete_dict['date2015']))
print("cdrn_loc length: ", len(cdrn_loc))

delete_dict2 = pd.DataFrame({"person2014":delete_dict['person2014'],"date2015":delete_dict['date2015']})
cdrn_loc = pd.merge(cdrn_loc, delete_dict2, left_index=True, right_index=True)

# pat_id = []
# for _ in cdrn_loc['person_id']:
#     pat_id.append(_)

# Identifies cases where:
#   PERSON has a date BEFORE END 2014
#   ADDRESS DATE is AFTER 2014
#   Is NOT the person's 1ST ADDRESS
delete_dup_after_end2014 = []
for index, row in cdrn_loc.iterrows():
    if row.person2014 == 1 and row.date2015 == 1 and row.dup_id_count>1:
        delete_dup_after_end2014.append(1)
    else: delete_dup_after_end2014.append(0)
    if len(delete_dup_after_end2014) % 10000 == 0:
        logger.info("Completed {} of {} records".format(len(delete_dup_after_end2014), len(cdrn_loc)))

person_delete = pd.DataFrame({"delete_dup_after_end2014":delete_dup_after_end2014})

print("person_delete length: ", len(person_delete))
print("cdrn_loc length: ", len(cdrn_loc))

cdrn_loc = pd.merge(cdrn_loc,person_delete, left_index=True, right_index=True)

pd.DataFrame(cdrn_loc).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_loc_all.csv',encoding='utf-8')

cdrn_loc_dedup = cdrn_loc[cdrn_loc['delete_dup_2'] != 1]
print("cdrn_loc_dedup length: ", len(cdrn_loc_dedup)," & nunique patients: ",cdrn_loc_dedup.person_id.nunique())
cdrn_loc_dedup = cdrn_loc_dedup[cdrn_loc_dedup['delete_dup_after_end2014'] != 1]
print("cdrn_loc_dedup length: ", len(cdrn_loc_dedup)," & nunique patients: ",cdrn_loc_dedup.person_id.nunique())

cdrn_loc_dedup = cdrn_loc_dedup.drop_duplicates(['person_id'], keep='first')
print("cdrn_loc_dedup length: ", len(cdrn_loc_dedup)," & nunique patients: ",cdrn_loc_dedup.person_id.nunique())

pd.DataFrame(cdrn_loc_dedup).to_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_dedup_loc_all.csv',encoding='utf-8')