def bmi(inches,pounds):
    value =703*pounds/(inches*inches)
    if (value <= 18.5):
        print("BMI = ",value,": Underweight")
    elif (value > 18.5 and value <= 25):
        print("BMI = ",value,": Normal weight")
    elif (value > 25 and value <= 30):
        print("BMI = ",value,": Overweight")
    elif (value > 30):
        print("BMI = ",value,": Obesity")
    
def main():
    inches=float(input("Enter your height in inches, including decimal fractional parts: "))
    pounds=float(input("Enter your weight in pounds: "))
    bmi(inches,pounds)

main()

"""
Output :


Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 120
BMI =  18.378834710856335 : Underweight

Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 121
BMI =  18.531991666780137 : Normal weight

Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 163
BMI =  24.964583815579854 : Normal weight

Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 164
BMI =  25.117740771503655 : Overweight

Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 195
BMI =  29.86560640514154 : Overweight

Enter your height in inches, including decimal fractional parts: 67.75
Enter your weight in pounds: 196
BMI =  30.018763361065346 : Obesity
"""