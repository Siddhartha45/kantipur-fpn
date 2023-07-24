class FPNBaseException(Exception):
    """Base Exception for Every FPN Exceptions"""

    def __init__(self, message, error_key="fpn_exception"):
        super(FPNBaseException, self).__init__(message, error_key)
        self.message = message
        self.error_key = error_key


class RecordAlreadyExists(FPNBaseException):
    """Raised when existing record for a certain month already exists for user"""
    def __init__(self, message="Record for this month has already been submitted.", error_key="record_exists"):
        super().__init__(message, error_key)