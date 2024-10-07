def calculate_pyramid_height(number_of_blocks):
  height = 0
  block_used = 0
  layer = 1

  while block_used + layer <= number_of_blocks:
    blocks_used += layer
    height += 1
    layer += 1

  missing_blocks = layer - (number_of_blocks - blocks_used) if blocks_used != number_of_blocks else 0

  return height, missing_blocks

number_of_blocks = int(input("Enter the number of blocks for the pyramid: "))
height, missing_blocks = calculate_pyramid_height(number_of_blocks)
print(f"The height of the pyramid: {height}")

if missing_blocks > 0:
  print(f"Missing blocks to complete the pyramid: {missing_blocks}")
else:
  print("Pyramid is complete")
