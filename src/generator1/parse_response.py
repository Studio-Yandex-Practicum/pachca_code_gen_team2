from .error_pars import UniversalEx


class Parse_Response:
    def __init__(self, response, data):
        self.response = response
        self.data = data

    def __str__(self):
        if 200 <= self.response.status_code < 300:
            content = self.response.content.decode("utf-8", errors="ignore")
            return f"response_status={self.response.status_code}, content={content})"
        else:
            raise UniversalEx(
                self.response.status_code, self.response.content
            )