import json
import random
import matplotlib.pyplot as plt
import os
# Added some more variables of the items if i want to use it for my dnd page, but for this problem i'll use only weight and value
path = "genetics/data/items.json"
image_path = 'genetics/img'

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

def roulette_wheel_selection(population, items, items_max_weight, number_of_selections):
    """
    Select individuals randomly
    """
    probabilities = set_probabilities_of_population(population, items, items_max_weight)
    selected = []
    
    for _ in range(number_of_selections):
        spin = random.uniform(0, 1)
        cumulative_probability = 0
        
        for i, probability in enumerate(probabilities):
            cumulative_probability += probability
            if spin <= cumulative_probability:
                selected.append(population[i])
                break
    
    return selected

def one_point_crossover(parent_a, parent_b, xover_point):
    """
    Creates two new individuals based on two parents
    """
    children = []
    child_1 = parent_a[0:xover_point]+parent_b[xover_point:len(parent_b)]
    children.append(child_1)
    child_2 = parent_b[0:xover_point]+parent_a[xover_point:len(parent_b)]
    children.append(child_2)
    return children

def mutate_individual(individual, chromosome_length):
    """
    Mutates a random gene in an individual by flipping its value (0 -> 1 or 1 -> 0).
    """
    random_index = random.randint(0, chromosome_length - 1)

    individual[random_index] = 0 if individual[random_index] == 1 else 1

    return individual


def run_ga(population_size, number_of_generations, knapsack_capacity):
    items = establish_individuals(path)
    individual_size = len(items)
    global_population = create_population(individual_size, population_size)
    best_global_fitness = 0
    fitness_progress = []

    for _ in range(number_of_generations):
        current_best_fitness = max(calculate_individual_fitness(ind, items, knapsack_capacity) for ind in global_population)
        fitness_progress.append(current_best_fitness)
        if current_best_fitness > best_global_fitness:
            best_global_fitness = current_best_fitness
        
        the_chosen = roulette_wheel_selection(global_population, items, knapsack_capacity, population_size // 2)
        the_children = []
        for i in range(0, len(the_chosen) - 1, 2):
            xover_point = random.randint(1, individual_size - 1)
            the_children.extend(one_point_crossover(the_chosen[i], the_chosen[i + 1], xover_point))
        the_children = [mutate_individual(child, len(child)) for child in the_children]
        global_population = the_children + the_chosen
    
    plt.plot(range(number_of_generations), fitness_progress, marker='o', linestyle='-', color='b')
    plt.xlabel('Generaciones')
    plt.ylabel('Mejor Aptitud')
    plt.title('Evolución de la Aptitud en el Algoritmo Genético')
    plt.grid()
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    plt.savefig(f"{image_path}/fitness_evolution.png")
    print("Gráfico guardado como fitness_evolution.png")
    
    return best_global_fitness


if __name__ == "__main__":
    final_fitness = run_ga(population_size=60, number_of_generations=100, knapsack_capacity=50)
    print("Mejor aptitud obtenida:", final_fitness)