#Exception Handling.
#Sometimes the program might crash.
#for that we use Exception handling.

#here if we enter a string, it will give me an error.

#for this we will be using exception handling.
#using try/except.

try:
    number2 = int(input("Enter a number : "))
    print(number2)
except:
    print("Please Enter a valid thing")

#the zero division error
try:
    val = 10/2
    print(val)
except ZeroDivisionError:
    print("INFINITY")


#if you want to run the code no matter what for that we use finally.
try:
    number = int(input("enter number : "))
    print(number)
except:
    print("Invalid Number")
finally:
    print("Program ended")
