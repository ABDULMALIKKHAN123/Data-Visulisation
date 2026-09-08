# # Arithmatic Operation
# a = 10
# b =5
# add_result =a+b  #addition
# sub_result = a-b  #sub
# mult_result = a*b
# div_result = a/b
# floor_div_result = a//b     ##floor division
# modulus_result = a%b       #modulus oparation
# exponent_result = a**b   ##exponentiation
# print(add_result)
# print(sub_result)
# print(mult_result)
# print(div_result)
# print(floor_div_result)
# print(modulus_result)
# print(exponent_result)



# c= '10'
# d = '20'
# f = c+d
# print(f)
# print(type(f))     #concatination



#print(' abdul ' *5)   #replication



#comparison
# >  <  ==  !=  >=  <=

# a = 5 
# b = 3
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b)


#Bitwise Operator
# & bitwise AND
# | bitwise OR
# ~ bitwise NOT
# ^ bitwise XOR
# >> bitwise right side
# << bitwise left side

# a = 10
# b = 5
# print(a&b)
# print(a|b)
# print(~b)
# print(a^b)
# print(a>>b)
# print(a<<b)

#print(9<<1)  ##1001   #10010   left shift
#print(9>>1)    #1001  


#Assignment Operator
# =  +=  -=  *=  /=  %=  //=  **=  &=  |=  ^=  >>=  <<= 

# x = 5 
# x += 5 
# x -= 5 
# x *= 5 
# x /= 5 
# x %= 5 
# x //= 5 
# x **= 5 
# x &= 5 
# x |= 5 
# x ^= 5 
# x >>= 5 
# x <<= 5 

# x = int (x)&5

#Logical Operator
# a = 10
# b = 20 
# print(a<b and a!=b)

# a = 10
# b = 20 
# print(a>b or a>b)

#AND operator
# a= 10
# b = 20
# print(a<b and a!=b)

#Identity Operator(is / is not) ka o/p -- True/False aata hai
# a = 10
# b =10 
# print(a is b)
# print(a == b)


# print(id(a),id(b))


#else statement
age = int(input("Enter your age:"))

if age >=18:
    print("You are allowed to vote in the election")


if age<13:
    print("you are a child: ")
elif age<18:
    print("You are a teenager: ")
elif age<24:
    print("You are Young")
    

