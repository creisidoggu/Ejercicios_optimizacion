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

def greedy_search_global(sets):
    previous_state = None
    output = []
    for states in sets:
        if previous_state != None:
            output.append(sets[states] - previous_state)
        previous_state = sets[states]
    return output

#greedy_search_local

def greedy_search_local(sets):
    pass

def main():
    print(greedy_search_global(radios))

if __name__ == "__main__":
    main()