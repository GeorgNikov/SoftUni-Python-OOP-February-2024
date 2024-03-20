from project.planet.planet import Planet
from project.space_station import SpaceStation

space_station = SpaceStation()

print(space_station.add_astronaut("Meteorologist", "Ivan"))
print(space_station.add_astronaut("Geodesist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "Jivko"))
print(space_station.add_astronaut("Geodesist", "Gogo"))
print(space_station.add_astronaut("Meteorologist", "Milena"))
print(space_station.add_astronaut("Biologist", "Sisi"))
print([a.name for a in space_station.astronaut_repository.astronauts])
#print(space_station.add_astronaut("Meteorologist2", "Peter"))
planet = space_station.add_planet("Earth", 'test, skill, broke, coke, sword, iron, cu_ore, ore, koks, water, flower, trow, port')
print(planet)
planet_mars = space_station.add_planet("Mars", 'test2, skill2, broke2, coke2, sword2, iron2, cu_ore2, ore2, koks2, water2, flower2, trow2, port2')
print(planet_mars)
print(space_station.send_on_mission("Earth"))
print(space_station.send_on_mission("Mars"))
print(space_station.report())