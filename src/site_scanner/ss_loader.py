from site_scanner.ss_crawler import search

from site_scanner.ss_crawler import Crawler

def insert_into_table():
    pass

def validate_pressReleases_sites(directory_tbl):
    '''this checks whether each representative has a press release website
    
    get names from directory table'''

    if directory_tbl.has_col_null("general_pressrelease_link"):

        driver_obj = Crawler('https://www.google.com/')

        names = directory_tbl.select_col_from_table("name")

        pressRelease_links = search(driver_obj, names)

        directory_tbl.insert(["general_pressrelease_link"], pressRelease_links)
        #link = search("Jerry Carl")
        #do some crawling
    

def load_individuals(database_connection, load: str):
    '''makes all the tables for the 441 people of congress + ur mom'''
    if load == "hard":
       
        #create them for the first time
        pass
    elif load == "light":
        #checks that they all exist, a.k.a stupid validation 
        pass
