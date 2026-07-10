"""
Guidos lasagne assignment
"""
EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 60


def bake_time_remaining(elapsed_baked_time):
    """
    returns remaining bake time
    takes elapsed baked time as parameter
    """
    return EXPECTED_BAKE_TIME - elapsed_baked_time

def preparation_time_in_minutes(number_of_layers):
    """
    returns the time taken to prepare the lasagne
    takes number of layers as parameter
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    returns the elapsed time in minutes
    takes number of laters and elapsed bake time in minutes
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time





#TODO (student): define the 'elapsed_time_in_minutes()' function below.



# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
