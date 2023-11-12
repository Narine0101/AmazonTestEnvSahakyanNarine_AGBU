import unittest


class StructureUnitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Called setUpClass method")

    def setUp(self):
        print("Called setUp method")

    def test_first(self):
        print("Called first test")

    def test_second(self):
        print("Called second test")

    def tearDown(self):
        print("Called tearDown method")

    @classmethod
    def tearDownClass(cls):
        print("Called tearDownClass method")