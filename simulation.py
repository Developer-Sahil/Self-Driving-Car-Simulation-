import pygame
import heapq
import math

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Self-Driving Car Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)

# Grid settings
grid_size = 20
rows = screen_height // grid_size
cols = screen_width // grid_size
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Clock for frame rate
clock = pygame.time.Clock()

# Car settings
car_width, car_height = 20, 20
car_x, car_y = 100, 500  # Initial position

# Obstacles
obstacles = [
    pygame.Rect(250, 150, 50, 50),
    pygame.Rect(300, 200, 50, 50),
    pygame.Rect(400, 300, 50, 50),
    pygame.Rect(450, 350, 50, 50),
    pygame.Rect(500, 400, 50, 50),
]

# Dynamic obstacles
dynamic_obstacles = [
    {"rect": pygame.Rect(350, 0, 50, 30), "speed": 3},
    {"rect": pygame.Rect(600, 275, 30, 50), "speed": 4},
    {"rect": pygame.Rect(450, 100, 40, 40), "speed": 2},
]

# Goal position (grid coordinates)
goal = (5, cols - 6)


# Utility functions
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance


def grid_to_pixel(cell):
    return cell[1] * grid_size + grid_size // 2, cell[0] * grid_size + grid_size // 2


def pixel_to_grid(x, y):
    return y // grid_size, x // grid_size


# Pathfinding (A* algorithm)
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, (int(start[0]), int(start[1]))))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (int(current[0] + dx), int(current[1] + dy))
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # No path found


# Obstacle and dynamic obstacle updates
def update_grid_with_obstacles():
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = 0  # Reset grid
    for obstacle in obstacles:
        grid_x = obstacle.x // grid_size
        grid_y = obstacle.y // grid_size
        grid[grid_y][grid_x] = 1
    for obstacle in dynamic_obstacles:
        grid_x = obstacle["rect"].x // grid_size
        grid_y = obstacle["rect"].y // grid_size
        grid[grid_y][grid_x] = 1


def move_dynamic_obstacles():
    for obstacle in dynamic_obstacles:
        rect = obstacle["rect"]
        if rect.y >= screen_height or rect.y <= 0:
            obstacle["speed"] *= -1
        rect.y += obstacle["speed"]

for obstacle in obstacles:
    grid_x = obstacle.x // grid_size
    grid_y = obstacle.y // grid_size
    if (grid_y, grid_x) == goal:
        print("Warning: Obstacle at goal location! Adjusting goal.")
        goal = (0, cols - 2)  # Adjust goal if needed
    grid[grid_y][grid_x] = 1


# Visualization
def draw_map():
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, (200, 0, 400, 600))  # Main road


def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * grid_size, row * grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, BLACK, rect, 1)


def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)


def draw_dynamic_obstacles():
    for obstacle in dynamic_obstacles:
        pygame.draw.rect(screen, BLUE, obstacle["rect"])


def draw_car(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, car_width, car_height))


def draw_path(path):
    for cell in path:
        x, y = grid_to_pixel(cell)
        pygame.draw.circle(screen, GREEN, (x, y), 5)


# Main loop
start = pixel_to_grid(car_x, car_y)
path = a_star(start, goal)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid and obstacles
    update_grid_with_obstacles()
    move_dynamic_obstacles()

    # Recalculate path dynamically
    start = pixel_to_grid(car_x, car_y)
    path = a_star(start, goal)

    # Follow the path
    if path:
        next_cell = path[0]
        target_x, target_y = grid_to_pixel(next_cell)
        if abs(car_x - target_x) > 1:
            car_x += math.copysign(5, target_x - car_x)
        if abs(car_y - target_y) > 1:
            car_y += math.copysign(5, target_y - car_y)

        if abs(car_x - target_x) < 5 and abs(car_y - target_y) < 5:
            path.pop(0)

    # Draw everything
    draw_map()
    draw_grid()
    draw_obstacles()
    draw_dynamic_obstacles()
    draw_path(path)
    draw_car(car_x, car_y)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
