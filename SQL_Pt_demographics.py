import io

from util import SQL_Connect


def main():
    cursor = SQL_Connect.connect_DB()

    if not os.path.exists("data"):
        os.mkdir("data")
    output_file = "cdrn_all_demographics.csv"

    # Selects all patients in the cohort and reports their gender, birth date, and age at '2014-01-01'
    sql = """
        SELECT
            one.*,
            round(ceil((extract(epoch FROM age('2014-01-01', birth_date)) / 86400)) / 365) AS age
        FROM ( SELECT DISTINCT
                person_id,
                gender_concept_id,
                make_date (year_of_birth,
                    month_of_birth,
                    day_of_birth) AS birth_date
            FROM
                staging.person) AS one
        UNION
        SELECT
            one.*,
            round(ceil((extract(epoch FROM age('2014-01-01', birth_date)) / 86400)) / 365) AS age
        FROM ( SELECT DISTINCT
                person_id,
                gender_concept_id,
                make_date (year_of_birth,
                    month_of_birth,
                    day_of_birth) AS birth_date
            FROM
                mdd_control.person) AS one
    """

    cursor.execute(sql)

    with io.open(os.path.join("data", output_file), "w", encoding="utf-8") as f:
        for index, row in enumerate(cursor):
            print(index)
            person_id = str(row[0])
            gender_concept_id = str(row[1])
            birth_date = str(row[2])
            age = str(row[3])

            line = ",".join([person_id, gender_concept_id, birth_date, age])

            f.write(line + "\n")

    print("Finished Reading!")


if __name__ == "__main__":
    main()
