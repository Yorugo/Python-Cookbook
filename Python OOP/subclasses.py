from employee import Employee


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")


dev_1 = Developer("Alice", "One", 20000, "Python")
dev_2 = Developer("Bob", "Two", 18000, "Java")

print(dev_1.prog_lang)
print(dev_2.first)

mgr_1 = Manager("Kobie", "Vega", 23000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp()
print()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
print()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))  # True
print(isinstance(mgr_1, Employee))  # True
print(isinstance(mgr_1, Developer))  # False
print()

print(issubclass(Manager, Manager))  # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Developer))  # False
