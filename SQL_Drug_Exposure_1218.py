import io
import os

from util import SQL_Connect


def main():
    cursor = SQL_Connect.connect_DB()

    if not os.path.exists("data"):
        os.mkdir("data")
    output_file = "cdrn_drug_exposure_1218.csv"

    # Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
    sql = """
        SELECT
            de.person_id,
            de.drug_exposure_start_date,
            co.concept_name,
            c1.concept_name AS drug_class
        FROM
            staging.drug_exposure de
            JOIN staging.concept co ON co.concept_id = de.drug_concept_id
            JOIN staging.concept_ancestor ca ON ca.descendant_concept_id = co.concept_id
            JOIN staging.concept c1 ON c1.concept_id = ca.ancestor_concept_id
                AND c1.vocabulary_id = 'VA Class'
            JOIN staging.visit_occurrence vi ON de.visit_occurrence_id = vi.visit_occurrence_id
        WHERE (de.drug_exposure_start_date BETWEEN '2012-01-01'
            AND '2017-12-31')
        and(vi.visit_concept_id = 9202)
        UNION
        SELECT
            de.person_id,
            de.drug_exposure_start_date,
            co.concept_name,
            c1.concept_name AS drug_class
        FROM
            mdd_control.drug_exposure de
            JOIN staging.concept co ON co.concept_id = de.drug_concept_id
            JOIN staging.concept_ancestor ca ON ca.descendant_concept_id = co.concept_id
            JOIN staging.concept c1 ON c1.concept_id = ca.ancestor_concept_id
                AND c1.vocabulary_id = 'VA Class'
            JOIN staging.visit_occurrence vi ON de.visit_occurrence_id = vi.visit_occurrence_id
        WHERE (de.drug_exposure_start_date BETWEEN '2012-01-01'
            AND '2017-12-31')
        AND vi.visit_concept_id = 9202
    """

    cursor.execute(sql)

    with io.open(os.path.join("data", output_file), "w", encoding="utf-8") as f:
        for index, row in enumerate(cursor):
            print(index)
            person_id = str(row[0])
            drug_exposure_start_date = str(row[1])
            concept_name = str(row[2])
            drug_class = str(row[3])

            line = ",".join(
                [person_id, drug_exposure_start_date, concept_name, drug_class]
            )

            f.write(line + "\n")

    print("Finished Reading!")


if __name__ == "__main__":
    main()
