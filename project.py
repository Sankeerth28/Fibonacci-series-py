
''''Project 12:
In this project user will enter single or multiple numbers and your system will predict that the entered number or number’s
 is/are valid number(s) in a Fibonacci series or not.
For example, if user inputs 2 numbers
0 and 7
0 is valid and 7 is invalid.
Because if we plot Fibonacci series 0 1 1 2 3 5 8 13……, In this series 0 is their but 7 is not present.
Constraint: range of the single number or multiple numbers you are entering can be huge.

(Student is free to decide the input and output layout for this mini project)'''

def fibonacci():
    num = int(input("Please enter: "))
    i = 1
    if num == 0:
        fib = "empty"
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 0
    return fib
print (fibonacci())
