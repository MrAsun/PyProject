from PyProject import *


#
project = Project()
#
window = Window()
window.transform.size = Vector2(800, 600)
#
camera = Camera()
camera.set_main()



    # PLAYER
# Player Move
class player_move(component):
    def update(self):
        self.object.transform.position.x += Input.get_axis("A", "D") * self.object.get_component("speed_text").current_speed
        self.object.transform.position.y += Input.get_axis("W", "S") * self.object.get_component("speed_text").current_speed
# Create player
player = Object() 
player.transform.size = Vector2(100, 100)
# Add Player Move
player.add_component("player_move", player_move())
# Import Player Image
image = Image("Cot.jpg")
# Set render and image
player.add_component("render", render())
player.get_component("render").image = image

# Text behavior
class speed_text(component):
    current_speed = 2
    def update(self):
        self.current_speed += Input.get_axis("Q", "E") * 0.01
# Add speed text
player.add_component("speed_text", speed_text())




#
speed = Object()
speed.transform.position = Vector2(-400, -300)
speed.add_component("text", text())



while Update():
    speed.get_component("text").text = player.get_component("speed_text").current_speed