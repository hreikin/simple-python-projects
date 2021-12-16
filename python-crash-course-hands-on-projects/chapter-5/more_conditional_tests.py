# You don’t have to limit the number of tests you create to 10. If you want to 
# try more comparisons, write more tests and add them to this file. Have at 
# least one True and one False result for each of the following:
# 
# Tests for equality and inequality with strings
# 
# Tests using the lower() function
# 
# Numerical tests involving equality and inequality, greater than and less than, 
# greater than or equal to, and less than or equal to
# 
# Tests using the and keyword and the or keyword
# 
# Test whether an item is in a list
# 
# Test whether an item is not in a list

my_string = "My String"
print("\nIs my_string == 'My String' ? I predict True.")
print(my_string == "My String")
print("\nIs my_string == 'my string' ? I predict False.")
print(my_string == "my string")
print("\nIs my_string != 'my string' ? I predict True.")
print(my_string != "My String")
print("\nIs my_string != 'My String' ? I predict False.")
print(my_string != "my string")
print("\nIs my_string.lower() == 'my string' ? I predict True.")
print(my_string.lower() == "my string")
print("\nIs my_string.lower() == 'My String' ? I predict False.")
print(my_string.lower() == "My String")
print("\nIs my_string.lower() != 'My String' ? I predict True.")
print(my_string.lower() != "My String")
print("\nIs my_string.lower() != 'my string' ? I predict False.")
print(my_string.lower() != "my string")

num = 10
print("\nIs num > 5 ? I predict True.")
print(num > 5)
print("\nIs num < 5 ? I predict False.")
print(num < 5)
print("\nIs num >= 5 ? I predict True.")
print(num >= 5)
print("\nIs num <= 5 ? I predict False.")
print(num <= 5)
print("\nIs num != 5 ? I predict True.")
print(num != 5)
print("\nIs num == 5 ? I predict False.")
print(num == 5)

age_1 = 22
age_2 = 18
print("\nIs age_1 > 21 and age_2 > 17 ? I predict True.")
print(age_1 > 21 and age_2 > 17)
print("\nIs age_1 > 23 and age_2 > 19 ? I predict False.")
print(age_1 > 22 and age_2 > 19)
print("\nIs age_1 > 21 or age_2 > 19 ? I predict True.")
print(age_1 > 21 or age_2 > 19)
print("\nIs age_1 > 22 or age_2 > 18 ? I predict False.")
print(age_1 > 22 or age_2 > 18)

my_list = ["item1", "item2", "item3"]
print("Is 'item1' in my_list ? I predict True.")
print("item1" in my_list)
print("Is 'item4' in my_list ? I predict False.")
print("item4" in my_list)
print("Is 'item4' not in my_list ? I predict True")
print("item4" not in my_list)
print("Is 'item1' not in my_list ? I predict False")
print("item1" not in my_list)