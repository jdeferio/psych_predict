import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_all_individual_visits.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select distinct vi.person_id from staging.visit_occurrence as vi where vi.visit_start_date between '2012-01-01' and '2015-12-31' union all select distinct vi.person_id from mdd_control.visit_occurrence as vi where vi.visit_start_date between '2012-01-01' and '2015-12-31'"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])

                line = ','.join(
                    [person_id])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()