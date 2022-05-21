from src.classes.database_class import Database
import config.local

def main():

    if not setup_database(): db = setup_database() 
    

def setup_database():

    db = Database(config.local.Directory_database_path)

    if db.connect(): pass
    else:
        print("database connection failed!")
        return False

    return db

if __name__ == "__main__":
    main()
    