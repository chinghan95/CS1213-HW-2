"""
Ching Han Huang, 113510994
Data : 8/30/19

I used If-Else function to check if any number that user entered was inside the 0-100 range. If the answer was yes, then the number was counted, 
and the summation, which default value was 0, added the number. If the answer was no, the number won't be counted, and the summation won't add any value,
and then other number was checked.

"""

name = input("What is your name?")
number1 = int ( input ("What is your score #1? ") )
number2 = int ( input ("What is your score #2? ") )
number3 = int ( input ("What is your score #3? ") )

sum = 0
count = 0
if number1 > 0 and number1 < 100:
    sum = number1
    count = 1
    if number2 > 0 and number2 < 100:
        sum = sum + number2
        count = 2
        if number3 > 0 and number3 < 100:
            sum = sum + number3
            count = 3
    else:
        if number3 > 0 and number3 < 100:
            sum = sum + number3
            count = 2   
else:
    if number2 > 0 and number2 < 100:
        sum = number2
        count = 1
        if number3 > 0 and number3 < 100:
            sum = sum + number3
            count = 2
    else: 
        if number3 > 0 and number3 < 100:
            sum = number3
            count = 1
        else: 
            count = 1

average = sum / count

if average >= 90:
    letter_grade = 'A'
elif average >= 80 and average < 90:
    letter_grade = 'B'
elif average >= 70 and average < 80:
    letter_grade = 'C'
elif average >= 60 and average < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Thank you, " + name + ", your average score was " +  str(average) + " and you earned an " + letter_grade)
