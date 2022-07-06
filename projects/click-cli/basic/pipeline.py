def pipeline(handler, **opts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return handler(result, **opts)

        return wrapper

    return decorator


def grep(content: str, pattern: str):
    import re

    filtered = []
    content = content.splitlines()
    for line in content:
        if re.search(pattern, line):
            filtered.append(line)

    return "\n".join(filtered)


def tr(content: str, delete: bool, char: str):
    final = []

    if delete:
        content = content.splitlines()
        for line in content:
            new_line = line.replace(char, "")
            final.append(new_line)
    if final:
        return "".join(final)

    return content


@pipeline(tr, delete=True, char="\n")
@pipeline(grep, pattern="ed")
def echo():
    poetry = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
    """
    return poetry.strip()


if __name__ == '__main__':
    result = echo()
    print(result)
