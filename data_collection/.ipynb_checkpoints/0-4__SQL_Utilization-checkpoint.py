import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_all_visits_2014.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select person_id, visit_start_date, visit_concept_id from staging.visit_occurrence where (visit_start_date between '2014-01-01' and '2014-12-31') union all select person_id, visit_start_date, visit_concept_id from mdd_control.visit_occurrence where (visit_start_date between '2014-01-01' and '2014-12-31')"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])
                condition_start_date = str(row[1])
                visit_type = str(row[2])

                line = ','.join(
                    [person_id, condition_start_date, visit_type])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()