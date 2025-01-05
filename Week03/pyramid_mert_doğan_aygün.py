def find_pyramid_height(total_blocks):
    current_height = 0
    for _ in range(total_blocks):
        current_height += 1
        if current_height * (current_height + 1) // 2 > total_blocks:
            current_height -= 1
            break
    return current_height
