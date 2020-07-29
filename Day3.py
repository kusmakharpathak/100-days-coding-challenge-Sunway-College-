"""
 Author :   Kusmakhar Pathak
 Created:   29 July 2020
 (c) Copyright by Kusmakhar Pathak.
 """

# Input and it's Type

# String Input
name = input("Enter your name:\t")
print(f"{name}\n")
# type
print(f"Data Type:\t{type(name)}\n")

#integer input
int_num = int(input("Enter intger number:\t"))
print(f"{int_num}\n")
# type
print(f"Data Type:\t{type(int_num)}\n")

#float input
float_num = float(input("Enter decimal number:\t"))
print(f"{float_num}\n")
# type
print(f"Data Type:\t{type(float_num)}\n")

# List input
list_in = [int(input(f"Enetr number {i+1}:\t")) for i in range(4)]
print(f"{list_in}\n")
# Type
print(f"Data Type:\t{type(list_in)}\n")


