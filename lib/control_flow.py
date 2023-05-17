#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == 12345:
        print("access garnted")
    else:
        print("access denied")
admin_login("admin", 12345)
        

def hows_the_weather(temperature):
    if temperature < 40:
        print("It's brisk out there!")
    elif temperature > 40 and temperature < 65:
        print("a little chilly")
    elif temperature < 85:
        print("It's too dang hot out there!")
    else:
        print("it's perfect out here")
hows_the_weather(90)

def fizzbuzz(num):
    if num %3 == 0:
        print ("Fizz")
    elif num %5 == 0:
        print ("Buzz")  
    elif num %3 == 0 and num %5 == 0:
        print("Fizz Buzz")
    else:
        print(num)
fizzbuzz(3)


num1= float(input(" Enter number 1: "))
num2= float(input(" Enter number 2: "))

def calculator(operation, num1, num2):
    print ("1:addition")
    print ("2:subtraction")
    print ("3:multiplication")
    print ("4:division")
    operation = int(input("enter your choice: "))
    
    
    if operation ==1:
        print(num1 + num2)
    elif operation ==2:
        print(num1 - num2)
    elif operation ==3:
        print(num1 * num2)
    elif operation == 4:
        print(num1 / num2)
    
    
calculator()

