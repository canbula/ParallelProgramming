"""
The number of blocks in the pyramid is calculated by the following formula: height * (height + 1) / 2 = number_of_blocks
Then, we simplify and solve the quadratic equation for height: height^2 + height - 2 * number_of_blocks = 0
a = 1, b = 1, c = -2 * number_of_blocks
height = −1 ± sqrt( 1^2 + 4 * 2 * number_of_blocks) / 2
The solution is the positive value of the equation, as height cannot be negative.
"""

import math

def calculate_pyramid_height(number_of_blocks : int) -> int:
    if number_of_blocks < 1:
        return 0
    return int((-1 + math.sqrt(1 + 8 * number_of_blocks)) / 2)
