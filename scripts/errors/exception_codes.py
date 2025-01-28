class MongoExceptionCodes:
    MONGO001 = (
        "Error Code MONGO001: Server was unable to establish connection with MongoDB"
    )
    MONGO002 = (
        "Error Code MONGO002: "
        + "Server faced a problem when inserting document(s) into MongoDB"
    )
    MONGO003 = (
        "Error Code MONGO003: "
        + "Server faced a problem to find the document(s) with the given condition"
    )
    MONGO004 = (
        "Error Code MONGO004: "
        + "Server faced a problem to delete the document(s) with the given condition"
    )
    MONGO005 = (
        "Error Code MONGO005: " + "Server faced a problem to update the ",
        "document(s) with the given condition and data",
    )
    MONGO006 = "Error Code MONGO006: Server faced a problem when aggregating the data"
    MONGO007 = (
        "Error Code MONGO007: Server faced a problem when closing MongoDB connection"
    )
    MONGO008 = (
        "Error Code MONGO008: Found an existing record with the same ID in MongoDB"
    )
    MONGO009 = (
        "Error Code MONGO009: "
        + "Server faced a problem when fetching distinct documents from MongoDB"
    )
    MONGO010 = (
        "Error Code MONGO010: "
        + "Server faced a problem when performing a search and ",
        "replace in MongoDB",
    )
    MONGO011 = (
        "Error Code MONGO011: Server faced a problem when "
        + "de-serializing MongoDB object"
    )


class ValidationExceptions:
    IL001 = "Error Code IL001: Required Keys are missing!"
    IL002 = "Error Code IL002: User id is missing in the cookies!"


class SupportLensExceptionCodes:
    SERV001 = (
        "Server did not get a successful response. "
        + "Check the server logs for more information"
    )
    SERV002 = (
        "Server faced a problem when processing the service. "
        "Check the server logs or contact administrator "
        "for more information"
    )
