'''
what this file does is manages the directory crawler and interfaces with the directory table in order to fill sql table and validate data'''
from database_class import DataTable
from directory_scanner.directory_crawler import crawl
from directory_scanner.directory_crawler import reformat_name

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

def fill_directory(data, directory_table):
    
    col_sql = directory_table.set_insert_columns(["name", "state", "party", "district_number", "homepage_link"])
    
    data_sql = ""

    for person in data:
        
        if person == data[-1]:
            data_sql += directory_table.set_insert_data([person[0], person[1], person[2], person[3], person[4]], last = True)
        else:
            data_sql += directory_table.set_insert_data([person[0], person[1], person[2], person[3], person[4]])

    directory_table.insert(col_sql, data_sql)
    
def load_directory(database_connection, load: str):
    '''this function is the main function of this file
    1 - first create the directory table if it does not exist
    2 - '''
    directory_tbl = directory_table_setup(database_connection)

    if load == "refresh":
        data = crawl()

        fill_directory(data, directory_tbl)


    