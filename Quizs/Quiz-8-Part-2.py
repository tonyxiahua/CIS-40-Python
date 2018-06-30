wordsList = []
word = input("Enter a word : ").strip()
counter  = 0
for i in range(len(word)):
    line = "".join(wordsList)
    if word[i] in line:
        counter -= 1
    elif word[i] not in line:
        wordsList.append(word[i])
        counter += 1
print(word, "contains", counter, "unique letters")