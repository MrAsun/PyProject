from PyProject import *
#


window = Window()
window.transform.size = Vector2(500, 400)


camera = Camera()
camera.set_main()


obj = Object()

obj.transform.size = Vector2(50, 50)
obj.get_component("Render").color = Color(155, 0, 155)


obj.add_component("Physic")
obj.get_component("Physic").gravity = Vector2(0, 0.001)


class Player:
    speed = 0.3


    def Update(self):
        obj.get_component("Physic").velocity =  Vector2(Input.get_axis("A", "D"), -Input.get_axis("S", "W")) * self.speed


obj.register_component("Player", Player())

obj.transform.set_child_object("Camera", camera)

obj.get_component("Collider").size = Vector2(50, 50)



obj2 = UIElements.Text()
obj2.transform.position = Vector2(-250, -200)

obj2.del_component("UI")


terra = Object()
terra.transform.position.y = 150
terra.get_component("Render").color = Color(100, 200, 100)


while Update():
    obj2.Text.text = "x: " + str(int(obj.transform.position.x)) + " | y: " + str(int(obj.transform.position.y))




















