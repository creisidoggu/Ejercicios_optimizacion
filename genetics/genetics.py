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
    """
    This step create a population in base of an individual size
    """
    population = []
    for individual in range(population_length):
        current_individual = []
        for gene in range(individual_size):
            current_individual.append(random.randrange(0,2))
        population.append(current_individual)
    return population

def calculate_individual_fitness(individual, items, items_max_weight):
    """
    Calculate the "Value" of any of the individuals
    """
    total_weight = 0
    total_value = 0
    
    for gene_index in range(len(individual)):
        if individual[gene_index] == 1:
            total_weight += items[gene_index]["weight"]
            total_value += items[gene_index]["value"]
            
            if total_weight > items_max_weight:
                return 0

    return total_value

def set_probabilities_of_population(population, items, items_max_weight):
    """
    Calculates the probability of selection for each individual in the population.
    """
    fitness_values = [calculate_individual_fitness(individual, items, items_max_weight) for individual in population]
    total_fitness = sum(fitness_values)

    if total_fitness == 0:
        return [1 / len(population)] * len(population)

    probabilities = [fitness / total_fitness for fitness in fitness_values]

    return probabilities


def main():
    items = establish_individuals(path)
    population = create_population(len(items), 60)
    items_max_weight = 5

    probabilities = set_probabilities_of_population(population, items, items_max_weight)
    print(probabilities)


if __name__ == '__main__':
    main()