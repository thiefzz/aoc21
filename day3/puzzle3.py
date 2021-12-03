def find_gamma():
    file = open("input")
    input = file.readlines()
    # initialize the array (to prevent errors)
    values = [0,0,0,0,0,0,0,0,0,0,0,0]
    # check each number of the file
    for line in input:
        # count all ones in each position and sum them
        for bit in range(0 , len(line)-1):
            values[bit] += int(line[bit])
    gamma = []
    # find the most common number (0 or 1) for each bit position
    for i in range(0, len(values)):
        if values[i] >= (len(input)/2):
            gamma.append(1)
        else:
            gamma.append(0)
    gamma_rate = 0
    epsilon_rate = 0
    for i in range(0, len(gamma)):
        # 2^i
        number = 2 ** i
        # check if the ith bit is a 1 then add this value to gamma else to epsilon
        if gamma[len(gamma)-1-i] == 1:
            gamma_rate += number
        else:
            epsilon_rate += number
    # return the value that is requested
    return gamma_rate*epsilon_rate


def bit_criteria():
    file = open("input")
    input = file.readlines()
    # copy input since we need it twice (for oxygen and for scrubber)
    leftover = input.copy()
    # position of the bit we want
    check = 0
    # find the oxygen rate value, continue loop until 1 value remains
    while len(leftover) > 1:
        # copy leftover since we want to check every value but cant remove while looping through it (gives errors)
        remove = leftover.copy()
        # find the most common bit see helper function find_most_common (similar approach as in find_gamma)
        most_common = find_most_common(leftover, check)
        # now check for each value in leftover if the bit at position check
        for line in leftover:
            if int(line[check]) != most_common:
                remove.remove(line)
        # now update leftover without the incorrect numbers
        leftover = remove
        # increase the bit we want to check, use modulo to go back from 11 to 0 (modulo is not required here I believe)
        check = (check + 1) % 12
    # this is our oxygen value we covert the string to an int value expecting a binary number (the 2)
    oxygen = int(leftover[0],2)
    leftover = input.copy()
    check = 0
    # same approach as with oxygen but now check the least common
    while len(leftover) > 1:
        remove = leftover.copy()
        least_common = find_least_common(leftover, check)
        for line in leftover:
            if int(line[check]) != least_common:
                remove.remove(line)
        leftover = remove
        check = (check + 1) % 12
    scrubber = int(leftover[0], 2)
    return oxygen*scrubber

def find_most_common(numbers, check):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in numbers:
        for bit in range(0, len(line) - 1):
            values[bit] += int(line[bit])
    most = []
    for i in range(0, len(values)):
        if values[i] >= (len(numbers) / 2):
            most.append(1)
        else:
            most.append(0)
    return most[check]


def find_least_common(numbers, check):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in numbers:
        for bit in range(0, len(line) - 1):
            values[bit] += int(line[bit])
    least = []
    for i in range(0, len(values)):
        if values[i] < (len(numbers) / 2):
            least.append(1)
        else:
            least.append(0)
    return least[check]


print(find_gamma())
print(bit_criteria())
