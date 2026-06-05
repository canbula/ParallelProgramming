def calculate_pyramid_height(blocks):
    total = 0
    for i in range(1, blocks + 1):
        total += i
        if total > blocks:
            return i - 1
    return i
