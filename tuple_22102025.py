# Part 1: Tuples

# Activity 1: Tuples Basics
# Given the tuple: fruits = ("apple", "banana", "cherry", "mango", "banana")

# Address the following:
# Determine the length of the fruits tuple.
fruits = ("apple", "banana", "cherry", "mango", "banana")
length = len(fruits)
print( length)





# Identify the index of the initial occurrence of "banana".
index_of_banana = fruits.index("banana")  
print("Index of first occurrence of 'banana':", index_of_banana)  


# Attempt to modify "cherry" to "grape" within the tuple. Explain the outcome and the reason behind it.
print("Original fruits tuple:", fruits)
replace = list(fruits)
replace[2] = "grape"
fruits = tuple(replace)
print("Modified fruits tuple:", fruits)


# Transform the tuple into a list, make a modification, and then convert it back to a tuple.
fruits_list = list(fruits)
fruits_list.append("orange")
fruits = tuple(fruits_list)
print("Fruits tuple after adding 'orange':", fruits)




# Activity 2: Tuples Grouping
# Given the following tuples:
# colors = ("red", "green", "blue")
# shapes = ("circle", "square", "triangle")
# Perform the following operations:

# Combine colors and shapes to create a new tuple called art.

colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
print("Combined art tuple:", art)





# Demonstrate how to repeat a tuple, specifically colors three times.



repeated_colors = colors * 3
print("Repeated colors tuple:", repeated_colors)

# Extract and print the middle element from the art tuple using slicing.
middle_index = len(art) // 2
middle_element = art[middle_index]
print( middle_element)

# Verify if the string "square" exists within the art tuple.
exists_square = "square" in art
print(  exists_square)
# Activity 3: Tuple Operations

# Given the following list of student marks:

# marks = (78, 85, 69, 90, 85)

# Perform the following operations:
# Determine the highest and lowest marks.
marks = (78, 85, 69, 90, 85)
highest_mark = max(marks)
lowest_mark = min(marks)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)

# Count the occurrences of the mark 85.
count_of_85 = marks.count(85)
print("Occurrences of mark 85:", count_of_85)
# Calculate the average marks using the sum() and len() functions.
average_marks = sum(marks) / len(marks)
print("Average marks:", average_marks)
# Activity 4: Rainfall Data:

# The monthly_rainfall tuple provides the rainfall in millimeters for each month from January to December:


monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)

# Calculate the total annual rainfall.

monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
month=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
total_annual_rainfall = sum(monthly_rainfall)
print("Total annual rainfall (mm):", total_annual_rainfall)


# Determine the average monthly rainfall.
average_monthly_rainfall = total_annual_rainfall / len(monthly_rainfall)
print("Average monthly rainfall (mm):", average_monthly_rainfall)
# Identify the month(s) with exactly 120 mm of rainfall. (Hint: Consider using enumerate() or .count().)
for i in  enumerate(monthly_rainfall):
    if i[1]==120:
        print("Month with 120 mm rainfall:",month[i[0]])
# Find the highest and lowest rainfall values recorded.
highest_rainfall = max(monthly_rainfall)
lowest_rainfall = min(monthly_rainfall) 
print(highest_rainfall)
print(lowest_rainfall)


