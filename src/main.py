from representative_class import rep
from database_class import directory_db_connect

def connect_to_databases():
    '''
    Code returns
    0: All connections are successful
    1: directory connection has failed
    '''
    code = 0
    print("Connecting to databases...\n")

    if not directory_db_connect():
        code = 1
    
    directory_conn = directory_db_connect()

    return (code, directory_conn)

def main():

    connect_to_databases()

    r = rep("a", "a", "a", "a", 0)

    print(r.name)

if __name__ == "__main__":
    main()

    '''
    possible structure

    connect to databases

    if not directory_data_valid
        scan directory

    if not individual_data_valid
        get press releases
    
    scan articles with new dates
    '''