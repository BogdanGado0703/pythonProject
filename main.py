from star_wars_api import StarWarsApi

api_client = StarWarsApi()

person = api_client.get_person(1)
planet = api_client.get_planet(1)


print(f"Person name:{person.name}")
print(f"Person hair_color : {person.hair_color }")
print(f"Person height : {person.height }")
print(f"Person eye_color : {person.eye_color}")
print(f"Person mass : {person.mass }")

planets = api_client.get_planet(1)
print(planets.name)
