inStr = input("Enter a sentence for pangram-checking:")
inStr = inStr.strip()
word = []
letters = []

for i in range(len(inStr)):
    if inStr[i].isalpha():
        if inStr[i] not in letters:
            letters.append(inStr[i])
            
if len(letters) == 26:
    print("\"",inStr,"\" is a pangram")
else:
    print("\"",inStr,"\" is a NOT pangram")