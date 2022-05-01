import os
from Employee import Employee
from FullTimeEmployee import FullTimeEmployee
from PartTimeEmployee import PartTimeEmployee
from WebScraper import WebScraper
from NumpyExample import NumpyExample

input_filename = 'input.txt'
output_filename = 'output.txt'
employees = []


def add_new_employee(eid, name, dept, salary):
    employees.append(Employee(eid, name, dept, salary))


def give_raise(eid, raise_percentage):
    for person in employees:
        if eid == person.eid:
            person.give_raise(raise_percentage)


def pay_employees():
    for person in employees:
        person.pay()


def fire_employee(eid):
    for person in employees:
        if eid == person.eid:
            person.fire()


def average_salary():
    num = 0
    total = 0
    for person in employees:
        num += 1
        total += person.salary
    return total / num


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                execute_command(line.strip())

    except IOError as e:
        print("Error Loading File: " + e)


def execute_command(line):
    line = line.split(' ')
    command = line.pop(0)

    if command == 'NEW':
        eid = int(line[0])
        name = line[1] + ' ' + line[2]
        dept = line[3]
        salary = float(line[4])
        add_new_employee(eid, name, dept, salary)

    elif command == 'RAISE':
        eid = int(line[0])
        percent = float(line[1])
        give_raise(eid, percent)

    elif command == 'PAY':
        pay_employees()

    elif command == 'FIRE':
        fire_employee(int(line[0]))


def output_to_file():
    try:
        if os.path.isfile(output_filename):
            os.remove(output_filename)
        with open(output_filename, 'a') as file:
            for person in employees:
                file.write(str(person))
            file.write('Total number of employees: {}\n'.format(Employee.num_of_employees))
            file.write('Average Salary paid to all employees: ${0:.2f}\n'.format(average_salary()))

    except IOError as e:
        print("Error Outputting to file: " + e + '\n')


def run_inheritance_example():
    employees.clear()
    employees.append(FullTimeEmployee(990, 'Thom Martin', 'CS', 100000))
    employees.append(FullTimeEmployee(991, 'Corwin Koller', 'IT', 50000))
    employees.append(PartTimeEmployee(992, 'Orion Parsons', 'IT', 25000))
    for person in employees:
        print(person)

    for person in employees:
        person.pay()

    temp = employees[2]
    temp.fire()

    for person in employees:
        person.pay()

    for person in employees:
        print(person)


def main():
    # Reading input from file, processing, and outputting to txt
    read_file(input_filename)
    output_to_file()

    # Run Inheritance Example
    run_inheritance_example()

    # Run Web Scraping Example
    WebScraper()

    # Run NumPy Example
    NumpyExample()

    print("Program Complete\n")


if __name__ == '__main__':
    main()
