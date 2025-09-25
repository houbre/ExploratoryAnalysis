import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Handler = RotatingFileHandler('DE_Python/Intermediate/logging/app.log', maxBytes=200, backupCount=5)
logger.addHandler(Handler)


for _ in range(10000):
    logger.info('Logging some info')



#Also TimeRotatingFileHandler
# Handler = RotatingFileHandler('DE_Python/Intermediate/logging/app.log', when='m', interval=3, backupCount=5) every 3 minutes create a file