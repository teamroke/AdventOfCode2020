def puzzle():
    with open('puzzle.input') as file_input:
        seats = []
        for line in file_input:
            row = 127
            line = line.strip()
            if line[0] == 'F':
                row -= 64
            if line[1] == 'F':
                row -= 32
            if line[2] == 'F':
                row -= 16
            if line[3] == 'F':
                row -= 8
            if line[4] == 'F':
                row -= 4
            if line[5] == 'F':
                row -= 2
            if line[6] == 'F':
                row -=1
            # print(row)
            seat = 7
            if line[7] == 'L':
                seat -= 4
            if line[8] == 'L':
                seat -= 2
            if line[9] == 'L':
                seat -= 1
            # print(seat)
            # print(row * 8 + seat)
            seats.append(row * 8 + seat)
        maxSeat = max(seats)
        print(maxSeat) # part1 = 980
        print(checkSeats(seats))


def checkSeats(seats):
    currentCheck = max(seats)
    for seat in seats:
        if currentCheck in seats:
            currentCheck -= 1
        else:
            return currentCheck
        





puzzle()

# For example, consider just the first seven characters of FBFBBFFRLR:

#     Start by considering the whole range, rows 0 through 127.
#     F means to take the lower half, keeping rows 0 through 63.
#     B means to take the upper half, keeping rows 32 through 63.
#     F means to take the lower half, keeping rows 32 through 47.
#     B means to take the upper half, keeping rows 40 through 47.
#     B keeps rows 44 through 47.
#     F keeps rows 44 through 45.
#     The final F keeps the lower of the two, row 44.

# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

#     Start by considering the whole range, columns 0 through 7.
#     R means to take the upper half, keeping columns 4 through 7.
#     L means to take the lower half, keeping columns 4 through 5.
#     The final R keeps the upper of the two, column 5.

# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.