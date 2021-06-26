import unittest

class TEstMycase(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_1(self):
        print("do test1")

    @unittest.skip
    def test_2(self):
        print("do test 2")

    def test_3(self):
        print("do test 3")

if __name__ == '__main__':
    unittest.main()