from logging import exception
from core.exceptions import (
    ExceptionBase, 
    ConfictException,
    NotFoundException,
    DomainException,
    SanicConflictException
)

from sanic.handlers import ErrorHandler
from sanic.exceptions import SanicException, Forbidden, NotFound

class ExceptionInterceptor(ErrorHandler):
    def default(self, request, exception: ExceptionBase):
        ''' handles errors that have no error handlers assigned '''
        
        if isinstance(exception, DomainException):
            print(exception)
            raise Forbidden()
        if isinstance(exception, NotFoundException):
            print(exception)
            raise NotFound()
        if isinstance(exception, ConfictException):
            print(exception)
            raise SanicConflictException()

        return super().default(request, exception)