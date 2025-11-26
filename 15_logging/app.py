import logging

## logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
## we can give filename and filemode separately or in handlers as above

logger = logging.getLogger('ArithmeticAppLogger')

def add(a, b):
    res = a + b
    logger.debug(f'Adding {a} and {b} = {res}')
    return res

def subtract(a, b):
    res = a - b
    logger.debug(f'Subtracting {b} from {a} = {res}')
    return res

def multiply(a, b):
    res = a * b
    logger.debug(f'Multiplying {a} and {b} = {res}')
    return res

def divide(a, b):
    try:
        res = a / b
        logger.debug(f'Dividing {a} by {b} = {res}')
        return res
    except ZeroDivisionError:
        logger.error('Attempted to divide by zero')
        return None

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 2)
divide(10, 0)