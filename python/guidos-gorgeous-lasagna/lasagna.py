"""
Define 40 minutes bake time expected
Define 2 minutes for preparation
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Function: 
    Calculate actual minutes the lasagna has been in the oven
    Return how many minutes lasagna still need to baked
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Function:
    Takes number of layers you want to add to the lasagna
    Return how manuy minutes you would spend making them
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Function:
    Take two parameter which are number of layers and elapsed bake time
    Return total minutes have been in the kitchen cooking
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
