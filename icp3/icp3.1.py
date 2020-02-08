class Employee():

    employCount = 0
    Sum=0
    Avg =0

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        Employee.employCount += 1
        Employee.Sum += self.salary

    def displayEmployee(self):
        print("id : ", self.id, ", Name : ", self.name, ", Salary: ", self.salary, ", department: ", self.department)


class FullTimeEmp(Employee):
    def __init__(self, id, name, salary, department):
        Employee.__init__(self, id, name, salary, department)


employ1 = Employee(1, "aneesh", 100000, "cse")
employ2 = Employee(2, "jerry", 8000, "scs")
employ3=FullTimeEmp(3, "cherry", 7000,"It")


print("Total Employees %d" % Employee.employCount)
print("Average salary of the employees is", (Employee.Sum/Employee.employCount))
print(employ1.displayEmployee())
print(employ2.displayEmployee())
print(employ3.displayEmployee())