def get_input():
    with open("04") as f:
        for line in f.readlines():
            yield line.strip()

def duplicate_from_indices(puzzle: list[str], y:int, x:int):
    up, down, left, right, ul, ur, dl, dr = "", "", "", "", "", "", "", ""
    height = len(puzzle)
    width = len(puzzle[0])
    if y > 2:
        up = puzzle[y][x] + puzzle[y-1][x] + puzzle[y-2][x] + puzzle[y-3][x]
    if y < height - 3:
        down = puzzle[y][x] + puzzle[y+1][x] + puzzle[y+2][x] + puzzle[y+3][x]
    
    if x > 2:
        left = puzzle[y][x] + puzzle[y][x-1] + puzzle[y][x-2] + puzzle[y][x-3]
    if x < width - 3:
        right = puzzle[y][x] + puzzle[y][x+1] + puzzle[y][x+2] + puzzle[y][x+3]
    #ul, ur, dl, dr
    
    if up and left:
        ul = puzzle[y][x] + puzzle[y-1][x-1] + puzzle[y-2][x-2] + puzzle[y-3][x-3]
    if up and right:
        ur = puzzle[y][x] + puzzle[y-1][x+1] + puzzle[y-2][x+2] + puzzle[y-3][x+3]
    if down and left:
        dl = puzzle[y][x] + puzzle[y+1][x-1] + puzzle[y+2][x-2] + puzzle[y+3][x-3]
    if down and right:
        dr = puzzle[y][x] + puzzle[y+1][x+1] + puzzle[y+2][x+2] + puzzle[y+3][x+3]
    return up, down, left, right, ul, ur, dl, dr

def main1():
    input = list(get_input())
    quads: list[str] = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            quads.extend(duplicate_from_indices(input, y, x))
    matches = 0
    for quad in quads:
        if quad == "XMAS":
            matches += 1
    print(matches)
main1()

def main2():
    input = list(get_input())
    acceptable = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == "A":
                try:
                    if (input[y-1][x-1], input[y+1][x+1]) in (("M", "S"), ("S", "M")):
                        if (input[y-1][x+1], input[y+1][x-1]) in (("M", "S"), ("S", "M")):
                            acceptable += 1
                except:
                    ...
    print(acceptable)
main2()