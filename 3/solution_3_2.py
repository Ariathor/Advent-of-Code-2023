import re
from collections import defaultdict
from solution_3_1 import get_adjacent_indices

with open("input.txt") as input:
    lines = [line.strip() for line in input]
    sum = 0
    candidateGears = defaultdict(set)
    for lineIdx, line in enumerate(lines):
        for number in re.finditer(r"(\d+)",line):  # Find all numbers in line
            idxStart, idxEnd = number.span()
            neighbors = list()  
            for j in range(idxStart, idxEnd):
                # More efficient to check for neighbors of *
                neighbors.extend(get_adjacent_indices(lineIdx, j, len(line), len(lines)))           
            for (row, col) in neighbors:
                if lines[row][col] == "*":
                    candidateGears[(row,col)].add((lineIdx, idxStart,idxEnd))
    for gear, numbersIdxs in candidateGears.items():
        if len(numbersIdxs) == 2:
            numbersIdxs = list(numbersIdxs)
            sum += int(lines[numbersIdxs[0][0]][numbersIdxs[0][1]:numbersIdxs[0][2]]) * \
                int(lines[numbersIdxs[1][0]][numbersIdxs[1][1]:numbersIdxs[1][2]])
    print(sum) 
            