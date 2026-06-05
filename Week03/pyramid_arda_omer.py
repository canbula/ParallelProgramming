def calculate_pyramid_height(number_of_blocks):
    current_height = 0
    blocks_needed_for_next_level = 1
    remaining_blocks = number_of_blocks

    while True:
        if remaining_blocks < blocks_needed_for_next_level:
            break

        remaining_blocks = remaining_blocks - blocks_needed_for_next_level
        current_height = current_height + 1
        blocks_needed_for_next_level = blocks_needed_for_next_level + 1

    return current_height