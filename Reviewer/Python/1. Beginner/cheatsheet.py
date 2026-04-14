"""
DATA TYPES AND COLLECTION
"""
######################################################################################################

# STRINGS
print("="*10, "STRINGS", "="*10)
#-------------------------------#
text = "#HellO world#" # string data type
print(text)
print(text.lower()) # lower() = lowercase
print(text.upper()) # upper() = uppercase
print(text.strip("#")) # strip() removes unleading whitespace or any element character (empty for whitespace)
print(text.replace("world", "John Doe")) # replace("WordToReplace", "Update")
print(len(text)) # len() to count the length of variable

#######################################################################################################

# LISTS
print("="*10, "LIST", "="*10)
#-------------------------------#
fruits=["apple", "banana", "orange"] # List datatype
print(fruits)
print(fruits[0]) # first item (index starts with 0)
print(fruits[-1]) # last item
print(fruits[0:2]) # Slicing, slicing at the specific index ['apple','banana',///'orange'] orange is index 2
fruits.append("strawberry") # adds at the end of list
fruits.insert(1, "grapes") # add at specific index
fruits.remove('apple') # remove specific item
print(fruits)
print(len(fruits))

##########################################################################################################

# --- LIST METHODS
print("-"*10)
nums = [2,1,3]
print(nums)

nums.append([4, 5]) # Add it as one whole list
print(nums)

nums = [2,1,3]
nums.extend([4,5]) # Extends the list or add each items
print(nums)

nums.sort() # Sorting list
print(nums)

nums.reverse() # Reverse the list
print(nums)

print(nums.pop()) # Returns the last item and remove it, can do it outside print() but doesnt return anything
print(nums)

###############################################################################################

# TUPLES
# Tuples is immutable which means its unchangeable even if you add or delete
print("="*10, "TUPLES", "="*10)
#-------------------------------#
point = (10, 20, 30)
print(point)
print(point[0])
# point[0] = 5 # this will result in error since its immutable, uncomment to try
a, b, c = point # Unpackaging the tuples
print(a)
print(c, b)

####################################################################################################

# SETS
# Set is unordered and unique which means it can go any order but cannot have duplicates
print("="*10, "SETS", "="*10)
#-------------------------------#
fruits={"apple", "banana", "orange"} # Re-use it cause why not
print(fruits) 
fruits.add("apple") # No changes cause cannot have duplicates
print(fruits) # To check if something changed
fruits.remove("apple")
print(fruits)

#####################################################################################################

# DICTIONARIES
print("="*10, "DICTIONARY", "="*10)
#-------------------------------#
p1 = {"name":"Bob", "age":21} # dictionary_name = {"KEYS":VALUES}
print(p1['age']) # p1['KEYS'] (usecase for MUST EXIST)

print(p1.get('name')) # p1.get('KEYS') (usecase for MIGHT BE MISSING)
print(p1.get('loc')) # returns None as default
p1['loc'] = "Los Lagunas" # to add a new KEY-VALUE pair
print(p1.keys()) # Show keys
print(p1.values())  # Show Values
print(p1.items()) # Shows BOTH

####################################################################################################
"""
CONTROL FLOW
"""
####################################################################################################

# CONDITIONAL STATEMENT
print("="*10, "IF-ELIF", "="*10)
#-------------------------------#
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C")   
     
###################################################################################################

print("-"*5)
age = 16
has_license = True # Boolean = True or False
if age >= 18 and has_license:
    print("Valid to drive")
if age < 18 or not has_license:
    print("Not valid to drive")
    
#####################################################################################################

print("="*10, "MEM-OPERATOR", "="*10)
#-------------------------------#
fruits=["apple", "banana", "orange"]
if "banana" in fruits:
    print("LETSGOO!!!!")
else:
    print("Aww :( ")
    
print("grapes" not in fruits) # True
print("bayabas" in fruits) # False
print("banana" in fruits) # True

########################################################################################################

print("="*10, "FOR LOOP", "="*10)
#-------------------------------#
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)
    
#####################################################################################################

print("="*10, "FOR IN RANGE LOOP", "="*10)
#-------------------------------#
for i in range(3): # from 0-2, this always start in 0
    print(i, end="")
print()
for i in range(2, 6): # (start, stop)
    print(i, end="")
print()
for i in range(1, 10, 2): # (start, stop, step)
    print(i, end="")
print()

##########################################################################################################

print("="*10, "WHILE LOOP", "="*10)
#-------------------------------#
count = 0
while count < 3:
    print(count, end="")
    count+=1
print()

###########################################################################################################

print("="*10, "BREAK 'N CONTINUE", "="*10)
#-------------------------------#
for i in range (5):
    if i == 3:
        break # Stops at index 3 or stops entirely if its already equal to 3
    print(i, end="")
print()

for i in range(5):
    if i == 1:
        continue # Skips this index or iteration
    print(i, end="")
print()

###########################################################################################################

print("="*10, "NESTED FOR LOOPS", "="*10)
#-------------------------------#
for i in range(1 ,5+1): # You can also do it like 5+1 to lessen confusion
    for j in range(1 ,5+1): 
        print(f"{i*j}\t", end=" ") # Generates a 5x5 Multiplication Table as an example for this
    print()    
    
###########################################################################################################

print("="*10, "CONDITIONAL LOOP", "="*10)
#-------------------------------#
for i in range (1, 10+1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
        
###########################################################################################################
"""
NESTED STRUCTURE
"""
###########################################################################################################

print("="*10, "LIST OF LIST", "="*10)
#-------------------------------#
matrix = [ [1,2,3]
          ,[4,5,6] ]
print(matrix[0][1]) 
#  |--0--|  |--1--| Which LIST - First []
#   0|1|2    0|1|2  Which ITEM - Second []
#[ [1,2,3] ,[4,5,6] ]

for row in matrix:
    print(row) # Prints the x axis or row (Horizontal --)
    
for row in matrix:
    for value in row:
        print(value, end=" ") # Prints the y axis or the values inside row (Vertical |)
print()

############################################################################################################

print("="*10, "LIST OF DICTIONARIES", "="*10)
#-------------------------------#
products = [
    {'name': 'chicken', 'price': 160},
    {'name': 'pork', 'price': 399}
]
for p in products:
    print(p["name"], p["price"])
    
for p in products:
    if p['name'] == 'chicken' and p['price'] < 200:
        print("YIPEEE")
    
cheap_foods = 0    
for p in products:      
    if p["price"] < 400:
        cheap_foods += 1
    else:
        cheap_foods += 0
        
print(f"Foods under 400 prices: {cheap_foods}")

###########################################################################################################
"""
INPUT 'N TYPE CONVERSION
"""
###########################################################################################################

print("="*5, "USER INPUT 'N TYPE CONVERSION", "="*5)
#-------------------------------#
"""
UNCOMMENT TO TRY 
"""
# name = input("Name: ") # Input is always string

# age = int(input("Age: ")) # Converts it to INT

# weight = float(input("Weight: ")) # Converts to FLOAT

# print(f"my name is {name}, {age} yrs old, weights {weight}")

###########################################################################################################
"""
MODULES BASICS
"""
###########################################################################################################

print("="*10, "MATH MODULE BASICS", "="*10)
#-------------------------------#
import math # Must use to use MATH MODULES
print(math.sqrt(16)) # Square Root 
print(math.pi) # Pi Numbers
print(math.floor(3.9)) # Rounds DOWN 
print(math.ceil(3.1)) # Rounds UP
print(math.pow(2, 3)) # Raise a number to power 2**3 = 2x2x2
print(2**3) # This also work in non-math modules

###########################################################################################################

print("="*10, "MATH MODULE BASICS", "="*10)
#-------------------------------#
import random # Import for RANDOM
print(random.randint(1, 10)) # Random INT from 1 - 10
print(random.random()) # Random float from 0.0 - 1.0

###########################################################################################################

print("="*10, "RANDOM MODULE", "="*10)
#-------------------------------#
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits)) # Randomly returns one item from list

random.shuffle(fruits) # Shuffle list
print(fruits)

###########################################################################################################

print("="*10, "DATE AND TIME MODULE", "="*10)
#-------------------------------#
import datetime
now = datetime.datetime.now() # Curent date and time
print(now)

print(now.year, now.month, now.day)
print(f"{now.hour}:{now.minute}")

d = datetime.date(2006, 7, 6) # Specific date
print(d) # MY BDAY :D

print(now.strftime("%Y-%m-%d")) # Just to format as string

###########################################################################################################
############
print()
############