import os
import sys
from dotenv import load_dotenv
from psycopg2 import connect, extras, errors

from utils import generateSample


def main():

    # Load environment variables
    load_dotenv()

    # Get test size from argument
    try:
        size = int(sys.argv[1])

    except IndexError:
        print('Missing input size argument, please try again')
        return

    except ValueError:
        print('Argument is not a number, please try again')
        return

    # Get DB environment variables
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    conn = connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host='localhost')
    user_list = generateSample(size)

    ## Debug
    # for user in user_list:
    #     print(user)

    insertUsers(conn, user_list)

    return


def insertUsers(conn, user_list):
    cur = conn.cursor()
    sql = "INSERT INTO users (name, user_id, email_address) VALUES %s;"

    try:
        extras.execute_values(
            cur, sql, user_list,
        )
    except errors.UniqueViolation as err:
        print(err)
        return

    conn.commit()
    return


if __name__ == '__main__':
    main()
