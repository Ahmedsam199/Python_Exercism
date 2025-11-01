"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides functions to calculate bake and preparation times
for making a lasagna.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # in minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes it still needs to bake
    based on the EXPECTED_BAKE_TIME.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of lasagna layers.
    :return: int - total preparation time (in minutes).

    Each layer takes PREPARATION_TIME minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (prep + bake).

    :param number_of_layers: int - the number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time spent (in minutes).

    This function returns the total time spent making the lasagna,
    which is the sum of preparation time and elapsed baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
