import arcade


class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        # 1. Create the SpriteList
        self.sprites = arcade.SpriteList()

        # 2. Create & append your Sprite instance to the SpriteList
        self.car = arcade.Sprite("auto.png", 0.1)  # Sprite with the default texture
        self.car.position = self.center  # center sprite on screen
        self.sprites.append(self.car)  # Append the instance to the SpriteList
        self.grid = arcade.Sprite("grid.png", 1)
        self.grid.position = (290,240)
        self.sprites.append(self.grid)

    def on_draw(self):
        # 3. Clear the screen
        self.clear()

        # 4. Call draw() on the SpriteList inside an on_draw() method
        self.sprites.draw()


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(600, 600, "Minimal SPrite Example")

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
main()