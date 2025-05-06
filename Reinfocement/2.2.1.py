import arcade

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
WINDOW_TITLE = "Hexapawn"


arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()


x1 = 100
y1 = 100
width = 200
height = 200
arcade.draw_rectangle_filled(x1, y1,width, height, arcade.color.ASH_GREY)

arcade.draw_rectangle_filled(x1+200, y1+200,width, height, arcade.color.ASH_GREY)

arcade.draw_rectangle_filled(x1+400, y1+400,width, height, arcade.color.ASH_GREY)

arcade.draw_rectangle_filled(x1, y1+400,width, height, arcade.color.ASH_GREY)

arcade.draw_rectangle_filled(x1+400, y1,width, height, arcade.color.ASH_GREY)

arcade.draw_rectangle_filled(x1+200, y1+400,width, height, arcade.color.ARMY_GREEN)

arcade.draw_rectangle_filled(x1+200, y1,width, height, arcade.color.ARMY_GREEN)

arcade.draw_rectangle_filled(x1+400, y1+200,width, height, arcade.color.ARMY_GREEN)

arcade.draw_rectangle_filled(x1, y1+200,width, height, arcade.color.ARMY_GREEN)

s1 = arcade.Sprite("cart.svg")
s1.set_position(200,600)

arcade.finish_render()

arcade.run()