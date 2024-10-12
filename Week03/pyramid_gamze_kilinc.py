def calculate_pyramid_height(number_of_blocks):
    height = 0
    total_blocks = 0 

  
        height += 1 
        total_blocks += height 

   
    if total_blocks > number_of_blocks:
        height -= 1

    return height 


blocks = int(input("Lütfen blok sayısını girin: "))


