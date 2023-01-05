import pytest


def setup_module():
    print("[module level]: setup")


def teardown_module():
    print("[module level]: teardown")


class TestFoo:
    def setup(self, method) -> None:
        print("\t\t[function level]: setup")

    def teardown(self, method) -> None:
        print("\t\t[function level]: teardown")

    @classmethod
    def setup_class(cls):
        print("\t[class level]: setup")

    @classmethod
    def teardown_class(cls):
        print("\t[class level]: teardown")

    def test_case1(self):
        print("\t\t\t--> test case 1 here")
        assert True

    def test_case2(self):
        print("\t\t\t--> test case 2 here")
        assert True


if __name__ == '__main__':
    pytest.main([__file__, "-s", "--no-header"])
