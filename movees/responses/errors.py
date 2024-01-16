from movees.responses.generic import generic


def error(data=None, message=None):
    return generic(400, message=message, data=data)


def not_found(data=None, message=None):
    return generic(404, message=message, data=data)


def invalid_method(data=None, message=None):
    return generic(405, message=message, data=data)


def already_exists(data=None, message=None):
    return generic(409, message=message, data=data)


def invalid(data=None, message=None):
    return generic(422, message=message, data=data)
