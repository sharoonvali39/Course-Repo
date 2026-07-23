##Lists
#Lists can store multiple values

x = [1,2,3]
print(type(x))
print(x)

#Lists are also indexed as strings are indexed

x = ['red','blue','white']
print(type(x))

#Lists can have any datatype within them 

x = [1,'red', ['blue','white'],True]
print(type(x))

#Lists are also really good because we can add or delete items within it

x = ['red','blue','white']
x.append('green')
print(x)
x[0] = 'yellow'
print(x)

#Nested List
x = [1,'red', ['blue','white'],True]
print(x[0])
print(x[2])
print(x[2][1])