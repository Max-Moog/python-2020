import unittest


class First_test(unittest.TestCase):
    def test_gleich(self):
        self.assertEqual(1, 1)

    def test_not_gleich(self):
        self.assertNotEqual(1, 2)

if __name__ == '__main__':
    unittest.main()

