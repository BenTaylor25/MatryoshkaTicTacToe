from dependency_importer import dep_import
dep_import("colorama")

from colorama import init, Fore, Style
init(convert = True)

def draw(grid, redlist, bluelist):
    display_grid = [row[:] for row in grid]

    for i in range(3):
        for j in range(3):
            if len(display_grid[i][j]) == 0:
                display_grid[i][j] = " "
            elif display_grid[i][j][0] == 'r':
                display_grid[i][j] = Fore.RED + display_grid[i][j][1:] + Style.RESET_ALL
            elif display_grid[i][j][0] == 'b':
                display_grid[i][j] = Fore.BLUE + display_grid[i][j][1:] + Style.RESET_ALL
            else:
                display_grid[i][j] = " "

    print("Red Counters: " + Fore.RED + ", ".join(redlist) + Style.RESET_ALL)
    print("Blue Counters: " + Fore.BLUE + ", ".join(bluelist) + Style.RESET_ALL)

    row = "\n" +"-"*11 + "\n"
    print(row.join(["|".join([f" {display_grid[y][x]} " for x in range(3)]) for y in range(3)]))
    print()
