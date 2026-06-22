#Functions
def greet(name):
    print("I am greeting : ",name)

greet("Ahmad")

print("----Factorial Taking----")
#returning Values in functions
def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)    

factorialVal = factorial(5)
print(factorialVal)
print("----Average Calculation----")
def arrayAvg(array):
    return sum(array)/len(array)

val = arrayAvg([2,3,4,5])
print(val)