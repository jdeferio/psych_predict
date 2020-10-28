import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        if not os.path.exists('data'):
            os.mkdir('data')
        output_file = 'cdrn_all_procs_1218.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select co.person_id, co.procedure_date, co.procedure_source_value from staging.procedure_occurrence as co where (co.procedure_date between '2012-01-01' and '2017-12-31') and ((co.procedure_source_value like 'ICD10%') or (co.procedure_source_value like 'ICD9%')) union all select co.person_id, co.procedure_date, co.procedure_source_value from mdd_control.procedure_occurrence as co where (co.procedure_date between '2012-01-01' and '2017-12-31') and ((co.procedure_source_value like 'ICD10%') or (co.procedure_source_value like 'ICD9%'))"
# 2012-01-01 to 2015-12-31
# 2016-01-01 to 2017-12-31
        cursor.execute(sql)

        with io.open(os.path.join('data',output_file), 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])
                procedure_date = str(row[1])
                procedure_source_value = str(row[2])

                line = ','.join(
                    [person_id, procedure_date, procedure_source_value])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()