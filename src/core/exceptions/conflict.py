from pydantic.fields import PrivateAttr
from core.exceptions.base import ExceptionBase
from core.exceptions.type import Exceptions
from sanic.exceptions import SanicException

class SanicConflictException(SanicException):
    """
    **Status**: 409 Conflict
    """

    status_code = 409
    quiet = True

class ConfictException(ExceptionBase):

    __name: str = PrivateAttr(Exceptions.conflict.value)
