# Write a function called city_country() that takes in the name of a city and 
# its country. The function should return a string formatted like this: 
# 
# "Santiago, Chile" 
# 
# Call your function with at least three city-country pairs, and print the value 
# that’s returned.

def city_country(city, country):
    print(city + ",", country)

city_country("Glasgow", "Scotland")
city_country("Edinburgh", "Scotland")
city_country("London", "England")

# Different solution from Jay using a tuple of tuples to feed the function its 
# parameters.

cc_pairs = (
  ('Glasgow', 'Scotland',),
  ('Edinburgh', 'Scotland'), 
  ('London', 'England'),
)

print("Jays solution.")
for pair in cc_pairs:
   city_country(*pair)