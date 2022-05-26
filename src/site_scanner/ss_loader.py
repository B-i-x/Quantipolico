from site_scanner.ss_crawler import search


def validate_pressReleases_sites(directory_tbl):
    '''this checks whether each representative has a press release website
    
    get names from directory table'''

    press_releases = 1 #check the directory table and do real validation
    if press_releases == 1:
        names = directory_tbl.select_col_from_table("name")

        print(names)
        link = search("Jerry Carl")
        #do some crawling
    

def load_individuals(database_connection, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
