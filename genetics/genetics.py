import json
import random
# Added some more variables of the items if i want to use it for my dnd page, but for this problem i'll use only weight and value
path = "genetics/data/items.json"

def establish_individuals(file):
    """
    This step will be used to define the structure of the individuals
    """
    
    with open(file) as json_file:
        json_data = json.load(json_file)
        json_file.close()

    return [{ "weight": obj["weight"], "value": obj["value"] } for obj in json_data]

def create_population(individual_size, population_length = 60):
    population = []
    for individual in range(population_length):
        current_individual = []
        for gene in range(individual_size):
            current_individual.append(random.randrange(0,2))
        population.append(current_individual)
    return population

def main():
    print(create_population(len(establish_individuals(path))))

if __name__ == '__main__':
    main()