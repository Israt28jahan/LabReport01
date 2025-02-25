import random

def generate_grid(N):
    grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
    return grid

def find_empty_cell(grid, N):
    while True:
        r, c = random.randint(0, N-1), random.randint(0, N-1)
        if grid[r][c] == 0:
            return r, c

def get_neighbors(node, N):
    r, c = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            neighbors.append((nr, nc))
    return neighbors

def dfs(grid, start, goal, N):
    stack = [start]
    visited = set()
    parent = {}
    order = []
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        
        if node == goal:
            break
        
        for neighbor in get_neighbors(node, N):
            if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = node
    
    path = []
    if goal in visited:
        current = goal
        while current != start:
            path.append(current)
            current = parent.get(current, start)
        path.append(start)
        path.reverse()
    
    return path, order

def print_grid(grid, source, goal, path):
    N = len(grid)
    for r in range(N):
        for c in range(N):
            if (r, c) == source:
                print('S', end=' ')
            elif (r, c) == goal:
                print('G', end=' ')
            elif (r, c) in path:
                print('*', end=' ')
            else:
                print('.' if grid[r][c] == 0 else '#', end=' ')
        print()

def main():
    N = random.randint(4, 7)
    grid = generate_grid(N)
    
    source = find_empty_cell(grid, N)
    goal = find_empty_cell(grid, N)
    while source == goal:
        goal = find_empty_cell(grid, N)
    
    path, order = dfs(grid, source, goal, N)
    
    print("Generated Grid:")
    print_grid(grid, source, goal, path)
    print("\nSource:", source)
    print("Goal:", goal)
    print("DFS Path:", path if path else "No path found")
    print("Topological Order of DFS Traversal:", order)

if __name__ == "__main__":
    main()
