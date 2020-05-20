def friend_besties(individual, friend_list):
    '''this function takes name of an individual and friend_list from immed_fri.py, 
    then find and output sorted list of degree-one friends of the specified individual
    ''' 
    
    if individual in friend_list: 
        return sorted(friend_list[individual])
    else: 
        return []
    
    