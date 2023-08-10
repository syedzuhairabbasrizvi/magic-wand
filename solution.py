def get_adjacent_pixels(image, visited, row, col, color):
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
        return 0

    if visited[row][col] or image[row][col] != color:
        return 0

    visited[row][col] = True
    count = 1

    count += get_adjacent_pixels(image, visited, row + 1, col, color)
    count += get_adjacent_pixels(image, visited, row - 1, col, color)
    count += get_adjacent_pixels(image, visited, row, col + 1, color)
    count += get_adjacent_pixels(image, visited, row, col - 1, color)

    return count

def magic_wand(image, color):
    visited = [[False] * len(image[0]) for _ in range(len(image))]
    largest_selection = 0

    for row in range(len(image)):
        for col in range(len(image[0])):
            if not visited[row][col] and image[row][col] == color:
                selection_size = get_adjacent_pixels(image, visited, row, col, color)
                if selection_size > largest_selection:
                    largest_selection = selection_size

    return largest_selection

# Input
row = int(input())
image_row=[]
image=[]
for x in range(row):
    image_row = input()
    image.append(image_row)
color=input()

# Find the largest possible selection
largest_selection = magic_wand(image, color)
print(largest_selection)
