class ErrorMessages:
    UNKNOWN = "Unknown Error occurred"
    ERR001 = "Configurations not available, please verify the database."
    ERR002 = "Data Not Found"
    K_ERROR1 = "Data Not Found in Time series Database"
    K_ERROR2 = "Time series Database returned with an error"
    K_ERROR3 = "Communication Error with Time series Database"
    DF_ERROR1 = "Error occurred while forming Dataframe"
    DF_ERROR2 = "Given group-by parameters are invalid"
    META_ERROR1 = "Tags not Found in Meta"


class ErrorCodes:
    ERR001 = "ERR001 - Operating Time is greater than Planned Time"
    ERR002 = "ERR002 - Zero Values are not allowed"
    ERR003 = "ERR003 - Operating Time is less than Productive Time"
    ERR004 = "ERR004 - Rejected Units is greater than Total Units"
    ERR005 = "ERR005 - Batch Start time not supplied"
    ERR006 = "ERR006 - Total Units Tag not found!!"
    ERR007 = "ERR007 - Reject Units Tag not found!!"
    ERR008 = "ERR008 - Cycle Time Tag not found!!"
    ERR009 = "ERR009 - Batch Tag not found!!"


class UnknownError(Exception):
    pass


class KairosDBError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class ILensError(Exception):
    pass


class NameExists(Exception):
    pass


class InputRequestError(ILensError):
    pass


class IllegalTimeSelectionError(ILensError):
    pass


class DataNotFound(Exception):
    pass


class AuthenticationError(ILensError):
    """
    JWT Authentication Error
    """


class JWTDecodingError(Exception):
    pass


class DuplicateReportNameError(Exception):
    pass


class PathNotExistsException(Exception):
    pass


class ImplementationError(Exception):
    pass


class ILensErrors(Exception):
    """Generic iLens Error"""


class DataFrameFormationError(ILensErrors):
    """Raise when there is an error during dataframe formation"""
