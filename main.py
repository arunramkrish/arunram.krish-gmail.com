from dao.DbFactory import DbFactory
from dao.BasicDbDemo import  BasicDbDemo
from dao.DbExtractor import DbExtractor

# Get a cursor
dbFactory = DbFactory()
cnx = dbFactory.getConnection()

basicDemo = BasicDbDemo()
currentDate = basicDemo.get_current_time(dbFactory)
print("Current date in OO way: {0}".format(currentDate))

dbExtractor = DbExtractor()
employees = dbExtractor.extract(dbFactory)
for emp in employees:
    print("emp {} {} {} {}".format(emp.id, emp.name, emp.dept, emp.salary))

# Close connection
cnx.close()