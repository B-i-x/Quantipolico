from database_class import db_connect
from database_class import DataTable

def directory_table_setup(database_connection):

    directory_table = DataTable(database_connection, "Directory")

    sql = directory_table.setup(True, 
    [
        ["name", "text"],
        ["party", "text"],
        ["state", "text"],
        ["district_number", "text"],
        ["homepage_link", "text"],
        ["general_pressrelease_link", "text"]
    ]
    )

    print(sql)

    

def main():

    db_conn = db_connect()

    if not db_conn:
        return
    
    directory_table_setup(db_conn)


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