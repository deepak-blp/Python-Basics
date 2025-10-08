#Assignment - 3
#Problem Statement - 1  
#1.Leap year or not using user input.
#Note - A year is a leap year if it is divisible by 4 but not divisible by 100, except if it is also divisible by 400.

# year = int(input("Enter a year (e.g. 2024): ")) 
# if (year % 4 == 0 and year % 100 != 0) or \
#     (year % 400 == 0):
#     print(f"{year} is a leap year." )
# else: 
#     print(f"{year} is not a leap year.")
    
    
#Login Authentication predefined username and password are valid or not;
 
predefined_username = "admin"
predefined_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")    
if username == predefined_username :
    if password == predefined_password:
        print("Welcome! Login was suceesfull.")
    else:
        print("Invalid password.")
else:
      print("Invalid Username !")  
      
#Admisson Eligiblity based on marks in 3 subjects
#Mathematics >= 65

print("Welcome to Admission Portal")
print("Please enter your marks out of 100 ")
physics_marks = int(input("Physics marks: "))
chemistry_marks = int(input("Chemistry marks: "))
math_marks = int(input("Mathematics marks: "))

if (math_marks >= 65 and
   physics_marks >= 55 and
   chemistry_marks >= 50 and
    (math_marks + physics_marks + chemistry_marks) >= 180) or \
    (math_marks + physics_marks) >= 140:
    print("Congratulations! You are eligible for admission.")
else:
    print("Sorry, you are not eligible for admission.")    
    