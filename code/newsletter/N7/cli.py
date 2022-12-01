import argparse
import pathlib

import jinja2

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "templates/project"

env = jinja2.Environment(
    trim_blocks=True,
    loader=jinja2.FileSystemLoader(TEMPLATE),
)


def setup_cli():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    startapp = subparser.add_parser("startapp")
    startapp.add_argument(
        "name",
        type=str,
        help="the app name",
    )
    return parser


def build_layout(name: str):
    app_dir = ROOT.joinpath(f"{name}")
    if app_dir.exists():
        print(f"{name} directory has exists!")
        return
    else:
        app_dir.mkdir()

    for base in TEMPLATE.iterdir():
        basename = base.stem
        fpath = app_dir.joinpath(f"{basename}")
        if basename == "__init__.py":
            fpath.write_text("")
            continue

        with open(fpath, mode="w+", encoding="utf-8") as f:
            content = env.get_template(base.name).render(app_name=name)
            f.write(content)


def main():
    parser = setup_cli()
    args = parser.parse_args()
    print(args)
    build_layout(name=args.name)


if __name__ == '__main__':
    main()
