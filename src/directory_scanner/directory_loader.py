from src.directory_scanner.database_class import Database
import config.local

def main():

    db = Database(config.local.Directory_database_path())

    if not db.connect: return

    
if __name__ == "__main__":
    main()
    