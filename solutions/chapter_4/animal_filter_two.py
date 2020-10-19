# Filter the animals DataFrame:

# Filter the animals DataFrame where the AnimalClass was Mammal or the PumpHoursTotal was greater than 8.


mammals_pumphours = animals[(animals['AnimalClass'] == "Mammal") | (animals['PumpHoursTotal'] > 8)]

mammals_pumphours.head()