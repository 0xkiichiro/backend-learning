import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-"*25)

# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122, "0xkiichiro", [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]

# print_types(test)

# class names start with capital letter
class Person:
    name = "0xkiichiro"
    birth_year = 1995

# to create a object from this class
person1 = Person()
person2 = Person()

print(person1)

Person.job = "developer"

print(person2)

print("-"*25)