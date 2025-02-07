"""Core module of Dundie"""
from dundie.utils.log import get_logger

log = get_logger()

def load(filepath):
    """Loads data from filepath to the database (using doctest below)
    
    >>> len(load("names.csv"))
    2
    """
    try:
        with open(filepath) as file_:
            return file_.readlines()
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

