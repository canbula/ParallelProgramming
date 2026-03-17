an_outside_variable = 10
a_global_variable = 20
a_list = [1, 2, 3, 4, 5]


def a_function():
    an_outside_variable = 30
    global a_global_variable
    a_global_variable = 40
    a_local_variable = 50
    print("Inside a_function:")
    print("an_outside_variable:", an_outside_variable)
    print("a_global_variable:", a_global_variable)
    print("a_local_variable:", a_local_variable)


def another_function(the_list):
    the_list.append(6)
    print("Inside another_function:")
    print("a_list:", the_list)


a_function()

print("Outside a_function:")
print("an_outside_variable:", an_outside_variable)
print("a_global_variable:", a_global_variable)
# print("a_local_variable:", a_local_variable)

another_function(a_list)

print("Outside another_function:")
print("a_list:", a_list)
# print("the_list:", the_list)


def fun():
    return


print(0 % 2)
