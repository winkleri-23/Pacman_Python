import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 50
MAP_LAYOUT_INIT = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

MAP_LAYOUT = MAP_LAYOUT_INIT.copy()

SCREEN_WIDTH = len(MAP_LAYOUT[0]) * TILE_SIZE
SCREEN_HEIGHT = len(MAP_LAYOUT) * TILE_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Game")
font = pygame.font.Font(None, 36)

# Game state variables
score = 0
total_dots = sum(row.count(2) for row in MAP_LAYOUT)  # Total dots in map

# Pac-Man class
class PacMan:
    def __init__(self):
        self.x, self.y = 1, 1  # Starting position
        self.direction = (0, 0)

    def move(self):
        # Calculate target position
        new_x = self.x + self.direction[0]
        new_y = self.y + self.direction[1]

        # Check if the target position is a wall
        if MAP_LAYOUT[new_y][new_x] != 1:
            self.x, self.y = new_x, new_y

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)

# Game functions
def draw_map():
    for y, row in enumerate(MAP_LAYOUT):
        for x, cell in enumerate(row):
            if cell == 1:  # Wall
                pygame.draw.rect(screen, BLUE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif cell == 2:  # Dot
                pygame.draw.circle(screen, WHITE, (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2), 3)

def check_dot_collision(pacman):
    global score, total_dots
    if MAP_LAYOUT[pacman.y][pacman.x] == 2:  # Dot cell
        MAP_LAYOUT[pacman.y][pacman.x] = 0  # Remove dot
        score += 10
        total_dots -= 1

def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def display_win_message():
    win_text = font.render("You Win! Press R to play again", True, YELLOW)
    screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2))

def reset_game():
    global score, total_dots, MAP_LAYOUT
    score = 0
    
    MAP_LAYOUT = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    total_dots = sum(row.count(2) for row in MAP_LAYOUT)

# Main game loop
def game_loop():
    global score
    pacman = PacMan()
    clock = pygame.time.Clock()
    game_over = False

    while True:
        screen.fill(BLACK)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    reset_game()
                    pacman = PacMan()
                    game_over = False
                elif not game_over:
                    if event.key == pygame.K_LEFT:
                        pacman.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        pacman.direction = (1, 0)
                    elif event.key == pygame.K_UP:
                        pacman.direction = (0, -1)
                    elif event.key == pygame.K_DOWN:
                        pacman.direction = (0, 1)

        # Move Pac-Man and check for collisions if the game is not over
        if not game_over:
            pacman.move()
            check_dot_collision(pacman)

        # Draw everything
        draw_map()
        pacman.draw()
        display_score()

        # Check if all dots are eaten
        if total_dots == 0:
            game_over = True
            display_win_message()

        # Update display
        pygame.display.flip()
        clock.tick(10)

# Run the game
if __name__ == "__main__":
    game_loop()
