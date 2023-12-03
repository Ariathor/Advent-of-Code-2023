numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum = 0
with open("input.txt") as input:
    for line in input:
        first = None
        last = None
        for ind, char in enumerate(line):
            line = line.strip()
            if char.isdigit():
                first = int(char)
                break;
            else:
                try:
                    if line[ind:ind+3] in numbers:
                        first = numbers[line[ind:ind+3]]
                    elif line[ind:ind+4] in numbers:
                        first = numbers[line[ind:ind+4]]
                    elif line[ind:ind+5] in numbers:
                        first = numbers[line[ind:ind+5]]
                    if first:
                        print(f"FOUND {first=} in {line=}")
                        break;
                except IndexError:
                    pass
        for ind, char in enumerate(reversed(line)):
            ind = len(line) - ind  # Count from the end
            if last is None and char.isdigit():
                last = int(char)
                break;
            else:
                try:
                    if line[ind-3:ind] in numbers:
                        last = numbers[line[ind-3:ind]]
                    elif line[ind-4:ind] in numbers:
                        last = numbers[line[ind-4:ind]]
                    elif line[ind-5:ind] in numbers:
                        last = numbers[line[ind-5:ind]]
                    if last:
                        print(f"FOUND {last=} in {line=}")
                        break;
                except IndexError:
                    pass
            
        if first is None and last is None:  # If there are no numbers in line
            first = last = 0
        print(f"{first=}, {last=}")
        sum += first*10 + last
print(sum)
 