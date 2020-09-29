# Inheritance -------> it is one of the main parts of object oriented programming
# ----> How do we implement or code or create inheritance in python
# ---> What are the benefits of using inheritance
#                 types of inheritance
#                (1) simple/single inheritance
#                (2) multiple inheritance
#                (3) multiplevel inheritance


class person:     #  Muhammad Raazq
    name = ""
    age = ""
    def introduce(self):
        print("my name is :" + self.name)
        print("my age is : "+ str(self.age) + "years"
        print("__________________________")
class student(person):  # Hassan Razzaq (Muhammad Razzaq)
    name = ""
    age = ""

p1 = person()
p1.name = "sir qasim"
p1.age = 25

p2 = person()
p2.name = "hassaam"
p2.age = 20

s1 = student()
s1.name = "sir qasim"
s1.age = 25

s2 = student()
s2.name = "hassan"
s2.age = 20

p1.introduce()
po2.introduce()

s1.introduce()
s2.introduce()
