from flask import Response
from .CONST import ResponseStatus as rs


class WebAppException(Exception):
    def __init__(self, descr="Unknown error", status=rs.UNKNOWN_ERROR_520):
        self.status = status
        self.descr = descr

    def get_response(self):
        return Response(self.descr, status=self.status)


class ClientException(WebAppException):
    def __init__(self, descr="Client error", status=rs.BAD_REQUEST_400):
        self.status = status
        self.descr = descr


class ServerException(WebAppException):
    def __init__(self, descr="Server error", status=rs.INTERNAL_SERVER_ERROR_500):
        self.status = status
        self.descr = descr
