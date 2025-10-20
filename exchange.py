import random  
from datetime import datetime  
  
# Historical gift exchange pairs  
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
    ],
    "2025": [
        "Abi : Gigi",
        "Andrew : Caleb",
        "Caleb : Abi",
        "Callie : Jordy",
        "Christina : Sam",
        "Deniz : Jesse",
        "Eric : Deniz",
        "Gigi : Christina",
        "Hannah : Callie",
        "Jesse : Hannah",
        "Jordy : Eric",
        "Sam : Andrew"
    ]
}  
  
# Participant lists by year  
participants_by_year = {  
    "2021": ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jesse", "Christina"],  
    "2022": ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jesse", "Gigi", "Christina", "Nathan", "Monty"],  
    "2023": ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jordy", "Jesse", "Gigi", "Christina"],  
    "2024": ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jordy", "Caleb", "Jesse", "Gigi", "Christina", "Deniz"],  
    "2025": ["Hannah", "Sam", "Abi", "Eric", "Andrew", "Callie", "Jordy", "Caleb", "Jesse", "Gigi", "Christina", "Deniz"]  
}  
  
# Significant other pairs (people who shouldn't give to each other)  
SO_PAIRS = {  
    ('Hannah', 'Sam'), ('Sam', 'Hannah'),  
    ('Abi', 'Eric'), ('Eric', 'Abi'),  
    ('Andrew', 'Callie'), ('Callie', 'Andrew'),  
    ('Caleb', 'Jordy'), ('Jordy', 'Caleb'),  
    ('Nathan', 'Monty'), ('Monty', 'Nathan'),  
    ('Jesse', 'Gigi'), ('Gigi', 'Jesse'),  
    ('Christina', 'Deniz'), ('Deniz', 'Christina')  
}  
  
  
def parse_pair(pair_string):  
    """Convert 'Name1 : Name2' to tuple ('Name1', 'Name2')"""  
    giver, receiver = pair_string.split(' : ')  
    return (giver.strip(), receiver.strip())  
  
  
def format_pair(giver, receiver):  
    """Convert tuple to 'Name1 : Name2' format"""  
    return f"{giver} : {receiver}"  
  
  
def generate_pairs(participants):  
    """Generate random gift exchange pairs ensuring no one gifts themselves"""  
    givers = participants.copy()  
    receivers = participants.copy()  
      
    # Keep shuffling until no one has themselves  
    max_attempts = 1000  
    for _ in range(max_attempts):  
        random.shuffle(receivers)  
        if all(givers[i] != receivers[i] for i in range(len(givers))):  
            return [format_pair(givers[i], receivers[i]) for i in range(len(givers))]  
      
    raise ValueError("Could not generate valid pairs after maximum attempts")  
  
  
def has_conflicts(pairs, excluded_pairs_list, so_pairs):  
    """Check if any pairs conflict with excluded pairs or SO pairs"""  
    pairs_set = {parse_pair(pair) for pair in pairs}  
      
    # Check against excluded pairs from previous years  
    for excluded_pairs in excluded_pairs_list:  
        excluded_set = {parse_pair(pair) for pair in excluded_pairs}  
        if pairs_set & excluded_set:  # If there's any intersection  
            return True  
      
    # Check against significant other pairs  
    if pairs_set & so_pairs:  
        return True  
      
    return False  
  
  
def generate_christmas_rotation(history_dict, participants, current_year=None):  
    """  
    Generate gift exchange pairs avoiding:  
    - Significant others  
    - Pairs from the last year  
    - Pairs from the year before last  
    """  
    if current_year is None:  
        current_year = datetime.now().year  
      
    last_year = str(current_year - 1)  
    year_before_last = str(current_year - 2)  
      
    # Get excluded pairs from previous years  
    excluded_pairs = []  
    if last_year in history_dict:  
        excluded_pairs.append(history_dict[last_year])  
    if year_before_last in history_dict:  
        excluded_pairs.append(history_dict[year_before_last])  
      
    # Try to generate valid pairs  
    max_attempts = 10000  
    for attempt in range(max_attempts):  
        pairs = generate_pairs(participants)  
          
        if not has_conflicts(pairs, excluded_pairs, SO_PAIRS):  
            print(f"✓ Valid pairing found after {attempt + 1} attempt(s)")  
            return pairs  
      
    raise ValueError(f"Could not generate valid pairs after {max_attempts} attempts. "  
                     "Consider relaxing constraints.")  
  
  
# Example usage  
if __name__ == "__main__":  
    current_year = 2025  
    participants = participants_by_year[str(current_year)]  
      
    print(f"\n🎄 Secret Santa {current_year} 🎄\n")  
    pairs = generate_christmas_rotation(history_dict, participants, current_year)  
      
    for pair in sorted(pairs):  
        print(pair)  
