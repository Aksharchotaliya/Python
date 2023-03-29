import array as arr 

numbers = arr.array('i',[10,20,30])

#this len() is used to find length of the array:
print("/n ")
print(len(numbers))

#arry start with 0 index value:
print("arry start with 0 index value:")
print(numbers[0])
print(numbers[1])
print(numbers[2])
#the position of the array is n -1
print("the position of the array is n -1")
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

#this index() is used to find position of the array:
print("this index() is used to find position of the array:")
print(numbers.index(10))

#using for loop you can print the element without writeing individually:
print("using for loop you can print the element without writeing individually:")
for numbers in numbers:
    print(numbers)

#the range() function and pass the len() method as its parameter This would give the same result as above:
print("the range() function and pass the len() method as its parameter This would give the same result as above:")    
for value in range(len(numbers)):
    print(numbers[value])