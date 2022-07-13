class Person:
    def __init__(self, name, lastname, age, sex):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def __str__(self):
        return "%s %s (wiek: %d, %s)" % (self.name, self.lastname, self.age, self.sex)

class Student(Person):
    def __init__(self, name, lastname, age, sex, grades):
        super().__init__(name, lastname, age, sex)
        self.grades = grades

    def avg(self):
        sum = 0
        for i in self.grades:
            sum += i
        return round((sum / len(self.grades)), 2)

    def __str__(self):
        s = super().__str__()
        avg = self.avg()
        return s + ", " + ("niezły" if avg >= 4 else "słaby") + " ze mnie studen, średnia: " + str(avg)

class Employee(Person):
    def __init__(self, name, lastname, age, sex, salary):
        super().__init__(name, lastname, age, sex)
        self.salary = salary

    def __str__(self):
        s = super().__str__()
        return s + ", zarabiam: " + str(self.salary)

