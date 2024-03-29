"""
Class for handling fonts
"""

import matplotlib.pyplot as plt
import numpy as np


class Fonts:
    def __init__(self, font_family="Jetbrains Mono"):
        self.good_fonts = [
            "PT Sans",
            "Open Sans",
            "Caecilia Light",
            "Product Sans Light",
        ]  # these are font families, not fonts
        self.font_family = font_family
        if font_family == "random":
            self.font_family = np.random.choice(self.font_family)
        plt.rcParams["font.family"] = font_family

    def get_fonts(self):
        print(plt.rcParams["font.family"])
        return plt.rcParams["font.family"]
