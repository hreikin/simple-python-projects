# Use a dictionary to store information about a person you know. Store their 
# first name, last name, age, and the city in which they live. You should have 
# keys such as first_name , last_name , age , and city . Print each piece of 
# information stored in your dictionary.

person = {"first_name": "richard", "last_name": "sayles", "age": 33, "town": "rotherham"}

for k, v in person.items():
    print(k + ":", v)