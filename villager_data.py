"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    all_animals = open(filename)
    for line in all_animals:
        animal_info = line.split('|')
        animal = animal_info[1]
        species.add(animal)

    all_animals.close()
    return species

# print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    all_animals = open(filename)
    for line in all_animals:
        animal_info = line.split('|')
        animal_name = animal_info[0]
        animal_species = animal_info[1]
        if search_string == "All":
            villagers.append(animal_name)
        
        elif animal_species == search_string:
            villagers.append(animal_name)

    all_animals.close()
    return sorted(villagers)

#print(get_villagers_by_species("villagers.csv", "Dog"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    all_animals = open(filename)

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    for line in all_animals:
        animal_info = line.split('|')
        animal_name = animal_info[0]
        animal_hobby = animal_info[3]
        if animal_hobby == "Fitness":
            fitness.append(animal_name)
        elif animal_hobby == "Nature":
            nature.append(animal_name)
        elif animal_hobby == "Education":
            education.append(animal_name)
        elif animal_hobby == "Music":
            music.append(animal_name)
        elif animal_hobby == "Fashion":
            fashion.append(animal_name)
        elif animal_hobby == "Play":
            play.append(animal_name)

    all_animals.close()
    return [fitness,nature,education,music,fashion,play]

# print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    all_animals = open(filename)

    for line in all_animals:
        line = line.strip()
        animal_info = line.split('|')
        animal_name = animal_info[0]
        animal_type = animal_info[1]
        animal_personality = animal_info[2]
        animal_hobby = animal_info[3]
        animal_saying = animal_info[4]
        animal_tuple = (animal_name, animal_type, animal_personality, animal_hobby, animal_saying)
        all_data.append(animal_tuple)

    all_animals.close()
    return all_data

# print(all_data("villagers.csv"))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    all_animals = open(filename)
    for line in all_animals:
        line = line.strip()
        animal_info = line.split('|')
        animal_name = animal_info[0]
        animal_motto = animal_info[2]
        if animal_name == villager_name:
            return animal_motto
   
    all_animals.close()
    return None    
       
#print(find_motto("villagers.csv", "Pashmina"))    


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    same_personality = set()
    all_animals = open(filename)
    target_personality = ''
    
    
    for line in all_animals:
        animal_info = line.split('|')
        animal_name = animal_info[0]
        animal_personality = animal_info[2]
        if animal_name == villager_name:
            target_personality = animal_personality
            print(animal_name,target_personality)
    
    # if animal_personality in target_personality:
    #     same_personality.add(animal_name)
    
    # for line in all_animals:
    #     animal_info = line.split('|')
    #     animal_name = animal_info[0]
    #     animal_personality = animal_info[2]
    #     print(animal_name)

    #     if animal_personality == target_personality:
    #         same_personality.add(animal_name)

    all_animals.close()

print(find_likeminded_villagers("villagers.csv", "Naomi"))
    



