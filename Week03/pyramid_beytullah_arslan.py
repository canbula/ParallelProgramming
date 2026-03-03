def calculate_pyramid_height(number_of_blocks):
    if number_of_blocks <= 0:
        return 0
    height = int((-1 + (1 + 8 * blocks) ** 0.5) / 2) 
    return height #O(1)

# def calculate_pyramid_height(number_of_blocks): 
#     number_of_blocks = 1
#     while True:
#         if blocks < height:
#             height = height-1
#             break
#         blocks = blocks - height
#         height += 1
#     return height O(n)
