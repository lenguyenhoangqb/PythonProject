from abc import ABCMeta, abstractstaticmethod, abstractmethod


class IPerson(metaclass=ABCMeta):
    # @abstractstaticmethod
    # def person_method():
    #     """Interface method"""

    @abstractmethod
    def person_method(self):
        """Interface method"""

    def get_person_name(self):
        print(self.name)


class Student(IPerson):
    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")

    def get_person_name(self):
        print(f"I am {self.name}")


p1 = Student()
p1.person_method()
p1.get_person_name()

p2 = Teacher()
p2.person_method()
p2.get_person_name()