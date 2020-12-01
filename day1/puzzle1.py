
def puzzle1():
    with open('puzzle1.input') as file_input:
        inputs = file_input.read().splitlines()
        for input in inputs:
            right = int(input)
            left = 2020 - right
            if str(left) in inputs:
                print(int(input) * left)
                return


def puzzle2():
    with open('puzzle1.input') as file_input:
        inputs = file_input.read().splitlines()
        for input in inputs:
            right = int(input)
            for input in inputs:
                left = 2020 - right - int(input)
                if str(left) in inputs:
                    print(int(input) * right * left)
                    return

puzzle1() # 955584
puzzle2() # 287503934

