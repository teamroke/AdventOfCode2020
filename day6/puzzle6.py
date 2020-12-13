def puzzle():
    with open('puzzle.input') as file_input:
        answers = 0
        groupAnswers = []
        for line in file_input:
            line = line.strip()
            if line == '':
                # print(groupAnswers)
                answers += len(set(groupAnswers))
                # print(answers)
                groupAnswers = []
                continue
            groupAnswers += groupAnswers + list(line)
        print(answers)

def puzzle2():
    with open('puzzle.input') as file_input:
        answers = 0
        groupAnswers = []
        for line in file_input:
            line = line.strip()
            if line == '':
                answers += getGroupTotal(groupAnswers)
                groupAnswers = []
                continue
            groupAnswers.append(list(line))
        print(answers)

def getGroupTotal(groupAnswers):
    toSet = []
    for group in groupAnswers:
        toSet += group 
    lettersToCheck = set(toSet)
    total = 0
    for letter in lettersToCheck:
        if checkAnswer(letter, groupAnswers):
            total += 1
    return total


def checkAnswer(letter, groupAnswers):
    for answer in groupAnswers:
        if letter not in answer:
            return False
    return True
            

puzzle()
puzzle2()
            


# Part 1
# This list represents answers from five groups:

#     The first group contains one person who answered "yes" to 3 questions: a, b, and c.
#     The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
#     The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
#     The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
#     The last group contains one person who answered "yes" to only 1 question, b.

# In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

# 6551

# Part 2
# This list represents answers from five groups:

#     In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
#     In the second group, there is no question to which everyone answered "yes".
#     In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
#     In the fourth group, everyone answered yes to only 1 question, a.
#     In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.


