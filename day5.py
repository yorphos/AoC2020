bpasses = []
for bpass in (open('input5.txt', 'r')).read().split('\n')[:-1]:
    row = range(127)
    col = range(7)
    for i, c in zip(range(len(bpass[:7])), bpass[:7]):
        row = ((row[:len(row) // 2] if c == 'F' else row[len(row) // 2 + 1:]) if i < len(bpass[:7]) - 1 else (tuple(row)[0] if c == 'F' else tuple(row)[0] + 1)) if c in ('F', 'B') else row
    for i, c in zip(range(len(bpass[7:])), bpass[7:]):
        col = ((col[:len(col) // 2] if c == 'L' else col[len(col) // 2 + 1:]) if i < len(bpass[7:]) - 1 else (tuple(col)[0] if c == 'L' else tuple(col)[0] + 1)) if c in ('L', 'R') else col
    bpasses.append((row, col))
for i, bid in zip(range(len(sorts := sorted([(lambda x: x[0] * 8 + x[1])(bpass) for bpass in bpasses]))), sorts):
    if i != 0 and bid - 1 != sorts[i - 1]:
        mypass = bid - 1

print(max([bpass[0] * 8 + bpass[1] for bpass in bpasses]), mypass)