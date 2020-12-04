def puzzle():
    with open('puzzle.input') as file_input:
        inputs = file_input.read().splitlines()
        line_length = len(inputs[0])
        start = 0
        trees = 0
        for i in range(1, len(inputs)):
            start = start + 3
            if start >= line_length:
                start = start - line_length
            if inputs[i][start] == '#':
                trees = trees + 1
        print(trees)


    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.


# This is horrible horrible code but I struggled on skipping lines.
# Will revisit it later as I am not proud at all of this.
def puzzle2():
    with open('puzzle.input') as file_input:
        inputs = file_input.read().splitlines()
        line_length = len(inputs[0])
        side = [1, 3, 5, 7, 1]
        total_trees = 0
        for i in range(len(side)):
            start = 0
            trees = 0
            if i < 4:
                for j in range(1, len(inputs)):
                    start = start + side[i]
                    if start >= line_length:
                        start = start - line_length  
                    if inputs[j][start] == '#':
                        trees = trees + 1
                if total_trees == 0:
                    total_trees = trees
                else:
                    total_trees = total_trees * trees
            else:
                h = 0
                for j in range(1, len(inputs)):
                    start = start + side[i]
                    if start >= line_length:
                        start = start - line_length
                    h = h + 2
                    if h >= len(inputs):
                        break  
                    if inputs[h][start] == '#':
                        trees = trees + 1
                if total_trees == 0:
                    total_trees = trees
                else:
                    total_trees = total_trees * trees
        print(total_trees)



puzzle() #159
puzzle2() #6419669520