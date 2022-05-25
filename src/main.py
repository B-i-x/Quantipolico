from database_class import db_connect
from directory_scanner.directory_loader import load_directory

def main():

    db_conn = db_connect()

    if not db_conn:
        return

    load_directory(db_conn, load="refresh")

if __name__ == "__main__":
    main()

    '''
    possible structure

    connect to database

    if not db_data_valid
        scan db

    if not individual_data_valid
        get press releases
    
    scan articles with new dates
    '''