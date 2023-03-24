import logging

class backend_log():

    logging.basicConfig(filename='backend_logs.log',
                        filemode='a',
                        format='[%(asctime)s][%(levelname)s]: %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.DEBUG)

    def debug(message):
        logging.debug(message)

    def info(message):
        logging.info(message)

    def warning(message):
        logging.warning(message)

    def error(message):
        logging.error(message)

    def critical(message):
        logging.critical(message)

class database_log():
    logging.basicConfig(filename='database_logs.log',
                        filemode='a',
                        format='[%(asctime)s][%(levelname)s]: %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.DEBUG)

    def debug(message):
        logging.debug(message)

    def info(message):
        logging.info(message)

    def warning(message):
        logging.warning(message)

    def error(message):
        logging.error(message)

    def critical(message):
        logging.critical(message)

class request_log():
    logging.basicConfig(filename='request_logs.log',
                        filemode='a',
                        format='[%(asctime)s][%(levelname)s]: %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.DEBUG)

    def debug(message):
        logging.debug(message)

    def info(message):
        logging.info(message)

    def warning(message):
        logging.warning(message)

    def error(message):
        logging.error(message)

    def critical(message):
        logging.critical(message)