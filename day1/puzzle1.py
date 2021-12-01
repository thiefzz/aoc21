def count_increase():
    file = open("input")
    input = file.readlines()
    count = 0
    previous = 99999
    for line in input:
        number = int(line)
        if number > previous:
            count += 1
        previous = number
    return count


def count_slide():
    file = open("input")
    lines = file.readlines()
    count = 0
    num1 = int(lines[0])
    num2 = int(lines[1])
    num3 = int(lines[2])
    previous = num1
    # only need to check if number you toss away is bigger than new number
    # keep in mind its len(lines) as range goes until but does not include that integer
    for line in range(3, len(lines)):
        num1 = num2
        num2 = num3
        num3 = int(lines[line])
        if num3 > previous:
            count += 1
        previous = num1
    return count


print(count_increase())
print(count_slide())
