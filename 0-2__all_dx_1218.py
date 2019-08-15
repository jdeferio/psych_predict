import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'cdrn_all_individual_dx_1218.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select co.person_id, co.condition_start_date, co.condition_source_value from staging.condition_occurrence as co where co.condition_start_date between '2012-01-01' and '2017-12-31' union all select co.person_id, co.condition_start_date, co.condition_source_value from mdd_control.condition_occurrence as co where co.condition_start_date between '2012-01-01' and '2017-12-31'"
# 2012-01-01 to 2015-12-31
# 2016-01-01 to 2017-12-31
        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])
                condition_start_date = str(row[1])
                condition_source_value = str(row[2])

                line = ','.join(
                    [person_id, condition_start_date, condition_source_value])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()