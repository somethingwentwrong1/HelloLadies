# from python system, import exit and randint (random integer)
from sys import exit
from random import randint

# a class that defines enter that contains self integer.
class Scene(object):
# defined enter as not configured syntax.
    def enter(self):    
        print "Not configured. Subclass it and implement enter()."
        exit(1)

# a class that consists of as follows:
class Engine(object):
    # opperates the scene_map by itself.
    def __init__(self, scene_map):
        self.scene_map = scene_map
    # 
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
        
# 
class Death(Scene):

    def enter(self):
        gg = [
        "You failed to survive.",
         "I think you needed some more skill to play this",
         "Beinging such a coward.",
         "Well basically you suck."
    ]

    def enter(self):
        print Death.gg[randint(0, len(self.gg)-1)]
        exit(1)
        


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

