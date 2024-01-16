from movees.responses.generic import generic
from movees.responses import Message


def error(data=None, message=None):
    return generic(400, message=message, data=data)


def not_found(data=None, message=Message.NOT_FOUND):
    return generic(404, message=message, data=data)


def invalid_method(data=None, message=Message.INVALID_METHOD):
    return generic(405, message=message, data=data)


def already_exists(data=None, message=None):
    return generic(409, message=message, data=data)


def invalid(data=None, message=None):
    return generic(422, message=message, data=data)


def service_unavailable(data=None, message=Message.SERVICE_UNAVAILABLE):
    return generic(503, message=message, data=data)
