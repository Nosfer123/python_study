from datetime import datetime


class Student:

    def __init__(self, input_name, birth_year):
        self.name = input_name
        self.birth_year = birth_year

    @property
    def get_age(self):
        cur_year = datetime.now().year
        return cur_year - self.birth_year

    def __str__(self):
        return "Student: {0}. Age: {1}".format(self.name, self.get_age)


stud1 = Student("John", 1992)
stud2 = Student("Tom", 1975)

print(stud1)
print(stud1)

print(stud1.get_age)
print(stud2.get_age)
