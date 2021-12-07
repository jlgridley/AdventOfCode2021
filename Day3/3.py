with open("input3", 'r') as f:
    numLines = 0
    line = f.readline().strip()
    counts = list(map(int, list(line)))
    strlen = len(counts)
    for line in f:
        numLines += 1
        for i in range(strlen):
            counts[i] += list(map(int, list(line)))
