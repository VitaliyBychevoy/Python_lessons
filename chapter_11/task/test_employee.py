import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = "Tom"
        last_name = "Green"
        junior_salary = 450
        self.rise_salary = 300
        self.empl = Employee(first_name, last_name, junior_salary)

    def test_give_default_rise(self):
        """Проверяем стадартную надбавку"""
        salary = self.empl.annual_salary + 5000
        self.empl.give_raise()
        self.assertEqual(salary, self.empl.annual_salary)

    def test_give_custom_raise(self):
        salary_1 = self.empl.annual_salary + self.rise_salary
        self.empl.give_raise(self.rise_salary)
        self.assertEqual(salary_1, self.empl.annual_salary)

if __name__ == "__main__":
    unittest.main()