number_grid = [[7, 2, 3], [4, 3, 6], [7, 1, 9], [4,3,2]]

# for row, numbers in enumerate(number_grid):
    # for number in row:
        # print(row)


flat = [i for row in number_grid 
        for i in row]

print(flat)