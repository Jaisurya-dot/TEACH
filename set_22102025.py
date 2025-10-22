# rainfall_data = {120, 150, 180, 120, 90, 110, 130}
# (This set represents the rainfall in mm recorded across various districts this week.)
# How many rainfall values are in the set?
rainfall_data = {120, 150, 180, 120, 90, 110, 130}
print("Number of unique rainfall values recorded:", len(rainfall_data))

# Can you directly change the value of an item in a set? What output would you get when you try to change the value using its index ?

# rainfall_data[2] = 200
# print(rainfall_data)
# TypeError: 'set' object does not support item assignment



# Check if 150 is present inside rainfall_data. (hint: use in keyword and research)

is_150_present = 150 in rainfall_data
print("Is 150 mm rainfall recorded?:", is_150_present)



# Convert the set to a list 
list_rainfall = list(rainfall_data)
print("List of rainfall values:", list_rainfall)


# Print every rainfall value by traversing through the set.

for rainfall in rainfall_data:
    print("Rainfall value (mm):", rainfall)



# Remove the value 120 from the above set.
rainfall_data.remove(120)
print("Rainfall data after removing 120 mm:", rainfall_data)



# Add the value 110 to the above set and observe if any changes happen ? Why does 110 not appear twice ?

rainfall_data.add(110)
print("Rainfall data after adding 110 mm again:", rainfall_data)
# Sets do not allow duplicate values, so adding 110 again does not change the set.

# Joining Multiple Sets 
# Given:
# rainfall_chennai = {120, 140, 160, 180}
# rainfall_madurai = {110, 130, 150, 180}
# rainfall_coimbatore = {100, 120, 180, 200}

rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
join_sets = rainfall_chennai.union(rainfall_madurai, rainfall_coimbatore)
print("Joined rainfall data from all three cities:", join_sets)





# The Rainfall data starts from Monday to Thursday here, if added more data, it will be considered as the next day in the week.
week = ("Mon", "Tue", "Wed", "Thu")





# Print all unique rainfall measurements for Chennai and Madurai.
unique_chennai_madurai = rainfall_chennai.union(rainfall_madurai)
print("Unique rainfall measurements for Chennai and Madurai:", unique_chennai_madurai)




# Merge all three readings into a new set using both the update() and union() methods.
merged_rainfall = rainfall_chennai.union(rainfall_madurai, rainfall_coimbatore)
print("Merged rainfall data using union():", merged_rainfall)
rainfall_chennai.update(rainfall_madurai)
rainfall_chennai.update(rainfall_coimbatore)    



# Common Rainfall: Identify rainfall values present in all three cities.
common_rainfall = rainfall_chennai.intersection(rainfall_madurai, rainfall_coimbatore)
print("Common rainfall values in all three cities:", common_rainfall)



# Unique Chennai Rainfall: Determine unique rainfall values observed exclusively in Chennai.
unique_chennai_rainfall = rainfall_chennai.difference(rainfall_madurai, rainfall_coimbatore)
print("Unique rainfall values in Chennai:", unique_chennai_rainfall)




# Rainfall in at least Two Cities: Find rainfall values recorded in a minimum of two cities.
rainfall_at_least_two = (rainfall_chennai.intersection(rainfall_madurai)).union(rainfall_chennai.intersection(rainfall_coimbatore)).union(rainfall_madurai.intersection(rainfall_coimbatore))
print("Rainfall values recorded in at least two cities:", rainfall_at_least_two)




# Create a new set where every rainfall value is increased by 10. 
increased_rainfall = {value + 10 for value in join_sets}
print("Rainfall values increased by 10 mm:", increased_rainfall)




# For e.g. if input is {120, 140, 160,180}, then output has to be {130, 150, 170, 190}
increased_rainfall = {value + 10 for value in join_sets}
print("Rainfall values increased by 10 mm:", increased_rainfall)
	



# Other Miscellaneous Methods:
# Delete the rainfall_coimbatore set in python.

del rainfall_coimbatore
# Clear the data inside rainfall_chennai set and make it empty.
rainfall_chennai.clear()
print("Rainfall Chennai after clearing:", rainfall_chennai)


