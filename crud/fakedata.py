import faker
from faker import Faker
import random


faker.Faker.seed(0)
#fake addresses in us proportional to state population
# Creat e an instance of the Faker class
fake = Faker()

# Define a dictionary with the population of each US state
state_population = {
    'Alabama': 4903185,
    'Alaska': 731545,
    'Arizona': 7278717,
    # ... add population data for other states
}

# Generate fake addresses in US proportional to state population
addresses = []
for state, population in state_population.items():
    num_addresses = int(population / sum(state_population.values()) * 100)  # Adjust the factor (1000) as needed
    for _ in range(num_addresses):
        address = fake.address().replace('\n', ', ')
        addresses.append((state, address))

# Print the generated addresses
for state, address in addresses:
    print(f'{state}: {address}')




