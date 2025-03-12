import random

# greedy_search_global


def greedy_search_global(radios):
    covered_states = set()
    needed_radios = []

    sorted_radios = sorted(radios.items(), key=lambda x: len(x[1]), reverse=True)

    for radio, states in sorted_radios:
        new_states = states - covered_states
        if new_states:
            covered_states.update(new_states)
            needed_radios.append(radio)

    return needed_radios


# random_search
def random_search(radios, iterations=1000):
    best_solution = None
    best_coverage = set()

    all_radios = list(radios.keys())
    all_states = set().union(*radios.values())

    for _ in range(iterations):
        random.shuffle(all_radios)  # Mezclamos aleatoriamente las radios
        selected_radios = []
        covered_states = set()

        for radio in all_radios:
            if covered_states == all_states:
                break
            new_states = radios[radio] - covered_states
            if new_states:
                covered_states.update(new_states)
                selected_radios.append(radio)

        if len(covered_states) == len(all_states):
            if best_solution is None or len(selected_radios) < len(best_solution):
                best_solution = selected_radios
                best_coverage = covered_states

    return best_solution


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
    return greedy_search_global(radios)


if __name__ == "__main__":
    print(main())