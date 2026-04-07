def calculate_pyramid_height(n):
    height = 0
    blocks = 0
    
    while blocks + height + 1 <= n:
        height += 1
        blocks += height
        
    return height
