class Counter: 
    def __init__(self, start: int = 0) -> None:
        self.value = start

    def increment(self) -> None:
        self.value += 1

    def current(self) -> int:
        return self.value
    
    def increment_2(self) -> None:
        self.value += 2


c = Counter(start = 5) #instantiation of the class or creating an object from the class (blueprint - concept)

c.increment()

c.increment()

c.increment() #calling the method on the object (instance of the class) to perform

print(f"{c.current()}")

c1 = Counter(start = 10)
c1.increment_2()

print(f"{c1.current()}")


#day 2
class Employee:
    def __init__(self, name: str, base_salary: float) -> None:
        self.name = name
        self.base_salary = base_salary

    def calculate_bonus(self, performance_multiplier: float) -> float:
        return self.base_salary * performance_multiplier

emp = Employee(name="Alice", base_salary=50000.0)

bonus = emp.calculate_bonus(1.1)

print(f"The bonus for {emp.name} is {bonus}")
