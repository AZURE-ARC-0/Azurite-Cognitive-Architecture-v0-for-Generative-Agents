from logging import Logger
from logging.handlers import TimedRotatingFileHandler
import streamlit as st
import logging


class YeLoggerOfYor(Logger):
    def __init__(self, log_file_name, log_level):
        super().__init__(log_file_name, log_level)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        file_handler = TimedRotatingFileHandler(
            log_file_name,
            when='midnight',
            backupCount=7
        )
        file_handler.setLevel(log_level)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)


logger: Logger = YeLoggerOfYor("azure/static/logs/log.log", logging.INFO)


@st.cache_resource()
def get_logger():
    return logger.logger
