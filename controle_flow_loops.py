#Control flow statements and loops
"""there are three types of control floe ststement:selection,and repetition sequential statements are executed are executed in th order they appear
selection statements are used for desisions and branching, such as if/elif/else statements. Repetition statements are used for looping, such as while and for statements"""
#loops: loops allow you to repeat a block of code multiple time until a certain condition is met or over a collection of iteams
num = 1
while num <= 10:#you can use a while loop to print numbers from 1 to 10
    print(num)
    num = num + 1
     
names =["Akshar","kirtan","jay"]#you can use a for loop to iterate over a list of names
for name in names:
    print(name)
    
#you can also use control statements inside loops, such as continue,break,and pass
for no in range(1,11):
    if no % 2 == 0:
        #you can use continue to skip the current iteration of loop, break to exit the loop, and pass to do nothing:
        continue# skip even numbers
    elif no == 7:
        break #stop the loop
    else:
        pass #do nothig like fivestar
    print(no)