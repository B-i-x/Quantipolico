import os, sys
sys.path.insert(0, os.path.abspath("."))

from src.representative_class import rep

def representative_class_test():

    r = rep("a", "a", "a", "0", 0)

    print(r.name)

if __name__ == "__main__":
    representative_class_test()

    