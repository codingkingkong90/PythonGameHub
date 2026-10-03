WIDTH = 1000
HEIGHT = 600

PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15

MENU = "menu"
CHOICE = "choice"
PLAY_AI = "play_ai"
PLAY_TWO = "play_two"
GAME_OVER = "game_over"

game_state = MENU
last_mode = None

class Paddle:
    def __init__(self, x):
        self.rect = Rect((x, HEIGHT // 2 - PADDLE_HEIGHT // 2), (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.speed = 5
    def move_player(self, up, down):
        if up:
            self.rect.y -= self.speed
        if down:
            self.rect.y += self.speed
        self.keep_on_screen()
    def move_ai(self, ball):
        if ball.rect.centery > self.rect.centery:
            self.rect.y += self.speed
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= self.speed
        self.keep_on_screen()
    def keep_on_screen(self):
        self.rect.y = max(0, min(HEIGHT - PADDLE_HEIGHT, self.rect.y))
    def draw(self):
        screen.draw.filled_rect(self.rect, "white")

class Ball:
    def __init__(self):
        self.reset()
    def reset(self):
        self.rect = Rect((WIDTH // 2, HEIGHT // 2), (BALL_SIZE, BALL_SIZE))
        self.vx = 4
        self.vy = 4
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1
    def bounce(self):
        self.vx *= -1
        self.vx *= 1.1
        self.vy *= 1.1
        sounds.bounce.play()
    def draw(self):
        screen.draw.filled_rect(self.rect, "white")

class Score():
    def __init__(self):
        self.left = 0
        self.right = 0

    def draw(self):
        screen.draw.text(
            str(self.left),
            center=(WIDTH // 4, 30),
            fontsize=40,
            color = "white"
        )
        screen.draw.text(
            str(self.right),
            center=(WIDTH * 3 // 4, 30),
            fontsize=40,
            color = "white"
        )

left_paddle = Paddle(20)
right_paddle = Paddle(WIDTH - 35)
ball = Ball()
score = Score()

def game_functions():
    global game_state

    ball.update()

    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
        ball.bounce()

    if ball.rect.left <= 0:
        score.right += 1
        ball.reset()
        sounds.score.play()

    if ball.rect.right >= WIDTH:
        score.left += 1
        ball.reset()
        sounds.score.play()

    if score.left == 5 or score.right == 5:
        game_state = GAME_OVER
        sounds.win.play()

def update():
    global game_state

    if game_state != PLAY_AI and game_state != PLAY_TWO:
        return

    if game_state == PLAY_AI:
        left_paddle.move_player(keyboard.w, keyboard.s)
        right_paddle.move_ai(ball)
        game_functions()


    if game_state == PLAY_TWO:
        left_paddle.move_player(keyboard.w, keyboard.s)
        right_paddle.move_player(keyboard.up, keyboard.down)
        game_functions()



def draw():
    screen.fill("black")

    if game_state == MENU:
        screen.draw.text(
            "PONG",
            center=(WIDTH // 2, HEIGHT // 2 - 60),
            fontsize=80,
            color="white"
        )
        screen.draw.text(
            "Press SPACE to start",
            center=(WIDTH // 2, HEIGHT // 2 + 20),
            fontsize=36,
            color="white"
        )
    elif game_state == CHOICE:
        screen.draw.text(
            "Press 1 to play against a AI",
            center=(WIDTH // 2, HEIGHT // 2 - 60),
            fontsize=36,
            color="white"
        )
        screen.draw.text(
            "Press 2 to play against a friend",
            center=(WIDTH // 2, HEIGHT // 2 + 20),
            fontsize=36,
            color="white"
        )

    elif game_state == PLAY_AI or game_state == PLAY_TWO:
        left_paddle.draw()
        right_paddle.draw()
        ball.draw()
        score.draw()

    elif game_state == GAME_OVER:

        if last_mode == PLAY_AI:
            winner_text = "You win" if score.left > score.right else "AI win"
        elif last_mode == PLAY_TWO:
            winner_text = "Player 1 wins" if score.left > score.right else "Player 2 wins"
        screen.draw.text(
            winner_text,
            center=(WIDTH // 2, HEIGHT // 2 - 40),
            fontsize=60,
            color="white"
        )
        screen.draw.text(
            "Press SPACE to restart",
            center=(WIDTH // 2, HEIGHT // 2 + 40),
            fontsize=36,
            color="white"
        )

def on_key_down(key):
    global game_state, last_mode

    if key == keys.SPACE:
        if game_state == MENU or game_state == GAME_OVER:
            game_state = CHOICE
    if key == keys.K_1:
        game_state = PLAY_AI
        last_mode = PLAY_AI
        if game_state == PLAY_AI:
            score.left = 0
            score.right = 0
            ball.reset()
    if key == keys.K_2:
        game_state = PLAY_TWO
        last_mode = PLAY_TWO
        if game_state == PLAY_TWO:
            score.left = 0
            score.right = 0
            ball.reset()
