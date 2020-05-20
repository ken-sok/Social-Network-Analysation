def friend_besties(individual, friend_dict):
    '''this function takes name of an individual and friend_dict from immed_fri.py, 
    then find and output sorted list of degree-one friends of the specified individual
    ''' 
    
    if individual in friend_dict: 
        return sorted(friend_dict[individual])
    else: 
        return []
    
    