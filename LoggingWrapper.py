import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def loggingwrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting function: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function {func.__name__} completed successfully.")
            return result
        except Exception as e:
            logging.error(f"Error in function {func.__name__}: {e}")
            raise
    return wrapper
