running = True
snax = {
    "fruit snacks" : 10,
    "apples" : 7,
    "rice krispys" : 8,
    "peanut butter" : 11
}

while running==True:
    snack=raw_input("Add a snack or type 'exit': ")
    if snack!="exit":
        rating=raw_input("What is it rated? ")
        snax[snack]=rating
    else:
        running = False
        
for item in snax:
    if item=="raisins":
        snax[item]="DISGUSTING"
    print "%s get a %s out of 10"%(item,snax[item])
