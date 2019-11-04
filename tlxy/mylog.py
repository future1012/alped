# import logging
#
# asctime/levelname/message程序定义好的名称
# LOG_FORMAT = "%(asctime)s %(levelname)s %(processName)s %(message)s"
#
# logging.basicConfig(filename='tlxy.log', level=logging.DEBUG, format=LOG_FORMAT)
# logging.debug('this is a debug log')
# logging.info('this is a info log')
# logging.warning('this is a warning log')
# logging.error('this is a error log')
# logging.critical('this is  a critical log')
#


import logging
import logging.handlers
import datetime

logger = logging.getLevelName('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1,)