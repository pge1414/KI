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
        arcade.set_background_color(arcade.color.BLACK)

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
        self.ball = arcade.SpriteSolidColor(BALL_SIZE, BALL_SIZE, arcade.color.WHITE)
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
        # draw center line
        arcade.draw_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, arcade.color.DARK_GRAY)

        # draw paddles and ball
        self.player.draw()
        self.bot.draw()
        self.ball.draw()

        # scores
        arcade.draw_text(str(self.player_score), WIDTH * 0.25, HEIGHT - 50, arcade.color.WHITE, FONT_SIZE, anchor_x="center")
        arcade.draw_text(str(self.bot_score), WIDTH * 0.75, HEIGHT - 50, arcade.color.WHITE, FONT_SIZE, anchor_x="center")

        if self.paused:
            arcade.draw_text("PAUSED — Press ENTER to resume", WIDTH / 2, HEIGHT / 2, arcade.color.YELLOW, 20, anchor_x="center")

    def on_update(self, delta_time: float):
        if self.paused:
            return

        # update player paddle
        self.player.center_y += self.player_velocity * delta_time
        # clamp
        half = PADDLE_HEIGHT / 2
        if self.player.center_y < half:
            self.player.center_y = half
        if self.player.center_y > HEIGHT - half:
            self.player.center_y = HEIGHT - half

        # simple bot: follow ball with max speed
        if abs(self.ball.center_y - self.bot.center_y) > 8:
            direction = 1 if self.ball.center_y > self.bot.center_y else -1
            move = direction * BOT_MAX_SPEED * delta_time
            # don't overshoot
            if abs(move) > abs(self.ball.center_y - self.bot.center_y):
                move = self.ball.center_y - self.bot.center_y
            self.bot.center_y += move
        # clamp bot
        if self.bot.center_y < half:
            self.bot.center_y = half
        if self.bot.center_y > HEIGHT - half:
            self.bot.center_y = HEIGHT - half

        # update ball
        self.ball.center_x += self.ball_dx * delta_time
        self.ball.center_y += self.ball_dy * delta_time

        # collision with top/bottom
        if self.ball.top >= HEIGHT:
            self.ball.center_y = HEIGHT - BALL_SIZE // 2
            self.ball_dy *= -1
        if self.ball.bottom <= 0:
            self.ball.center_y = BALL_SIZE // 2
            self.ball_dy *= -1

        # collision with paddles
        if arcade.check_for_collision(self.ball, self.player):
            # reflect and add spin based on hit position
            offset = (self.ball.center_y - self.player.center_y) / (PADDLE_HEIGHT / 2)
            self.ball_dx = abs(self.ball_dx) * BALL_SPEED_INCREASE
            self.ball_dy = self.ball_dy + offset * 200
            # nudge ball out to avoid repeated collisions
            self.ball.center_x = self.player.center_x + PADDLE_WIDTH / 2 + BALL_SIZE / 2 + 1

        if arcade.check_for_collision(self.ball, self.bot):
            offset = (self.ball.center_y - self.bot.center_y) / (PADDLE_HEIGHT / 2)
            self.ball_dx = -abs(self.ball_dx) * BALL_SPEED_INCREASE
            self.ball_dy = self.ball_dy + offset * 200
            self.ball.center_x = self.bot.center_x - PADDLE_WIDTH / 2 - BALL_SIZE / 2 - 1

        # scoring
        if self.ball.left <= 0:
            # bot scores
            self.bot_score += 1
            self.reset_ball(serve_to_player=False)
        if self.ball.right >= WIDTH:
            # player scores
            self.player_score += 1
            self.reset_ball(serve_to_player=True)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W or symbol == arcade.key.UP:
            self.player_velocity = PADDLE_SPEED
        elif symbol == arcade.key.S or symbol == arcade.key.DOWN:
            self.player_velocity = -PADDLE_SPEED
        elif symbol == arcade.key.ENTER:
            self.paused = not self.paused
        elif symbol == arcade.key.SPACE:
            # reset scores and ball
            self.player_score = 0
            self.bot_score = 0
            self.reset_ball()

    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN):
            self.player_velocity = 0


def main():
    window = PongWindow()
    arcade.run()


if __name__ == "__main__":
    main()
