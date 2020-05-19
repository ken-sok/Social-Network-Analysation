def get_friendly_dict(friend_list):
    ''' this function takes list of friendship links between 2 people as 
    argument, finds the immediate friend of each person and return a 
    dictionary of friends each person has'''
    
    # dictionary of friend each person has 
    key_names = {}
    # find all unique names in friend_list and set as key to dictionary
    for i in range(0, len(friend_list)): 
        
        # look through each tuple for unique name and one friend
        for j in range(0, len(friend_list[i]) - 1):
            if friend_list[i][j] not in key_names: 
                key_names[friend_list[i][j]] = {friend_list[i][j + 1]}
            if friend_list[i][j + 1] not in key_names: 
                key_names[friend_list[i][j + 1]] = {friend_list[i][j]}
   
            # find the other friends each person has
            if friend_list[i][j] in key_names: 
                key_names[friend_list[i][j]].add(friend_list[i][j + 1])
                key_names[friend_list[i][j + 1]].add(friend_list[i][j])
    
    return key_names           

    
    
    
   
    