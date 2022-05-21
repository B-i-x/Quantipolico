import sys

from src.database_class import Database
import config.local

sys.path.append(r"C:\Users\alexr\Documents\Projects\Mathematical Politics\repository\src")

def main():

    db = Database(config.local.Directory_database_path())

    if not db.connect: return

    
if __name__ == "__main__":
    main()
    