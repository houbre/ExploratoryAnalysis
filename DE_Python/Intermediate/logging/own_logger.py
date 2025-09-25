import logging

#best practice to create your own logger

logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('hello from my own logger')