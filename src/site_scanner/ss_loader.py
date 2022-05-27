from site_scanner.ss_crawler import PressRelease_Scanner

def insert_into_table():
    pass

def validate_pressReleases_sites(directory_tbl):
    '''this checks whether each representative has a press release website
    
    get names from directory table'''

    if directory_tbl.has_col_null("general_pressrelease_link"):

        names = directory_tbl.select_col_from_table("name")

        crawler = PressRelease_Scanner(names, debug=True)

        crawler.set_return_at_count(5)

        crawler.run()

        links = crawler.get_data()

        print(links)

        #directory_tbl.insert_list(["general_pressrelease_link"], pressRelease_links)
        
        #do some crawling
    

def load_individuals(database_connection, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
