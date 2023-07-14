from services.system_tools.ye_logger_of_yor import get_logger

logger = get_logger()


class FileLoadError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"FileLoadError: File not found: %s, {self.message}"
                    )
        return f"File not found: %s, {self.message}"


class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Could not parse, invalid format, {self.message}"
                    )
        return f"Could not parse, invalid format, {self.message}"


class MessageError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Could not parse, invalid format, {self.message}"
            )
        return f"Message error: {self.message}"


class HistoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"History error: {self.message}"
            )
        return f"History error: {self.message}"


class ContextError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Context error: {self.message}"
        )
        return f"Context error: {self.message}"


class PrimerError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Primer error: {self.message}"
        )
        return f"Primer error: {self.message}"


class RoleError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Role error: {self.message}"
        )
        return f"Role error: {self.message}"


class ContextError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        logger.error(
            f"Context error: {self.message}"
        )
        return f"Context error: {self.message}"