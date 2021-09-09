from sanic.exceptions import SanicException


class SanicConflictException(SanicException):
    """
    **Status**: 409 Conflict
    """

    status_code = 409
    quiet = True