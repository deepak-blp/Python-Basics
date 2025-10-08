print("Operator in Python")

#precedence of operators
#arithmatic operators -->> PEMDAS(Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction)
#logical operators -->> and, or, not             
#assignment operators-->> =, +=, -=, *=, /=, //=, **=, %=   
#comparison operators -->> ==, !=, >, <, >=, <=
#bitwise operators -->> &(AND), |(OR), ^(XOR), ~(NOT), <<(left shift), >>(right shift)   
#identity $ membership operators-->> is (a is b), is not(a is not b), in(a in b), not in(a not in b)  
       
print("#example of arithmatic operators")
a = 10
b = 3
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation

print("#example of comparison operators")

x = 5
y = 10
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to  

#examples of assignment operators
print("#example of assignment operators")
c = 5
print("Initial value of c:", c)
c += 3
print("After c += 3:", c)
c -= 2
print("After c -= 2:", c)
c *= 4      

#examples of logical operators
print("#example of logical operators")
p = True
q = False
#rulessss
# True + True = True
# True + False = False
# False + False = False  
# #Rulesss
 
print("p and q:", p and q)  # Logical AND
print("p or q:", p or q)    # Logical OR
    
print("not p:", not p)      # Logical NOT
print("not q:", not q)      # Logical NOT

print("#example of identity operators")
list1 = [1, 2, 3]
list2 = list1       
list3 = [1, 2, 3]
print("list1 is list2:", list1 is list2)  # True, because list2 references list1
print("list1 is list3:", list1 is list3)  # False, because they are different objects
print("list1 is not list3:", list1 is not list3)  # True, because they are different objects
print("list1 == list2:", list1 == list2)  # True, because they have the same content            
print("list1 == list3:", list1 == list3)  # True, because they have the same content
print("list1 != list3:", list1 != list3)  # False, because they have the same content
print("list1 != list2:", list1 != list2)  # False, because they have the same content
print("#example of membership operators")
fruits = ['apple', 'banana', 'cherry']
print("Is 'banana' in fruits?", 'banana' in fruits)  # True
print("Is 'grape' not in fruits?", 'grape' not in fruits)  # True



print("#example of bitwise operators")
m = 6  # In binary: 110
n = 3  # In binary: 011
# #RULESS AND
# True & True = True
# True & False = False
# False & False = False
# #Rulesss OR
# True | True = True
# True | False = True
# False | False = False
# #Rulesss XOR
# True ^ True = False
# True ^ False = True
# False ^ False = False
# #Rulesss NOT
# ~True = False
# ~False = True
#Rulesss LEFT SHIFT
#Shifting bits to the left by 1 position (equivalent to multiplying by 2)
# 110 << 1 = 1100 (which is 12 in decimal)
#Rulesss RIGHT SHIFT
#Shifting bits to the right by 1 position (equivalent to dividing by 2)
# 110 >> 1 = 011 (which is 3 in decimal)        



print("m & n:", m & n)  # Bitwise AND
print("m | n:", m | n)  # Bitwise OR
print("m ^ n:", m ^ n)  # Bitwise XOR
print("~m:", ~m)        # Bitwise NOT
print("m << 1:", m << 1)  # Left Shift
print("m >> 1:", m >> 1)  # Right Shift
         