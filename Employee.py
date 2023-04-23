class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, annual_bonus=5000):
        self.salary += annual_bonus
    
empl = Employee('E', 'C', 50000)
empl.give_raise(10000)
print(f"{empl.salary}")
