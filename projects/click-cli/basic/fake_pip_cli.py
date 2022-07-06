import argparse
from importlib.metadata import requires


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


def _tidy_requirements(requirements):
    filtered = filter(lambda r: not r.startswith("#") and r.strip() != "", requirements)
    keep = list(map(lambda r: r.strip(), filtered))
    return keep


def main():
    parser = argparse.ArgumentParser(
        description="the fake pip usage example",
    )
    subparsers = parser.add_subparsers(
        description="the sub-command for fake pip tools",
    )

    parser_install = subparsers.add_parser("install")
    parser_install.add_argument(
        "package",
        type=str,
        nargs="?",
        help="the name of package",
    )
    parser_install.add_argument(
        "-r",
        "--requirements",
        dest="requirements",
        help="the requirements file",
        type=argparse.FileType("r", encoding="utf-8"),
    )

    args = parser.parse_args()
    deps = (
        _tidy_requirements(args.requirements.readlines()) if args.requirements else None
    )
    pip = PipCommand()
    pip.install(args.package, deps)


if __name__ == '__main__':
    main()
