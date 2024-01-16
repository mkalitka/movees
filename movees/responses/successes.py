from movees.responses.generic import generic


def success(data=None, message=None):
    return generic(200, message=message, data=data)


def added(item, message=None):
    return generic(201, message=message, data=item)


def listed(items, message=None):
    return generic(200, message=message, data=items)


def found(item, message=None):
    return generic(200, message=message, data=item)


def updated(item, message=None):
    return generic(200, message=message, data=item)


def deleted(item, message=None):
    return generic(200, message=message, data=item)
