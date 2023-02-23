class Student:
    def __init__(self, name, ID, age, mark):
        self.name = name
        self.ID = ID
        self.age = 0
        self.mark = 0

    def Display(self):
        print("Name: ", self.name)
        print("ID: ", self.ID)
        print("Age: ", self.age)
        print("Mark : ", self.mark)

    def setAge(self, age):
        self.age = age

    def setMark(self, mark):
        self.mark = mark

student1 = Student("Reza", 123,20,100)
student1.Display()
