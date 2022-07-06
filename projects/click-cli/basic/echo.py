import argparse


def echo(name=None):
    print(f"Hello, {name}!")


def main():
    parser = argparse.ArgumentParser(
        description="the argparse usage example",
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="name",
        help="the name pass to echo",
        default="World",
    )
    args = parser.parse_args()

    echo(name=args.name)


if __name__ == '__main__':
    main()
