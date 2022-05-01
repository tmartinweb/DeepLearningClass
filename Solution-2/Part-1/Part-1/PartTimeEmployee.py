from Employee import Employee


class PartTimeEmployee(Employee):

    def __init__(self, eid, name, dept, salary, balance=0.0, is_employed=True):
        Employee.__init__(self, eid, name, dept, salary, balance, is_employed)
