import random
import logging
import time
from cube import Cube
import pandas as pd

# Adding Another comment to create PR
class SolvePuzzle:
    def __init__(self) -> None:

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        # Front, back, left, right, top, bottom
        Cube1 = Cube("yellow", "yellow", "red", "blue", "yellow", "green")
        Cube2 = Cube("yellow", "green", "red", "green", "red", "blue")
        Cube3 = Cube("blue", "yellow", "green", "green", "red", "blue")
        Cube4 = Cube("red", "green", "blue", "yellow", "yellow", "red")
        

        # Itterate through all possible orientations of each cube and check if they are considered a solution to the puzzle
        time_now = time.time()
        All_Possible_Orientations_Cube_1 = Cube1.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_2 = Cube2.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_3 = Cube3.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_4 = Cube4.list_all_possible_orientations_per_cube()

        for orientation1 in All_Possible_Orientations_Cube_1:
            for orientation2 in All_Possible_Orientations_Cube_2:
                for orientation3 in All_Possible_Orientations_Cube_3:
                    for orientation4 in All_Possible_Orientations_Cube_4:
                        # Set the orientations of the cubes
                        Cube1.set_orientation(orientation1)
                        Cube2.set_orientation(orientation2)
                        Cube3.set_orientation(orientation3)
                        Cube4.set_orientation(orientation4)
                        # Check if the current orientations solve the puzzle
                        if self.check_solution(Cube1, Cube2, Cube3, Cube4):
                            all_possible_solutions = []


                            possible_solution = {
                                "Cube 1": Cube1.get_orientation(),
                                "Cube 2": Cube2.get_orientation(),
                                "Cube 3": Cube3.get_orientation(),
                                "Cube 4": Cube4.get_orientation()
                            }

                            if possible_solution not in all_possible_solutions:
                                all_possible_solutions.append(possible_solution)

                                print("___________________________________________________________")
                                print("Solution found!")
                                print("Cube 1:", Cube1.get_orientation())
                                print("Cube 2:", Cube2.get_orientation())
                                print("Cube 3:", Cube3.get_orientation())
                                print("Cube 4:", Cube4.get_orientation())
                                print("___________________________________________________________")
                                break  # Exit the loop if a solution is found
                        else:
                            logging.debug("Not a solution")
        
            break
    

    def check_solution(self,  cube1, cube2, cube3, cube4):
            count_of_unique_sides = 0

            top_colors = [cube1.top, cube2.top, cube3.top, cube4.top]
            bottom_colors = [cube1.bottom, cube2.bottom, cube3.bottom, cube4.bottom]
            left_colors = [cube1.left, cube2.left, cube3.left, cube4.left]
            right_colors = [cube1.right, cube2.right, cube3.right, cube4.right]
            front_colors = [cube1.front, cube2.front, cube3.front, cube4.front]
            back_colors = [cube1.back, cube2.back, cube3.back, cube4.back]

            if len(set(top_colors)) == 4 and len(top_colors) == len(set(top_colors)):
                count_of_unique_sides += 1

            if len(set(bottom_colors)) == 4 and len(bottom_colors) == len(set(bottom_colors)):
                count_of_unique_sides += 1

            if len(set(left_colors)) == 4 and len(left_colors) == len(set(left_colors)):
                count_of_unique_sides += 1

            if len(set(right_colors)) == 4 and len(right_colors) == len(set(right_colors)):
                count_of_unique_sides += 1

            if len(set(front_colors)) == 4 and len(front_colors) == len(set(front_colors)):
                count_of_unique_sides += 1

            if len(set(back_colors)) == 4 and len(back_colors) == len(set(back_colors)):
                count_of_unique_sides += 1


            print("Count of unique sides:", count_of_unique_sides)
            if count_of_unique_sides >= 4:
                return True
            
            
            
        

if __name__ == "__main__":
    SolvePuzzle()