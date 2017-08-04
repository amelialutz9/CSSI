running=True
emoji_dic = {
    ':)' : 'happy',
    '<3' : 'hearts',
    ':(' : 'unhappy',
    'lol' : 'laughing out loud',
    '._.' : 'unimpressed',
}
while running:
    print "Add an emoji or type 'exit' to quit"
    emoji = raw_input("Please give me an emoji to define: ")
    in_dictionary=emoji in emoji_dic
    if in_dictionary==True:
        print emoji_dic[emoji]
    else:
        if emoji == "exit":
            running=False
        else:
            definition = raw_input("Not in the dictionary! Please define: ")
            emoji_dic[emoji]=definition
            if len(emoji)>4:
                print "That's almost TOO long to be an emoji...."
            print "Added!"
            print "%s : %s"%(emoji, definition)
