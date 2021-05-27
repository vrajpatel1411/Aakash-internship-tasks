''' Day 2 basic task Date:-26-5-2021'''

print("Hello world")

' Single comment'

'''Multi line 
comment'''

' Their is no required of data type delaration'
n1 = 'vraj'
n2 = 10
n3 = 10.5

print(n1)
print(n2)
print(n3)

n1 = n2 = n3 = 10

print(n1)
print(n2)
print(n3)

'type() return the data type of variable'

print(type(n3))

a = 1 + 10j

'isinstance() function returns True if the specified object is of the specified type, otherwise False'

print(isinstance(a, complex))

'String in python are surronded by either single quotation marks or double quotation marks'

name = "Vraj Patel"

print(name)

print(name[0])

print(name[2:5])

print(name[2:])

print(name[:6])

print(name[-1])

print(name + ' hello')

print(name, "hello world")

print(name * 2)

'List is similar to array but it contains different type of data type inside single list and list is mutable'
list1 = [10, 10.5, "Vraj patel"]

print(type(list1))

print(list1[0:2])

print(list1[2])

list1[2] = "Vraj"

list1.append("hello world")

print(list1)

'tuple is similar to list but only difference is tuple is immutable'

tuple1 = (10, 20, 30, "Akash", 40, 50, "technologies", 60)

'tuple1[1]=20.5'

print(tuple1)

'dict is used to store data valuse in key:value pairs'

dict1 = {1: 'Akash', 2: 'Technolabs', 'Key': 10}
print(dict1)
print(dict1[1])
print(dict1[2])
print(dict1['Key'])

dict1[3] = 12
print(dict1)
