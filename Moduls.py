# Import
import pygame
import math
# Register
    #
from Addition import *
    #
from PyProject import *






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
time_configs = {"start_time" : time.time()}
last_frame_time = 0

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

    @staticmethod
    def delta_time():
        current_time = Time.time()
        global last_frame_time
        delta_time = current_time - last_frame_time
        last_frame_time = Time.time()
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


