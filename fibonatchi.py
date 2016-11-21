#!/usr/bin/python3

# Fibunacci algorithm.
# auther : Ahmad Abdollahzade (ahmadabd13741112@gmail.com)

class fibunacci(object):
    def __init__(self,a,b):
        self.a, self.b = a, b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b

choice = input("Enter a number : ")
f = fibunacci(0,1)
for i in f.series():
    if i > choice:
        break
    print (i)
