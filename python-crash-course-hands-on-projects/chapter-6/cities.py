# Make a dictionary called cities. Use the names of three cities as keys in 
# your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one 
# fact about that city. The keys for each city’s dictionary should be something 
# like country , population , and fact . Print the name of each city and all of 
# the information you have stored about it.

cities = {
    "glasgow" : {"country" : "scotland", "population" : "598000", "fact" : "Glasgow is home to more people than any other city in Scotland."},
    "edinburgh" : {"country" : "scotland", "population" : "482000", "fact" : "The Edinburgh Fringe Festival is the largest arts festival in the world."},
    "london" : {"country" : "england", "population" : "8900000", "fact" : "Over 300 languages are spoken in London."}
    }

for name in cities.keys():
    print(name)
    for k, v in cities[name].items():
        print(k + ":", v)