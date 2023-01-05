name: str = "100gle"
number: int = 1
yes_or_no: bool = True


def greet(name: str = '') -> str:
    if not name:
        name = "world"

    return f"Hello, {name}"
