# Start with the program you wrote for "person.py". Make two new 
# dictionaries representing different people, and store all three dictionaries 
# in a list called people . Loop through your list of people. As you loop 
# through the list, print everything you know about each person.

person_one = {"first_name": "richard", "last_name": "sayles", "age": 33, "town": "rotherham"}

for k, v in person_one.items():
    print(k + ":", v)

person_two = {"first_name": "victoria", "last_name": "brown", "age": 36, "town": "saltcoats"}
person_three = {"first_name": "chris", "last_name": "haslam", "age": 31, "town": "guildford"}

people = [person_one, person_two, person_three]

print(people)

for item in people:
    for k, v in item.items():
        print(k + ":", v)