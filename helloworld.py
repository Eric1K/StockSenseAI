#asdiofjaoisjdfoas
import pandas as pd

startdate = "2021-7-30"
enddate = pd.to_datetime(startdate) + pd.DateOffset(days=5)
enddate = enddate.date()
print(enddate)
"""asdasd
asdasd
asdasd"""

"""
a = "Hello World"
print(a)

#list
b = ['yo1', 'yo2']
print(b)
print(b[0])

#dictionary
cdictionary = {"favcolor":"blue", "leastfav":"red"}
print(cdictionary["favcolor"])

d={1,2,3,4,5,5,5,5,6,6,6}
print(d)

poop = 1
if poop ==1:
    print("not cappa")
else:
    print("cappa")

for i in range(0,10):
    poop += i
    print(poop)

try:
    print(b[2])
except IndexError:
    print("ur badd")

#classes
class Person:
    def __init__(self, name):
        print("New Person")
        self.name=name
    def printname(self):
        print("Hi, my name is: " + self.name)



p1 = Person("Bob")
p1.printname()

"""