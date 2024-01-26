# Import
import pygame
import math
import time
import random

# Register
    #
from Addition import Vector2
from Addition import Color
    #
from Moduls import Input
from Moduls import Math
from Moduls import Random


# Initialization
pygame.init()
pygame.font.init()











# ======== ADITION FUNCTIONS ================
#   # Type checking
def type(variable, type):
        if isinstance(variable, type):
            return True
        return False

#   # Exceptions
def False_to_exception(value, error):
    if not value:
        raise Exception(error)
    return True
def True_to_exception(value, error):
    if value:
        raise Exception(error)
    return False


def position_to_World(pos):
    if False_to_exception(type(pos, Vector2), "Type Error!!! Pos can be only Vector2"):
        return pos + program_objects["window"].transform.size/2
#   # Positions
def pos_to_world(pos):
    if False_to_exception(type(pos, Vector2), ""):
        return pos + program_objects["window"].transform.size/2 - program_objects["camera"].transform.position








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
        self.__components = { }
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
        component_.object_ = self
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
    def update(self):
        pos = position_to_World(self.object.transform.position)

        program_objects["window"].window.set_at((int(pos.x), int(pos.y)), (255, 255, 255))


#   # COLLIDER
class collider(component):
    pass


#   # PHYSIC BODY
class physic_body(component):
    pass











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

































































