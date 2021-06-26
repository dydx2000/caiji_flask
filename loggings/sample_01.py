import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('access.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s %(name)s | %(levelname)-9s |: %(message)s ")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.info('I am info')
logger.debug('I am debug')
logger.warning('I am warning')
logger.error("I am error")
logger.critical("I am critical")