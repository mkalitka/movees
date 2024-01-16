def generic(code, data=None, message=None):
    if data is None and message is None:
        return {"status_code": code}
    elif data is None:
        return {"status_code": code, "message": message}
    elif message is None:
        return {"status_code": code, "data": data}
    return {"status_code": code, "data": data, "message": message}
