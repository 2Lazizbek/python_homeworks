h, w = map(int, input().split())
grid = []
y_max = 0
y_min = h
for i in range(h):
    text = input()
    grid.append([j for j in text])
    if y_min == h and '#' in grid[i]:
        x = grid[i].index('#')
        y_min = i
    if '#' not in grid[i] and y_min != h:
        y_max = i-1
        break
    elif y_max == 0 and i == h-1:
        y_max = i
        break
y = (y_max + y_min)//2
print(x, y)
print(f"({y+1}, {x+1})")