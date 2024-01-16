import fastapi


def create_json_response(response):
    return fastapi.responses.JSONResponse(
        status_code=response["status_code"],
        content=response,
    )
