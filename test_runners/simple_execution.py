#This file contains some classes and functions 
#which will be tested by the test_sample.py file 
#using pytest
def cuber(num :int):
    return num * num * num

def incrementor(num :int, diff: int):
    x = 0
    while True:
        x = x + diff
        num = num - 1
        if num == 0:
            break
    return x

#print(incrementor(15, 30))
#print(incrementor(25, 86))

class Smartphone():
    def __init__(self,charge=57,brightness=100):
        self.charge = charge
        self.brightness = brightness

    def use_wifi(self, hour):
        self.charge = self.charge - self.charge * hour * 0.1
        if self.charge < 1:
            raise Exception("Smartphone is going down!!!")
       
    def brightpower(self):
        if self.charge > 35:
            self.brightness = 100

        else:
            self.brightness = 10

pointer = Smartphone(78,90)

pointer.use_wifi(5)
pointer.brightpower()
print(pointer.charge)
print(pointer.brightness)

