from model.Employee import Employee
class DbExtractor:
    def extract(self, dbFactory):
        cnx = dbFactory.getConnection()
        cursor = cnx.cursor()

        query = ("SELECT id, name, dept, salary from employee")

        cursor.execute(query)

        employees = []
        for(id,name, dept, salary) in cursor:
            emp = Employee(id, name, dept, salary)
            employees.append(emp)

        cursor.close()
        return employees