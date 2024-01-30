from PyProject import *


project = Project()


window = Window()
window.transform.size = Vector2(1000, 1000)


camera = Camera()
camera.set_main()

class player(component):
    def update(self):
        pass
        
obj = Object() 
obj.add_component("pizda", player())

obj.transform.size = Vector2(100, 100)

image = Image("Cot.jpg")
obj.add_component("render", render())
obj.get_component("render").image = image



while Update():
    pass