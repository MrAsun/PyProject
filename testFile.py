from PyProject import *


#
project = Project()
#
window = Window()
window.transform.size = Vector2(800, 600)
window.background_color = Color(150, 150, 150)
#
camera = Camera()
camera.set_main()



    # PLAYER
# Player Move
class player_move(component):
    def update(self):
        self.object.transform.rotation += Input.get_axis("A", "D") 
        self.object.transform.size.x += Input.get_axis("W", "S") 
        
# Create player
player = Objects.SblN()
player.transform.size = Vector2(100, 100)
# Add Player Move
player.add_component("player_move", player_move())



obj = Objects.Square()
obj.transform.position = Vector2(100, 300)





while Update():
    pass