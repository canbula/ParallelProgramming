def calculate_pyramid_height(cube_number):
    total_cube = 0
    height = 0
    
    while total_cube < cube_number:
        height += 1
        total_cube += height
        if total_cube == cube_number:
            return height
