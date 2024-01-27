from PyProject import *


window = Window()
window.transform.size = Vector2(500, 400)


camera = Camera()
camera.set_main()


obj = Object()
obj.add_component("render", render())


while Update():
    pass
