import arcade
import random

WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 100
PADDLE_SPEED = 400
BOT_MAX_SPEED = 320
BALL_SIZE = 12
BALL_START_SPEED = 300
BALL_SPEED_INCREASE = 1.05
FONT_SIZE = 36

class PongWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Pong — Spieler vs Bot")
        arcade.set_background_color(arcade.color.ORIOLES_ORANGE)

        # Player paddle (left)
        self.player = arcade.SpriteSolidColor(PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        self.player.center_x = 40
        self.player.center_y = HEIGHT // 2
        self.player_velocity = 0

        # Bot paddle (right)
        self.bot = arcade.SpriteSolidColor(PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        self.bot.center_x = WIDTH - 40
        self.bot.center_y = HEIGHT // 2

        # Ball
        self.ball = arcade.SpriteSolidColor(BALL_SIZE, BALL_SIZE, arcade.color.YELLOW)
        self.reset_ball()

        # Scores
        self.player_score = 0
        self.bot_score = 0

        # State
        self.paused = False

    def reset_ball(self, serve_to_player=None):
        # center
        self.ball.center_x = WIDTH // 2
        self.ball.center_y = HEIGHT // 2
        speed = BALL_START_SPEED
        angle = random.uniform(-0.5, 0.5)
        # decide horizontal direction
        if serve_to_player is None:
            dir_x = random.choice([-1, 1])
        else:
            dir_x = -1 if serve_to_player else 1
        self.ball_dx = dir_x * speed * abs(1)
        self.ball_dy = speed * angle
    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, arcade.color.WHITE, line_width=5)
        self.player.draw()
        self.bot.draw()
        self.ball.draw()


    def on_update(self, delta_time):
        if self.paused:
            return

        # Update player paddle position
        self.player.center_y += self.player_velocity * delta_time
        # Keep player paddle on screen
        if self.player.top > HEIGHT:
            self.player.top = HEIGHT
        if self.player.bottom < 0:
            self.player.bottom = 0

        # Update bot paddle position
        if self.ball.center_y > self.bot.center_y:
            self.bot.center_y += BOT_MAX_SPEED * delta_time
        elif self.ball.center_y < self.bot.center_y:
            self.bot.center_y -= BOT_MAX_SPEED * delta_time
        # Keep bot paddle on screen
        if self.bot.top > HEIGHT:
            self.bot.top = HEIGHT
        if self.bot.bottom < 0:
            self.bot.bottom = 0

        # Update ball position
        self.ball.center_x += self.ball_dx * delta_time
        self.ball.center_y += self.ball_dy * delta_time

        # Ball collision with top/bottom
        if self.ball.top > HEIGHT or self.ball.bottom < 0:
            self.ball_dy *= -1

        # Ball collision with player paddle
        if arcade.check_for_collision(self.ball, self.player):
            self.ball_dx *= -BALL_SPEED_INCREASE
            offset = (self.ball.center_y - self.player.center_y) / (PADDLE_HEIGHT / 2)
            self.ball_dy += offset * BALL_START_SPEED * 0.5

        # Ball collision with bot paddle
        if arcade.check_for_collision(self.ball, self.bot):
            self.ball_dx *= -BALL_SPEED_INCREASE
            offset = (self.ball.center_y - self.bot.center_y) / (PADDLE_HEIGHT / 2)
            self.ball_dy += offset * BALL_START_SPEED * 0.5

        # Check for scoring
        if self.ball.right < 0:
            self.bot_score += 1
            self.reset_ball(serve_to_player=False)
        elif self.ball.left > WIDTH:
            self.player_score += 1
            self.reset_ball(serve_to_player=True)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.player_velocity = PADDLE_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player_velocity = -PADDLE_SPEED
        elif key == arcade.key.SPACE:
            self.paused = not self.paused

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN):
            self.player_velocity = 0

def main():
    window = PongWindow()
    arcade.run()
if __name__ == "__main__":
    main()