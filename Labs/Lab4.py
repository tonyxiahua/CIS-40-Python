'''
Create a program that does the following:

Asks the user to enter a four-digit number.
Outputs the number as Roman numerals.
Your code should all be in one file. To get the hang of Arabic-to-Roman numeral conversion, look at this online converter (Links to an external site.)Links to an external site.. Do not worry about the second column of Roman numerals, i.e., those with lines above them. Your program only needs the numerals I (1) - M (1000)

To submit: Copy/paste your code and the output from running it with all of these inputs:

0000
2999
1973
1956
2018
2000
0400
0040
0004
DO NOT USE any features that we have not yet studied!

Hint-1: Use incremental development techniques for this program. For example, don't even think about the conversion problem until you have first managed to separate the four-digit string into four one-digit strings.

Hint-2: I started off solving the conversion problem by writing out a table of all the digits for each of the four positions within the four-digit string, along with the Roman equivalent of each one. For example, here is the table I created for just the second digit (the hundreds place):

  0
  1 C
  2 CC
  3 CCC
  4 CD
  5 D
  6 DC
  7 DCC
  8 DCCC
  9 CM

Thus, whenever a 9 is the second digit, the Roman numeral equivalent will contain a CM to represent 900. I put the table above into my docstring for the function that processes the second digit.
'''

'''
Core identify function 
@input int
@output string
'''
def checker(num,Romanone,Romanfive,Romanten):
    if num == 1 or num == 2 or num == 3: 
        roman = Romanone*num
    elif num == 4: 
        roman = Romanone+Romanfive
    elif num == 5: 
        roman = Romanfive
    elif num == 6 or num == 7 or num == 8: 
        roman = Romanfive+Romanone*(num-5)
    elif num == 9: 
        roman = Romanone+Romanten
    elif num == 0:
        roman = '' 
    else:
        roman = 'Error'
    return roman 

'''
Dictionary functions 

@input num
@output string
'''
def thousandRomanDic(num):
    Romanone = 'M'
    if num == 1 or num == 2 or num == 3:
        romanthousand = Romanone*num
    elif num == 0:
        romanthousand = ''
    else:
        romanthousand = 'Error'
    return romanthousand
def hundredRomanDic(num):
    return checker(num,'C','D','M')
def tenRomanDic(num):
    return checker(num,'X','L','C')    
def oneRomanDic(num): 
    return checker(num,'I','V','X')

'''
Core function... convertion str to int
@input int 
@output void
'''
def toRoman(num):
    num=int(num)
    thousands = num // 1000
    hundreds = (num-thousands*1000)//100
    tens = (num-thousands*1000-hundreds*100)//10
    ones = (num-thousands*1000-hundreds*100-tens*10)
    #print (thousands, hundreds, tens, ones)
    print(thousandRomanDic(thousands)+hundredRomanDic(hundreds)+tenRomanDic(tens)+oneRomanDic(ones))
'''
Main function 
'''
def main():
    #toRoman(input("Enter 4 digit number\n"))
    '''
    As the requirement says.....
    '''
    toRoman('0000')
    toRoman('2999')
    toRoman('1973')
    toRoman('1956')
    toRoman('2018')
    toRoman('2000')
    toRoman('0400')
    toRoman('0040')
    toRoman('0004')
main()
'''
Screen Output:

MMCMXCIX
MCMLXXIII
MCMLVI
MMXVIII
MM
CD
XL
IV

'''