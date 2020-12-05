print(
    (lambda x, y: 'Results:')(inp := tuple(map(int, open('input1.txt', 'r').read().split('\n')[:-1])), part := 0),
    '-Part-' + str(part := part + 1) + '-> ' + str((lambda x, y: x * y)(*[(x, y) for i, x in zip(range(len(inp)), inp) for y in inp[i:] if x + y == 2020][0])),
    '-Part-' + str(part := part + 1) + '-> ' + str((lambda x, y, z: x * y * z)(*[(x, y, z) for i, x in zip(range(len(inp)), inp) for j, y in zip(range(len(inp[1:])), inp[i:]) for z in inp[j:] if x + y + z == 2020][0])),
    sep='\n')
