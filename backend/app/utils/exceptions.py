class CustomException(Exception):
    """Base class for all custom exceptions in the application."""
    pass

class DatabaseConnectionError(CustomException):
    """Exception raised for errors in the database connection."""
    def __init__(self, message="Database connection error occurred."):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomException):
    """Exception raised when a resource is not found."""
    def __init__(self, resource_name, message="Not found error occurred."):
        self.resource_name = resource_name
        self.message = f'{resource_name} not found. {message}'
        super().__init__(self.message)

class InvalidInputError(CustomException):
    """Exception raised for invalid input errors."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)