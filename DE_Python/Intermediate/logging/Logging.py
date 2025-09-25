import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')

# By default, logging level is warning that why only warning and above gets printed
logging.debug('This is a debug message')
logging.info('This is a debug message')
logging.warning('This is a debug message')
logging.error('This is a debug message')
logging.critical('This is a debug message')


import own_logger

