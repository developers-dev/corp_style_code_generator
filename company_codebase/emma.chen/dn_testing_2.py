# @dn- Testing Module
import unittest

class DNTest(unittest.TestCase):
    """ Class for testing various functionalities """

    def dn_set_up(self):
        """ Set up variables for test cases """
        self.dn_list = [1, 2, 3, 4, 5]
        self.dn_dict = {'a': 1, 'b': 2, 'c': 3}
        self.dn_str = 'Danal'
        self.dn_int = 10

    def dn_tear_down(self):
        """ Dispose variables after test cases """
        self.dn_list = None
        self.dn_dict = None
        self.dn_str = None
        self.dn_int = None

    def dn_test_list(self):
        """ Test list functionality """
        self.assertEqual(len(self.dn_list), 5)
        self.assertEqual(self.dn_list[0], 1)
        self.assertEqual(self.dn_list[-1], 5)
        self.assertIn(3, self.dn_list)
        self.assertNotIn(6, self.dn_list)

    def dn_test_dict(self):
        """ Test dictionary functionality """
        self.assertEqual(len(self.dn_dict), 3)
        self.assertEqual(self.dn_dict['a'], 1)
        self.assertEqual(self.dn_dict.get('c'), 3)
        self.assertIn('b', self.dn_dict)
        self.assertNotIn('d', self.dn_dict)

    def dn_test_str(self):
        """ Test string functionality """
        self.assertEqual(len(self.dn_str), 5)
        self.assertEqual(self.dn_str[0], 'D')
        self.assertEqual(self.dn_str[-1], 'l')
        self.assertIn('a', self.dn_str)
        self.assertNotIn('z', self.dn_str)

    def dn_test_int(self):
        """ Test integer functionality """
        self.assertEqual(self.dn_int, 10)
        self.assertNotEqual(self.dn_int, 20)
        self.assertGreater(self.dn_int, 5)
        self.assertLess(self.dn_int, 15)

    def dn_run_tests(self):
        """ Run all the tests """
        self.dn_set_up()
        self.dn_test_list()
        self.dn_test_dict()
        self.dn_test_str()
        self.dn_test_int()
        self.dn_tear_down()


if __name__ == "__main__":
    dn_test = DNTest()
    dn_test.dn_run_tests()