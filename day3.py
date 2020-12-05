from functools import reduce
import math
m = (open('input3.txt', 'r')).read()
lines = m.split('\n')[:-1]
height = len(lines)
length = len(lines[0])

# currXs, currYs = ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0))
# xDeltas, yDeltas = ((1, 3, 5, 7, 1), (1, 1, 1, 1, 2))
# nums = []
# numTrees = 0
# for currX, currY, deltaX, deltaY in zip(currXs, currYs, xDeltas, yDeltas):
#     while(currY < height):
#         numTrees += 1 if lines[currY][currX % length] == '#' else 0
#         currX += deltaX
#         currY += deltaY
#     nums += [numTrees]
#     numTrees = 0
# print(nums[1], reduce((lambda x,y: x * y), [range(0, length, dX), range(0, height, dY) for dX, dY in zip((1, 3, 5, 7, 1), (1, 3, 5, 7, 1))), for cX, cY, dX, dY in  for ]))
x = [list(zip(*(list(Xs) * math.ceil(len(Ys) / len(Xs)), Ys) if len(Xs) < len(Ys) else (list(Ys) * math.ceil(len(Xs) / len(Ys)), Xs))) for Xs, Ys in [(range(0, length, dX), range(0, height, dY)) for dX, dY in zip((1, 3, 5, 7, 1), (1, 1, 1, 1, 2))]]
y = ([(lambda x, y: 1 if lines[y][x] == '#' else 0)(x, y) for x, y in x[1]])
print(lines)
#print(sum(y), x[1]) # sum([1 if lines[y][x] == '#' else 0 for x, y in zip(Xs, Ys)])