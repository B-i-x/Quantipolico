from sqlite3_interface import Database, DataTable
from article_scanner.article_crawler import Press_Release_Organizer
from sql_generation import SQL

import random

sql = None

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

def get_pr_link_from_ids_where_col_is_null(id_list: list, col: str) -> list:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns(["id", "general_pressrelease_link"])

    id = select.where_paramater_for_col("id")
    id.has_values(id_list)

    where_pr_layout = select.where_paramater_for_col(col)
    where_pr_layout.is_null()

    return sql.get_result_from_query(select, return_type="tuples")

    
def get_layout_popularity_for_column(col: str) -> dict:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns(["press_release_layout"])

    where_pr_layout = select.where_paramater_for_col(col)
    where_pr_layout.not_null()

    layouts =  sql.get_result_from_query(select)

    #print(layouts)

    popularity = {}

    for layout in layouts:

        if layout not in popularity:

            popularity[layout] = 1

        else:

            popularity[layout] += 1
        
    return popularity

def summary_col(col: str):

    popularity = get_layout_popularity_for_column(col)

    total = 440
    sum_of_matches = 0
    
    for count in popularity.values():

        sum_of_matches += count

    print(f"{'__________CURRENT SUMMARY__________':^79}")
    print(f"{'LAYOUT' : ^60} {'COUNT' : ^7} {'PERCENTAGE%':^12}")

    for layout in popularity:
        
        print(f"{layout : <60} {popularity[layout] : ^7} {((popularity[layout]/sum_of_matches)*100):^12.2f}")

    print(f"{'TOTAL' : <60} {sum_of_matches : ^7} {((sum_of_matches/total)*100):^12.2f}")

    print(f"STILL MISSING {total - sum_of_matches}")

def get_random_pr_links(active_column: str, amount) -> list:

    generated_random_id_set = random.sample(range(0,441), amount)

    links_w_ids = get_pr_link_from_ids_where_col_is_null(sql, generated_random_id_set, active_column)

    return links_w_ids


def get_type_popularity(active_column: str) -> list:

    popularity = get_layout_popularity_for_column(active_column)

    #print(layout_popularity)

    sorted_popularity = [k for k, v in sorted(popularity.items(), key = lambda item: item[1], reverse=True)]

    return sorted_popularity


def characeterize_press_release_sites(sql_conn: SQL, load: str, type: str = None) -> str:
    '''
    defines types of press release article layout and types of next buttons
    '''

    global sql

    sql = sql_conn

    crawler = Press_Release_Organizer()

    amount_of_sites_to_use = 10


    if load == "research":
        
        crawler.research(links_w_ids)

    elif load == "characterize":

        active_column = None

        if type == "article_layout":

            active_column = "press_release_layout"

        elif type == "next_button":

            active_column = "next_page_control"


        get_random_pr_links(active_column, amount_of_sites_to_use)

        get_type_popularity(active_column)


    elif load == "match_press_release_layout":

        active_column = "press_release_layout"

        links_w_ids = get_pr_link_from_ids_where_col_is_null(sql, generated_random_id_set, active_column)

        popularity = get_layout_popularity_for_column(sql, active_column)

        #print(layout_popularity)

        sorted_popularity = [k for k, v in sorted(popularity.items(), key = lambda item: item[1], reverse=True)]

        matches = crawler.find_press_release_website_type(links_w_ids, sorted_popularity)
       
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
        
        summary_col(sql)

    elif load == "match_next_button_layout":

        active_column = "next_page_control"

        find_type_of_press_release_site(active_column, amount=amount_of_sites_to_use)

