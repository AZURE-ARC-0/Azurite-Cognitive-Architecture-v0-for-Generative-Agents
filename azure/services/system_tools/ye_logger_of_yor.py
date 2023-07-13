# -*- coding: utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler


class YeLoggerOfYor(object):
    def __init__(self):
        self.log_file_name = "azure/static/logs/logger_of_yor.log"
        self.logger = logging.getLogger(__name__)

    # set the log level
    def set_logging_level(self):
        self.logger.setLevel()
        self.log_file_name = "azure/static/logs/logger_of_yor.log"

            # add a timed rotating file handler to the logger
    def fileHandler(self):
        input_values(
            "atTime":'',
            "backupCount",
            "interval",
            "when",
            "filename",
            "interval",
            "encoding",
            "errors",
            "delay",
            "utc"
        )
        if not input_values:
            when = 'midnight',
        if not backupCount:
            backupCount = 7
        if not interval:
            interval = 1


        return self.logger.addHandler(
            TimedRotatingFileHandler(
            atTime=when,
            backupCount=7,
            filename=self.log_file_name,
            interval=1,
            encoding='utf-8',
            errors='strict',
            delay=False,
            utc=False
            )
        )


        self.file_handler.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s - Line %(lineno)d'
            )
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)



def get_logger(self,):
    return YeLoggerOfYor().logger