import random

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 50

class SnakeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.draw.filled_rect(Rect((self.x, self.y), (CELL_SIZE, CELL_SIZE)), "green")

class Snake:
    def __init__(self):
        self.segments = [
            SnakeSegment(WIDTH // 2, HEIGHT // 2),
            SnakeSegment(WIDTH // 2 - CELL_SIZE, HEIGHT // 2),
            SnakeSegment(WIDTH // 2 - 2 * CELL_SIZE, HEIGHT // 2),
        ]
    def draw(self):
        for segment in self.segments:
            segment.draw()
    def move(self, dx, dy, grow=False):
        head = self.segments[0]

        new_x = (head.x + dx * CELL_SIZE) % WIDTH
        new_y = (head.y + dy * CELL_SIZE) % HEIGHT
        new_head = SnakeSegment(new_x, new_y)

        for segment in self.segments:
            if segment.x == new_head.x and segment.y == new_head.y:
                return True
        self.segments.insert(0, new_head)
        if not grow:
            self.segments.pop()
        return False
    
class Food:
    def __init__(self, x, y, color="red"):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        screen.draw.filled_rect(Rect((self.x, self.y), (CELL_SIZE, CELL_SIZE)), self.color)

snake = Snake()
dx, dy = 0, 0
score  = 0
game_over = False

move_delay = 0.2
time_since_move = 0

def random_food_position():
    x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    return x, y

food = Food(*random_food_position())

def update(dt):
    global time_since_move, food, score, game_over

    if game_over:
        return
    time_since_move += dt
    if time_since_move >= move_delay:
        time_since_move = 0
        if dx != 0 or dy != 0:
            head = snake.segments[0]
            next_x = (head.x + dx * CELL_SIZE) % WIDTH
            next_y = (head.y + dy * CELL_SIZE) % HEIGHT

            grow  = next_x == food.x and next_y == food.y

            collision = snake.move(dx, dy, grow)
            if collision:
                game_over = True
            if grow:
                score += 1
                food.x, food.y = random_food_position()

def draw():
    screen.clear()
    snake.draw()
    food.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")
    if game_over:
        screen.draw.text("GAME OVER!!!!", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")

def on_key_down(key):
    global dx, dy

    if key == keys.RIGHT and dx == 0:
        dx, dy = 1, 0
    elif key == keys.LEFT and dx == 0:
        dx, dy = -1, 0
    elif key == keys.UP and dy == 0:
        dx, dy = 0, -1
    elif key == keys.DOWN and dy == 0:
        dx, dy = 0, 1

        