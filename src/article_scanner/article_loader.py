from sqlite3_interface import Database, DataTable
from article_scanner.article_crawler import Article_Scanner
from database_searcher import SELECT_Searcher, WHERE

def load_articles(db_conn: Database, load: str) -> DataTable:

    articles_table = DataTable(db_conn, "Articles")

    if load == "hard":

        sql_str = '''
            CREATE TABLE IF NOT EXISTS Articles (
                article_id INTEGER PRIMARY KEY,
                article_title TEXT,
                article_julian_day INTEGER,
                article_content TEXT,
                rep_id INTEGER,
                FOREIGN KEY (rep_id)
                REFERENCES Directory (rep_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            );
        '''

        articles_table.set_custom_query(sql_str).execute()

    elif load == "light":
        """TODO: #9 I dont even know why I am doing these load situations"""
        pass

    return articles_table

def search_and_load_articles(db_conn, load) -> str:
    '''returns 
    a code of diagnostics like new articles added and 
    success/failure codes'''

    crawler = Article_Scanner()

    if load == "research":

        random_id_set_1 = [420, 324,357,251,218,297,167,302,174,20]

        select = SELECT_Searcher(db_conn)

        select.table("Directory")
        select.columns(["general_pressrelease_link"])
        select.add_parameter(WHERE("id").has_values(random_id_set_1))

        print(select)

        links = select.get_result()

        print(links)
