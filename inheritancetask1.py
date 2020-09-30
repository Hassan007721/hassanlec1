# create two class name of first class is parent and name of second class is child

class parent:     #  Muhammad Raazq
    fatherName = ""
    age  = ""
    def introduce(self):
        print("my fatherName is :" + self.name)
        print("my age is :" + str(self.age) + " years")

        print("__________________________")
class child():  # Hassan Razzaq (Muhammad Razzaq)
    childName = ""
    childAge = ""


    p1 = parent()
    p1.name = "muhammad razzaq"
    p1.name = "shazia"

    c1 = child()
    c1.name = "ali"
    c1.age = 25

    c2 = child()
    c2.name = "hassan"
    c2.age = 21

    p1.introduce()

    c1.introduce()
    c2.introduce()