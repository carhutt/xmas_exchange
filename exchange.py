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
	],
    "2021": [
        "Abi : Christina",
        "Jesse : Andrew",
        "Callie : Abi",
        "Hannah : Callie",
        "Christina : Jesse",
        "Eric : Gigi",
        "Gigi : Hannah",
        "Andrew : Sam",
        "Sam : Eric"
    ],
    "2022": [
        "Abi : Sam",
        "Christina : Gigi",
        "Andrew : Hannah",
        "Callie : Jesse",
        "Gigi : Eric",
        "Sam : Abi",
        "Hannah : Christina",
        "Jesse : Callie",
        "Eric : Andrew"
    ],
    "2023": [
        "Andrew : Gigi",
        "Gigi : Callie",
        "Jesse : Eric",
        "Abi : Jesse",
        "Jordy : Sam",
        "Eric : Jordy",
        "Hannah : Andrew",
        "Sam : Christina",
        "Callie : Hannah",
        "Christina : Abi"
    ],
    "2024": [
        "Deniz : Abi",
        "Sam : Caleb",
        "Andrew : Eric",
        "Abi : Hannah",
        "Jordy : Gigi",
        "Eric : Jesse",
        "Gigi : Andrew",
        "Christina : Callie",
        "Hannah : Deniz",
        "Jesse : Jordy",
        "Callie : Sam",
        "Caleb : Christina"
    ]

}

#a list of all the names participating in given year
inclusion_array_2021 = ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jesse", "Christina"]
inclusion_array_2022 = ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jesse", "Gigi", "Christina", "Nathan", "Monty"]
inclusion_array_2023 = ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jordy", "Jesse", "Gigi", "Christina"]
inclusion_array_2024 = ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jordy", "Caleb", "Jesse", "Gigi", "Christina", "Deniz"]

#a list of all the significant other pairs
so_pairs = [
'Hannah : Sam',
'Sam : Hannah',
'Abi : Eric',
'Eric : Abi',
'Andrew : Callie',
'Callie : Andrew',
'Caleb : Jordy',
'Jordy : Caleb',
'Nathan : Monty',
'Monty : Nathan',
'Jesse : Gigi',
'Gigi : Jesse' ,
'Christina : Deniz'
'Deniz : Christina'
]

def check_repetition(previous_year, this_year):
    if any(name_pair in previous_year for name_pair in this_year):
        #print("Duplicates found.")
        return False
    else:
        #print("No duplicates found.")
        return True

def generate_pairs(inclusion_array):
    names_dict = dict()
    for n in range(len(inclusion_array)):
        names_dict[n] = inclusion_array[n]
	
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
    last_year = history_dict['2023']
    year_before_last = history_dict['2022']

    while any(name_pair in this_year for name_pair in so_pairs):
        print("starting over for so")
        this_year = generate_pairs(inclusion_array)
        if check_repetition(last_year, this_year) == True and check_repetition(year_before_last, this_year) == True:
            return this_year
        else:
            while (check_repetition(last_year, this_year) == False) or (any(name_pair in this_year for name_pair in so_pairs) or (check_repetition(year_before_last, this_year) == False)):
                this_year = generate_pairs(inclusion_array)
            return this_year

print(generate_christmas_rotation(history_dict, inclusion_array_2024))
