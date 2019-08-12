'''
Quiz 9
Write a small program that:

Asks the user to enter a sentence
Outputs a message indicating whether the sentence is a pangram or not. A pangram is a sentence that uses every letter of the alphabet at least once, regardless of the case of the letters.
 

Enter a sentence for pangram-checking: Waltz, nymph, for quick jigs vex bud.
"Waltz, nymph, for quick jigs vex bud." is a pangram

Enter a sentence for pangram-checking: Python is an object-oriented programming (OOP) language.
"Python is an object-oriented programming (OOP) language." is NOT a pangram

'''

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
    
'''
Quiz 8

Write a tiny program (mine was 12 lines before I added comments) which:

Asks the user to enter a word
Prints the number of unique letters in that word
Here are three separate executions of my program, showing my input and the program's output:

Enter a word : disambiguate
disambiguate contains 8 unique letters
Enter a word : the
the contains 3 unique letters
Enter a word : noon
noon contains 0 unique letters
'''

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


'''
Quiz 7

Write a program that calculates the average number of words per sentence in the input text file. To keep this simple, you may assume that:

every sentence ends with a period (when, in reality, sentences can end with !, ", ?, etc.)
no periods are used for purposes other than ending sentences (such as after abbreviations)
My solution for this problem is 9 lines long.

Here's my output using the python-description.txtPreview the document file as input:

Average number of words/sentence : 13.6
'''

def AvgSentenceWords(file):
    sentence = 0
    words = 0 
    for line in open(file):
        words = words + len(line.split())
        for character in line:
            if character == '.': 
                sentence += 1
print("Average number of words/sentence :",words/sentence)
AvgSentenceWords("python-description.txt")



'''
Quiz 6
Write a program that mimics the Linux wc (wordcount) utility. Given an input file (which you should hardcode the name of right in your file), it outputs three integers:

the number of lines,
the number of words, and,
the number of characters, in the input file.
Use python-description.txtPreview the document as your input file for testing purposes. Put it in the same folder/directory as your source code so that when I download and execute the source code, Python will be able to find MY copy of python-description.txt.

My solution is only 9 lines of Pythson source code. Still, you should approach this problem in an incremental development fashion. Focus on getting just the line count correct. Only after that is correct should you start on one of the other two counts. And only after the second count is correct, should you start on the third count! Don't try to write the whole program at once, even though it's small!

8 points for correct code, 9 points for concise and well-structured code.

My output (which matches that of the wc utility) is this:
'''
countList = [0, 0, 0]
def counter(countList):
    fin = open("python-description.txt")
    for line in fin:
        countList[0] += 1;
        countList[1] += len(line.split());
        for characters in line:
            countList[2] += 1;
    print(countList[0],countList[1],countList[2]);
counter(countList);

'''
Quiz 5
Complete the function below and then submit your completed program via uploading the .py file. The function is a Boolean one that returns True if both the second and second-from-last character in a string are vowels, regardless of case; otherwise, it returns False.

def second_from_ends_are_vowels(word):
# You write the function body

print(second_from_ends_are_vowels("beloved"))
print(second_from_ends_are_vowels("HATED"))
print(second_from_ends_are_vowels("indifferent"))
print(second_from_ends_are_vowels("undecided"))
To submit, upload your .py file, which MUST include both your function and the four calls shown above, just as they are. In addition, please copy/paste your output into a Canvas Comment.
'''
def second_from_ends_are_vowels(word):
    word = word.lower()
    if word[-2] and word[1] in 'aeiou':
        return True
    return False
print(second_from_ends_are_vowels("beloved"))
print(second_from_ends_are_vowels("HATED"))
print(second_from_ends_are_vowels("indifferent"))
print(second_from_ends_are_vowels("undecided"))
'''
Screen Output

True
True
False
False
'''

'''
Quiz 4

Create a function count_by(num) that outputs the first 50 numbers (starting with 0) when counting by num.

To answer this question, copy/paste your code (function definition and function call using 5 as the argument) along with your output as shown below.

count_by(5)

0
5
10
15
.
.
.
210
215
220
225
230
235
240
245
'''

def count_by(difference):
    sumis = 0 
    counter = 0
    while (counter < 50):
        print(sumis)
        sumis = sumis + difference
        counter = counter+1
count_by(5)