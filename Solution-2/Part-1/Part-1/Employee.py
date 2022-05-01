class Employee:
    num_of_employees = 0

    def __init__(self, eid, name, dept, salary, balance=0.0, is_employed=True):
        Employee.num_of_employees += 1

        self.eid = eid
        self.name = name
        self.dept = dept
        self.salary = salary
        self.balance = balance
        self.isEmployed = is_employed

    def __str__(self):
        temp = ''
        temp += self.name + ', ' + str(self.eid) + ', ' + self.dept + ':\n'
        temp += 'Current salary: $' + str(self.salary) + '\n' if self.isEmployed \
            else 'Not employed with the company.\n'
        temp += 'Pay earned to date: ${0:.2f}\n'.format(self.balance) + '\n'

        return temp

    def give_raise(self, percent_raise):
        self.salary += self.salary * (percent_raise / 100)

    def pay(self):
        self.balance += self.salary

    def fire(self):
        self.salary = 0
        self.isEmployed = False

    def is_employed(self):
        return self.isEmployed
