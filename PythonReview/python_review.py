dictionary = {
    ":-)" : "happy",
    ":)" : "happy",
    ":-(" : "sad",
    ":(" : "sad"
}

new_dict = []
final_dict = []


for item in dictionary:
    new_dict.append(dictionary[item])

i=0
for x in range(len(new_dict)):
    if new_dict[i]!=new_dict[x]:
        final_dict.append(new_dict[i])
        i+=1

print final_dict
