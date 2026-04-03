import other_file


other_file._protected_function()


def distance(from_, to_):
    return to_ - from_


other_object = other_file.OtherClass()
print(other_object.puclic_var)
print(other_object._protected_var)
print(other_object._OtherClass__private_var)
