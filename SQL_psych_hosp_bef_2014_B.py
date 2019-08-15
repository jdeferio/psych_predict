import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_psych_hosp_bef_2014_B.csv'

# Selects all patients in the cohort and reports their gender, birth date, and age at '2014-01-01'
        sql = "select distinct v.person_id from staging.condition_occurrence as co join staging.visit_occurrence as v on co.visit_occurrence_id = v.visit_occurrence_id where (v.visit_concept_id = 9201) and ((co.condition_source_value like 'ICD9CM:295%') or (co.condition_source_value like 'ICD9CM:296%') or (co.condition_source_value like 'ICD9CM:297%') or (co.condition_source_value like 'ICD9CM:298%') or (co.condition_source_value like 'ICD9CM:300%') or (co.condition_source_value like 'ICD9CM:301%') or (co.condition_source_value like 'ICD9CM:302%') or (co.condition_source_value like 'ICD9CM:306%') or (co.condition_source_value like 'ICD9CM:307%') or (co.condition_source_value like 'ICD9CM:308%') or (co.condition_source_value like 'ICD9CM:309%') or (co.condition_source_value like 'ICD9CM:311%') or (co.condition_source_value like 'ICD9CM:312%') or (co.condition_source_value like 'ICD9CM:313%') or (co.condition_source_value like 'ICD9CM:314%') or (co.condition_source_value like 'ICD10CM:F32%') or (co.condition_source_value like 'ICD10CM:F33%') or (co.condition_source_value like 'ICD10CM:F34.1%')) and co.condition_type_concept_id in(44786627, 44786629) and (v.visit_start_date < '2014-01-01') and v.person_id in(select distinct person_id from staging.visit_occurrence where (visit_start_date between '2012-01-01' and '2012-12-31') and person_id in(select distinct person_id from staging.visit_occurrence where (visit_start_date between '2013-01-01' and '2013-12-31') and person_id in(select distinct person_id from staging.visit_occurrence where (visit_start_date between '2014-01-01' and '2014-12-31') group by person_id having count(*) >=1) group by person_id having count(*) >=1 ) group by person_id having count(*) >=1) union select distinct v.person_id from mdd_control.condition_occurrence as co join mdd_control.visit_occurrence as v on co.visit_occurrence_id = v.visit_occurrence_id where (v.visit_concept_id = 9201) and ((co.condition_source_value like 'ICD9CM:295%') or (co.condition_source_value like 'ICD9CM:296%') or (co.condition_source_value like 'ICD9CM:297%') or (co.condition_source_value like 'ICD9CM:298%') or (co.condition_source_value like 'ICD9CM:300%') or (co.condition_source_value like 'ICD9CM:301%') or (co.condition_source_value like 'ICD9CM:302%') or (co.condition_source_value like 'ICD9CM:306%') or (co.condition_source_value like 'ICD9CM:307%') or (co.condition_source_value like 'ICD9CM:308%') or (co.condition_source_value like 'ICD9CM:309%') or (co.condition_source_value like 'ICD9CM:311%') or (co.condition_source_value like 'ICD9CM:312%') or (co.condition_source_value like 'ICD9CM:313%') or (co.condition_source_value like 'ICD9CM:314%') or (co.condition_source_value like 'ICD10CM:F32%') or (co.condition_source_value like 'ICD10CM:F33%') or (co.condition_source_value like 'ICD10CM:F34.1%')) and co.condition_type_concept_id in(44786627, 44786629) and (v.visit_start_date < '2014-01-01') and v.person_id in(select distinct person_id from mdd_control.visit_occurrence where (visit_start_date between '2012-01-01' and '2012-12-31') and person_id in(select distinct person_id from mdd_control.visit_occurrence where (visit_start_date between '2013-01-01' and '2013-12-31') and person_id in(select distinct person_id from mdd_control.visit_occurrence where (visit_start_date between '2014-01-01' and '2014-12-31') group by person_id having count(*) >=1) group by person_id having count(*) >=1 ) group by person_id having count(*) >=1)"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])

                line = ','.join([person_id])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()