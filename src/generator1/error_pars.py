class UniversalEx(Exception):
    def __init__(self, status_code: int, content: bytes):
        content = content.decode("utf-8", errors="ignore")
        self.status_code = status_code
        self.content = content
        if status_code >= 400 and status_code < 500:
            super().__init__(f"API {status_code}: {content}")
        elif status_code >= 500:
            super().__init__(f"HTTP {status_code}: {content}")
        else:
            super().__init__(f"UNKNOWN, {content}")