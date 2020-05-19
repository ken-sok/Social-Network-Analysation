def get_friendly_dict(friend_list):
    ''' this function takes list of friendship links 'friend_list' between 2 people as 
    argument, finds the immediate friend of each person and return a 
    dictionary of sets of all immediate friends each person has'''

    #dictionary of all immediate friends of each individual 
    friend_dict = {}

    #record each individual in dictionary, and add both individual in each other's set of 
    #friends
    for (p1, p2) in friend_list:
        add_friend(p1, p2, friend_dict)
        add_friend(p2, p1, friend_dict)
    return friend_dict

def add_friend(individual, friend, friend_dict):
    """ add the 'friend' as a friend of the 'individual' in 'friend_dict' """

    #if the individual is not yet added to the friend_dict
    if individual not in friend_dict:
        friend_dict[individual] = set()

    # add the individual set of immediate friends of 'individual'
    # using a set, so there are no duplicate names    
    friend_dict[individual].add(friend)

    
    
    
   
    