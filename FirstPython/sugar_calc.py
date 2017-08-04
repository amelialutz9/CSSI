running = True
total = 0
while running == True:
    response = raw_input("Enter the grams of sugar or type 'exit' to total: ")
    if response == "exit":
        running = False
    else:
        total+=int(response)
print "Total sugar: "+str(total)+ "g"
