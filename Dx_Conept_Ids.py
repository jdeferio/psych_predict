import io
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()

        output_file = 'dx_concept_ids.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select distinct condition_source_value, condition_concept_id, condition_source_concept_id from staging.condition_occurrence union select distinct condition_source_value, condition_concept_id, condition_source_concept_id from mdd_control.condition_occurrence"

        cursor.execute(sql)

        with io.open(output_file, 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                condition_source_value = str(row[0])
                condition_concept_id = str(row[1])
                condition_source_concept_id = str(row[2])

                line = ','.join(
                    [condition_source_value, condition_concept_id, condition_source_concept_id])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()