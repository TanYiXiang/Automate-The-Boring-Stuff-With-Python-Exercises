# This program 'rotates' the grid ninety degrees to form a more eligible pattern.


def rotate_ninety_degree(grid_to_rotate):
    """ Prints list column wise """
    for y in range(len(grid_to_rotate[0])):
        for x in range(len(grid_to_rotate)):
            print(grid_to_rotate[x][y], end=" ")
        print('\n')


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rotate_ninety_degree(grid)
