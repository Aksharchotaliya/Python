import random
lover = "abcdefghijklomnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]#()*;._-"

all = lover + upper + number + symbol
length = 9
password = "".join(random.sample(all,length))
print("this Password You Generated is :",password)
