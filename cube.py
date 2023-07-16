import random

class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


    # Func to rotate cube in any given direction
    def rotate_cube(self, direction):
        if direction == "right":
            self.front, self.right, self.back, self.left = self.right, self.back, self.left, self.front
        elif direction == "left":
            self.front, self.right, self.back, self.left = self.left, self.front, self.right, self.back
        elif direction == "up":
            self.front, self.top, self.back, self.bottom = self.bottom, self.front, self.top, self.back
        elif direction == "down":
            self.front, self.top, self.back, self.bottom = self.top, self.back, self.bottom, self.front
        elif direction == "front":
            self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        elif direction == "back":
            self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top
        elif direction == "random":
            # Randomly choose a direction to rotate cube
            directions = ["right", "left", "up", "down", "front", "back"]
            random_direction = random.choice(directions)
            self.rotate_cube(random_direction)
        else:
            print("Invalid direction")
