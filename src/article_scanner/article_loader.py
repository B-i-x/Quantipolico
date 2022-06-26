from certifi import where
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
    select.columns(["id", "general_pressrelease_link"])

    id = select.where_paramater_for_col("id")
    id.has_values(id_list)

    where_pr_layout = select.where_paramater_for_col("press_release_layout")
    where_pr_layout.is_null()

    return sql.get_result_from_query(select, return_type="tuples")

def get_layout_popularity(sql: SQL) -> dict:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns(["press_release_layout"])

    where_pr_layout = select.where_paramater_for_col("press_release_layout")
    where_pr_layout.not_null()

    layouts =  sql.get_result_from_query(select)

    print(layouts)

    popularity = {}

    for layout in layouts:

        if layout not in popularity:

            popularity[layout] = 1

        else:

            popularity[layout] += 1

    #print(popularity)

    sorted_popularity = [k for k, v in sorted(popularity.items(), key = lambda item: item[1], reverse=True)]
        
    return sorted_popularity


def search_for_articles(sql: SQL, load) -> str:
    '''returns 
    a code of diagnostics like new articles added and 
    success/failure codes'''

    crawler = Article_Finder()

    if load == "research":

        random_id_set_length = 25

        generated_random_id_set = random.sample(range(0,441), random_id_set_length)

        links_w_ids = get_links_from_ids(sql, generated_random_id_set)

        print(links_w_ids)

        #crawler.research(links)

        layout_popularity = get_layout_popularity(sql)

        print(layout_popularity)

        matches = crawler.find_press_release_website_type(links_w_ids, layout_popularity)
       
        for match in matches:

            id = match[0]

            press_release_layout_type = match[1]

            update = sql.create_update_query()

            update.table("Directory")
            update.col("press_release_layout")
            update.value(press_release_layout_type)

            where_id = update.where_paramater_for_col("id")
            where_id.is_value(id)

            sql.print_query(update)

            sql.commit_query(update)
        