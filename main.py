class User:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)


harsh = User()

try:
    harsh = User()
except Exception as e:
    print(e)
else:
    print("No exception occured")
def count(start, step):
    while True:
        yield start
        start += step

