#!/usr/bin/env python3

import pathlib

CURRENT_DIR = pathlib.Path(__file__).parent
ARCHIVE_DIR = CURRENT_DIR.joinpath("archive")
IGNORES = {
    ".idea/**",
    "*.xml",
    "*.iml",
    ".vscode/*",
    ".vscode/**/*",
    "backup/*",
    "backup/**/*",
    __file__,
}


def filter_ignores(files):
    keep = []

    for file in files:
        matched = any(
            [file.match(ignore) or file.name.startswith(".") for ignore in IGNORES]
        )
        if not matched:
            keep.append(file)
        else:
            print(f"[WARNING] ignore file: {file}")

    return keep


def seek_files(path, recursive=False, ignore=True):
    files = []

    for file in path.iterdir():
        if file.is_file():
            files.append(file)
        elif recursive and file.is_dir():
            files.extend(seek_files(file, recursive))

    if ignore:
        files = filter_ignores(files)

    return files


def extract_suffixes(files):
    suffixes = set()
    for file in files:
        suffix = file.suffix
        if not suffix:
            continue

        suffix = suffix.replace(".", "")
        suffixes.add(suffix)

    return suffixes


def groupby(files, suffixes):
    group = {}
    for file in files:
        suffix = file.suffix.replace(".", "")
        if suffix in suffixes:
            group.setdefault(suffix, []).append(file)
        else:
            continue

    return group


def classify(files, verbose=False):
    suffixes = extract_suffixes(files)
    grouper = groupby(files, suffixes)

    if not grouper.keys():
        return

    for suffix, fs in grouper.items():
        directory = ARCHIVE_DIR.joinpath(suffix)
        directory.mkdir(parents=True, exist_ok=True)
        if verbose:
            print(f"[INFO   ] handle .{suffix} files:")

        for file in fs:
            dest = directory.joinpath(file.name)
            file.rename(dest)
            if verbose:
                print(f"  change {file} -> {dest}")


def main():

    path = CURRENT_DIR / "testdata"
    print(f"Use current directory: {path}")

    files = seek_files(path, recursive=True)
    classify(files, verbose=True)


if __name__ == "__main__":
    main()
