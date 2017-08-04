from random import randint

def game():
    counter=1
    comp_num=randint(0,10)
    print comp_num
    player_num=int(raw_input("What is your guess? "))
    while player_num!=comp_num:
        if (player_num>comp_num):
            print "Guess lower"
        else:
            print "Guess higher"
        player_num=int(raw_input("What is your guess? "))
        counter+=1
    grammar=""
    if counter==1:
        grammar="try"
    else:
        grammar="tries"
    print "You got it! It took you %s %s." % (counter, grammar)

game()
