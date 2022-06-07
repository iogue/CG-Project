import math

from core_ext.object3d import Object3D


class MovementCamera(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=1, degrees_per_second=60):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second
        self.initial = self._look_attachment.local_matrix

        self.RESTART = "r"
        self.CONTINUE = "return"
        self.LEFT = "f1"
        self.CENTER = "f2"
        self.RIGHT = "f3"
        self.isGame = False
        self.level = 0

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)
    def remove(self, child):
        self._look_attachment.remove(child)

    def Play(self):
        return self.isGame

    def setPlay(self, play):
        self.isGame = play

    def update(self, input_object, level, win):
        if level == 1 and self.level == 0:
            self.isGame = False
            self.set_position([10,0,-119.25])
            
        if input_object.is_key_down(self.CONTINUE) and self.level == 0:
            self.isGame = False
            self.translate(-2.5,0,0.25)
            self.level = self.level+1
        
        elif input_object.is_key_down(self.CONTINUE) and self.level == 1:
            self.isGame = True
            self.set_position([0,0,0])

        if level == 6 and win == True:
            self.isGame = False
            self.set_position([2.5,0,-119.25])
            self.level = self.level+1

        if level == 6 and win == False:
            self.isGame = False
            self.set_position([5,0,-119.25])
            self.level = self.level+1

        if input_object.is_key_down(self.RESTART) and level == 6:
            self.isGame = True
            self.set_position([0,0,0])
        
        #NIVEL 1
        if input_object.is_key_down(self.CENTER) and level == 1:
            self.isGame = False
        if input_object.is_key_pressed(self.CENTER) and level == 1:
            self.isGame = False
            self.set_position([0.7,-1.5,-15])
        if input_object.is_key_up(self.CENTER) and level == 1:
            self.isGame = True
            self.set_position([0,0,0])
        #===============================

        #NIVEL 2
        if input_object.is_key_down(self.LEFT) and level == 2:
            self.isGame = False
            self.rotate_y(math.pi/2)
        if input_object.is_key_pressed(self.LEFT) and level == 2:
            self.isGame = False
            self.set_position([-10,-1.5,-15])
        if input_object.is_key_up(self.LEFT) and level == 2:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(-math.pi/2)

        if input_object.is_key_down(self.RIGHT) and level == 2:
            self.isGame = False
            self.rotate_y(-math.pi/2)
        if input_object.is_key_pressed(self.RIGHT) and level == 2:
            self.isGame = False
            self.set_position([15,-1.5,-10])
        if input_object.is_key_up(self.RIGHT) and level == 2:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(math.pi/2)
        #=======================================

        #NIVEL 3
        if input_object.is_key_down(self.LEFT) and level == 3:
            self.isGame = False
            self.rotate_y(math.pi/2)
        if input_object.is_key_pressed(self.LEFT) and level == 3:
            self.isGame = False
            self.set_position([-15,0,-18])
        if input_object.is_key_up(self.LEFT) and level == 3:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(-math.pi/2)

        if input_object.is_key_down(self.CENTER) and level == 3:
            self.isGame = False
        if input_object.is_key_pressed(self.CENTER) and level == 3:
            self.isGame = False
            self.set_position([5,0,-20])
        if input_object.is_key_up(self.CENTER) and level == 3:
            self.isGame = True
            self.set_position([0,0,0])

        if input_object.is_key_down(self.RIGHT) and level == 3:
            self.isGame = False
            self.rotate_y(-math.pi/2)
        if input_object.is_key_pressed(self.RIGHT) and level == 3:
            self.isGame = False
            self.set_position([5,0,-18])
        if input_object.is_key_up(self.RIGHT) and level == 3:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(math.pi/2)
        #=======================================

        #NIVEL 4
        if input_object.is_key_down(self.LEFT) and level == 4:
            self.isGame = False
            self.rotate_y(math.pi/2)
        if input_object.is_key_pressed(self.LEFT) and level == 4:
            self.isGame = False
            self.set_position([-18,-1.5,-15])
        if input_object.is_key_up(self.LEFT) and level == 4:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(-math.pi/2)

        if input_object.is_key_down(self.CENTER) and level == 4:
            self.isGame = False
        if input_object.is_key_pressed(self.CENTER) and level == 4:
            self.isGame = False
            self.set_position([0,-1.5,-15])
        if input_object.is_key_up(self.CENTER) and level == 4:
            self.isGame = True
            self.set_position([0,0,0])

        if input_object.is_key_down(self.RIGHT) and level == 4:
            self.isGame = False
            self.rotate_y(-math.pi/2)
        if input_object.is_key_pressed(self.RIGHT) and level == 4:
            self.isGame = False
            self.set_position([13,-1.5,-20])
        if input_object.is_key_up(self.RIGHT) and level == 4:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(math.pi/2)
        #=======================================

        #NIVEL 5
        if input_object.is_key_down(self.LEFT) and level == 5:
            self.isGame = False
            self.rotate_y(math.pi/2)
        if input_object.is_key_pressed(self.LEFT) and level == 5:
            self.isGame = False
            self.set_position([-5,-1.5,5])
        if input_object.is_key_up(self.LEFT) and level == 5:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(-math.pi/2)

        if input_object.is_key_down(self.CENTER) and level == 5:
            self.isGame = False
        if input_object.is_key_pressed(self.CENTER) and level == 5:
            self.isGame = False
            self.set_position([0.7,-1.5,-22])
        if input_object.is_key_up(self.CENTER) and level == 5:
            self.isGame = True
            self.set_position([0,0,0])

        if input_object.is_key_down(self.RIGHT) and level == 5:
            self.isGame = False
            self.rotate_y(-math.pi/2)
        if input_object.is_key_pressed(self.RIGHT) and level == 5:
            self.isGame = False
            self.set_position([10,-1.5,-12])
        if input_object.is_key_up(self.RIGHT) and level == 5:
            self.isGame = True
            self.set_position([0,0,0])
            self.rotate_y(math.pi/2)