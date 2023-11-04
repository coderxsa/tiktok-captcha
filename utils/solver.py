# This is how easy it is to solve TikTok captchas

import cv2
import base64
import numpy as np


class PuzzleSolver:
    def __init__(self, base64puzzle, base64piece):
        self.puzzle = base64puzzle
        self.piece = base64piece

    def get_position(self):
        puzzle = self.__background_preprocessing()
        piece = self.__piece_preprocessing()
        matched = cv2.matchTemplate(
          puzzle, 
          piece, 
          cv2.TM_CCOEFF_NORMED
    )
# solver still works but i removed the rest of the code for reasons!
