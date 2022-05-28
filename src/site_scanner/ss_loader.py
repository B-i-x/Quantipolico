from matplotlib.pyplot import sca
from site_scanner.ss_crawler import PressRelease_Scanner
from sqlite3_interface import DataTable

def insert_into_table():
    pass

def validate_pressReleases_sites(directory_tbl: DataTable) -> bool:
    '''this checks whether each representative has a press release website
    
    if press releases valid return true
    if not valid return false'''

    if directory_tbl.has_col_null("general_pressrelease_link"):

        scanner = PressRelease_Scanner(debug=True)

        while directory_tbl.has_col_null("general_pressrelease_link"):

            name = directory_tbl.cell_satisfying_condition("name", "general_pressrelease_link", "NULL").get(all=False)

            name = "".join(name) #converts tup name to string name
            
            scanner.set_name(name)

            scanner.run()

            link = scanner.get_link()

            sql = directory_tbl.insert_into_cell(link, "general_pressrelease_link", "name", name)

            print(sql)
            sql.commit()
    
    #i should prolly still do some validation down here????

    return True

def load_individuals(database_connection, directory_tbl: DataTable, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":

        all_names = directory_tbl.col_from_table("name").get()

        for n in all_names:
            name = "".join(n)
            

        print(all_names)
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
