from pydantic.fields import PrivateAttr
from core.exceptions.base import ExceptionBase
from core.exceptions.type import Exceptions

class ConfictException(ExceptionBase):

    __name: str = PrivateAttr(Exceptions.conflict.value)
