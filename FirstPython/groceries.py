from random import randint

def get_groceries():
    groceries=[]
    amount=[]
    count=0
    num=int(raw_input("How many groceries do you need? "))
    for i in range(num):
        food=raw_input("What food do you need? ")
        num_food=int(raw_input("How many do you need? "))
        if (count==0):
            groceries.append(food)
            amount.append(num_food)
            count+=1
        else:
            in_list=0
            for i in range(len(groceries)):
                if (food == groceries[i]):
                    amount[i]+=num_food
                    in_list=1
            if (in_list==0):
                groceries.append(food)
                amount.append(num_food)

    for i in range(len(groceries)):
        print "%s. %s: %s" % (str(i+1), groceries[i], amount[i])

get_groceries()
