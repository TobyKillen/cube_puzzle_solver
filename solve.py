import random
import logging

class Cube:
    def __init__(self, front, back, left, right, top, bottom):
        self.front = front
        self.back = back
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


    # Func to rotate cube in any given direction
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



    def does_cube_match(self, TestCube1, TestCube2):
        if TestCube1.front == TestCube2.front:
            if TestCube1.back == TestCube2.back:
                if TestCube1.left == TestCube2.left:
                    if TestCube1.right == TestCube2.right:
                        if TestCube1.top == TestCube2.top:
                            if TestCube1.bottom == TestCube2.bottom:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False






class SolvePuzzle:
    def __init__(self) -> None:
        # Front, back, left, right, top, bottom
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        Cube1 = Cube("yellow", "green", "red", "blue", "green", "red")
        Cube2 = Cube("red", "yellow", "yellow", "blue", "green", "red")
        Cube3 = Cube("blue", "yellow", "green", "green", "red", "blue")
        Cube4 = Cube("red", "blue", "yellow", "yellow", "yellow", "green")

        is_puzzle_solved = False
        while not is_puzzle_solved:
            
            logging.debug("Beginning to Solve Puzzle")

            cube1_cube2_match = False
            while not cube1_cube2_match:
                logging.debug("Cube 1 and Cube 2 do not match - Rotate Cube 2")
                Cube1.rotate_cube("random")
                Cube2.rotate_cube("random")
                cube1_cube2_match = Cube1.does_cube_match(Cube1, Cube2)
                logging.debug(f"Cube 1 and Cube 2 match: {cube1_cube2_match}")
                is_puzzle_solved = True
                

            


    def is_puzzle_solved(self, Cube1, Cube2, Cube3, Cube4) -> bool:
        if Cube1.front == Cube1.back == Cube1.top == Cube1.bottom:
            if Cube2.front == Cube2.back == Cube2.top == Cube2.bottom:
                if Cube3.front == Cube3.back == Cube3.top == Cube3.bottom:
                    if Cube4.front == Cube4.back == Cube4.top == Cube4.bottom:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    SolvePuzzle()