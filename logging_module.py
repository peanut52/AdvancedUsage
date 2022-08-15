import logging
logging.basicConfig( level= logging.DEBUG, format = '%(asctime)s : %(levelname)s : %(message)s', filename= "test.log")
logging.debug('debug message')
logging.info("info message")
logging.warning('warn message')
logging.error("error message")
logging.critical('critical message')