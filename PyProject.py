# Import
import pygame
import math
import time
import random

# Initialization
pygame.init()
pygame.font.init()























# ======== ADITION FUNCTIONS ================
#   # Type checking
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






ERRORS = {
    "Access" : "Access Error!!! This atribute isonly for reading!!!",    

    "Type_1" : "Type Error!!! This attribute can be only - ",
    
    "Project_exists" : "Project Error!!! You have not created the Project!!!"
    }








































#   # ========== PROJECT
project = None
class Project:
    __project_objects = {"window" : None, "camera" : None, "scene" : None}
    config = {"fixed update time" : 2, "razmer chlena" : 26, "max fps" : 5, "limited fps" : True}

    # Initialization
    def __init__(self):
        # Link
        global project
        project = self

        # Attributes
            # Main
        __name = "Project"
        __company = "DefaultCompany"
        __version = "v.1"
            # Objects
        __project_objects = {"window" : None, "camera" : None}


        #
        scene = Scene("scene")
        scene.load()
        


    # Getters and setters
        # Setters
    def set_name(self, name):
        self.__name = str(name)
    def set_company(self, company):
        self.__company = str(company)
    def set_version(self, version):
        self.__version = str(version)
    #  # Set Attributes
    name = property(lambda self: self.__name, set_name)
    company = property(lambda self: self.__company, set_company)
    version = property(lambda self: self.__version, set_version)
    


    # Add | Set project objects
        # Add
    def add_project_object(self, title, obj):
        self.__project_objects[title] = obj
        # Get
    def get_project_object(self, obj):
        return self.__project_objects[obj]





#   # ========== WINDOW
class Window:
    # Initialization
    def __init__(self):   
        # Check project
        if False_to_exception(project != None, ERRORS["Project_exists"]):
            # Attributes
                # Main
            self.__transform = transform()
            self.__title = "PyProject window"
                # Render
            self.__background_color = Color(10, 10, 10)
        

            # Link
            self.__window = pygame.display.set_mode(self.transform.size())
            project.add_project_object("window", self)


            # Set settings
            pygame.display.set_caption(self.__title)


    # Getters and Setters
        # Setters
    def set_window(self, window):
        raise Exception(ERRORS["Access"])
    def set_transform(self, transform):
        raise Exception(ERRORS["Access"])
    def set_background_color(self, background_color):
        if False_to_exception(type(background_color, Color), ERRORS["Type_1"] + "Color!!!"):
            self.__background_color = background_color
    def set_title(self, title):
            self.__title = str(title)
            pygame.display.set_caption(str(title))
    #    # Set attributes
        # Link
    window = property(lambda self: self.__window, set_window)
        # Attributes
    transform = property(lambda self: self.__transform, set_transform)
    title = property(lambda self: self.__title, set_title)
        # Render
    background_color = property(lambda self: self.__background_color, set_background_color)




    # Update
    def update(self):
        # Check if window exists
        if (self.window != None):
            
            # Update window size if necessary
            if (self.window.get_size() != self.transform.size()):
                self.__window = pygame.display.set_mode(self.transform.size())
                
            # Fill window with background color
            self.window.fill(self.background_color())





#   # ========== SCENE
class Scene:
    # Initialization
    def __init__(self, name, auto_load = True):
        # Attributes
        self.__name = name
        self.__objects = {}
        

        
        # Set
        if auto_load:
            self.load()
    
    # Getters and Setters
        # Setters
    def set_name(self, name):
        self.__name = name
    #    # Set attributes
    name = property(lambda self: self.__name, set_name)
    
    # Objects
    def add_obj(self, obj):
        if False_to_exception(type(obj, Object) or type(obj, Camera), ERRORS["Type_1"] + "Object or Camera!"):
            self.__objects[str(obj)] = obj
    def get_obj(self, name):
        return self.__objects[str(name)]
    def del_obj(self, obj):
        self.__objects[str(obj)] = None
    def get_objects(self):
        return self.__objects


    # Load this scene
    def load(self):
        # Project check
        if False_to_exception(project != None, ERRORS["Project_exists"]):       
            project.add_project_object("scene", self)




#    # ========== CAMERA
class Camera:
    # Initialization
    def __init__(self):
        # Project check
        if False_to_exception(project != None, ERRORS["Project_exists"]):
            # Attributes
            self.object = Object()
            self.transform = transform()





    # Set as main camera
    def set_main(self):
        # Check project
        if False_to_exception(project != None, ERRORS["Project_exists"]):
            project.add_project_object("camera", self)
















































# ADDITION CLASSES

#   # ========== Vector 2
class Vector2:
    
    # Initialization
    def __init__(self, x, y):
        # Attributes
        self.__x = x
        self.__y = y     
        self.center = "CENTER"
               

    # Return self
    def __call__(self):
        #
        if self.center == "LEFT_UP" and False_to_exception(project != None, ERRORS["Project_exists"]):
            return (Vector2(self.x, self.y) + Vector2(-(project.get_project_object("window").transform.size/2).x, (project.get_project_object("window").transform.size/2).y))()
        #
        if self.center == "LEFT_DOWN" and False_to_exception(project != None, ERRORS["Project_exists"]):
            return (Vector2(self.x, self.y) + Vector2(-(project.get_project_object("window").transform.size/2).x, -(project.get_project_object("window").transform.size/2).y))()
        #
        if self.center == "RIGHT_UP" and False_to_exception(project != None, ERRORS["Project_exists"]):
            return (Vector2(self.x, self.y) + Vector2((project.get_project_object("window").transform.size/2).x, (project.get_project_object("window").transform.size/2).y))()
        #
        if self.center == "RIGHT_DOWN" and False_to_exception(project != None, ERRORS["Project_exists"]):
            return (Vector2(self.x, self.y) + Vector2((project.get_project_object("window").transform.size/2).x, -(project.get_project_object("window").transform.size/2).y))()
        #
        if self.center == "CENTER":
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
        self.__red = Math.clamp(red, 0, 255)
        self.__blue = Math.clamp(blue, 0, 255)
        self.__green = Math.clamp(green, 0, 255)
        
    # Return self
    def __call__(self):
        return (self.__red, self.__green, self.__blue)        



    # Getters and setter
        # Settters
    def set_red(self, red):
        if False_to_exception(type(red, int), "Type error!!! This attribute can be only int!!!"):
            self.__red = Math.clamp(red, 0, 255)
    def set_blue(self, blue):
        if False_to_exception(type(blue, int), "Type error!!! This attribute can be only int!!!"):
            self.__blue = Math.clamp(blue, 0, 255)
    def set_green(self, green):
        if False_to_exception(type(green, int), "Type error!!! This attribute can be only int!!!"):
            self.__green = Math.clamp(green, 0, 255)
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
           










        

 



















































# ========== MAIN CLASSES ==========

    # ========== Object
min_update_layer = 0
max_update_layer = 0

class Object:
    # Initialization
    def __init__(self):
        # Attributes
        self.__components = { }
        self.__transform = transform()
        self.__update_layer = 0
        self.__last_fixed_update_time = 0
        
        # Register
        if False_to_exception(project != None, ERRORS["Project_exists"]):
            if False_to_exception(project.get_project_object("scene") != None, "Scene doesn`t exist!!!"):
                project.get_project_object("scene").add_obj(self)
        
        

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
        component_.object = self
        self.__components[title] = component_
        component_.start()
        # Delete component
    def del_component(self, component):
        if self.__components[component] != None:
            self.__components[component].delete()
            self.__components[component] = None




    # ----- UPDATE SELF -----
    def Update(self):
        # Update components
        for component_ in self.__components:
            component = self.__components[component_]
            if component != None:
                if component.enabled:                   
                    component.update()

                    if self.__last_fixed_update_time + project.config["fixed update time"] <= Time.time():
                        self.__last_fixed_update_time = Time.time()
                        component.fixed_update()


         
    















































# ========== COMPONENTS ==========

class component:
    object = None
    __enabled = True    

    # When you add 
    def start(self):
        pass
    
    # Every tick
    def update(self):
        pass
    
    #
    def fixed_update(self):
        pass
    
    # What you delete
    def delete(self):
        pass
    
    
    # Enabled
    def set_enabled(self, enabled):
        if False_to_exception(type(enabled, bool), "Type Error!!! "):
            self.__enabled = enabled
    enabled = property(lambda self: self.__enabled, set_enabled)




#   # RENDER
class render(component):
    # Initialization
    def __init__(self):
        self.__color = Color(255, 255, 255)

    # Getters and Setters
        # Setters
    def set_color(self, color):
        if False_to_exception(type(color, Color), "Type Error!!! color can be only Color"):
            self.__color = color
        # Set attributes
    color = property(lambda self: self.__color, set_color)

    # Update
    def update(self):
        pos = self.object.transform.position("RIGHT_UP")
        project.get_project_object("window").window.set_at((int(pos[0]), int(pos[1])), self.color())


#   # COLLIDER
class collider(component):
    pass


#   # PHYSIC BODY
class physic_body(component):
    pass




#   # Text
class text(component):
    #
    def __init__(self):
        self.__text = "text"

        self.__color = Color(255, 255, 255)
        self.__size = 25
    
    # Getters and Setters
        # Setters
    def set_text(self, text):
        self.__text = str(text)
    def set_color(self, color):
        if False_to_exception(type(color, Color), "Type Error!!! Color can be only Color"):
            self.__color = color
    def set_size(self, size):
        if False_to_exception(type(size, int) or type(size, float), "Type Error!!! Size can be only int or float"):
            self.__size = size
        # Set attributes
    text = property(lambda self: self.__text, set_text)
    color = property(lambda self: self.__color, set_color)
    size = property(lambda self: self.__size, set_size)

    def update(self):
        font = pygame.font.Font(None, int(self.__size))
        text = font.render(self.__text, True, self.__color())
        project.get_project_object("window").window.blit(text, self.object.transform.position("RIGHT_UP"))















































# ========== MAIN FUNCTIONS ==========
last_update_time = 0
def Update():
    # Check project
    if project != None:
                    # Check window
        if project.get_project_object("window") != None: 

                # Window update
            project.get_project_object("window").update()
            
            Time.set_delta_time()
            # Check scene
            if project.get_project_object("scene") != None:
                # Check camera
                if (project.get_project_object("camera") != None):
                
                    # Object update
                    for layer in range(min_update_layer, max_update_layer + 1):
                        for name in project.get_project_object("scene").get_objects():
                            obj = project.get_project_object("scene").get_obj(name)
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
    # Variables
    def clamp(value, min_, max_):
        if value < min_:
            return min_
        if value > max_:
            return max_
        return value
            
    

  
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
last_frame_time = 0
save_time = 0
delta_time = 0
class Time:    
    # ===== Main time management
        # Get time of start
    @staticmethod
    def all_time():
        return int((time.time() * 100) * 1000) / 1000
        # Get time with start
    @staticmethod
    def start_time():
        return time_configs["start_time"]
    @staticmethod
    def time():
        return (Time.all_time() - Time.start_time())
        # Waiting for current time
    @staticmethod
    def wait(time):
        timePoint = Time.time_point()
        while True:
            if timePoint.timer(time):
                return True

    @staticmethod
    def set_delta_time():
        global save_time
        global last_frame_time
        global delta_time
        if Time.time() != last_frame_time:
            delta_time = Time.time() - last_frame_time
            last_frame_time = Time.time()

        else:
            delta_time = last_frame_time - save_time 
            last_frame_time = save_time
            save_time = Time.time()
    
    @staticmethod
    def delta_time():
       return delta_time

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

time_configs = {"start_time" : Time.all_time()}








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
        











class Physic:
    @staticmethod
    def Raycast(startPoint, direction, range_, step=1):
        points = list()
        for i in range(0, range_, step):           
            points.append((startPoint + direction * i)())
        return points












































