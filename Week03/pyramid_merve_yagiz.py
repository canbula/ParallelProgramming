
# number_of_blocks = 10

def calculate_pyramid_height(number_of_blocks):
    block = 1
    height = 0
    while number_of_blocks >= block:  # Koşulu düzelttik
        number_of_blocks -= block      # number_of_blocks değerini güncelliyoruz
        #print("Kalan blok:", number_of_blocks)
        height += 1
        #print("Height:", height)
        block += 1
        #print("Block:", block)
    return height

# Fonksiyonu çağırarak sonucu görelim
#print("Pyramid height:", calculate_pyramid_height(number_of_blocks))
    
