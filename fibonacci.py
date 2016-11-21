#!/usr/bin/python3

# Fibonacci algorithm.
# auther : Ahmad Abdollahzade (ahmadabd13741112@gmail.com)

class fibonacci(object):
    def __init__(self,a,b):
        self.a, self.b = a, b

    def series(self):
        while True:
            yield (self.b)
            self.a, self.b = self.b, self.a + self.b

choice = input("Enter a number : ")
f = fibonacci(0,1)
for i in f.series():
    if i > choice:
        break
    print (i)
