import io

from util import SQL_Connect


def main():
    cursor = SQL_Connect.connect_DB()

    if not os.path.exists("data"):
        os.mkdir("data")
    output_file = "cdrn_all_individual_dx_1218.csv"

    # Selects all patient diagnoses that match the inclusion criteria: visit in 2012, 2013, 2014
    sql = """SELECT
                co.person_id,
                co.condition_start_date,
                co.condition_source_value
            FROM
                staging.condition_occurrence AS co
            WHERE
                co.condition_start_date BETWEEN '2012-01-01'
                AND '2017-12-31'
            UNION ALL
            SELECT
                co.person_id,
                co.condition_start_date,
                co.condition_source_value
            FROM
                mdd_control.condition_occurrence AS co
            WHERE
                co.condition_start_date BETWEEN '2012-01-01'
                AND '2017-12-31'
        """

    cursor.execute(sql)

    with io.open(os.path.join("data", output_file), "w", encoding="utf-8") as f:
        for index, row in enumerate(cursor):
            print(index)
            person_id = str(row[0])
            condition_start_date = str(row[1])
            condition_source_value = str(row[2])

            line = ",".join([person_id, condition_start_date, condition_source_value])

            f.write(line + "\n")

    print("Finished Reading!")


if __name__ == "__main__":
    main()
