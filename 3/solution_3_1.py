import re

def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    if i + 1 < m and j+1 < n:
        adjacent_indices.append((i+1, j+1))
    if i > 0 and j + 1 < n:
        adjacent_indices.append((i-1, j+1))
    if i + 1 < m and j > 0:
        adjacent_indices.append((i+1, j-1))
    return adjacent_indices

if __name__ == "__main__":
    with open("input.txt") as input:
        lines = [line.strip() for line in input]
        sum = 0
        for lineIdx, line in enumerate(lines):
            for number in re.finditer(r"(\d+)",line):  # Find all numbers in line
                idxStart, idxEnd = number.span()
                neighbors = list()
                for j in range(idxStart, idxEnd):
                    # More efficient to check every index as it's identified, but doesn't matter here
                    neighbors.extend(get_adjacent_indices(lineIdx, j, len(line), len(lines)))          
                for (row, col) in neighbors:
                    if lines[row][col] != "." and not lines[row][col].isdigit():
                        sum += int(line[idxStart:idxEnd])
                        break;
        print(sum) 
            