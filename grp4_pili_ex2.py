#MDAS
#1 Create a Python program to perform arithmetic Operations  (Addition, Subtraction, Division, Multiplication, Modulus,Exponent) using two variable numbers for int, float and complex

#integer
j = 8
a = 2  

#float
y = 6.5    
s = 2.2     

#complex
o = 6+4j  
n = 2+2j  

#Addition
print("Addition:")
print(j+a) 
print(y+s) 
print(o+n) 

#Subtraction
print("\nSubtraction:")
print(j-a) 
print(y-s) 
print(o-n) 

#Multiplication
print("\nMultiplication:")
print(j*a) 
print(y*s) 
print(o*n) 

#Division
print("\nDivision:")
print(j/a)  
print(y/s) 
print(o/n) 

#Modulus 
print("\nModulus:")
print(j%a) 
print(y%s) 
print(o*n) 

#Exponentiation
print("\nExponentiation:")
print(j**a) 
print(y**s) 
print(o**n) 


#2 Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.

num1 = 25_000_000 
num2 = 25000000   

print() 
print(num1)
print(num2)
print() 

#3 Creating int,float and complex variable then check the type using the Python Code.
int_var = 8         
float_var = 14.2     
complex_var = 0 + 1j  

print("Value of int_var:",int_var,"Type:",type(int_var))
print("Value of float_var:",float_var,"Type:",type(float_var))
print("Value of complex_var:",complex_var,"Type:",type(complex_var))
