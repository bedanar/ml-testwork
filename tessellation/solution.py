import random

def is_valid_move(x, y, visited, m, n):
    return 0 <= x < m and 0 <= y < n and not visited[x][y]

def main(desk_size: list[int, int]) -> list[list[int, int]]:
    # Possible moves of the knight
    moves = [[1, 2], [2, 1], [-2, 1], [-2, -1], [2, -1], [1, -2], [-1, 2], [-1, -2]]
    N, M = desk_size[0], desk_size[1]

    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    # starting position
    x, y = 0, 0
    step_count = 0

    result = []

    while step_count < M * N * 5:
        result.append([x, y])
        visited[x][y] = True
        step_count += 1

        # Trying to make a move with the knight
        possible_moves = []

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if is_valid_move(nx, ny, visited, M, N):
                possible_moves.append((nx, ny))

        # Selecting a random move from the list of all possible moves
        if possible_moves:
            x, y = possible_moves[random.randint(0, len(possible_moves) - 1)]
        else:
            # Exiting the loop of there are no possible moves
            break

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                result.append([i, j])
                visited[i][j] = True

    return result

print(main([5, 5]))