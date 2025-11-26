from logger import logging

def add(a, b):
    logging.debug(f"Adding {a} and {b}, happening now")
    return a + b

logging.info("Starting the addition operation")
add(12,3)