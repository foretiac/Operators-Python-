#Anthony Foretich
#ISAT 340
#Operator Badge Program
#This program takes a user integer input, divides it by 3.0, and finds the remainder.
#It then adds ten to this remainder value, and divides that value by 40.
#If the new value is greater than or equal to five, it is incremented +1 ten times and each value is printed.
#If the new value is less than 5, it is incremented +2 ten times and each value is printed.
#The purpose of this program is to gain familiarity with Python operators.
#Remainder, addition, devision, greater than or equal to comparison, less than comparison, and incrementing operators are used. 

x = int(input(' enter an integer to divide by 3.0 and find the remainder '))
y = "3"
z = 3.0

value = x // z
print (value)

valuechanged = (value + 10)/40
print(valuechanged)

if valuechanged >= 5:
    for i in range (10):
        vuechangedagain = 0
        valuechanged += 1
        print(valuechanged)

if valuechanged < 5:
    for i in range (10):
        vuechangedagain = 0
        valuechanged += 2
        print(valuechanged)
    
