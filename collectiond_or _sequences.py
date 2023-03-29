#list: ordered collectons of values that can be changed or modified. list are created using square brackets([])
fruits = ["apple","banana","orange"]#fruits is a list of stings

fruits.append("grape")# add "grape" to the end of the list

fruits[0] = "pear" # change the first element of the list to "pear"

#Dictionaries: unorder collections of key-values pairs that can be changed or modified dictionaries are created using curly braces({})
person = {"name":"aksh","age": 17,"gender":"male"}#Person is dictionary
person["name"] = "Akshar"# change the value associated whith the key "name" to "Akshar"
person["height"] = 170#add a new key-value pair to the dictionary

#Tuple: ordered collections of values that cannot be changed or modified,tuples are created using parenrheses(()) or just commas(,)
point = (10,20)#point is a tuple of two integers
point = point + (30,)#add another element to the tuple (note the camma after the single element)
#point[0] = 5#this will cause an error because tuples cannot be modified
print(point)