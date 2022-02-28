class LoggerInstance(object):
    def __new__(cls):
        from app.utils.logger.custom_logging import LogHandler
        return LogHandler()