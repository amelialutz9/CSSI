#import statement
from random import randint

#creating a function
def print_stuff(number, word):
    print number*word

def addition(num1, num2):
    print num1+num2

print_stuff(int(raw_input("num? ")), raw_input("word? "))
addition(int(raw_input("num1? ")),int(raw_input("num2? ")))

#create an array
groceries = ['peanut butter','banana','pretzels','carrots','sweet potato','almond milk']

#print the length of the grocery list
#print len(groceries)


#print a random item from the grocery list
#print groceries[randint(0,5)]
