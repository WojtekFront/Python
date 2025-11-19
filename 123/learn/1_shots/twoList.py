number_grid = [[7, 2, 3], [4, 3, 6], [7, 1, 9], [4,3,2]]

for row in number_grid:
    for number in row:
        print(number)


# print(number_grid[0][0])


flat = [i for row in number_grid 
        for i in row]

print(flat)
