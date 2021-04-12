import random
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 2],
    [1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

def start_position(maze):
    x = random.randrange(len(maze))
    y = random.randrange(len(maze))
    while maze[x][y] != 0:
        x = random.randrange(len(maze))
        y = random.randrange(len(maze))
    return x, y

def end_game(x, y):
    return (maze[x][y] == 2)

def valid_move(x):
    next_x = x + (random.randrange(3) - 1)

    while next_x >= len(maze) or next_x < 0:
        next_x = x + (random.randrange(3) - 1)

    return next_x

def next_move(x, y):
    next_x = valid_move(x)
    next_y = valid_move(y)

    while maze[next_x][next_y] == 1:
        next_x = valid_move(x)
        next_y = valid_move(y)

    return next_x, next_y

def start_game(maze):
    x, y = start_position(maze)
    seconds = 1

    while end_game(x, y) == False:
        x, y = next_move(x, y)
        seconds += 1
    
    return seconds

seconds = start_game(maze)
print(f"The game lasted {seconds} {'second' if seconds == 1 else 'seconds'}")