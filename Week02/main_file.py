"""
from other_file import *

public_function()
_protected_function() # error
__private_function() # error
"""

import other_file

other_file.public_function()
other_file._protected_function()
other_file.__private_function()

other_class = other_file.OtherClass()
print(other_class.public_var)
print(other_class._protected_var)
# print(other_class.__private_var) # raise error
print(other_class._OtherClass__private_var)