class APIQueryException(Exception):
    def __init__(self, status_code: int, detail) -> None:
        self.status_code = status_code
        self.detail = detail

    def __str__(self) -> str:
        return f"staus_code={self.status_code}, detail={self.detail}"
