# print("Conditional statements If, if-else, if-elif-else, nested if else AND Ternary operator in Python")
# #exeute a block of code if a specified condition is true. If the condition is false, the block of code will not be executed.

# #syntax is if condition:
# #                    statements

# #example of if statement           
# a = 10
# b = 5
# if a > b:
#     print("a is greater than b")    
# #example of if-else statement
# a = 10
# b = 15
# if a > b:   
#     print("a is greater than b")
# else:
#     print("a is not greater than b")

# #example of if-elif-else statement
# num = 0
# if num > 0: 
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:       
#     print("Negative number")   
     
# #example of nested if-else statement
# num = 10
# if num >= 0:    
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")
# #example of ternary operator
# age = 18


# status = "Adult" if age >= 18 else "Minor"
# print("Status:", status)    

#positive,negative or zero,positive - even/odd
# number = int(input("Enter a number: "))

# if number > 0 : #checking positive number
#     if number % 2 == 0: #checking even number
#         print("Positive even number")
#     else:
#         print("Positive odd number")
# else:
#     if number ==0:#checking zero
#         print("Zero")
#     else:
#         print("Negative number")#negative number        


#COnditinol Expressioons(ternary operator)

age = 16
stauts = "Major" if age >= 18 else "Minor"
print("Status:", stauts)    