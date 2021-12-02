def marineposition():
    file = open("input")
    input = file.readlines()
    horizontal, depth = 0, 0
    for line in input:
        coordinates = line.split(" ")
        #coordinates[1] = coordinates[1].split("\n")[0]
        if coordinates[0] == "forward":
            horizontal += int(coordinates[1])
        elif  coordinates[0] == "down":
            depth += int(coordinates[1])
        elif coordinates[0] == "up":
            depth -= int(coordinates[1])
    return horizontal*depth

def aimposition():
    file = open("input")
    input = file.readlines()
    horizontal, depth, aim = 0, 0, 0
    for line in input:
        coordinates = line.split(" ")
        # coordinates[1] = coordinates[1].split("\n")[0]
        if coordinates[0] == "forward":
            horizontal += int(coordinates[1])
            depth += aim*int(coordinates[1])
        elif coordinates[0] == "down":
            aim += int(coordinates[1])
        elif coordinates[0] == "up":
            aim -= int(coordinates[1])
    return horizontal * depth


print(marineposition())
print(aimposition())
