from database_class import db_connect

from directory_scanner.ds_loader import load_directory

from site_scanner.ss_loader import load_pressReleases_sites
from site_scanner.ss_loader import load_individuals


def main():

    db_conn = db_connect()

    if not db_conn:
        return

    load_directory(db_conn, load="light")

    load_individuals(db_conn, load="hard")

    load_pressReleases_sites(db_conn, load="hard")



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