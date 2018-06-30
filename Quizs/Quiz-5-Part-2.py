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