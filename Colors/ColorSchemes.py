from ColorScheme import ColorScheme
import numpy as np


class ColorSchemes:
    """
    This class contains different color schemes that have a primary, secondary, accent, background and text color. Each Scheme has a name.
    """

    def __init__(self):
        self.schemes = [
            ColorScheme("Dark", "#1F1F1F", "#2D2D2D", "#FFD700", "#000000", "#FFFFFF"),
            ColorScheme("Light", "#FFFFFF", "#F0F0F0", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Blue", "#0000FF", "#0000A0", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Green", "#00FF00", "#00A000", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Red", "#FF0000", "#A00000", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme(
                "Yellow", "#FFFF00", "#A0A000", "#FFD700", "#FFFFFF", "#000000"
            ),
            ColorScheme(
                "Purple", "#800080", "#600060", "#FFD700", "#FFFFFF", "#000000"
            ),
            ColorScheme(
                "Orange", "#FFA500", "#A06000", "#FFD700", "#FFFFFF", "#000000"
            ),
            ColorScheme("Cyan", "#00FFFF", "#00A0A0", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Pink", "#FFC0CB", "#A06070", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Brown", "#A52A2A", "#802020", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Grey", "#808080", "#606060", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("Black", "#000000", "#000000", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme("White", "#FFFFFF", "#FFFFFF", "#FFD700", "#FFFFFF", "#000000"),
            ColorScheme(
                "Default", "#FFFFFF", "#F0F0F0", "#FFD700", "#FFFFFF", "#000000"
            ),
        ]
        self.dark = self.schemes[0]
        self.light = self.schemes[1]
        self.blue = self.schemes[2]
        self.green = self.schemes[3]
        self.red = self.schemes[4]
        self.yellow = self.schemes[5]
        self.purple = self.schemes[6]
        self.orange = self.schemes[7]
        self.cyan = self.schemes[8]
        self.pink = self.schemes[9]
        self.brown = self.schemes[10]
        self.grey = self.schemes[11]
        self.black = self.schemes[12]
        self.white = self.schemes[13]
        self.default = self.schemes[14]
        self.random = np.random.choice(self.schemes)

    def get_schemes(self):
        return self.schemes

    def get_scheme(self, name):
        for scheme in self.schemes:
            if scheme.name == name:
                return scheme

    def get_random(self):
        return np.random.choice(self.schemes)
