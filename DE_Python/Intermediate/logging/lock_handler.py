import logging

logger = logging.getLogger(__name__)

#create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('DE_Python/Intermediate/logging/file.log')

# define level and format of handlers
stream_h.setLevel(logging.WARNING) # stream  (terminal) loggs warning and above
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s -- %(levelname)s -- %(message)s -- %(lineno)d')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')


