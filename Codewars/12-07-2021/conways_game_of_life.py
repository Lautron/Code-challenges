import pprint
cells = [
    [1,0,0],
    [0,1,1],
    [1,1,0],
]
def get_alive_neighbors(coords, cells):
    y, x = coords
    y_size, x_size = len(cells), len(cells[0])
    neighbor_coords = [cells[Y][X] for Y in [y-1, y, y+1] 
                                   for X in [x-1, x, x+1] 
                                   if (Y,X) != (y,x) and 0 <= X < x_size and 0 <= Y < y_size]
    return sum(neighbor_coords)
    
def does_cell_live(is_alive, alive_neighbors):
    if alive_neighbors < 2: return False
    if alive_neighbors > 3: return False
    if alive_neighbors == 3: return True
    if alive_neighbors == 2 and is_alive: return True
    else: return False

def get_generation(cells, generations):
    result = [[None for i in range(len(cells[0]))] for j in range(len(cells))] 
    # for each generation
    for generation in range(generations):
        # loop through every cell with enumerate
        for row, items in enumerate(cells):
            for col, cell in enumerate(items): 
                is_alive = True if cell else False
                alive_neighbors = get_alive_neighbors((row, col), cells)
                # decide if cell dies, lives or revives
                cell_lives = does_cell_live(is_alive, alive_neighbors)
                print(is_alive, alive_neighbors, cell_lives, row, col)
                if cell_lives: 
                    result[row][col] = 1
                else:
                    result[row][col] = 0
    return result

pprint.pprint(get_generation(cells, 1))
