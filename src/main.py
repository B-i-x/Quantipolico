
from sqlite3_interface import db_connect

from directory_scanner.ds_loader import load_directory

from site_scanner.ss_loader import validate_pressReleases_sites

from article_scanner.article_loader import load_articles, search_for_articles

from sql_generation import SQL

def main():

    db_conn = db_connect()

    if not db_conn:
        return

    sql = SQL(db_conn)

    directory_table = load_directory(db_conn, load="light")

    validate_pressReleases_sites(directory_table)

    articles_table = load_articles(db_conn, load="hard")

    search_for_articles(sql, load="research")

if __name__ == "__main__":
    main()

    d = {0: "s", 1: 'd', 2: 'g'}

    '''
    possible structure

    connect to database

    if not db_data_valid
        scan db

    if not individual_data_valid
        get press releases
    
    scan articles with new dates

    '''