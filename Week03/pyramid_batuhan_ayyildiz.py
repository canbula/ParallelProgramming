def calculate_pyramid_height(blocks):
    height = 0
    blocks_needed = 1  # İlk katman için gereken blok sayısı

    # Verilen bloklar yeterliyken piramidin yüksekliğini artırır
    while blocks >= blocks_needed:
        blocks -= blocks_needed  # Kullanılan blokları düşürür
        height += 1  # Bir sonraki seviyeye geçer
        blocks_needed += 1  # Her seviyede bir blok daha fazla gerekecek

    return height
