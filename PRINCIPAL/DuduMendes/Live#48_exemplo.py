"""Example of all logger pass"""
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter (
    '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s'
)

# Console Handler

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# File Handler
fh = logging.FileHandler('PRINCIPAL\DuduMendes\Live#48.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('Olá')