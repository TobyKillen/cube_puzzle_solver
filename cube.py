import random
class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        # Front, back, left, right, top, bottom
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def get_cube_orientation(self):
        return self.front, self.back, self.left, self.right, self.top, self.bottom

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
        
    def list_all_possible_orientations_per_cube(self):
        all_possible_orientations = []
        for _ in range(4):
            for _ in range(4):
                for _ in range(4):
                    # Front, back, left, right, top, bottom
                    possible_orientation = self.get_cube_orientation()
                    if possible_orientation not in all_possible_orientations:
                        cube_pos = {
                            "front": possible_orientation[0],
                            "back": possible_orientation[1],
                            "left": possible_orientation[2],
                            "right": possible_orientation[3],
                            "top": possible_orientation[4],
                            "bottom": possible_orientation[5]
                        }
                        all_possible_orientations.append(cube_pos)
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

