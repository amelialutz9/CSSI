from random import randint

def game(min, max):
    comp_num=randint(min,max)
    print "Computer number: " +str(comp_num)
    player_num=randint(min,max)
    print "Player number: "+str(player_num)
    while player_num!=comp_num:
        if (min>max):
            min=max;
        if (player_num>comp_num and min<max):
            print "Guess lower"
            max-=(max-min)/2
            print "min: "+ str(min) + " max: "+str(max)
        else:
            print "Guess higher"
            min+=(max-min)/2
            print "min: "+ str(min) + " max: "+str(max)
        player_num=randint(min,max)
        print "New guess: " + str(player_num)
    print "You got it!"

game(0,10)
