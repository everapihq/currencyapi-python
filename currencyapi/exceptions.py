class RateLimitExceeded(Exception):
    """Raised when the rate limit was exceeded"""
    pass

class QuotaExceeded(Exception):
    """Raised when the rate limit was exceeded"""
    pass

class NotAllowed(Exception):
    """Raised when you are not allowed to access this route"""
    pass

class ApiError(Exception):
    """The API returned the following error"""
    pass