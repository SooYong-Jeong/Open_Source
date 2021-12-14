class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printInfo(self):
        print("이름 : {}, 나이 : {}".format(self.name, self.age))
        
    def getInfo(self):
        return self.name + ', ' + str(self.age)
    
class Student(Person):
    def __init__(self, name, age, department, id):
        super().__init__(name, age)
        self.department = department
        self.id = id
        
    def printStudentInfo(self):
        name_age = super().getInfo()
        print(name_age)
        print("{}님의 학과 : {}, 학번 : {}".format(self.name, self.department, self.id))

x = Student("정수용", 24, "정보통신SW공학과", "17110205")
x.printInfo()
x.printStudentInfo()