#!/usr/bin/python3
#Calculator program
#Programmer: Hein Min Htet
# Date:14072022
while 1:
    first_no = float(input("Please enter first number"))
    operator = input("please Enter operator:   ")
    second_no = float(input("Please enter second number"))
    if operator == "+":
        result= first_no + second_no
    elif operator == "-":
        result= first_no - second_no
    elif operator == "*":
        result= first_no * second_no
    elif operator == "/":
        result= first_no / second_no
    elif operator == "%":
        result= first_no % second_no
    else:
        print("Wrong Operator")
    print("Result is:", result)

