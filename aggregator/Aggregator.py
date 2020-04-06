from model.EmployeeAggregate import EmployeeAggregate

class Aggregator:
    def aggregate(self, employees):
        sum = 0;
        count = 0;
        for e in employees:
            sum += e.salary
            count += 1

        avgSalary = sum/count
        empAggregate = EmployeeAggregate("AVG_SALARY", avgSalary)
        return empAggregate