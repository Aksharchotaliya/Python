import random
lover = "abcdefghijklomnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "{}[]#()*;._-"

all = lover + upper + number + symbol
length = 9

n = int(input(" No of password:"))
for i in range (0,n):
     password = "".join(random.sample(all,length))
     print(password)
