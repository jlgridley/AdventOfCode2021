scores = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137,
}

matches = {
    ")" : "(",
    "]" : "[",
    "}" : "{",
    ">" : "<",
}

score = 0
with open("input10") as f:
    for line in f:
        stack = []
        for char in line.strip():
            if char in scores:
                if stack[-1] != matches[char]:
                    score += scores[char]
                    break
                else:
                    stack.pop()
            else:
                stack.append(char)
print(score)
