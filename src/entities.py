from vector import Vector

class Entity:
    def __init__(self,position,velocity,size):
        self.position = position 
        self.velocity = velocity 
        self.size = size

    def move(self):
        self.position += self.velocity

    def set_velocity(self,velocity):
        self.velocity = velocity

    def update_velocity(self,velocity_delta):
        self.velocity += velocity_delta

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def set_size(self,s):
        self.size = s

    def get_size(self):
        return self.size

    
class Ball(Entity):
    def __init__(self,position,velocity,size):
        super().__init__(position,velocity,size)




class Player(Entity):
    def __init__(self,position,velocity,size):
        super().__init__(position,velocity,size)
        self.points = 0
    def add_point(self):
        self.points += 1


