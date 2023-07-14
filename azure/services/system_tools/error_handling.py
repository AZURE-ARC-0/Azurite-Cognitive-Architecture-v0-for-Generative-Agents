class FileLoadError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"FileLoadError: File not found: {self.message}"


class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Could not parse, invalid format, {self.message}"


class MessageError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Message error: {self.message}"


class HistoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"History error: {self.message}"


class ContextError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Context error: {self.message}"


class PrimerError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Primer error: {self.message}"


class RoleError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Role error: {self.message}"


class ContextError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Context error: {self.message}"



try:
    raise FileLoadError("test_file.txt")
except FileLoadError as e:
    error_message = str(e)

error_message
