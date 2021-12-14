class MyClass:
    number = 100
    def inc_10(self):
        self.number += 10
        
    def inc_20(self):
        self.number += 20
        
obj1 = MyClass()
obj1.inc_10()
print(obj1.number)

obj2= MyClass()
obj2.inc_20()
print(obj2.number)