import itertools


def exact_global_min(radios):
    """
    Find the global minimun of the states.
    """
    all_states = set().union(*radios.values())
    best_solution = None

    sorted_radios = sorted(radios.items(), key=lambda x: len(x[1]), reverse=True)

    for k in range(1, len(radios) + 1):
        for combo in itertools.combinations(sorted_radios, k):
            current_names = [r[0] for r in combo]
            covered = set().union(*[r[1] for r in combo])
            if len(covered) == len(all_states):
                if best_solution is None or len(current_names) < len(best_solution):
                    best_solution = current_names
                return best_solution
    return best_solution


def local_search(radios, initial_solution=None, max_iterations=100):
    """
    Find a local minimun using local search on the enviroment
    """
    all_states = set().union(*radios.values())

    current_solution = (
        initial_solution if initial_solution else exact_global_min(radios)
    )
    current_size = len(current_solution)

    def evaluate(solution):
        covered = set().union(*[radios[radio] for radio in solution])
        return len(covered) == len(all_states), len(solution)

    for _ in range(max_iterations):
        improved = False

        neighbors = [
            current_solution[:i] + current_solution[i + 1 :]
            for i in range(len(current_solution))
        ]

        for neighbor in neighbors:
            if not improved:
                break

            full_coverage, size = evaluate(neighbor)

            if full_coverage and size < current_size:
                current_solution = neighbor
                current_size = size
                improved = True
                break
    return current_solution


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

    print("Seleccione el método de búsqueda:\n1. Mínimo global\n2. Mínimo local\n")
    choice = input("Ingrese el número de la opción: ")

    if choice == "1":
        search_method = exact_global_min
    elif choice == "2":
        search_method = local_search
    else:
        print("Opción no válida. Se usará el mínimo global por defecto.")
        search_method = exact_global_min

    print("Solución encontrada:", search_method(radios))


if __name__ == "__main__":
    main()
