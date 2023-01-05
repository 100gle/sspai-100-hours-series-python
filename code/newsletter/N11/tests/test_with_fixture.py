def test_sql_with_mock_sqlite_database(sqlite):
    ok = sqlite.execute("SELECT 1;")
    assert ok


def test_sql_with_mock_mysql_database(mysql):
    ok = mysql.execute("SELECT * FROM mock_table;")
    assert ok


def test_gender_fixture(gender):
    print(f"Gender fixture value: {gender}")
    assert ["male", "female"] == gender


class TestClassScopeFixture:
    def test_foo(self, logger):
        assert True

    def test_bar(self, logger):
        assert True


class TestClassScopeFixture2:
    def test_foo2(self, logger):
        assert True

    def test_bar2(self, logger):
        assert True


def test_with_mock_database(database):
    sql = "SELECT * FROM mock_table;"
    ok = database.execute(sql)
    assert ok


def test_with_request_fixture(request):
    from pprint import pformat

    props = [prop for prop in dir(request) if not prop.startswith("_")]

    print(f"request properties:\n{pformat(props)}")
    assert True


def test_with_capsys_fixture(capsys):
    def greet(name: str = ""):
        msg = name or "World"
        print(f"Hello, {msg}")

    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World\n"

    greet("100gle")
    captured = capsys.readouterr()
    assert captured.out == "Hello, 100gle\n"


def test_with_tmp_path_fixture(tmp_path):
    import pathlib

    p = tmp_path.joinpath("foo")
    print(f"\n{p}")

    assert isinstance(p, pathlib.Path)
    assert p.stem == "foo"
