
# import random
# # first code in python
# if 5 > 2:
#     print("true")


# z = 4
# y = "John"


# x = str(z)
# f = float(z)


# abe = aman = kass = 23
# print(aman)
# print(kass)


# # Unpack collection
# fruits = ["apple", "banana", "cherry"]
# fi, se, th = fruits
# # print(th)
# # print(se)
# # print(fi)


# # Global Variables

# x = "awesome"


# def myfunc():
#     global x
#     x = "fantastic"
#     print("python is " + x)


# myfunc()
# # print("python is " + x)


# # Types

# # print(type(1j))
# # print(type(frozenset({"apple", "banana", "cherry"})))
# # print(type(-34.3e4))


# # Random Numbers

# # print(random.randrange(1, 20))


# # python Casting
# b = int(1)   # x will be 1
# h = int(2.8)  # y will be 2
# j = int("3")  # z will be 3

# # print(b, h, j)


# # python String

# a = "Hello , World!"

# # print(a[1])

# # for x in "banana":
# #     print(x)

# text = "The best things in life are free!"

# # if "free" in text:
# #     print("yes, 'free' is present")

# # str = "The things in life are free!"
# # print("in" not in str)


# b = " Hello, Biruk "

# # print(b[6:])

# # print(b[-6:-1])
# # print(b.strip())

# # print(b.replace("Hello", "Comon"))

# print(b.split(","))

# age = 12
# year = 2011
# wealth = 4000
# des = "My name is Biruk and I am {} years and I was born in {}. I have almost net worth of {}$."


# print(des.format(age, year, wealth))

# # lists
# #          - allow duplicate values
# #          - any Datatypes
# #          -

# thelists = ["apple", "banana", "mango", "q"]

# lst = list(("volo", "turbo", "Mbc"))
# # print(len(thelists))
# # print(type(thelists))
# # print(lst)
# thelists.insert(0, "pineapple")
# thelists.extend(lst)

# # thelists.remove('banana')
# # thelists.clear()
# # del thelists[1]

# # for i in range(len(thelists)):
# #     print(thelists[i])

# # i = 0
# # while i < len(thelists):
# #     print(thelists[i])
# #     i  = i + 1


# # [print(x) for x in thelists]


# newList = []

# # for x in thelists:
# #     if "a" in x:
# #         newList.append(x)

# # newList = [x.upper() for x in thelists]
# # newList = [x if x != "banana" else "biruk" for x in thelists]

# nums = [23, 34, 1, 45, 67]
# # nums.sort(reverse=True)
# # thelists.sort()
# # print(nums)

# # def myfunc(n):
# #     return abs(n-100)

# # nums.sort(key=myfunc)
# # print(nums)


# # thelists.sort(key=str.lower)

# # print(thelists)


# # newList = nums.copy()
# # newList  = list(nums)
# # newList = thelists + nums
# print(newList)


# # tuples

# tuples = ("dany", "naty", "yony")

# # print(tuples)
# # print(len(tuples))

# thistuple = tuple(("Shapeof",))


# # print(type(thistuple))

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (*green, yellow, red) = fruits

# # print(green)
# # print(yellow)
# # print(red)
# # print(fruits.index("cherry"))

# thisd = {
#     'phone1': {
#         'name': 'Huawe',
#         'model': '2013A',
#         'year': 2004,
#         'price': '20$'
#     },
#     'phone2': {
#         'name':'Tecno',
#         'model':'22AA',
#         'year': 2013,
#         'price': '60$'
#     }
# }

# # for x in thisd:
# #      print(thisd[x])
# # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# # for x in thisd.keys():
# #     print(x)
# # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# # for x in thisd.values():
# #     print(x)
# # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


# # for keys, values in thisd.items():
# #     print(keys.upper(),": ", values)


# # mydic = dict(thisd)
# # print("this is copied: ", mydic)


# # for s in range(2,12):
# #     print(s)

# # for x in range(6):
# #     print(x)
# # else:
# #     print("Finally finished!")

# # for b in range(6):
# #     if b == 3: break
# #     print(b)
# # else:
# #     print("Finally broken")

# # adj = ["read","big","tasty"]

# # fruits = ["apple", "banana",'cherry']

# # for x in adj:
# #     for y in fruits:
# #         print(x, y)


# # for x in [0,1,2]:
# #     pass


# # def my_function(**kids):
# #     print("His last name is: "+ kids['lname'])

# # my_function(fname="Tabia", lname='Rafas')

# # def Countries(country = "Ethiopia"):
# #     print("I am from "+ country)
# # Countries("Sweden")
# # Countries()

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion Example Results: ")
# tri_recursion(6)

# Lambda is a small anonymous function that can take any number of arguments


import camelcase
import re
def we(a): return a + 23

# print(we(12))


def myfuc(a):
    return lambda b: a*b


mydoubler = myfuc(3)
# print(mydoubler(12))

arr = [["hi", "hel", "seoul", "Go"], ["hi", "hel", "seoul", "Go"],
       ["hi", "hel", "seoul", "Go"], ["hi", "hel", "seoul", "Go"]]

#


# Class


# class MYClass:
#     x = 20

# C1 = MYClass()
# print(C1.x)

# class Person:
#     def __init__(self, name,age):
#       self.name = name
#       self.age = age

#     # def __str__(self):
#     #    return f"{self.name}({self.age})"
#     def myfunc(self):
#        print("Hellow my name is "+ self.name)

# P1 = Person("Biruk",36)

# del P1.age
# print(P1.myfunc())

# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# use person class to creat an object, and then excuate the printname method

# x = Person('Biruk', 'Tafesse')

# x.printname()
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome!, ", self.firstname,self.lastname, " to the class of", self.graduationyear)


# P1 = Student("Biruk", "Tafesse", 2024)

# print(P1.welcome())

# mytuple = ["apple","banana","cherry"]

# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self


#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myClass = MyNumbers()
# myit = iter(myClass)

# for x in myit:
#     print(x)

# myDic = {
#     'brand':'Ford',
#     'model':'Mustang',
#     'year':2023
# }

# print(len(myDic))

# class Car:
#     def __init__(self, brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Drive!")


# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Sail!")


# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Fly! ")


# car1 = Car("Ford","Mustang")     #create A Car class
# boat1 = Boat("Ibiza", "Touring 20")  #create a Boat class
# plane1 = Plane("Boeing","747")     #create a plane class

# for x in (car1, boat1, plane1):
#     x.move()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("Move")

# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")

# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")

# car1 = Car("Ford","Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing","747")


# for x in (car1,boat1,plane1):
#     print(x.brand)
#     print(x.model)

# y = 10

# def change(m):
#   global y
#   y = m
#   print(y)

# change(23)
# print(y)

# from module import person1
# import platform as pf
# md.greeting("BUTA")


# print(a)

# print(pf.system())
# print(dir(pf))
# print(person1['age'])

# python dates ...

# import datetime as dt

# x = dt.datetime.now()

# print(x.strftime("%W"))


# import math as mt
# import json as js
# print(min(23,5,32,12,3))
# print(max(45,5,23,55))
# print(pow(3,2))

# print(mt.sqrt(23.23))
# print(mt.ceil(7.66))
# print(mt.floor(3.643))
# print(mt.pi)

# x =  '{"name":"Kedir", "age":30, "city":"new york"}'

# y = js.loads(x)

# # print(y['age'])

# fileOS = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }


# af = js.dumps(fileOS)

# print(af)


txt = 'The rain in spain'

# x = re.search('^The.*spain$',txt)

# print(x)

# print(re.findall('ai',txt))

# print("The first white-space character is located in position: ",re.search('\s',txt).start())

# print(re.split('\s',txt))  # splits based on the given value

# print(re.sub('\s','9',txt)) # replace the given value

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())
# print(x.string)
# print(x.group())


c = camelcase.CamelCase()

txt = "hello world"

# print(c.hump(txt))

# try:
#     print(weer)
# except NameError:
#     print("Variable weer is not defined")
# except: #else
#     print("An exception occurred")

# finally:
#     print("The 'try except' is finished")
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# num = -1

# if num < 0:
#   raise Exception("Sorry, no numbers below zero")


stroin = input("Write something: ")

if not type(stroin) is int:
  raise TypeError("only integers are allowed")