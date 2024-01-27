from PyProject import *


project = Project()


window = Window()
window.transform.size = Vector2(500, 400)


camera = Camera()
camera.set_main()




scene = Scene(0)
obj = Object()
obj.transform.position = Vector2(0, 0)
obj.add_component("text", text())


scene2 = Scene(1)
obj2 = Object()
obj2.transform.position = Vector2(100, 100)
obj2.add_component("text", text())




while Update():
    if Input.get_key("Q"):
        scene.load()
    if Input.get_key("W"):
        scene2.load()