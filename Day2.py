"""
 Author :   Kusmakhar Pathak
 Created:   28 July 2020
 (c) Copyright by Kusmakhar Pathak.
 """

# Challenge related to string

string_1 = "Day 2 challenge related to String."
string_2 = "Today I am plaining to manuplate the string and how it works"

# print string_1
print(string_1)

# print string_1
print(string_2)

# adding string_1 and string_2
merg_2_string = string_1+string_2
print(merg_2_string)

# picking only day feom string 1
print(string_1[:3])

# picking works from string_2 negative indexing
print(string_1[:3-len(string_1)])

# picking works from string_2
print(string_2[len(string_2)-5:])

# picking works from string_2 negative indexing
print(string_2[-5:])
