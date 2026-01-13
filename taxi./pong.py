import arcade
import arcade.gui
import random

WIDTH = 800
HEIGHT = 600
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 100
PADDLE_SPEED = 400
BOT_MAX_SPEED = 320
BALL_SIZE = 15
BALL_START_SPEED = 300
BALL_SPEED_INCREASE = 1.05
FONT_SIZE = 36
MAX_BALL_SPEED = 3500

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class PongWindow0(arcade.Scene):
    def __init__(self):
        super().__init__(800, 600, "UIFlatButton Example", resizable=True)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button)
        # spacer statt with_space_around (Kompatibilität)
        self.v_box.add(arcade.gui.UIWidget(height=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button)
        self.v_box.add(arcade.gui.UIWidget(height=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        @settings_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("Start:", event)
        self.window.change_scene(PongWindow1())

    def on_draw(self):
        self.clear()
        self.manager.draw()


class PongWindow1(arcade.Scene):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Pong / Spieler vs Bot")
        arcade.set_background_color(arcade.color.DARK_CORAL)

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

        # put sprites into a SpriteList for drawing
        self.sprites = arcade.SpriteList()
        self.sprites.append(self.player)
        self.sprites.append(self.bot)
        self.sprites.append(self.ball)

        # Scores
        self.player_score = 0
        self.bot_score = 0

        # State
        self.paused = False

    def reset_ball(self, serve_to_player=None):
        # center
        x = WIDTH // 2
        self.ball.center_y = HEIGHT // 2
        speed = BALL_START_SPEED
        angle = random.uniform(-0.5, 0.5)
        # decide horizontal direction
        if serve_to_player is None:
            dir_x = random.choice([-1, 1])
        else:
            dir_x = -1 if serve_to_player else 1
        # set velocities (no redundant abs)
        self.ball_dx = dir_x * speed
        self.ball_dy = speed * angle

    def on_draw(self):
        # Use clear() in on_draw instead of arcade.start_render()
        self.clear()
        # draw center line
        arcade.draw_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, arcade.color.WHITE, line_width=5)


        # draw all sprites via SpriteList
        self.sprites.draw()

        # draw scores
        arcade.draw_text(str(self.player_score), WIDTH * 0.25, HEIGHT - 50, arcade.color.WHITE, FONT_SIZE, anchor_x="center")
        arcade.draw_text(str(self.bot_score), WIDTH * 0.75, HEIGHT - 50, arcade.color.WHITE, FONT_SIZE, anchor_x="center")


    def on_update(self, delta_time):
        if self.paused:
            return

        half_paddle = PADDLE_HEIGHT / 2

        # Update player paddle position and clamp
        self.player.center_y += self.player_velocity * delta_time
        if self.player.center_y < half_paddle:
            self.player.center_y = half_paddle
        if self.player.center_y > HEIGHT - half_paddle:
            self.player.center_y = HEIGHT - half_paddle

        # Update bot paddle position (follow ball, limited speed)
        dist = self.ball.center_y - self.bot.center_y
        max_move = BOT_MAX_SPEED * delta_time
        if abs(dist) > 1:
            move = max(-max_move, min(max_move, dist))
            self.bot.center_y += move
        # clamp bot
        if self.bot.center_y < half_paddle:
            self.bot.center_y = half_paddle
        if self.bot.center_y > HEIGHT - half_paddle:
            self.bot.center_y = HEIGHT - half_paddle

        # Update ball position
        self.ball.center_x += self.ball_dx * delta_time
        self.ball.center_y += self.ball_dy * delta_time

        # Ball collision with top/bottom using explicit extents
        ball_top = self.ball.center_y + BALL_SIZE / 2
        ball_bottom = self.ball.center_y - BALL_SIZE / 2
        if ball_top > HEIGHT:
            self.ball.center_y = HEIGHT - BALL_SIZE / 2
            self.ball_dy *= -1
        if ball_bottom < 0:
            self.ball.center_y = BALL_SIZE / 2
            self.ball_dy *= -1

        # Ball collision with player paddle
        if arcade.check_for_collision(self.ball, self.player):
            # reflect to the right
            offset = (self.ball.center_y - self.player.center_y) / (PADDLE_HEIGHT / 2)
            speed = min(MAX_BALL_SPEED, abs(self.ball_dx) * BALL_SPEED_INCREASE)
            self.ball_dx = abs(speed)
            self.ball_dy = self.ball_dy + offset * BALL_START_SPEED * 0.5
            # nudge ball outside paddle
            self.ball.center_x = self.player.center_x + PADDLE_WIDTH / 2 + BALL_SIZE / 2 + 1

        # Ball collision with bot paddle
        if arcade.check_for_collision(self.ball, self.bot):
            offset = (self.ball.center_y - self.bot.center_y) / (PADDLE_HEIGHT / 2)
            speed = min(MAX_BALL_SPEED, abs(self.ball_dx) * BALL_SPEED_INCREASE)
            self.ball_dx = -abs(speed)
            self.ball_dy = self.ball_dy + offset * BALL_START_SPEED * 0.5
            self.ball.center_x = self.bot.center_x - PADDLE_WIDTH / 2 - BALL_SIZE / 2 - 1

        # Check for scoring using explicit extents
        ball_left = self.ball.center_x - BALL_SIZE / 2
        ball_right = self.ball.center_x + BALL_SIZE / 2
        if ball_left < 0:
            self.bot_score += 1
            self.reset_ball(serve_to_player=False)
        elif ball_right > WIDTH:
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


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.current_scene = PongWindow0(self) # Startet mit der Menü-Szene

    def change_scene(self, new_scene):
        self.current_scene = new_scene

    def on_draw(self):
        # Zeichnet die aktuelle Szene
        self.current_scene.on_draw()

    def on_key_press(self, key, modifiers):
        # Leitet Tastendrücke an die aktuelle Szene weiter
        self.current_scene.on_key_press(key, modifiers)

def main():
    window = MyGame(800, 600, "Arcade Szenenwechsel")
    arcade.run()
if __name__ == "__main__":
    main()