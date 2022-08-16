# name = "my name is \" baris \
#     baris"
# print(name)

# first_name = "baris"
# last_name = "aytimur"
# full_name = first_name + " " + last_name
# print(full_name)

list1 = ["a", "b", "c"]
# print(list1)
# list1.append("d")
# print(list1)
# popped_val = list1.pop()  #removes & return last element
# print(popped_val) 
# print(list1)

# list2 = ["Apple", 1, 3.5, True, [1, 3], {"Ready": "yes"}]
# list1.extend(list2)
# print(list1)

# list2_reversed=list2.reverse()
# print(reversed_list2) #returns None
# print(list2.reverse()) #returns None

# list2.reverse()
# print(list2) #returns list reversed

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = thisdict.keys()
# print(x)

# def personel_bilgileri(**Clarusway):
#   print("-"*30)
#   for key,value in Clarusway.items():
#     print("{:<10}: {}".format(key, value))
  
#   print("-"*30)
# personel_bilgileri(Ad="Henry",Soyad="FRSTR",Tel="040504054",Şehir="NewYork")
# personel_bilgileri(Ad="David",Soyad="MOSSES",Tel="3040504054",Şehir="AYDIN")

# def my_function(*args, **kwargs):
#     print( "youngest child is " + kwargs["child1"] + " and " + args[1] + " years old.")

# my_function("1", "2", "3", child1="Hans", child2="Laura")

# def my_function(country = "Norway"):
#   return "I am from " + country

# my_function("Sweden")
# my_function()

def make_posh(func):
    def wrapper():
        print('+---------+')
        print('|         |')
        result = func()
        print(result)
        print('|         |')
        print('+=========+')
        return result
    return wrapper

@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '