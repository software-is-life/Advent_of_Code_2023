"""
12 red cubes, 13 green cubes, and 14 blue cubes
"""

colors_threshold = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

input_file = open('./day2/input.txt', 'r')
lines = input_file.readlines()
total_id = 0

def remove_comma(str):
    output = []
    for elem in str:
        if elem not in [",", "\n"]:
            output.append(elem)
    return "".join(output)

i = 1
line_good = True
# question 1
for line in lines:
    row_arr = line.split(":")[1].split(";")

    for row in row_arr:
        info = row.split(" ")
        info = info[1:]
        for x in range(0, len(info), 2):
            num = int(info[x])
            color = remove_comma(info[x+1])

            if num > colors_threshold[color]:
                line_good = False
                break

    if line_good:
        total_id += i
    i += 1
    line_good = True

print(total_id)

#question 2
sum_of_powers_total = 0
for line in lines:
    row_arr = line.split(":")[1].split(";")

    red_max = 0
    green_max = 0
    blue_max = 0
    for row in row_arr:
        info = row.split(" ")
        info = info[1:]
        for x in range(0, len(info), 2):
            num = int(info[x])
            color = remove_comma(info[x+1])

            if color == "red":
                red_max = max(red_max, num)
            elif color == "green":
                green_max = max(green_max, num)
            else:
                blue_max = max(blue_max, num)

    sum_of_powers_total += (red_max * green_max * blue_max)
print(sum_of_powers_total)