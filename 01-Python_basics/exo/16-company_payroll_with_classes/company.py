from employee import Employee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees_name(self):
        for employee in self.employees:
            print(employee.lname, employee.fname, employee.salary)
        print('----------------------------------')
    
    def pay_employee(self):
        print('Paying Employees:')
        for employee in self.employees:
            print('Paycheck for:', employee.fname, employee.lname)
            print(f'Amount: ${employee.calculate_paycheck():,.2f}')
            print('----------------------------------')


def main():
    my_company = Company()
    employee1 = Employee('Sarah', 'Hess', 50000)
    employee2 = Employee('Toto', 'Acc', 30000)
    employee3 = Employee('Tata', 'Icc', 20000)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    my_company.display_employees_name()
    my_company.pay_employee()

main()