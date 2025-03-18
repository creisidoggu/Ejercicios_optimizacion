import itertools
import random

def get_all_states(radios):
    """
    Returns all the states of the problem's country
    """
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

def minimun_local_search(radios, max_iterations=100):
    """
    Find a local minimum using local search with restarts to approximate the global minimum.
    """
    all_states = get_all_states(radios)
    stations = list(radios.keys())
    limit = len(exact_global_min(radios))
    if limit is None:
        limit = len(stations)  

    locals = []

    for _ in range(max_iterations):
        random.shuffle(stations)
        selected = stations[:limit]

        covered_states = set().union(*(radios[s] for s in selected))
        missing_states = all_states - covered_states
        missing_count = len(missing_states)

        locals.append(missing_count) 

        if missing_count == 0:
            return locals

    return locals

method_list = {
    "Global minimun": exact_global_min,
    "Local minimun": minimun_local_search,
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
        print("Invalid option. Global minimun will be used.")
        search_method = exact_global_min

    print("Solution found:", search_method(radios))


if __name__ == "__main__":
    main()
