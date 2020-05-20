def friend_besties(individual, friend_list):
    '''this function takes individual and friend_list as arg then find and output 
    sorted list of degree-one friends of specified individual
    ''' 
    
    if individual in friend_list: 
        return sorted(friend_list[individual])
    else: 
        return []
    
    