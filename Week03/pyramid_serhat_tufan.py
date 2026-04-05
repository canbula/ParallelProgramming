
def calculate_pyramid_height(number: int) -> int :
    height=0
    needed=1
    while number>0:
        if number >= needed:
            height+=1 
            number= number -1*needed
            needed+= 1
        else:
            print("else awoken")
            break
    print(f"number is +{number}")
    return height
# print(calculate_pyramid_height(100000))
