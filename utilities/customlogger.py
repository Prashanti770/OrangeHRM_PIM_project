import logging


class LogGen:

    @staticmethod
    def loginfo():
        logging.basicConfig(filename=".\\logs\\automationlogs.log",
                            format='%(asctime)s %(levelname)s %(message)s',
                            filemode='w',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force= True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


