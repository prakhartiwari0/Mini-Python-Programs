

file = open("text.txt", "r")
content = file.read()
file.close()

list_of_all_words = content.split()


list_of_tags = []

for i in range(len(list_of_all_words)):
    word = list_of_all_words[i]
    if (word[0]=="<") and (word[len(word)-1]==">"):
        if word[1]=="/":
            continue
        else:
            list_of_tags.append(word)


list_of_tags = sorted(set(list_of_tags))


var = "\n".join(list_of_tags)

print(var)





