from sqlite3_interface import Database, DataTable
from article_scanner.article_crawler import Article_Finder
from sql_generation import SQL

import random

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

def get_links_from_ids(sql: SQL, id_list: list) -> list:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns(["general_pressrelease_link"])

    id = select.where_paramater_for_col("id")
    id.has_values(id_list)

    return sql.get_result_from_query(select)

def search_for_articles(sql: SQL, load) -> str:
    '''returns 
    a code of diagnostics like new articles added and 
    success/failure codes'''

    crawler = Article_Finder()

    if load == "research":

        random_id_set_1 = [420, 324,357,251,218,297,167,302,174,20]

        random_id_set_2 = [296, 75, 243, 411, 136, 221, 106, 247, 407, 201]

        random_id_set_length = 20

        generated_random_id_set = random.sample(range(0,441), random_id_set_length)

        links = get_links_from_ids(sql, )

        print(links)

        crawler.research(links)
