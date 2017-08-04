#import statement
from random import randint



#prompting for the number of tasks/excuses
num_tasks=int(raw_input("How many tasks do you have?"))
num_excuses=int(raw_input("How many excuses do you have?"))

#creating the arrays
tasks=[]
excuses=[]

#adding items to the arrays based on the user prompted number of items for each
for i in range (1,num_tasks+1):
    tasks.append(raw_input("Enter a task: "))
    i+=1

for i in range (1,num_excuses+1):
    excuses.append(raw_input("Enter an excuse: "))
    i+=1

#final print statement of the task and the excuse
print "Sorry, I couldn't complete my task of %s because of %s."%(tasks[randint(0,len(tasks)-1)],excuses[randint(0,len(excuses)-1)])
