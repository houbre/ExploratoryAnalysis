import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('SimpleExemple')

logger.debug('Debu msg from simple exemple logger')