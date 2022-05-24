from representative_class import rep
from database_class import db_db_connect

def connect_to_database():
    '''
    Code returns
    0: All connections are successful
    1: connection has failed
    '''
    code = 0
    print("Connecting to database...")

    db_conn = db_db_connect()

    if not db_conn:
        code = 1

    return (code, db_conn)

def main():

    code, db_conn = connect_to_database()


if __name__ == "__main__":
    main()

    '''
    possible structure

    connect to databases

    if not db_data_valid
        scan db

    if not individual_data_valid
        get press releases
    
    scan articles with new dates
    '''