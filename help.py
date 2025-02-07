class Swim:
    def swim(self):
        print("Men suzaman")

class English:
    def speak(self):
        print("Ingliz tilida gapiraman")

class Math:
    def  solve(self):
        print("Misollarni ishlayman")


class Student(English, Math, Swim):
    pass

s = Student()
s.solve()
s.speak()
s.swim()
