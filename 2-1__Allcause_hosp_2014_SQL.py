import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_all_hosp_2014.csv'

# Selects all patients in the cohort and reports their gender, birth date, and age at '2014-01-01'
        sql = "select v.person_id, v.visit_start_date, v.visit_concept_id from staging.visit_occurrence as v where (v.visit_concept_id = 9201) and (v.visit_start_date between '2014-01-01' and '2014-12-31') union select v.person_id, v.visit_start_date, v.visit_concept_id from mdd_control.visit_occurrence as v where (v.visit_concept_id = 9201) and (v.visit_start_date between '2014-01-01' and '2014-12-31')"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])
                visit_start_date = str(row[1])
                visit_concept_id = str(row[2])

                line = ','.join([
                    person_id, visit_start_date, visit_concept_id])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()