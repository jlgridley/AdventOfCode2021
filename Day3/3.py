with open("input3", 'r') as f:
    numLines = 1
    line = f.readline().strip()
    counts = list(map(int, list(line.strip())))
    strlen = len(counts)
    for line in f:
        numLines += 1
        currCounts = list(map(int, list(line.strip())))
        for i in range(strlen):
            counts[i] += currCounts[i]

threshold = numLines // 2 + (numLines % 2 != 0)

gamma = ["1" if count >= threshold else "0" for count in counts]
gamma = int("".join(gamma), 2)
mask = ~(-1 << strlen)
print("solution:", gamma * (~gamma & mask))
