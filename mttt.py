import os
from display import draw

def move(turn, grid, redlist, bluelist):
    players = ["One", "Two"]
    colours = ["r", "b"]
    colLists = [redlist, bluelist]

    while True:
        x = input(f"Player { players[turn] }:")

        wrong_format = len(x) != 3 or not x.isdecimal()
        if wrong_format:
            continue

        col = int(x[0])
        row = int(x[1])
        val = int(x[2])

        out_of_bounds = min([row, col, val]) < 0 or max([row, col]) > 2 or val > 5
        if out_of_bounds:
            continue
        
        colour = colours[turn]

        val_available = True
        for r in grid:
            for item in r:
                if item == colour+str(val):
                    val_available = False
        if not val_available:
            continue

        current = grid[row][col]
        if current != "":
            if current[0] == colour:
                continue

            if int(current[1]) >= val:
                continue
        
        grid[row][col] = colour+str(val)
        colLists[turn].remove(str(val))
        print()
        break

def to_col(sl):
    nsl = [x for x in sl]
    for i in range(3):
        if len(nsl[i]) == 0:
            nsl[i] = ""
        else:
            nsl[i] = nsl[i][0]
    return nsl

def check_game_over(grid, redlist, bluelist):
    game_over = False
    game_draw = False
    red_win = False

    if len(redlist + bluelist) == 0:
        game_over = True
        game_draw = True

    grid_full = True
    for row in grid:
        for itm in row:
            grid_full = grid_full and (itm)
    if grid_full:
        game_over = True
        game_draw = True

    col_grid = [to_col(row[:]) for row in grid]

    # check row
    for row in col_grid:
        if "" not in row:
            if row.count("b") == 3 or row.count("r") == 3:
                if row.count("r") == 3:
                    red_win = True
                game_over = True

    # check col
    for c in range(3):
        col = [row[c] for row in col_grid]
        
        if col.count("b") == 3 or col.count("r") == 3:
            if row.count("b") == 3:
                red_win = True
            game_over = True
    
    # check (n, n) diag
    diag1 = [col_grid[i][i] for i in range(3)]
    if diag1.count("r") == 3 or diag1.count("b") == 3:
        if diag1.count("r") == 3:
            red_win = True
        game_over = True
    
    # check (n, 2-n) diag
    diag2 = [col_grid[i][2-i] for i in range(3)]
    if diag2.count("r") == 3 or diag2.count("b") == 3:
        if diag2.count("r") == 3:
            red_win = True
        game_over = True


    return game_over, game_draw, red_win


def start_game():
    redlist = [str(x) for x in range(1, 6)]
    bluelist = [str(x) for x in range(1, 6)]
    grid = [['' for _ in range(3)] for _ in range(3)]
    turn = 0
    game_loop = True
    draw(grid, redlist, bluelist)
    while game_loop:
        move(turn, grid, redlist, bluelist)
        os.system("cls" if os.name == "nt" else "clear")
        draw(grid, redlist, bluelist)

        game_over, game_draw, red_win = check_game_over(grid, redlist, bluelist)
        if game_over:
            if game_draw:
                print("draw")
            else:
                players = ["One", "Two"]
                print(f"Player {players[not red_win]} Wins!")
            game_loop = False
        turn = 1 - turn


start_game()
