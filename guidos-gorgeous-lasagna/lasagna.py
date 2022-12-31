
EXPECTED_BAKE_TIME = 40 # EXPECTED_BAKE_TIME
PREPARATION_TIME = 2
def bake_time_remaining(minutes):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return EXPECTED_BAKE_TIME - minutes
    
def preparation_time_in_minutes(layers):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time

            
