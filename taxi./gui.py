import arcade, random


class GameView(arcade.View):

    liste = [[100,100],[200,100],[300,100],[400,100],[500,100],[100,200],[200,200],[300,200],[400,200],[500,200],[100,300],[200,300],[300,300],[400,300],[500,300],[100,400],[200,400],[300,400],[400,400],[500,400],[100,500],[200,500],[300,500],[400,500],[500,500]]
    sprites = arcade.SpriteList()

    def move(x : int, liste : list, sprites):
        car = arcade.Sprite("auto.png", 0.1)
        car.position = (liste[x][0], liste[x][1])
        sprites.append(car)
    
    def passengerpos(sprites, liste):
        x = random.randint(0,24)
        block = arcade.Sprite("omma.png", 0.05)
        block.position = (liste[x][0], liste[x][1])
        sprites.append(block)

    def blockpositioning(sprites, liste):
        x = random.randint(0,24)
        block = arcade.Sprite("block.png", 0.3)
        block.position = (liste[x][0], liste[x][1])
        sprites.append(block)
    
    # 2. Create & append your Sprite instance to the SpriteList
    move(12, liste, sprites) # center sprite on screen
    passengerpos(sprites,liste)
    blockpositioning(sprites, liste)
    blockpositioning(sprites, liste)
    blockpositioning(sprites, liste)
    grid = arcade.Sprite("grid.png", 1)
    grid.position = (290,240)
    sprites.append(grid)

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

main()