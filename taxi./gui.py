import arcade, random


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # grid of possible positions (x,y)
        self.liste = [[100,100],[200,100],[300,100],[400,100],[500,100],[100,200],[200,200],[300,200],[400,200],[500,200],[100,300],[200,300],[300,300],[400,300],[500,300],[100,400],[200,400],[300,400],[400,400],[500,400],[100,500],[200,500],[300,500],[400,500],[500,500]]
        # a smaller set of special positions
        self.liste_pos = [[100,100],[200,300],[500,500],[200,200]]

        # sprite container
        self.sprites = arcade.SpriteList()

        # add background grid as image sprite
        self.grid = arcade.Sprite("gitter.png", 0.4)
        self.grid.position = (300,300)
        self.sprites.append(self.grid)

        # placeholders
        self.car_sprite = None
        self.other_sprites = []

    def setup(self):
        """Create sprites and schedule non-blocking moves."""
        # helper to create and append sprite using image filenames
        def add_sprite(filename, scale, pos, placeholder_color=arcade.color.RED):
            # try to create sprite from image; fall back to colored box if missing
            try:
                spr = arcade.Sprite(filename, scale)
            except Exception:
                size = max(8, int(32 * (scale / 0.05)))
                spr = arcade.SpriteSolidColor(size, size, placeholder_color)
            spr.center_x, spr.center_y = pos
            spr.alpha = 255
            self.sprites.append(spr)
            self.other_sprites.append(spr)
            return spr

        # place car in the centre index (12)
        try:
            self.car_sprite = arcade.Sprite("auto.png", 0.06)
        except Exception:
            self.car_sprite = arcade.SpriteSolidColor(48, 24, arcade.color.BLUE)
        self.car_sprite.center_x, self.car_sprite.center_y = self.liste[12]
        self.sprites.append(self.car_sprite)

        # choose 4 unique positions from liste_pos
        positions = random.sample(self.liste_pos, 4)

        passenger = add_sprite("omma.png", 0.05, positions[0], placeholder_color=arcade.color.YELLOW)
        block1 = add_sprite("block.png", 0.3, positions[1], placeholder_color=arcade.color.DARK_BROWN)
        block2 = add_sprite("block.png", 0.3, positions[2], placeholder_color=arcade.color.DARK_BROWN)
        ziel = add_sprite("bücher.png", 0.05, positions[3], placeholder_color=arcade.color.GREEN)

    def on_show(self):
        # Called when this view is shown; initialize sprites here
        self.setup()

    def on_draw(self):
        # Clear the screen and draw all sprites
        self.clear()
        self.sprites.draw()


def main():
    # Create and show the game window and view
    window = arcade.Window(600, 600, "Minimal Sprite Example")
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()