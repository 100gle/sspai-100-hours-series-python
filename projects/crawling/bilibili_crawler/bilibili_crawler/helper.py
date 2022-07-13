import re
from datetime import datetime

pats = dict(
    rank=re.compile(r"(\d+)"),
    length=re.compile(r"(?P<minute>\d{2}):(?P<second>\d{2})"),
)


def parse_rank(value):
    matched = pats["rank"].search(value.strip())
    if matched:
        number = matched.group()
        return int(number)
    return 0


def parse_ops(value):

    if not value:
        return 0

    value = value.strip()

    if "万" in value:
        digits = float(value.replace("万", "")) * 10000
        return int(digits)
    else:
        return int(value)


def parse_length(value):
    length = value.strip()
    pat = pats["length"]
    matched = pat.search(length).groupdict()
    if matched:
        minute = int(matched["minute"])
        second = int(matched["second"])

        total = minute * 60 + second
    else:
        total = 0

    return total


def parse_timestamp(value):
    timestamp = int(value)
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
