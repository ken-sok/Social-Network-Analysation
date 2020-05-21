
#adapted from University of Melbourne's sample solution

from one_indiv_immed_fri import friend_besties
from second_degree_fri import friend_second_besties

def besties_coverage(individuals, friend_dict, relationship_list):
    
    """
    calculate the proportion of individuals are connected in the network
    """

    #set to include connected individuals in network according to 
    #relationship type in relationship list
    #individual themselves are also included
    network = set()

    for individual in individuals:

        # only add the individual to network if in friend_dict
        if individual in friend_dict:
            network.add(individual)

        #adding people to network according to degree of friendship
        for relationship in relationship_list:
            network = network.union(relationship(individual, friend_dict))

    return len(network) / len(friend_dict)

