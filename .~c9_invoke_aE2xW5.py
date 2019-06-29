


def make_grid(cols, rows):
    grid = {}
    
    
    for  c in range(cols):  # if cols is 5 c will be 0 to 4
        for r in range(rows): # if rows is 3 r will be 0 to 2
            grid[(c, r)] = "A"
    return grid