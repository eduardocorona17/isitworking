# Fix this test case
# FIXED!!!

from Employee import Employee
import unittest

class TestEmployeeClass(unittest.TestCase):
        def setUp(self):
              self.employee1 = Employee('E', 'C', 1000)

        def test_give_default_raise(self):
              self.employee1.give_raise()
              self.assertEqual(self.employee1.salary, 6000)

        def test_custom_raise(self):
              self.employee1.give_raise(6000)
              self.assertEqual(self.employee1.salary, 7000)
            

if __name__ == '__main__':
    unittest.main()