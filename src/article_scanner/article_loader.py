from sqlite3_interface import Database, DataTable
from article_scanner.article_crawler import Press_Release_Organizer
from article_scanner.article_layouts import Article_Layout_Structure
from article_scanner.next_page_layouts import Next_Layout_Structure
from article_scanner.title_layouts import Title_Layout_Structure
from article_scanner.website_attribute import Site_Attribute

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

def get_pr_link_where_col_is_null(col: str) -> list:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns(["id", "general_pressrelease_link"])

    #where_pr_layout = select.where_paramater_for_col(col)
    #where_pr_layout.is_null()

    return sql.get_result_from_query(select, return_type="tuples")

    
def get_layout_popularity_for_column(col: str) -> dict:

    select = sql.create_select_query()
    select.table("Directory")
    select.columns([col])

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

def get_count_of_rows_in_table() -> int:

    select = sql.create_select_query()

    select.table("Directory")

    select.count_all_rows()

    c = sql.get_result_from_query(select, return_type= "tuples")

    return c[0][0]


def summary_col(col: str):

    popularity = get_layout_popularity_for_column(col)

    total = get_count_of_rows_in_table()
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

    links_w_ids = get_pr_link_where_col_is_null(active_column)

    if amount >= len(links_w_ids):

        return links_w_ids

    else: return random.sample(links_w_ids, amount)


def get_active_property_classes(active_column: str) -> list:

    sorted_layout_order = {}

    attribute_classes = [attr_cls() for attr_cls in Site_Attribute.__subclasses__()]

    print(attribute_classes)
    for attr_class in attribute_classes:

        if attr_class.attribute_column_name == active_column:

            Article_Layout_Structure.__subclasses__()
                
            active_classes = [property_cls() for property_cls in attr_class.__subclasses__()]

            print(active_classes)

    return active_classes

    '''
    d = {
        "article_layout" : [cls() for cls in Article_Layout_Structure.__subclasses__()],
        "next_page_control" : [cls() for cls in Next_Layout_Structure.__subclasses__()],
        "title_layout" : [cls() for cls in Title_Layout_Structure.__subclasses__()]
    }

    popularity = get_layout_popularity_for_column(active_column)

    sorted_popularity = [k for k, v in sorted(popularity.items(), key = lambda item: item[1], reverse=True)]
    
    print(sorted_popularity)

    all_type_layouts = d[active_column]

    
    for index, layout in enumerate(sorted_popularity):

        for cls in all_type_layouts:

            if cls.name == layout and not cls.specialized:

                sorted_layout_order[index] = cls

    temp = 0

    for index, cls in enumerate(all_type_layouts):

        if cls not in sorted_layout_order.values() and not cls.specialized:

            if not len(sorted_layout_order):

                sorted_layout_order[temp] = cls

                temp += 1
                
            else:
            
                sorted_layout_order[max(sorted_layout_order) + 1] = cls

    [print(cls.name) for cls in sorted_layout_order.values()]

    if r == "general":

        return sorted_layout_order

    specialized_ids = {}

    for cls in all_type_layouts:

        if cls.specialized:

            if type(cls.ids) == int:

                specialized_ids[cls.ids] = cls

            elif type(cls.ids) == list:

                for id in cls.ids:

                    specialized_ids[id] = cls

    if r  == "specialized":

        return specialized_ids

    '''

def update_col_with_values(col: str, data: list) -> None:

    for set in data:

        id = set[0]

        value = set[1]

        update = sql.create_update_query()

        update.table("Directory")
        update.col(col)
        update.value(value)

        where_id = update.where_paramater_for_col("id")
        where_id.is_value(id)

        sql.print_query(update)

        sql.commit_query(update)

def characeterize_press_release_sites(sql_conn: SQL, load: str, active_column: str = None) -> str:
    '''
    defines types of press release article layout and types of next buttons
    '''
    global sql

    sql = sql_conn

    crawler = Press_Release_Organizer()

    amount_of_sites_to_use = 20
    
    get_active_property_classes(active_column)

    if load == "research":

        press_release_links_w_ids = get_random_pr_links(active_column, amount_of_sites_to_use)

        crawler.research(press_release_links_w_ids)

    elif load == "characterize":

        crawler.links_w_ids = get_random_pr_links(active_column, amount_of_sites_to_use)

        #crawler.set_types(get_types(active_column, "general"),get_types(active_column, "specialized"))

        matches = crawler.run_characterization()

        update_col_with_values(active_column, matches)

        summary_col(active_column) 


