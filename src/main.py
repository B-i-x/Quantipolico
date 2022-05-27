
from database_class import db_connect

from directory_scanner.ds_loader import load_directory

from site_scanner.ss_loader import validate_pressReleases_sites
from site_scanner.ss_loader import load_individuals


def main():

    db_conn = db_connect()

    if not db_conn:
        return

    directory_table = load_directory(db_conn, load="light")

    individual_tables = load_individuals(db_conn, load="hard")

    validate_pressReleases_sites(directory_table)

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