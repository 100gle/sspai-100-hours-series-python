def fetch(target):
    print(f"fetch {target}...")


def is_url(src):
    if not (src.startswith("http") and src.startswith("https")):
        return False
    return True


def download(url_or_package):
    if not is_url(url_or_package):
        fetch(url_or_package)
        return


def _install(package=None, requirements=None):
    if not package and requirements:
        for _package in requirements:
            download(_package)
    elif package and not requirements:
        download(package)
    else:
        raise ValueError(
            "`package` parameter is required "
            "if there isn't `requirements` parameter."
        )


class PipCommand:
    def __init__(self) -> None:
        pass

    def install(self, *args, **kwargs):
        _install(*args, **kwargs)


if __name__ == '__main__':
    pip = PipCommand()
    package = "pandas"
    requirements = ["pandas", "numpy"]

    # usage
    pip.install(package=package)
    pip.install(requirements=requirements)
