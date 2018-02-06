#Review

'''
Basic python data types:
    We have 4 main data types that we use.
    int, float, str, boolean
'''
6 #this is an int
5.0 #this is a float
"tester test" #this is a string
False #this is a boolean

'''
We can store data of any type in variables.
Variables can only hold one thing at a time...if a new object is placed in an already existing variable,
it overwrites the previously existing value
'''

x = 6 # x is the variable, it holds the integer 6
x = 7 # x is the variable, putting 7 in x means the 6 is gone...for good

#variables can be called whatever you want, as long as the word isn't reserved
my_super_happy_variable_farm = "this is a string example"

#float variables
decimal = 5.0
decimal_2 = 7.8

#Booleans are only True or False, but can be in variables
MyTrueVar = True
MyFalseVar = False

'''
Mathematical operations:
    ( ) - Parentheses I.E. brackets
    ** - Exponential
    * - Multiplication
    / - Division
    // - Integer division (floor)
    % - Modulus (remainder)
    + - addition
    - - subtraction
We can chain these operations together and perform them on data, as well as on variables containing data.
Order of operations (BEDMAS) applies to these operators
'''

x = 5.6
y = 7.8
z = x + y
a = x ** y

b = (x + 2 / y - 1) * (x + y) % 2 *6

'''
Boolean expressions
We can evaluate expressions to see if certain conditions are true or false.
Boolean operators:
    <, <=, >, >=, ==, !=, in, not in, is not, not, and, or
'''

print( 5 != 6 )
print( 2 ** 2 <= 10 )
print( 2 is 3 )
print( 2 is not 3 and 4 is not 5 )
print( True and "this" )
print( "this" and True )

'''
If statements
To execute a block of code conditionally (only if certain states are reached) we can use if statements
If statments use a boolean expression (that evaluates to True or False).
If the expression is true, run the inner block
'''

x = 5
if( x < 10 ):
    print("x is less than 10")
    
'''
Else ifs provide us with alternate conditions to check in case the first one was wrong
'''

string = "test string"
if( "w" in string ):
    print("string contains a w")
elif( "b" in string ):
    print("string contains a b")
elif( "r" in string ):
    print("string contains a r")

'''
Else blocks provide us with a default block of code to run in case NONE of the if/elif statements are true
'''

x = 10
if( x == 11 ):
    print( "x is 11" )
elif( x == 12 ):
    print( "x is 12" )
else:
    print("x is neither 11 or 12" )


'''
For loops
Define a variable and iterate over a collection (iterator).
An iterator is any of: string, list, tuple, range, etc
For loops contain a variable that is defined and will be assigned each value of the iterator as the loop executes
'''

for myVar in range(5):
    print("The current value in myVar is {}".format(myVar))

'''
In the above example myVar is the variable we create for the sole purpose of this for loop
The iterator in this case is a range... range(5)
'''

'''
Lists and tuples are collections of data, separated by commas
Lists are made with square brackets, Tuples with parantheses
Lists are Mutable (can be changed). Tuples are Immutable (cannot be changed)
'''

myList = ["this", "is", "a", "list", 1, 2, 3]
myTuple = ("this", "is", "a", "tupe", 1, 2, 3)

'''
Lists can be appended to, that is, add an element to the end of the list
'''

print( myList )
myList.append("NewLastElement")
print(myList)

'''
Lists and tuples are iterators that can be looped on
'''

for item in myList:
    print(item)

'''
Each element in a list, tuple, string, etc (ANY ITERATOR) has a position.
Positions start counting at 0. That is, the first element is in the 0 position.
We can access elements in these iterators by using the element indices
'''

print( myList[0] ) #Get just the first element of the list

print( myList[1] ) #Get just the second element of the list

print( myList[-1] ) #-1 negative indices start counting at the right side of the iterator and go left

'''
Slices use the same concept but allow us to retrieve multiple elements at once.
Three values separated by colons -> [start:stop:step]
'''

print( "This Is My String"[1:15:2] )

print( "This is another string"[::-1] ) #This slice reverses the string

print( range(6)[2] ) 

'''
While loops are similar to if statements except instead of executing their internal block of code one time,
they execute the block of code UNTIL the condtional expression becomes false.
'''

x = 10
if( x < 20 ):
    print( "X is less than 20" ) #this is run ONE time
    
y = 10
while( y < 20 ):
    print( "Y is less than 20" ) #this runs TEN times
    y += 1#NOTE you need to ensure the expression can become false, without this increment the loop will run forever
    
'''
Functions, like if statements and while loops, are a means of separating a block of code.
Except unlike if statements and while loops (which only execute a certain number of times and 
only when they are reached in the program. Functions can be run any number of times and simply by calling
the function by its name
'''

def testFunction():
    print( "This is my test function" )
    
'''
The above function is simply a function DEFINITION. It does not run anything on its own
In order for it to run you must CALL it
'''

testFunction() #Calling the function!

'''
When the function is called, python jumps to the first line in the function and continues running there until the end of
the function or until a return statement is hit
'''


def testFunctionNumTwo():
    print( "This is my other test function" )
    return 500
    
testFunctionNumTwo() #this returned 500...but we didn't do anything with the result!!

x = testFunctionNumTwo() #here we save the 500 in the variable x and can now use it!

print(x)

'''
Function definitions can specify a set of PARAMETERS that are required for the function to run.
These are defined in the parentheses of the function definition. Data is passed in for these parameters when 
THE FUNCTION IS CALLED. The name represents a variable that will hold that data within the function
'''

def testFunc( paramOne ):
    print(paramOne)
    
testFunc( 2 ) #Pass in a 2, print a 2
testFunc(4.5) #Pass in 4.5, print a 4.5

testFunc( range(6) ) #Pass in a range, print a range

'''
Often we'll establish a certain type of data we want to be passed in and assume that data is correct so 
we can perform operations.
'''

def division( x, y):
    print( x / y )
    
division(9, 3) #if I don't use data that can actually be divided, I break the function
