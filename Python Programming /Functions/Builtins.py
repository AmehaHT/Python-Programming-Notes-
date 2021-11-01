import math
import random

# string functions
string = 'Monty Python'
length = len(string)
print("String = ",string,"\tlength = ",length)
rep = string.replace('n','N')
print(rep)
upper = string.upper()
lower = string.lower()
print(upper)
print(lower)

# data functions
character = 'A'
ordchar = ord(character)
char = chr(ordchar)
print("Character = ",char,"\tOrd value = ",ordchar)

# math functions
degrees = 90
radians = math.radians(degrees)
sinvalue = math.sin(radians)
cosvalue = math.cos(radians)
print("Degrees = ",degrees,"\tSin = ",sinvalue,"\tCos = ",cosvalue)
print("Cos rounded = ",round(cosvalue,3))

#binary functions
decimal = 123
binarynumber = bin(decimal)
print("Decimal ",decimal,"\tBinary value ",binarynumber)
hexnumber = hex(decimal)
print("Decimal ",decimal,"\tHex value ",hexnumber)

#exponential functions
number = 2.0
exponent = 10.0
powervalue = math.pow(number,exponent)
logvalue = math.log2(powervalue)
print("Number = ",powervalue,"\tlog2 = ",logvalue)

#random numbers
rand = random.randint(0,100)
print("Random value from 0 to 100 = ",rand)
dice = random.randint(1,7)
print("random dice value = ",dice)

#accumulator
sumstring = eval("1+2+3+4+5+6+7+8+9+10")
print("Sum1 = ",sumstring)
sumvalue = sum([1,2,3,4,5,6,7,8,9,10]) #list
print("Sum2 = ",sumvalue)
N = 10
sumcalc = N * (N+1) // 2
print("Sum3 = ",sumcalc)



