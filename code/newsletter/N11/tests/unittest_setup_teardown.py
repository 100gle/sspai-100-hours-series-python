import unittest


def setUpModule():
    print("[module level]: setup")


def tearDownModule():
    print("[module level]: teardown")


class TestFoo(unittest.TestCase):
    def setUp(self) -> None:
        print("\t\t[function level]: setup")

    def tearDown(self) -> None:
        print("\t\t[function level]: teardown")

    @classmethod
    def setUpClass(cls):
        print("\t[class level]: setup")

    @classmethod
    def tearDownClass(cls):
        print("\t[class level]: teardown")

    def test_case1(self):
        print("\t\t\t--> test case 1 here")
        self.assertEqual(1, 1)

    def test_case2(self):
        print("\t\t\t--> test case 2 here")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
