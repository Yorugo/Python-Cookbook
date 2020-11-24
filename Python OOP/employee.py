import datetime


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f"{first}.{last}@company.com"
        Employee.num_of_emps += 1  # everytime an employee gets instantiated, the num_of_emps increases.

    def fullname(self):
        return f"{self.first} {self.last}"

    # Adding the property decorator made this function into a getter.
    # This allows us to update email without everyone needing to change their code
    # Since with functions you need to add parentheses at the end.
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def name(self):
        return f"{self.first} {self.last}"

    # To create a setter, you need a getter
    @name.setter
    def name(self, fullname):
        self.first, self.last = fullname.split(" ")

    @name.deleter
    def name(self):
        self.first = None
        self.last = None
        print("Name Deleted!")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Alternative constructor"""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        """Official string representation of an object.
        Meant to be seen by other developers"""
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        """Informal string representation of an object.
        Meant to be readable for an end user"""
        return f"{self.fullname()} - {self.email}"


# Creating instances of the class, we can see number of employees increasing
print(Employee.num_of_emps)
emp_1 = Employee("Alice", "One", 20000)
emp_2 = Employee("Bob", "Two", 18000)
print(Employee.num_of_emps)
print(emp_1.email)


def test0():
    """Outputs a dictionary of informations"""
    print(emp_1.__dict__)
    print(Employee.__dict__)


def test1():
    """These two do the same thing"""
    print(emp_1.fullname())
    print(Employee.fullname(emp_1))


def test2():
    """Changing the raise amount of the whole class and of one instance have different effects"""
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print()

    Employee.raise_amount = 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print()

    emp_1.raise_amount = 1.06
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print()

    Employee.raise_amount = 1.11
    print(Employee.raise_amount)
    print(emp_1.raise_amount)  # still remains 1.06.
    print(emp_2.raise_amount)


def test3():
    """Using class method"""
    Employee.set_raise_amt(1.05)  # Same thing as saying: Employee.raise_amount = 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)


def test4():
    """Creating employee instances through strings"""
    emp_str_3 = "Kobie-Vega-23000"
    emp_3 = Employee(*emp_str_3.split("-"))
    print(emp_3.first)

    # if creating employees with strings is common, we can create an alternative constructor using a classmethod
    emp_str_4 = "Tai-Butler-16000"
    emp_4 = Employee.from_string(emp_str_4)
    print(emp_4.first)


def test5():
    my_date = datetime.date(2020, 11, 22)
    print(Employee.is_workday(my_date))


def test6():
    print(repr(emp_1))
    print(str(emp_1))


def test7():
    """dunder __add__ is equivalent to +"""
    print(int.__add__(10, 2))
    print(10 + 2)


def test8():
    emp_1.name = "Peter Three"
    print(emp_1.name)
    del emp_1.name
    print(emp_1.name)


test8()
