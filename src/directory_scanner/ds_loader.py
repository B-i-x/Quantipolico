'''
what this file does is manages the directory crawler and interfaces with the directory table in order to fill sql table and validate data'''
from database_class import DataTable
from directory_scanner.ds_crawler import crawl

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

    directory_table.execute(sql)

    return directory_table
    
def load_directory(database_connection, load: str):
    '''this function is the main function of this file
    1 - first create the directory table if it does not exist
    2 - '''
    directory_tbl = directory_table_setup(database_connection)

    if load == "hard":
        directory_tbl.delete_self()
        directory_tbl = directory_table_setup(database_connection)

        data = crawl()

        directory_tbl.insert(["name", "state", "party", "district_number", "homepage_link"], data, committing=True)

    elif load == "light":
        return directory_tbl

    else: print("load configuration not recognized")



    