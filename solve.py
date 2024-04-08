import logging
import time
from cube import Cube
class SolvePuzzle:
    def __init__(self) -> None:

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        # Front, back, left, right, top, bottom
        Cube1 = Cube("yellow", "yellow", "red", "blue", "yellow", "green")
        Cube2 = Cube("yellow", "green", "red", "green", "red", "blue")
        Cube3 = Cube("blue", "yellow", "green", "green", "red", "blue")
        Cube4 = Cube("red", "green", "blue", "yellow", "yellow", "red")
        
        time_now = time.time()
        All_Possible_Orientations_Cube_1 = Cube1.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_2 = Cube2.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_3 = Cube3.list_all_possible_orientations_per_cube()
        All_Possible_Orientations_Cube_4 = Cube4.list_all_possible_orientations_per_cube()
        # Fetch all possible orientations for each cube. Using a class will retain the position of each color on each cube.

        for cube1 in All_Possible_Orientations_Cube_1:
            for cube2 in All_Possible_Orientations_Cube_2:
                for cube3 in All_Possible_Orientations_Cube_3:
                    for cube4 in All_Possible_Orientations_Cube_4:
                        if self.check_solution(cube1, cube2, cube3, cube4):
                            logging.info("==================================")
                            logging.info("Solution found!")
                            logging.info(f"Cube 1: {cube1}")
                            logging.info(f"Cube 2: {cube2}")
                            logging.info(f"Cube 3: {cube3}")
                            logging.info(f"Cube 4: {cube4}")
                            logging.info(f"Time taken: {time.time() - time_now}")
                            logging.info("==================================")
                            raise SystemExit

    def check_solution(self, cube1, cube2, cube3, cube4):
        """
        Function to validate if the sides of the cubes contain unique colors. They should not contain the same color.
        """
        try:
            cube_top_colors = [cube1['top'], cube2['top'], cube3['top'], cube4['top']]
            cube_bottom_colors = [cube1['bottom'], cube2['bottom'], cube3['bottom'], cube4['bottom']]
            cube_front_colors = [cube1['front'], cube2['front'], cube3['front'], cube4['front']]
            cube_back_colors = [cube1['back'], cube2['back'], cube3['back'], cube4['back']]

            if len(set(cube_top_colors)) == 4 and len(set(cube_bottom_colors)) == 4 and len(set(cube_front_colors)) == 4 and len(set(cube_back_colors)) == 4:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"Error: {e}")
            return False
            
            
        

if __name__ == "__main__":
    SolvePuzzle()