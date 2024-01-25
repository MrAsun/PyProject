# Import
import pygame
import math
import time
import random


# Initialization
pygame.init()
pygame.font.init()














# ======== ADITION FUNCTIONS ================
    # Type checking
def type(variable, type):
        if isinstance(variable, type):
            return True
        return False

# Exceptions
def False_to_exception(value, error):
    if not value:
        raise Exception(error)
    return True
def True_to_exception(value, error):
    if value:
        raise Exception(error)
    return False
























# ========== TYPE CLASSES ==========

    # ========== Vector 2
class Vector2:
    
    # Initialization
    def __init__(self, x, y):
        # Attributes
        self.__x = x
        self.__y = y     
               
    # Return self
    def __call__(self):
        return (self.__x, self.__y)        


    # Getters and setters
        # Setters
    def set_x(self, x):
        if False_to_exception(type(x, int) or type(x, float), "Type error!!! This attribute can be only int or float!!!"):
            self.__x = x        
    def set_y(self, y):
        if False_to_exception(type(y, int) or type(y, float), "Type error!!! This attribute can be only int or float!!!"):
            self.__y = y  
        # Set attributes
    x = property(lambda self: self.__x, set_x)
    y = property(lambda self: self.__y, set_y)


    # Arithmetic
    def __add__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x + other.__x, self.__y + other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x + other, self.__y + other)
    def __sub__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x - other.__x, self.__y - other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x - other, self.__y - other)
    def __truediv__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x / other.__x, self.__y / other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x / other, self.__y / other)
    def __mul__(self, other):
        if type(other, Vector2):
            return Vector2(self.__x * other.__x, self.__y * other.__y)
        if type(other, int) or type(other, float):
            return Vector2(self.__x * other, self.__y * other)


    # Addition
        # Distance
    @staticmethod
    def distance(pos1, pos2):
        return math.sqrt((pos2.x - pos1.x) ** 2 + (pos2.y- pos1.y) ** 2)
        # Axis
    @staticmethod
    def Up():
        return Vector2(0, 1)
    @staticmethod
    def Down():
        return Vector2(0, -1)
    @staticmethod
    def Right():
        return Vector2(1, 0)
    @staticmethod
    def Left():
        return Vector2(-1, 0)
        # Get direction
    @staticmethod
    def Direction(angle):
        return Vector2(Math.cos(angle), Math.sin(angle))






#   # ========== Color
class Color:
    
    # Initialization
    def __init__(self, red, blue, green):
        # Attributes
        self.__red = red
        self.__blue = blue
        self.__green = green
        
    # Return self
    def __call__(self):
        return (self.__red, self.__blue, self.__green)        


    # Getters and setter
        # Settters
    def set_red(self, red):
        if False_to_exception(type(red, int), "Type error!!! This attribute can be only int!!!"):
            self.__red = red
    def set_blue(self, blue):
        if False_to_exception(type(blue, int), "Type error!!! This attribute can be only int!!!"):
            self.__blue = blue
    def set_green(self, green):
        if False_to_exception(type(green, int), "Type error!!! This attribute can be only int!!!"):
            self.__green = green
        # Register attributes
    red = property(lambda self: self.__red, set_red)
    blue = property(lambda self: self.__blue, set_blue)
    green = property(lambda self: self.__green, set_green)

























# ========== ADDITION CLASSES ==========

#   # ========== Transform
class transform:
    # Initialization
    def __init__(self):
        # Attributes
            # Properties
        self.__enabled = True
            # Main
        self.__position = Vector2(0, 0)
        self.__size = Vector2(10, 10)
        self.__rotation = 0
            # Addition
        self.__child_objects = {}
            # Save last
        self.__last_pos = Vector2(0, 0)
        self.__last_rot = 0
        

        # Local axis
        self.__local_axis = {
            "Up" : 90, "Down" : 270, "Right" : 0, "Left" : 180
            }
        

    # Getters and setters
        # Setters
    def set_position(self, position):
        if False_to_exception(type(position, Vector2), "Type Error!!! This attribute can be only Vector2"):
            delta_pos = position - self.__position
            self.__position = position
            if len(self.__child_objects) != 0:
                for obj in self.__child_objects.values:
                    if obj != None:
                        obj.transform.position += delta_pos
    def set_size(self, size):
        if False_to_exception(type(size, Vector2), "Type Error!!! This attribute can be only Vector2"):
            delta_size = size - self.__size
            self.__size = size
            if len(self.__child_objects) != 0:
                for obj in self.__child_objects.values:
                    if obj != None:
                        obj.transform.size += delta_size
    def set_rotation(self, rotation):
        if False_to_exception(type(rotation, int) or type(rotation, float), "Type Error!!! This attribute can be only int or float"):
            delta_rotation = rotation - self.__size
            self.__rotation = rotation
            if len(self.__child_objects) != 0:
                for obj in self.__child_objects.values:
                    if obj != None:
                        obj.transform.rotation += delta_rotation
    def set_enabled(self, enabled):
        if False_to_exception(type(enabled, bool), "Type Error!!! This attribute can be only bool"):
            self.__enabled = enabled
        # Register attributes
            # Properties
    enabled = property(lambda self: self.__enabled, set_enabled)
            # Main
    position = property(lambda self: self.__position, set_position)
    size = property(lambda self: self.__size, set_size)
    rotation = property(lambda self: self.__rotation, set_rotation)
    

    # ===== Addition function

        # Child objects
    def set_child_object(self, title, obj):
        if False_to_exception(type(title, str) and type(obj, Object), "Type Error!!! Title must be str! Obj must be Object!"):
            self.__child_objects[title] = obj
    def get_child_object(self, title):
        if self.__child_objects.get(title):
             return self.__child_objects[title]
        return None
    def del_child_object(self, title):
        self
        self.__child_objects[title] = None
        
        # Local axis
    def get_local_axe(self, axis):
        angle = self.__rotation + self.__local_axis[axis]
        axe = Vector2.Direction(angle)
        return axe
    
        # Set rotation to other position
    def look_at(self, other_position):
        delta_pos = self.position - other_position
            
        distance = Vector2.distance(self.position, other_position)

        sin = delta_pos.y / distance
        cos = delta_pos.x / distance
        
        angle = Math.get_angle(cos, sin)
            
        self.rotation = angle
           























# ========== PROGRAM CLASSES ==========

    # List of program objects
program_objects = {
    "window" : None, "camera" : None
    }





    # ========== Window
class Window:
    # Initialization
    def __init__(self):        
        # Attributes
            # Main
        self.__transform = transform()
        self.__title = "PyProject window"
            # Render
        self.__background_color = Color(10, 10, 10)
        

        # Link
        program_objects["window"] = self
        self.__window = pygame.display.set_mode(self.transform.size())

        # Set settings
        pygame.display.set_caption(self.__title)


    # Getters and Setters
        # Setters
    def set_window(self, window):
        raise Exception("Access Error!!! This attribute is only for reading!!!")
    def set_transform(self, transform):
        raise Exception("Access Error!!! This attribute is only for reading!!!")
    def set_background_color(self, background_color):
        if False_to_exception(type(background_color, Color), "Type Error!!! This attribute can be only Color!!!"):
            self.__background_color = background_color
    def set_title(self, title):
        if False_to_exception(type(title, str), "Type Error!!! This attribute can be onlu string!!!"):
            self.__title = title
            pygame.display.set_caption(title)

    # Register attributes
        # Link
    window = property(lambda self: self.__window, set_window)
        # Attributes
    transform = property(lambda self: self.__transform, set_transform)
    title = property(lambda self: self.__title, set_title)
        # Render
    background_color = property(lambda self: self.__background_color, set_background_color)




    # Update
    def Update(self):
        # Transform update
        self.__transform.Update()        

        # window check
        if (self.window != None):
            
            # Size
            if (self.window.get_size() != self.transform.size()):
                self.__window = pygame.display.set_mode(self.transform.size())
                
            # Background
            self.window.fill(self.background_color())





#    # ========== Camera
class Camera:
    def __init__(self):
        # Attributes
        self.transform = transform()





    # Set as main camera
    def set_main(self):
        program_objects["camera"] = self
        



    # Transform update
    def Update(self):
        self.transform.Update()      














# ========== MAIN CLASSES ==========
    # ========== Object
# List of objects
objects = list()
min_update_layer = 0
max_update_layer = 0

class Object:
    # Initialization
    def __init__(self):
        # Attributes
        self.__components = {
        "Render" : None, "Collider" : None, "Physic" : None, "Text" : None, "UI" : None
        }
        self.__transform = transform()
        self.__update_layer = 0
        
        
        # Register
        objects.append(self)
        

        # Static configure
        self.add_component("Render")
        self.get_component("Render").mesh = Mesh.square();
    
        self.add_component("Collider")

    # Getters and setters
        #
    def get_transform(self):
        return self.__transform
    transform = property(get_transform)
    def get_update_layer(self):
        return self.__update_layer
        #
    def set_update_layer(self, layer):
        if False_to_exception(type(layer, int), ""):
            self.__update_layer = layer
            
            global max_update_layer
            global min_update_layer            

            if layer > max_update_layer:
                max_update_layer = layer
            if layer < min_update_layer:
                min_update_layer = layer
        #
    update_layer = property(get_update_layer, set_update_layer)
                

    # ----- COMPONENTS -----
    #region
        # Get component
    def get_component(self, component):
        if component in self.__components:
            return self.__components[component]
        return None
        # Add new component
    def add_component(self, component):
        if component == "Render":
            self.__components["Render"] = Render(self)
        if component == "Collider":
            self.__components["Collider"] = Collider(self)
        if component == "Physic":
            self.__components["Physic"] = Physic(self)
        if component == "Text":
            self.__components["Text"] = Text(self)


        if component == "UI":
            self.__components["UI"] = UI()
            program_objects["camera"].transform.set_child_object(str(self), self)

        # Register component
    def register_component(self, title, component):
        self.__components[title] = component    
        # Delete component
    def del_component(self, component):
        if component == "UI":
            program_objects["camera"].transform.del_child_object(str(self))
            self.__components[component] = None

        self.__components[component] = None
    #endregion



    # ----- UPDATE SELF -----
    #region 
    def Update(self):
        #
            #
            self.transform.Update()    
        
            # Update components
            for component_ in self.__components:
                component = self.__components[component_]
                if component != None:
                    component.Update()
    #endregion


         
    









# ========== COMPONENTS ==========

    # Render
class Render:
    # Initialization
    def __init__(self, obj):
        self.__mesh = Mesh()
        self.__color = Color(255, 255, 255)
                
        self.__obj = obj
        
    # Getters ans setters
    #region
        # Getters
    def get_mesh(self):
        return self.__mesh
    def get_color(self):
        return self.__color
        # Setters
    def set_mesh(self, mesh):
        if False_to_exception(type(mesh, Mesh), "Type Error!!! This attribute can be only Mesh"):
            mesh.obj = self.__obj
            self.__mesh = mesh
    def set_color(self, color):
        if False_to_exception(type(color, Color), "Type Error!!! This attribute can be only Color"):
            self.__color = color
        # Attribute setting
    mesh = property(get_mesh, set_mesh)
    color = property(get_color, set_color)
    #endregion


        
    #
    def Update(self):
        self.__mesh.Update()
        #
        center = self.__obj.transform.position + program_objects["window"].transform.size/2 - program_objects["camera"].transform.position

        #
        poses = []
        for pos in self.mesh.vertices:
            poses.append((pos.position + center)())
            
        #
        pygame.draw.polygon(program_objects["window"].window, self.color(), poses, 3)
   
    



#    # Collider
class Collider:
    # Initialization
    def __init__(self, obj):
        self.obj = obj    
    
        self.__points = []        

        self.mesh = None
        
        #
        self.center = Vector2(0, 0)

        #
        self.type = "Rectangle"
         # Rectangle
        self.size = Vector2(10, 10)
        
        
    #
    def Update(self):
        #
        if self.type == "Rectangle":
            #
            for obj2 in objects:
                #
                if obj2.get_component("Collider") != None:
                    #
                    if obj2.get_component("Collider").type == "Rectangle":
                        collision = (
                            
                            self.obj.transform.position.x < obj2.transform.position.x + obj2.get_component("Collider").size.x
                           
                            and self.obj.transform.position.x + self.size.x > obj2.transform.position.x and
                        self.obj.transform.position.y < obj2.transform.position.y + obj2.get_component("Collider").size.y and self.obj.transform.position.y + self.size.y > obj2.transform.position.y
                        
                        )
                        
                        if collision:
                            print(0)
    




#    # Physic
class Physic:
    # Initialization
    def __init__(self, obj):
        self.__gravity = Vector2(0, -0.1)
        
        #
        self.velocity = Vector2(0, 0)
        self.angular_velocity = 0
        
        #
        self.obj = obj
        

    # Getters and setters
    #region
        # Getters
    def get_gravity(self):
        return self.__gravity
        # Setters
    def set_gravity(self, gravity):
        if False_to_exception(type(gravity, Vector2), "Type Error!!! This attribute can be only Vector2"):
            self.__gravity = gravity
        # Set attributes
    gravity = property(get_gravity, set_gravity)

    #endregion
      
    #
    def Update(self):
        # Velocity config
        self.velocity += self.gravity        

        # Set velocity
        self.obj.transform.position += self.velocity
        self.velocity = Vector2(0, 0)
        

        #
        self.obj.transform.rotation += self.angular_velocity
        self.angular_velocity = 0



#    # Text
class Text:
    
    #
    def __init__(self, obj):
        self.__text = "TEXT"
        self.obj = obj
        self.color = Color(255,255,255)
        


    # Getters and Setters
    #region
        # Getters
    def get_text(self):
        self.__text
        # Setters
    def set_text(self, text):
        if False_to_exception(type(text, str), "Type Error!!! This attribute can be only str"):
            self.__text = text
        # Set attribute
    text = property(get_text, set_text)
    #endregion



    def Update(self):
        f1 = pygame.font.Font(None, 36)
        text = f1.render(self.__text, True, self.color())
        center = self.obj.transform.position + program_objects["window"].transform.size/2 - program_objects["camera"].transform.position
        program_objects["window"].window.blit(text, (center)())


class UI:
    def Update(self):
        pass











# ===== classes for OBJECTS ===== 

    # ========== Meshes
class Mesh:
    #
    def __init__(self): 
        self.vertices = list()
        self.triangles = list()
        
        self.__obj = None
        self.size = 1
        # Getters
    def get_obj(self):
        pass
        # Setters
    def set_obj(self, obj):
        self.Reset(obj)
        #
        
        #
    obj = property(get_obj, set_obj)
    



    def Reset(self, obj):
        self.__obj = obj        
        
        for vertex in self.vertices:
            vertex.position /= self.size
            vertex.position *= obj.transform.size
            
            delta_pos = vertex.position - obj.transform.position
            
            distance = Vector2.distance(vertex.position, obj.transform.position)

            sin = delta_pos.y / distance
            cos = delta_pos.x / distance
        
            angle = Math.get_angle(cos, sin)
            
            angle = angle - obj.transform.rotation
            
            vertex.distance = distance
            vertex.angle = angle
        self.size = obj.transform.size


    def Update(self):
        if self.size != self.__obj.transform.size:
            self.set_obj(self.__obj)            

        for vertex in self.vertices:
            angle = vertex.angle + self.__obj.transform.rotation          
            sin = Math.sin(angle)
            cos = Math.cos(angle)

            vertex.position = Vector2(cos * vertex.distance, sin * vertex.distance)


    #
    def square():
        mesh = Mesh()        

        mesh.vertices.append(Vertex(Vector2(-0.5, -0.5)))
        mesh.vertices.append(Vertex(Vector2(-0.5, 0.5)))
        mesh.vertices.append(Vertex(Vector2(0.5, 0.5)))
        mesh.vertices.append(Vertex(Vector2(0.5, -0.5)))
        
        mesh.triangles.append(Triangle(0, 1, 3))
        mesh.triangles.append(Triangle(0, 2, 3))
        
        return mesh
    
    #
    def triangle():
        mesh = Mesh()        

        mesh.vertices.append(Vertex(Vector2(-0.5, -0.5)))
        mesh.vertices.append(Vertex(Vector2(0, 0.5)))
        mesh.vertices.append(Vertex(Vector2(0.5, -0.5)))
        
        mesh.triangles.append(Triangle(0, 1, 2))
        
        return mesh


class Vertex:
    # Attributes
    position = Vector2(0, 0)
    
    distance = 0
    angle = 0
        
    # Initialization
    def __init__(self, pos):
        # position
        self.position = pos

        
        
    # ========== Triangle
class Triangle:
    # Attributes
    vertex1 = 0
    vertex2 = 1
    vertex3 = 2


    # Initialization
    def __init__(self, v1, v2, v3):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3


    # Call
    def __call__(self):
        return (self.vertex1, self.vertex2, self.vertex3)




















# ========== MAIN FUNCTIONS ==========

def Update():
    # Check window
    if program_objects["window"] != None: 
        
        # Window update
        program_objects["window"].Update()
        
        # Check camera
        if (program_objects["camera"] != None):
                
            program_objects["camera"].Update()
            
            # Object update
            for layer in range(min_update_layer, max_update_layer + 1):
                for obj in objects:
                    if obj.get_component("UI") == None and obj.update_layer == layer:
                        obj.Update()
            # UI update
            for layer in range(min_update_layer, max_update_layer + 1):
                for obj in objects:
                    if obj.get_component("UI") != None and obj.update_layer == layer:
                        obj.Update()


        # Buffers swap
        pygame.display.flip()
        

    # Exit from project
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
    return True











# ========== MODULS ==========

    # ========== Math
class Math:
  
    # ===== Angle
    @staticmethod
    def radians(degrees):
        return math.radians(degrees)
    @staticmethod
    def degrees(radians):
        return math.degrees(radians)
    @staticmethod
    def get_angle(cos, sin):
            angle = Math.arccos(Math.abs(cos)) 
                    
            if cos > 0 and sin > 0:
                angle = angle + 0
            if cos < 0 and sin > 0:
                angle = angle + 90
            if cos < 0 and sin < 0:
                angle = angle + 180
            if cos > 0 and sin < 0:
                angle = angle + 270
    
            return angle

    # ===== sin/cos and arcsin/arccos

        # sin (rad)
    @staticmethod
    def sin_rad(angle):
        return math.sin(angle)
        # cos (rad)
    @staticmethod
    def cos_rad(angle):
        return math.cos(angle)

            # arcsin (rad)
    @staticmethod
    def arcsin_rad(angle):
        return math.asin(angle)
        # arccos (rad)
    @staticmethod
    def arcco_rads(angle):
        return math.acos(angle)
    


         # sin
    @staticmethod
    def sin(angle):
        result = math.sin(math.radians(angle))
        return 0 if abs(result) < 1e-10 else result
        # cos
    @staticmethod
    def cos(angle):
        result = math.cos(math.radians(angle))
        return 0 if abs(result) < 1e-10 else result    
    
        # arcsin
    @staticmethod
    def arcsin(angle):
        return Math.degrees(math.asin(angle))
        # arccos
    @staticmethod
    def arccos(angle):
        return Math.degrees(math.acos(angle))
    


    @staticmethod
    def abs(n):
        if n < 0:
            return -n
        return n





#    # ========== Time
time_configs = {"start_time" : time.time()}

class Time:    
    # ===== Main time management
        # Get time of start
    @staticmethod
    def all_time():
        return time_configs["start_time"]
        # Get time with start
    @staticmethod
    def time():
        return time.time() - time_configs["start_time"]
        # Waiting for current time
    @staticmethod
    def wait(time):
        timePoint = Time.time_point()
        while True:
            if timePoint.timer(time):
                return True;


    # Point in the time
    class time_point:
        # Attributes
        ticks = 0
        
        # Initialization
        def __init__(self):
            self.reset()
            
        # Reset ticks
        def reset(self):
            self.ticks = Time.time()
        
        # Get delta time
        def delta_time(self, reset = False):

			# Save delta
            delta = Time.time() - self.ticks

			# Reset
            if (reset):
                self.reset()

			# Return
            return delta

		# Timer(float currentTime - time for timer, bool reset - return and reset ticks)
        def timer(self, current_time, reset = False):

			# Save delta
            delta = self.delta_time()

			# Reset
            if reset and delta > current_time:
                self.reset()

			# Return 
            return delta > current_time
   




#  # ========== Random
class Random:
    @staticmethod
    def range(min_, max_):
        return random.randint(min_, max_)


#    # ========== Input
class Input:
    # List of keys
    keys = {
        #
        "Q" : pygame.K_q, "W" : pygame.K_w, "E" : pygame.K_e, "R" : pygame.K_r, "T" : pygame.K_t,
        "Y" : pygame.K_y, "U" : pygame.K_u, "I" : pygame.K_i, "O" : pygame.K_o, "P" : pygame.K_p,
        "A" : pygame.K_a, "S" : pygame.K_s, "D" : pygame.K_d, "F" : pygame.K_f, "G" : pygame.K_g,
        
        #
        }
    
    # List of buttons
    buttons = {
        "RMB" : (pygame.MOUSEBUTTONUP, 0)
        }




    # Get key
    @staticmethod
    def get_key(key):
        #
        if key in Input.keys:
            keys = pygame.key.get_pressed()
            return keys[Input.keys[key]]
    
        #
        if key in Input.buttons:
            buttons = pygame.mouse.get_pressed()
            print(pygame.MOUSEBUTTON)
    



    # Get axis of 2 keys
    @staticmethod
    def get_axis(min_key, max_key, type = "prefer 1"):
        
        #
        if type == "prefer 1":
            if Input.get_key(min_key):
                return -1
            if Input.get_key(max_key):
                return 1
            return 0
        



    # Get position of something
    def get_pos(obj):
        if obj == "Mouse":
            return Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) - program_objects["window"].transform.size/2

















#   # UI
class UIElements:
    #
    @staticmethod
    def Text():
        #
        text = Object()
        
        #
        text.add_component("Text")
        text.add_component("UI")
        

        #
        text.del_component("Render")
        

        #
        text.Text = text.get_component("Text")
        text.UI = text.get_component("UI")

        #
        return text
































































