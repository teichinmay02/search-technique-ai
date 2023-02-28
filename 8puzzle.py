initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def bfs(initial_state):
    queue = [(initial_state, [])]
    while queue:
        (state, path) = queue.pop(0)
        if state == goal_state:
            return path
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    zero_row = i
                    zero_col = j
                    break
        moves = []
        if zero_row > 0:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = \
                new_state[zero_row - 1][zero_col], new_state[zero_row][zero_col]
            moves.append(new_state)
        if zero_row < 2:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = \
                new_state[zero_row + 1][zero_col], new_state[zero_row][zero_col]
            moves.append(new_state)
        if zero_col > 0:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = \
                new_state[zero_row][zero_col -
                                    1], new_state[zero_row][zero_col]
            moves.append(new_state)
        if zero_col < 2:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = \
                new_state[zero_row][zero_col +
                                    1], new_state[zero_row][zero_col]
            moves.append(new_state)
        for move in moves:
            if move not in [p[0] for p in queue]:
                new_path = path + [move]
                queue.append((move, new_path))
    return None


def swap(x, y):
    x, y = y, x


def dfs(state, path):
    if state == goal_state:
        return path
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row = i
                zero_col = j
                break
    moves = []
    if zero_row > 0:
        new_state = [row[:] for row in state]
        # new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = \
        #     new_state[zero_row - 1][zero_col], new_state[zero_row][zero_col]
        swap(new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col])
        moves.append(new_state)
    if zero_row < 2:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = \
            new_state[zero_row + 1][zero_col], new_state[zero_row][zero_col]
        moves.append(new_state)
    if zero_col > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = \
            new_state[zero_row][zero_col - 1], new_state[zero_row][zero_col]
        moves.append(new_state)
    if zero_col < 2:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = \
            new_state[zero_row][zero_col + 1], new_state[zero_row][zero_col]
        moves.append(new_state)
    for move in moves:
        if move not in path:
            new_path = path + [move]
            result = dfs(move, new_path)
            if result:
                return result
    return None


def dls(state, limit, path):
    if state == goal_state:
        return path
    if limit == 0:
        return None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row = i
                zero_col = j
                break
    moves = []
    if zero_row > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row - 1][zero_col] = \
            new_state[zero_row - 1][zero_col], new_state[zero_row][zero_col]
        moves.append(new_state)
    if zero_row < 2:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row + 1][zero_col] = \
            new_state[zero_row + 1][zero_col], new_state[zero_row][zero_col]
        moves.append(new_state)
    if zero_col > 0:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col - 1] = \
            new_state[zero_row][zero_col - 1], new_state[zero_row][zero_col]
        moves.append(new_state)
    if zero_col < 2:
        new_state = [row[:] for row in state]
        new_state[zero_row][zero_col], new_state[zero_row][zero_col + 1] = \
            new_state[zero_row][zero_col + 1], new_state[zero_row][zero_col]
        moves.append(new_state)
    for move in moves:
        if move not in path:
            new_path = path + [move]
            result = dls(move, limit - 1, new_path)
            if result is not None:
                return result
    return None


print("1) BFS\n2) DFS\n3) DLS")
choice = int(input("Enter Your Choice"))

if (choice == 1):
    path = bfs(initial_state)
    if path:
        print("BFS")
        print('Solution found in', len(path) - 1, 'moves:')
        for state in path:
            for row in state:
                print(row)
            print()
    else:
        print('No solution found')

elif (choice == 2):
    for state in initial_state:
        print(state)
    path = dfs(initial_state, [])
    if path:
        print("DFS")
        print('Solution found in', len(path) - 1, 'moves:')
        for state in path:
            for row in state:
                print(row)
            print()
    else:
        print('No solution found')

elif (choice == 3):
    # Prompt the user to enter the depth limit
    depth_limit = int(input('Enter the depth limit: '))

    # Call the DLS function with the initial state and depth limit
    path = dls(initial_state, depth_limit, [initial_state])
    if path:
        print("DLS")
        print('Solution found in', len(path) - 1, 'moves:')
        for state in path:
            for row in state:
                print(row)
            print()
    else:
        print('No solution found within the depth limit')

else:
    print("Wrong Choice")
