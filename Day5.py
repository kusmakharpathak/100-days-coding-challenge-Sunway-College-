"""
Author :   Kusmakhar Pathak
Created:   31 July 2020
(c) Copyright by Kusmakhar Pathak.
"""


# program to build a calculator using class and object
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Addition method
    def Addition(self):
        return f"Sum of {self.num1} and {self.num2} = {self.num1 + self.num2}"

    # Subtraction method
    def Subtraction(self):
        return f"Difference of {self.num1} and {self.num2} = {self.num1 - self.num2}"

    # Multiply method
    def Multiply(self):
        return f"Product of {self.num1} and {self.num2} = {self.num1 * self.num2}"

    # Division method
    def Division(self):
        try:
            return f"Division of {self.num1} and {self.num2} = {self.num1 / self.num2}"
        except Exception:
            raise Exception("Division by 0 is not allowed")

    # Reminder method
    def Reminder(self):
        try:
            return f"Reminder of {self.num1} and {self.num2} = {self.num1 % self.num2}"
        except Exception:
            raise Exception("Division by 0 is not allowed")


# Running Python program checking if __name__ == __main__
if __name__ == "__main__":
    # user input number 1
    num1 = int(input("Enter 1st number:\t"))
    # user input operation +, -, *, /, %
    operation = input("Enter a operation you want to perform (+, _, *, /, %):\t")
    # user input number 2
    num2 = int(input("Enter 2nd number:\t"))
    # creating calculator object
    calculate = Calculator(num1, num2)
    # checking operation
    if operation == '+':
        # calling object methods calculate.Addition()
        print(calculate.Addition())
    elif operation == '-':
        print(calculate.Subtraction())
    elif operation == '*':
        print(calculate.Multiply())
    elif operation == '/':
        print(calculate.Division())
    elif operation == '%':
        print(calculate.Reminder())
    else:
        print(f"Syntax error, could not find {operation} operation")
