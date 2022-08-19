import re
import unittest

FLAGS = re.X | re.S
REGEXP = r"""
(?P<date>\d{4}(-\d{2}){2})  # date format like: YYYY-MM-DD
    \s
(?P<time>\d{2}(:\d{2}){2})  # time format like: HH:MM:SS
    [\s-]+
(?P<project>[^\s-]+)        # project name
    [\s-]+
(?P<filename>.*)            # filename
"""
pat = re.compile(REGEXP, FLAGS)

files = """
2021-10-10 20:20:20-其他 - 数据.csv
2021-10-21 12:23:41-写作 - 少数派稿子.md
2020-01-13 13:45:15-测试 - 测试案例.py
2019-08-09 10:21:39-日记 -20190809 日记.md
2017-12-12 12:12:12-工作 - 公司合同.docx
"""
files = files.strip().split("\n")


def rename(file):
    matched = pat.search(file).groupdict()
    date = matched["date"].replace("-", "")
    project = matched["project"].replace(" ", "_")
    filename = matched["filename"].replace(" ", "_")
    return "_".join([date, project, filename])


class TestRename(unittest.TestCase):

    cases = [
        ("2021-10-10 20:20:20-其他 - 数据.csv", "20211010_其他_数据.csv"),
        ("2021-10-21 12:23:41-写作 - 少数派稿子.md", "20211021_写作_少数派稿子.md"),
        ("2020-01-13 13:45:15-测试 - 测试案例.py", "20200113_测试_测试案例.py"),
        ("2019-08-09 10:21:39-日记 -20190809 日记.md", "20190809_日记_20190809_日记.md"),
        ("2017-12-12 12:12:12-工作 - 公司合同.docx", "20171212_工作_公司合同.docx"),
    ]

    def test_rename(self):
        for (raw, expected) in self.cases:
            file = rename(raw)
            self.assertEquals(file, expected)


if __name__ == '__main__':
    unittest.main()
