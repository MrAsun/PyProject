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
                for obj_name in self.__child_objects:
                    obj = self.__child_objects[obj_name]
                    if obj != None:
                        obj.transform.position += delta_pos
    def set_size(self, size):
        if False_to_exception(type(size, Vector2), "Type Error!!! This attribute can be only Vector2"):
            delta_size = size - self.__size
            self.__size = size
            if len(self.__child_objects) != 0:
                for obj_name in self.__child_objects:
                    obj = self.__child_objects[obj_name]
                    if obj != None:
                        obj.transform.size += delta_size
    def set_rotation(self, rotation):
        if False_to_exception(type(rotation, int) or type(rotation, float), "Type Error!!! This attribute can be only int or float"):
            delta_rotation = rotation - self.__rotation
            self.__rotation = rotation
            if len(self.__child_objects) != 0:
                for obj_name in self.__child_objects:
                    obj = self.__child_objects[obj_name]
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
    def update(self):
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
        self.object = Object()
        self.transform = transform()





    # Set as main camera
    def set_main(self):
        program_objects["camera"] = self
        

 













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
        # Get component
    def get_component(self, component):
        if component in self.__components:
            return self.__components[component]
        return None
        # Add new component
    def add_component(self, title, component_):
        self.__components[title] = component_
        component_.object = self
        component_.start()
        # Delete component
    def del_component(self, component):
        if self.__components[component] != None:
            self.__components[component].delete()
            self.__components[component] = None




    # ----- UPDATE SELF -----
    def Update(self):
        #
            #
        
            # Update components
            for component_ in self.__components:
                component = self.__components[component_]
                if component != None:
                    if component.enabled:
                        component.update()


         
    









# ========== COMPONENTS ==========


class component:
    object_ = None
    __enabled = True    

    # When you add 
    def start(self):
        pass
    
    # Every tick
    def update(self):
        pass
    
    # Whet you delete
    def delete(self):
        pass
    
    
    # Enabled
    def set_enabled(self, enabled):
        if False_to_exception(type(enabled, bool), "Type Error!!! "):
            self.__enabled = enabled
    enabled = property(lambda self: self.__enabled, set_enabled)




#   # RENDER
class render(component):
    pass


#   # COLLIDER
class collider(component):
    pass


#   # PHYSIC BODY
class physic_body(component):
    pass




#   # LIGHT
class light(component):
    def start(self):
        self.radius = 50








# ========== MAIN FUNCTIONS ==========

def Update():
    # Check window
    if program_objects["window"] != None: 
        
        # Window update
        program_objects["window"].update()
        
        # Check camera
        if (program_objects["camera"] != None):
                
            
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




















class Physic:
    @staticmethod
    def Raycast(startPoint, direction, range_, step=1):
        points = list()
        for i in range(0, range_, step):           
            points.append((startPoint + direction * i)())
        return points



























































