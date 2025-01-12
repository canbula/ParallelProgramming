def calculate_pyramid_height(number_of_blocks):
    height = 0
    layer = 1  # Her seviyedeki blok sayısı
    
    while number_of_blocks >= layer:  # Yeterli blok olduğu sürece
        number_of_blocks -= layer  # Blokları azalt
        height += 1  # Yüksekliği artır
        layer += 1  # Bir sonraki seviyeye geç
    
    return height
