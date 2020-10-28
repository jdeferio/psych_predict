import os
import sys
from configparser import ConfigParser

import psycopg2
import psycopg2.extras


def connect_DB():
    CREDENTIALS = os.environ["CREDENTIALS"]

    parser = ConfigParser()
    parser.read("/" + CREDENTIALS + "/user.cfg")
    data = {
        "host": parser.get("wcm_credentials", "host"),
        "dbname": parser.get("wcm_credentials", "database"),
        "user": parser.get("wcm_credentials", "user_name"),
        "password": parser.get("wcm_credentials", "password"),
    }

    # get a connection, is a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(data)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor(
        "cursor_unique_name", cursor_factory=psycopg2.extras.DictCursor
    )

    return cursor


if __name__ == "__main__":
    main()
