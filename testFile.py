from PyProject import *


project = Project()


window = Window()
window.transform.size = Vector2(500, 400)


camera = Camera()
camera.set_main()

class player(component):
    def fixed_update(self):
        pass

obj = Object() 
obj.add_component("pizda", player())




while Update():
    if Input.get_key("W"):
        print(Time.delta_time())