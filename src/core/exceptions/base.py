from abc import ABC, abstractmethod, abstractproperty
from typing import (Dict, Optional, Any)
from pydantic import BaseModel
from pydantic.fields import PrivateAttr
from core.exceptions.type import Exceptions
import traceback

class SerializedException(BaseModel, ABC):

    name: str
    message: str
    stack: Optional[str]
    metadata: Optional[Dict[str, Any]]

class ExceptionBase(BaseModel, ABC):

    __name: str = PrivateAttr()

    def __init__(self, message: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)   

    @property
    def name(self) -> str: 
        return self.__name

    def to_json(self) -> SerializedException:
        return SerializedException(
            name=self.name,
            message=self.message,
            stack=''.join(traceback.format_stack()),
            metadata=self.metadata
        ).json()
