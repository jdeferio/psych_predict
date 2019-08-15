import io
import pandas as pd
import functools
from datetime import datetime

def main():

    outputfile_1 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/psych_hosp_time_to_event.csv'
    outputfile_2 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/prevent_hosp_time_to_event.csv'
    outputfile_3 = '/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/allcause_hosp_time_to_event.csv'

    visits1213 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_visits_1213.csv', encoding='utf-8', names=['visit_occurrence_id', 'person_id', 'visit_start_date'])
    visits14 = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_visits_2014_.csv', encoding='utf-8', names=['visit_occurrence_id', 'person_id', 'visit_start_date'])

    psych = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_psych_hosp_2014_1st_.csv', encoding='utf-8')
    prevent = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_prevent_hosp_2014_1st_.csv', encoding='utf-8')
    allcause = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/cdrn_all_hosp_2014_1st_.csv', encoding='utf-8')

    no_psychid = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/no_psych_hosp.csv',encoding='utf-8')
    no_preventid = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/no_prevent_hosp.csv',encoding='utf-8')
    no_allcauseid = pd.read_csv('/Users/jdeferio/PycharmProjects/CDRN_Individual/venv/no_allcause_hosp.csv',encoding='utf-8')

    features = ['person_id', 'time_to_event']

    def days_between(d1, d2):
        d1 = datetime.strptime(d1, '%Y-%m-%d')
        d2 = datetime.strptime(d2, '%Y-%m-%d')
        return abs((d2 - d1).days)

    # Create a 'last visit' of 2014 set for non-hospitalized patients
    nopsych_merge14 = pd.merge(visits14, no_psychid, on='person_id', how='inner')
    noprevent_merge14 = pd.merge(visits14, no_preventid, on='person_id', how='inner')
    noallcause_merge14 = pd.merge(visits14, no_allcauseid, on='person_id', how='inner')

    nopsych_merge14 = nopsych_merge14.sort_values(by=['person_id', 'visit_start_date'], ascending=False)
    noprevent_merge14 = noprevent_merge14.sort_values(by=['person_id', 'visit_start_date'], ascending=False)
    noallcause_merge14 = noallcause_merge14.sort_values(by=['person_id', 'visit_start_date'], ascending=False)

    nopsych_merge14 = nopsych_merge14.drop_duplicates(subset='person_id', keep='first')
    noprevent_merge14 = noprevent_merge14.drop_duplicates(subset='person_id', keep='first')
    noallcause_merge14 = noallcause_merge14.drop_duplicates(subset='person_id', keep='first')

    # Merge Visits with First Hospitalization
    psych_merge = pd.merge(visits1213, psych, on='person_id', how='inner')
    prevent_merge = pd.merge(visits1213, prevent, on='person_id', how='inner')
    allcause_merge = pd.merge(visits1213, allcause, on='person_id', how='inner')

    # Merge Visits with Non-hospitalized Patients
    nopsych_merge = pd.merge(visits1213, nopsych_merge14, on='person_id', how='inner')
    noprevent_merge = pd.merge(visits1213, noprevent_merge14, on='person_id', how='inner')
    noallcause_merge = pd.merge(visits1213, noallcause_merge14, on='person_id', how='inner')

    # Create 'time_to_event' for hospitalizations
    psych_merge['time_to_event'] = psych_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)
    prevent_merge['time_to_event'] = prevent_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)
    allcause_merge['time_to_event'] = allcause_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)

    nopsych_merge['time_to_event'] = nopsych_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)
    noprevent_merge['time_to_event'] = noprevent_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)
    noallcause_merge['time_to_event'] = noallcause_merge.apply(lambda row: days_between(str(row.visit_start_date_x), str(row.visit_start_date_y)), axis=1)

    # Sort by 'person_id' and  'time_to_event'
    psych_merge = psych_merge.sort_values(by=['person_id', 'time_to_event'], ascending=False)
    prevent_merge = prevent_merge.sort_values(by=['person_id', 'time_to_event'],  ascending=False)
    allcause_merge = allcause_merge.sort_values(by=['person_id', 'time_to_event'],  ascending=False)

    nopsych_merge = nopsych_merge.sort_values(by=['person_id', 'time_to_event'], ascending=False)
    noprevent_merge = noprevent_merge.sort_values(by=['person_id', 'time_to_event'], ascending=False)
    noallcause_merge = noallcause_merge.sort_values(by=['person_id', 'time_to_event'], ascending=False)

    # Remove Duplicates
    psych_merge = psych_merge.drop_duplicates(subset='person_id', keep='first')
    prevent_merge = prevent_merge.drop_duplicates(subset='person_id', keep='first')
    allcause_merge = allcause_merge.drop_duplicates(subset='person_id', keep='first')

    nopsych_merge = nopsych_merge.drop_duplicates(subset='person_id', keep='first')
    noprevent_merge = noprevent_merge.drop_duplicates(subset='person_id', keep='first')
    noallcause_merge = noallcause_merge.drop_duplicates(subset='person_id', keep='first')


    # Drop Unnecessary Features
    psych_merge = psych_merge.loc[:, features]
    prevent_merge = prevent_merge.loc[:, features]
    allcause_merge = allcause_merge.loc[:, features]

    nopsych_merge = nopsych_merge.loc[:, features]
    noprevent_merge = noprevent_merge.loc[:, features]
    noallcause_merge = noallcause_merge.loc[:, features]

    # Append The Two Files
    psych_merge = psych_merge.append(nopsych_merge, sort=False)
    prevent_merge = prevent_merge.append(noprevent_merge, sort=False)
    allcause_merge = allcause_merge.append(noallcause_merge, sort=False)

    # Save Files
    pd.DataFrame(psych_merge).to_csv(outputfile_1, encoding='utf-8', index=False)
    pd.DataFrame(prevent_merge).to_csv(outputfile_2, encoding='utf-8', index=False)
    pd.DataFrame(allcause_merge).to_csv(outputfile_3, encoding='utf-8', index=False)

if __name__=='__main__':
    main()



