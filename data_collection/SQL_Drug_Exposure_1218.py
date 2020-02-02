import io
import os
import SQL_Connect

def main():
        cursor = SQL_Connect.connect_DB()
        
        if not os.path.exists('data'):
            os.mkdir('data')
        output_file = 'cdrn_drug_exposure_1218.csv'

# Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
        sql = "select de.person_id, de.drug_exposure_start_date, co.concept_name, c1.concept_name as drug_class  from staging.drug_exposure de  join staging.concept co on co.concept_id = de.drug_concept_id join staging.concept_ancestor ca on ca.descendant_concept_id = co.concept_id join staging.concept c1 on c1.concept_id = ca.ancestor_concept_id and c1.vocabulary_id = 'VA Class' join staging.visit_occurrence vi on de.visit_occurrence_id = vi.visit_occurrence_id where (de.drug_exposure_start_date between '2012-01-01' and '2017-12-31') and (vi.visit_concept_id = 9202)  union  select de.person_id, de.drug_exposure_start_date, co.concept_name, c1.concept_name as drug_class from mdd_control.drug_exposure de  join staging.concept co on co.concept_id = de.drug_concept_id join staging.concept_ancestor ca on ca.descendant_concept_id = co.concept_id join staging.concept c1 on c1.concept_id = ca.ancestor_concept_id and c1.vocabulary_id = 'VA Class' join staging.visit_occurrence vi on de.visit_occurrence_id = vi.visit_occurrence_id where (de.drug_exposure_start_date between '2012-01-01' and '2017-12-31') and vi.visit_concept_id = 9202"

        cursor.execute(sql)

        with io.open(os.path.join('data',output_file), 'w', encoding='utf-8') as f:
            for index, row in enumerate(cursor):
                print(index)
                person_id = str(row[0])
                drug_exposure_start_date = str(row[1])
                concept_name = str(row[2])
                drug_class = str(row[3])


                line = ','.join(
                    [person_id, drug_exposure_start_date, concept_name, drug_class])

                f.write(line + '\n')

        print("Finished Reading!")

if __name__=='__main__':
    main()