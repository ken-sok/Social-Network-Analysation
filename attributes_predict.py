from one_indiv_immed_fri import friend_besties
from second_degree_fri import friend_second_besties
from collections import defaultdict

#adapted from University of Melbourne's sample solution

def predict_attribute(friends, feat_dict, feature):
    """predict the target 'feature' from the set 'friends' based on the
    attributes in 'feat_dict' """

    # dictionary for counting attribute frequency among 'friends'
    freq = defaultdict(int)

    #add vote for feature if feature exists as friend's 
    for friend in friends:
        if friend in feat_dict and feature in feat_dict[friend]:
            freq[feat_dict[friend][feature]] += 1

    #in case there is at least 1 count of target feature among 'friends', 
    #find which attribute has majority count to predict
    if freq:
        max_count = 0
        for attribute, count in freq.items():
            if count > max_count:
                att_list = [attribute]
                max_count = count
            elif count == max_count:
                att_list.append(attribute)
        return sorted(att_list)

    #if no attributes of feature are found, return empty list
    else:
        return []


def friendly_prediction(unknown_user, features, friend_dict, feat_dict):
    
    '''friendly_prediction takes name of 'unkwown_user', target 'features' to predict, 
    information of friends in 'friend_dict' and predicts features of that person according 
    to their friends' attributes in 'feat dict'
    '''
    # to record predictions about unknown_user's features
    feat_user={}
    
    # check if the user is in the social network or not
    if unknown_user in friend_dict: 

        # look for features of 1st degree friend to predict unkown_user's 
        for feature in features:

            predict_closeFri_attribute = predict_attribute(friend_besties(unknown_user,
                                            friend_dict), feat_dict, feature)

            #use degree one friends' attribute for feature if it exists
            if (predict_closeFri_attribute): 
                feat_user[feature] = predict_closeFri_attribute

            #in case no degree one friends have attribute for target feature, check degree two's     
            else: 
                predict_second_deg_attribute = predict_attribute(friend_second_besties(unknown_user,
                                            friend_dict), feat_dict, feature)
                feat_user[feature] = predict_second_deg_attribute                            

            
    return feat_user
       

        
                
           

                    
                   
                    

            
           