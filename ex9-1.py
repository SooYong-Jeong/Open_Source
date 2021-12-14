class Claculator:
    def set(self, x, y):
        self.first = x
        self.second = y
        
    def add(self):
        result = self.first + self.second
        return result
    
cal1 = Claculator()
cal1.set(10, 20)
print("{} + {} = {}".format(cal1.first, cal1.second, cal1.add()))
cal1.set(100, 200)
print("{} + {} = {}".format(cal1.first, cal1.second, cal1.add()))