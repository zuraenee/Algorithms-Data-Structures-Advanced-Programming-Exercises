class person(object):
    def __init__(self):
        self.name = "John"
        self.age = 36

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):
        return "Name: " + self.name + " Age: " + str(self.age)

p1 = person("zee", 20)
p2 = person("bob", 30)
print(p1.getName())
print(p2.getAge())
print(p1)
print(p2)
