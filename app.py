radios = {
    "kone" : {"ID", "NV", "UT"},
    "ktwo" : {"WA", "ID", "MT"},
    "kthree" : {"OR", "NV", "CA"},
    "kfour" : {"NV", "UT"},
    "kfive" : {"CA", "AZ"},
    "ksix" : {"NM", "TX", "OK"},
    "kseven" : {"OK", "KS", "CO"},
    "keight" : {"KS", "CO", "NE"},
    "knine" : {"NE", "SD", "WY"},
    "kten" : {"ND", "IA"},
    "keleven" : {"MN", "MO", "AR"},
    "ktwelve" : {"LA"},
    "kthirteen" : {"MO", "AR"},
}

#greedy_search_global

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

#greedy_search_local

def greedy_search_local(radios):
    pass

def main():
    print(greedy_search_global(radios))

if __name__ == "__main__":
    main()