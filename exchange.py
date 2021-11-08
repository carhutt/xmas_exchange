import random, itertools, copy

#this data structure can be filled out with new data each year after Christmas
history_dict = {
	"2020": [
		"Hannah : Abi",
		"Abi : Andrew",
		"Andrew : Caleb",
		"Caleb : Nathan",
		"Nathan : Jesse",
		"Jesse : Christina",
		"Christina : Hannah"
	]
}

#a list of all the names participating in given year
inclusion_array_2021 = ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jesse", "Christina"]

def check_repetition(previous_year, this_year):
    if any(name_pair in previous_year for name_pair in this_year):
        print("Duplicates found.")
        return False
    else:
        print("No duplicates found.")
        return True

def generate_pairs(inclusion_array):
    names_dict = dict()
    for n in range(len(inclusion_array)):
        names_dict[n] = inclusion_array[n]
        
    #print(names_dict)
    
    list_a = list(range(len(inclusion_array)))
    random.shuffle(list_a)
    
    list_b = copy.copy(list_a)
    
    while list_b == list_a:
        random.shuffle(list_b)
        for idx, value in enumerate(list_b):
            #print(idx, value)
            #print(list_a[idx])
            if list_a[idx] == value:
                list_b = copy.copy(list_a)
            else:
                pass
    
    for idx, value in enumerate(list_a):
        list_a[idx] = names_dict[value]
        
    for idx, value in enumerate(list_b):
        list_b[idx] = names_dict[value]

    pairs_list = []
    
    for i in list(range(len(inclusion_array))):
        name1 = list_a[i]
        name2 = list_b[i]
        pair = name1 + ' : ' + name2
        pairs_list.append(pair)
    
    return pairs_list

def generate_christmas_rotation(history_dict, inclusion_array):
    #random sort+pair inclusion_array and transform to dict
    #make names dict with int keys
    #random sort per name
    this_year = generate_pairs(inclusion_array)
    #check for repetition from previous year(s), rerun if needed
    last_year = history_dict['2020']
    if check_repetition(last_year, this_year) == True:
        return this_year
    else:
        while check_repetition(history_dict['2020'], this_year) == False:
            #return "blaaaah"
            this_year = generate_pairs(inclusion_array)
            if check_repetition(last_year, this_year) == True:
                return this_year

generate_christmas_rotation(history_dict, inclusion_array_2021)
