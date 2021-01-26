import io

from util import SQL_Connect


def main():
    cursor = SQL_Connect.connect_DB()

    if not os.path.exists("data"):
        os.mkdir("data")
    output_file = "cdrn_psych_dx_bef_18_indiv_codes.csv"

    # Selects all patients in the cohort and reports their gender, birth date, and age at '2014-01-01'
    sql = """
        SELECT
            v.person_id,
            v.visit_start_date,
            co.condition_source_value
        FROM
            staging.visit_occurrence AS v
            JOIN staging.condition_occurrence AS co ON (v.visit_occurrence_id = co.visit_occurrence_id
                    AND v.person_id = co.person_id)
        WHERE (v.visit_concept_id != 9201)
        and((co.condition_source_value LIKE 'ICD9CM:293.81%')
            or(co.condition_source_value LIKE 'ICD9CM:293.82%')
            or(co.condition_source_value LIKE 'ICD9CM:295%')
            or(co.condition_source_value LIKE 'ICD9CM:296%')
            or(co.condition_source_value LIKE 'ICD9CM:297%')
            or(co.condition_source_value LIKE 'ICD9CM:298%')
            or(co.condition_source_value LIKE 'ICD9CM:300.4%')
            or(co.condition_source_value LIKE 'ICD9CM:311%')
            or(co.condition_source_value LIKE 'ICD10CM:F06.0%')
            or(co.condition_source_value LIKE 'ICD10CM:F06.2%')
            or(co.condition_source_value LIKE 'ICD10CM:F20%')
            or(co.condition_source_value LIKE 'ICD10CM:F21%')
            or(co.condition_source_value LIKE 'ICD10CM:F22%')
            or(co.condition_source_value LIKE 'ICD10CM:F23%')
            or(co.condition_source_value LIKE 'ICD10CM:F24%')
            or(co.condition_source_value LIKE 'ICD10CM:F25%')
            or(co.condition_source_value LIKE 'ICD10CM:F28%')
            or(co.condition_source_value LIKE 'ICD10CM:F29%')
            or(co.condition_source_value LIKE 'ICD10CM:F30%')
            or(co.condition_source_value LIKE 'ICD10CM:F31%')
            or(co.condition_source_value LIKE 'ICD10CM:F32%')
            or(co.condition_source_value LIKE 'ICD10CM:F33%')
            or(co.condition_source_value LIKE 'ICD10CM:F34.1%')
            or(co.condition_source_value LIKE 'ICD10CM:F34.8%')
            or(co.condition_source_value LIKE 'ICD10CM:F39%'))
        AND co.condition_type_concept_id in(44786627, 44786629)
        and(v.visit_start_date < '2018-01-01')
        UNION
        SELECT
            v.person_id,
            v.visit_start_date,
            co.condition_source_value
        FROM
            mdd_control.visit_occurrence AS v
            JOIN mdd_control.condition_occurrence AS co ON (v.visit_occurrence_id = co.visit_occurrence_id
                    AND v.person_id = co.person_id)
        WHERE (v.visit_concept_id != 9201)
        and((co.condition_source_value LIKE 'ICD9CM:293.81%')
            or(co.condition_source_value LIKE 'ICD9CM:293.82%')
            or(co.condition_source_value LIKE 'ICD9CM:295%')
            or(co.condition_source_value LIKE 'ICD9CM:296%')
            or(co.condition_source_value LIKE 'ICD9CM:297%')
            or(co.condition_source_value LIKE 'ICD9CM:298%')
            or(co.condition_source_value LIKE 'ICD9CM:300.4%')
            or(co.condition_source_value LIKE 'ICD9CM:311%')
            or(co.condition_source_value LIKE 'ICD10CM:F06.0%')
            or(co.condition_source_value LIKE 'ICD10CM:F06.2%')
            or(co.condition_source_value LIKE 'ICD10CM:F20%')
            or(co.condition_source_value LIKE 'ICD10CM:F21%')
            or(co.condition_source_value LIKE 'ICD10CM:F22%')
            or(co.condition_source_value LIKE 'ICD10CM:F23%')
            or(co.condition_source_value LIKE 'ICD10CM:F24%')
            or(co.condition_source_value LIKE 'ICD10CM:F25%')
            or(co.condition_source_value LIKE 'ICD10CM:F28%')
            or(co.condition_source_value LIKE 'ICD10CM:F29%')
            or(co.condition_source_value LIKE 'ICD10CM:F30%')
            or(co.condition_source_value LIKE 'ICD10CM:F31%')
            or(co.condition_source_value LIKE 'ICD10CM:F32%')
            or(co.condition_source_value LIKE 'ICD10CM:F33%')
            or(co.condition_source_value LIKE 'ICD10CM:F34.1%')
            or(co.condition_source_value LIKE 'ICD10CM:F34.8%')
            or(co.condition_source_value LIKE 'ICD10CM:F39%'))
        AND co.condition_type_concept_id in(44786627, 44786629)
        and(v.visit_start_date < '2018-01-01')
    """

    cursor.execute(sql)

    with io.open(os.path.join("data", output_file), "w", encoding="utf-8") as f:
        for index, row in enumerate(cursor):
            print(index)
            person_id = str(row[0])
            visit_start_date = str(row[1])
            condition_source_value = str(row[2])

            line = ",".join([person_id, visit_start_date, condition_source_value])

            f.write(line + "\n")

    print("Finished Reading!")


if __name__ == "__main__":
    main()
