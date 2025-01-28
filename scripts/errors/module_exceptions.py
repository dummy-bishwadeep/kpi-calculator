class ILensException(Exception):
    pass


class MongoException(ILensException):
    pass


class MongoConnectionException(MongoException):
    pass


class MongoQueryException(MongoException):
    pass


class MongoEncryptionException(MongoException):
    pass


class MongoRecordInsertionException(MongoQueryException):
    pass


class MongoFindException(MongoQueryException):
    pass


class MongoDeleteException(MongoQueryException):
    pass


class MongoUpdateException(MongoQueryException):
    pass


class MongoUnknownDatatypeException(MongoEncryptionException):
    pass


class MongoDistictQueryException(MongoException):
    pass


class MongoFindAndReplaceException(MongoException):
    pass


class MongoObjectDeserializationException(MongoException):
    pass


class MongoException(Exception):
    pass


class FileExceptions(Exception):
    pass


class FileFormatNotSupported(FileExceptions):
    pass


class MandatoryColumnsMissing(Exception):
    pass


class UnableToReadFile(FileExceptions):
    pass


class PathNotFound(FileExceptions):
    pass


class UnknownHandlerFailureException(ILensException):
    pass


class SiteIdNotFound(ILensException):
    pass


class DataNotFound(ILensException):
    pass


class QueryFormationError(ILensException):
    pass


class DataError(ILensException):
    pass
