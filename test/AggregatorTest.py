import unittest
from aggregator.Aggregator import Aggregator
from model.Employee import Employee

class MyTestCase(unittest.TestCase):
    def test_aggregate(self):
        employees = []
        employees.append(Employee(1,"Arun","swe", 1000))
        employees.append(Employee(2, "Chung", "swe", 100000))

        empAgg = Aggregator().aggregate(employees)
        self.assertEqual(empAgg.aggregateType, "AVG_SALARY")
        self.assertEqual(empAgg.aggregateValue, 50500)

if __name__ == '__main__':
    unittest.main()
