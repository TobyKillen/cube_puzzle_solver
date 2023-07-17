import random
import pandas
class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        # Front, back, left, right, top, bottom
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def __str__(self) -> str:
        return f"Cube Front: {self.front}, Cube Back: {self.back}, Cube Left: {self.left}, Cube Right: {self.right}, Cube Top: {self.top}, Cube Bottom: {self.bottom}"

    def rotate_cube(self, axis):
        if axis == "random":
            axis = random.choice(["x", "y", "z"])
        if axis == "x":
            self.front, self.top, self.back, self.bottom = self.bottom, self.front, self.top, self.back
        elif axis == "y":
            self.front, self.left, self.back, self.right = self.right, self.front, self.left, self.back
        elif axis == "z":
            self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom
        else:
            raise ValueError(f"Axis must be 'x', 'y', or 'z', not {axis}")
        
    def get_orientation(self):
        return pandas.Series([self.front, self.back, self.left, self.right, self.top, self.bottom], index=["Front", "Back", "Left", "Right", "Top", "Bottom"])
        
    def list_all_possible_orientations_per_cube(self):
        all_possible_orientations = []
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    # Front, back, left, right, top, bottom
                    possible_orientation = Cube(self.front, self.back, self.left, self.right, self.top, self.bottom)
                    all_possible_orientations.append(possible_orientation)
                    self.rotate_cube("z")
                self.rotate_cube("y")
            self.rotate_cube("x")
        return all_possible_orientations

    def set_orientation(self, orientation):
        self.front = orientation.front
        self.back = orientation.back
        self.left = orientation.left
        self.right = orientation.right
        self.top = orientation.top
        self.bottom = orientation.bottom

