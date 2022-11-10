class InvalidTypeError(Exception):
    def __init__(self, value, code, detail, *args) -> None:
        super().__init__(value, *args)
        self.code = code
        self.detail = detail

    def __repr__(self) -> str:
        return self.detail


def check(v, klass):
    klass_names = [k.__name__ for k in klass]

    if not isinstance(v, tuple(klass)):
        raise InvalidTypeError(
            f"{v.__class__.__name__} class is unknown, use {klass_names}.",
            code=500,
            detail={"value": v, "type": v.__class__.__name__},
        )
    return v


def add(a, b):
    klass = [int, float]
    try:
        a = check(a, klass)
        b = check(b, klass)
    except InvalidTypeError as e:
        error = {
            "name": InvalidTypeError.__name__,
            "code": e.code,
            "detail": e.detail,
        }
        raise TypeError(error) from e

    return a + b


def main():

    try:
        print(add(1, "2"))
    except TypeError as e:
        print(e.args)


if __name__ == '__main__':
    main()
