def friend_second_besties(individual, friend_dict):
    '''
    this function takes in 'individual' and 'friend_dict', then finds and output 
    a sorted list of degree-two friends/ friend of a friend of 'individual' through 
    'friend_dict'
    '''
    # list of degree-two friends
    degree_2=[]
    
    # test whether individual is in friend_dict or not
    if individual in friend_dict:
        
        # search through each person in friend_dict
        for name in friend_dict: 
            
            # avoid looking in own name for degree one friend
            if individual != name: 
                
                # if friend of individual is also a friend of another 
                # person and if the individual is not a friend of that 
                # other person, then we get degree two friend
                if (individual not in friend_dict[name] and
                    friend_dict[individual] & friend_dict[name]): 
                    degree_2.append(name)
        
        return sorted(degree_2)
    
    
    
   
        