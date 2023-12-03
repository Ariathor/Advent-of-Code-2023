numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


sum = 0
with open("input.txt") as input:
    for line in input:
        first = None
        last = None
        for char in line:
            if first is None and char.isdigit():
                first = int(char)
                break;
        for char in reversed(line):
            if last is None and char.isdigit():
                last = int(char)
                break;

        if first is None and last is None:
            first = last = 0

        sum += first*10 + last  # If there are no digits in line
print(sum)
 