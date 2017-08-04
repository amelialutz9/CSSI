from random import randint
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

specials=['!','@','#','$','%','?','~','&','*']



def create_password(len):
    password=""
    counter=0;
    while (counter<len):
        letter_num=randint(0,3)
        letter_case=randint(0,50)
        num_special=randint(0,2)
        if(letter_num<3):
            if(letter_case<40):
                password+=letters[randint(0,25)]
            else:
                password+=letters[randint(0,25)].upper()
        else:
            if (num_special==0) or (num_special==1):
                password+=numbers[randint(0,9)]
            else:
                password+=specials[randint(0,8)]
        counter+=1
    print "Your password is: %s" % (password)

create_password(int(raw_input("How long do you want your password? ")))
