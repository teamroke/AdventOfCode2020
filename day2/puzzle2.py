def puzzle1():
    total_right = 0
    with open('puzzle.input') as file_input:
        inputs = file_input.read().splitlines()
        for input in inputs:
            process = input.split()
            letter_count = process[2].count(process[1].split(':')[0])
            lesser = int(process[0].split("-")[0])
            greater = int(process[0].split("-")[1])
            if (letter_count >= lesser) and (letter_count <= greater):
                total_right = total_right + 1
    print(total_right)


def puzzle2():
    total_right = 0
    with open('puzzle.input') as file_input:
        inputs = file_input.read().splitlines()
        for input in inputs:
            process = input.split()
            letter = process[1].split(':')[0]
            first= int(process[0].split("-")[0]) - 1
            second = int(process[0].split("-")[1]) - 1
            if (letter == process[2][first]):
                if (letter != process[2][second]):
                    total_right = total_right + 1
            else:
                if (letter == process[2][second]):
                    total_right = total_right + 1

    print(total_right)

puzzle1()
puzzle2()