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


text_ = UIElements.Text()



    # PLAYER
# Player Move
class player_move(component):
    def update(self):
        self.object.transform.rotation += Input.get_axis("A", "D") * -0.2
        self.object.transform.position += Vector2(self.object.transform.get_local_axe("Up").x, -self.object.transform.get_local_axe("Up").y) * Input.get_axis("S", "W") * .7
        
# Create player
player = Objects.Cot()
player.transform.size = Vector2(100, 100)
# Add Player Move
player.add_component("player_move", player_move())



obj = Objects.Square()
obj.transform.position = Vector2(100, 300)





while Update():
    pass