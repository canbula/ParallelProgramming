def calculate_pyramid_height(number_of_blocks):
    """
    Calculates the maximum height of a pyramid given a total number of blocks.
    Each layer requires one more block than the layer above it.
    """
    height = 0
    blocks_needed_for_next_layer = 1
    
    while number_of_blocks >= blocks_needed_for_next_layer:
        number_of_blocks -= blocks_needed_for_next_layer
        height += 1
        blocks_needed_for_next_layer += 1
        
    return height


def remove_duplicates(seq: list) -> list:
    """This function removes duplicates from a list while preserving order."""
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result


def list_counts(seq: list) -> dict:
    """This function counts the number of occurrences of each item in a list."""
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(d: dict) -> dict:
    """This function reverses the keys and values of a dictionary."""
    reversed_d = {}
    for key, value in d.items():
        reversed_d[value] = key
    return reversed_d

# --- Example Usage ---
if __name__ == "__main__":
    # Pyramid example
    print(f"Pyramid Height (6 blocks): {calculate_pyramid_height(6)}") 
    
    # Sequence examples
    my_list = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Unique List: {remove_duplicates(my_list)}")
    print(f"Counts: {list_counts(my_list)}")
    
    # Dictionary example
    my_dict = {"Apple": "Red", "Banana": "Yellow"}
    print(f"Reversed Dict: {reverse_dict(my_dict)}")
