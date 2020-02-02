import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_psych_hosp_2014.csv'

# Selects patients who had a psych hospitalization in 2014
        sql = "select v.person_id, v.visit_start_date from staging.condition_occurrence as co join staging.visit_occurrence as v on co.visit_occurrence_id = v.visit_occurrence_id where (v.visit_concept_id = 9201) and ((condition_source_value like '%295%') or (condition_source_value like '%296%') or (condition_source_value like '%297%') or (condition_source_value like '%298%') or (condition_source_value like '%300%') or (condition_source_value like '%301%') or (condition_source_value like '%302%') or (condition_source_value like '%306%') or (condition_source_value like '%307%') or (condition_source_value like '%308%') or (condition_source_value like '%309%') or (condition_source_value like '%ICD9CM:311%') or (condition_source_value like '%312%') or (condition_source_value like '%313%') or (condition_source_value like '%314%') or (condition_source_value like '%F32%') or (condition_source_value like '%F33%') or (condition_source_value like '%F34.1%')) and co.condition_type_concept_id in(44786627, 44786629) and (v.visit_start_date between '2014-01-01' and '2014-12-31') union select v.person_id, v.visit_start_date from mdd_control.condition_occurrence as co join mdd_control.visit_occurrence as v on co.visit_occurrence_id = v.visit_occurrence_id where (v.visit_concept_id = 9201) and ((condition_source_value like '%295%') or (condition_source_value like '%296%') or (condition_source_value like '%297%') or (condition_source_value like '%298%') or (condition_source_value like '%300%') or (condition_source_value like '%301%') or (condition_source_value like '%302%') or (condition_source_value like '%306%') or (condition_source_value like '%307%') or (condition_source_value like '%308%') or (condition_source_value like '%309%') or (condition_source_value like '%ICD9CM:311%') or (condition_source_value like '%312%') or (condition_source_value like '%313%') or (condition_source_value like '%314%') or (condition_source_value like '%F32%') or (condition_source_value like '%F33%') or (condition_source_value like '%F34.1%')) and co.condition_type_concept_id in(44786627, 44786629) and (v.visit_start_date between '2014-01-01' and '2014-12-31')"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])

                line = ','.join(
                    person_id)

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()