# Strings can be enclosed in single or double quotes
myString='Hello'
myString2="hello2"
print (myString)
print (myString2)

# Special charcaters can be escaped with forward slash \
print('he does\'nt know')
print("he does'nt know")

print('he shoulted "hola!"')
print("he shoulted \"hola!\"")

# New line charcater = \n
print("this will print in \n 2 lineS")

'''
If you don’t want characters prefaced by \ to be interpreted as special characters, 
you can use raw strings by adding an r before the first quote:
'''
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote


#String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
#End of lines are automatically included in the string, but it’s possible to prevent this by
#adding a \ at the end of the line. The following example:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# concatenation with  +
print('um'+'hum')

#string index
'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''
var='Python'
print(var[2])
print(var[1:3]) # starte from 1 to 3 excluded
print(var[:3]) # starte from 1 to 3 excluded

