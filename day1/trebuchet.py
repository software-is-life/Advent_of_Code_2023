number_text_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

input_file = open('./day1/input.txt', 'r')
lines = input_file.readlines()

total = 0

for line in lines:
    indices_and_number = []
    for i in range(len(line)):
        ch = line[i]
        if ch.isdigit():
            indices_and_number.append((i, int(ch))) # (index, char)
        else:
            for key in number_text_to_num.keys():
                if i + len(key) < len(line) and line[i: i+len(key)] == key:
                    indices_and_number.append((i, number_text_to_num[key]))

    indices_and_number.sort(key=lambda x : x[0])
    print(indices_and_number)
    total += (indices_and_number[0][1] * 10) + indices_and_number[-1][1]
print(total)