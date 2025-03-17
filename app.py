import itertools
import random

def get_all_states(radios):
    return set().union(*radios.values())

def exact_global_min(radios):
    """
    Find the global minimum using exact search.
    """
    all_states = get_all_states(radios)
    sorted_radios = sorted(radios.items(), key=lambda x: len(x[1]), reverse=True)

    for k in range(1, len(radios) + 1):
        for combo in itertools.combinations(sorted_radios, k):
            if get_all_states(dict(combo)) == all_states:
                return [radio[0] for radio in combo]
    return None


def local_search_with_restarts(radios, max_iterations=100, max_restarts=10):
    """
    Find a local minimum using local search with restarts to approximate the global minimum.
    """
    all_states = get_all_states(radios)

    def is_valid(solution):
        return get_all_states({k: radios[k] for k in solution}) == all_states

    best_solution = None
    best_size = float('inf')

    for _ in range(max_restarts):
        # Iniciar con una solución aleatoria válida
        current_solution = list(radios.keys())
        random.shuffle(current_solution)

        # Reducir la solución por eliminación
        for _ in range(max_iterations):
            improved = False
            neighbors = [
                current_solution[:i] + current_solution[i + 1 :]
                for i in range(len(current_solution))
            ]

            for neighbor in neighbors:
                if len(neighbor) >= len(current_solution):
                    continue
                
                if is_valid(neighbor):
                    current_solution = neighbor
                    improved = True
                    break

            if not improved:
                break
        
        # Verificar si encontramos una mejor solución global
        if len(current_solution) < best_size:
            best_solution = current_solution
            best_size = len(current_solution)

    return best_solution

method_list = {
    "Global minimun" : exact_global_min,
    "Local minimun" : local_search_with_restarts,
}

def main():
    radios = {
        "kone": {"ID", "NV", "UT"},
        "ktwo": {"WA", "ID", "MT"},
        "kthree": {"OR", "NV", "CA"},
        "kfour": {"NV", "UT"},
        "kfive": {"CA", "AZ"},
        "ksix": {"NM", "TX", "OK"},
        "kseven": {"OK", "KS", "CO"},
        "keight": {"KS", "CO", "NE"},
        "knine": {"NE", "SD", "WY"},
        "kten": {"ND", "IA"},
        "keleven": {"MN", "MO", "AR"},
        "ktwelve": {"LA"},
        "kthirteen": {"MO", "AR"},
    }

    print("Select a search method:")
    for i, method_name in enumerate(method_list, start=1):
        print(f"{i}. {method_name}")
    choice = input("Enter the number of the option: ")

    if choice == "1":
        search_method = method_list["Global minimun"]
    elif choice == "2":
        search_method = method_list["Local minimun"]
    else:
        print("Unvalid option. Global minimun will be used.")
        search_method = exact_global_min

    print("Solution found:", search_method(radios))


if __name__ == "__main__":
    main()
