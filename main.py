class Person:
    def __init__(self, name, fam):
        self.name = name
        self.fam = fam
    def say_hi(self):
        print("Hello")

class Pupil(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

p = Pupil("P", "P")
s = Student("S", "S")
p.say_hi()
s.say_hi()

# shu holatga 5 ta misol



