class ApiResponse:
    def __init__(self, status: str, data=None, message: str = None):
        self.status = status
        self.data = data
        self.message = message

    def to_dict(self):
        response = {"status": self.status}
        if self.data is not None:
            response["data"] = self.data
        if self.message is not None:
            response["message"] = self.message
        return response

def success_response(data):
    return ApiResponse(status="success", data=data).to_dict()

def error_response(message, status_code=400):
    # Puedes incluir status_code en la respuesta si lo requieres
    return ApiResponse(status="error", message=message).to_dict()
