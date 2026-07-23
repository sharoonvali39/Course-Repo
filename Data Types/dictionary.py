##Dictionaries
# Dictionaries have something called a Key/Value pair

x = {'name':'Sharoonvali', 'gender': 'male', 'favorite games': ['cricket','football']}
print(type(x))
print(x)

print(x.values())
print(x.keys())
print(x.items())

#you cannot call a dictionary by an index you can call it by keys
#print(x[0])
print(x['name'])

#you can also change stuff in dictionaries
x['name'] = 'Sharoon'
print(x)

#you can also use functions like update which updates the whole dictionary
#this doesnt delete the already existing key value pairs
x.update({'name': 'sharoonvali','gender':'male', 'hair colour':'Black'})
print(x)

#you can also delete stuff from dictionary using del keyword
del x['hair colour']
print(x)