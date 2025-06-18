"""This module is made to make graphs of all sorts, and standardize them so i can use them everywhere. The library
will always be available to copy the code from anyway. So i can always modify the code, but atleast there will be a
set template of all the graphs that I may need. I will use any module that I think looks good here."""

import numpy as np
import matplotlib.pyplot as plt
from kptgraphs.Colors.ColorSchemes import ColorSchemes

class Basics:
    def __init__(
        self,
        matplotlib_style="default",
        code_font_family="Jetbrains Mono",
        text_font_family="PT Sans",
        color_scheme="default",
    ):
        self.good_fonts_for_text = [
            "PT Sans",
            "Open Sans",
            "Caecilia Light",
            "Product Sans Light",
        ]  # these are font families, not fonts

        # get all color schemes from ColorSchemes.py
        self.color_schemes = ColorSchemes()

        # now for this class, and this instance, set the color scheme that was specified by the user.
        self.color_scheme = self.color_schemes.get_scheme(color_scheme)

        plt.style.use(matplotlib_style)
        self.matplotlib_style = matplotlib_style
        self.code_font_family = code_font_family
        self.text_font_family = text_font_family
        if code_font_family == "random":
            self.code_font_family = np.random.choice(self.good_fonts_for_text)
        if text_font_family == "random":
            self.text_font_family = np.random.choice(self.good_fonts_for_text)

        plt.rcParams["font.family"] = self.code_font_family

    # getters
    def get_fonts(self):
        print(plt.rcParams["font.family"])
        return plt.rcParams["font.family"]


class BasicGraphs(Basics):
    """Contains graphs for Line, Bar, Pie, and Scatter plots"""

    def __init__(
        self,
        matplotlib_style="default",
        code_font_family="Jetbrains Mono",
        text_font_family="PT Sans",
        color_scheme="default",
    ):
        print("Thank you for using KPT Graphs!")
        super().__init__(
            matplotlib_style,
            code_font_family=code_font_family,
            text_font_family=text_font_family,
            color_scheme=color_scheme,
        )

    def line_plot(
        self, x, y, title, subtitle, xlabel, ylabel, color_scheme, size=(10, 6)
    ) -> tuple:
        """Creates a line plot with the given data
        and then returns the figure and axis objects.
        """

        # first create the line plot
        fig, ax = plt.subplots(figsize=size)
        ax.plot(x, y, color=self.color_scheme.primary)

        # now formatting

        # axes

        # tilt the x-axis labels by 45 degrees
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)

        # set the font size of the tick labels
        for tick in ax.xaxis.get_major_ticks():
            tick.label1.set_fontsize(16)
        for tick in ax.yaxis.get_major_ticks():
            tick.label1.set_fontsize(16)

        # title

        # add title + subtitle to plot
        plt.text(
            x=0.125,
            y=0.90,
            s=title,
            fontname=self.text_font_family,
            fontsize=24,
            ha="left",
            transform=fig.transFigure,
        )

        plt.text(
            x=0.125,
            y=0.86,
            s=subtitle,
            fontname=self.text_font_family,
            fontsize=18,
            ha="left",
            transform=fig.transFigure,
        )

        # line between titles and chart
        plt.gca().plot(
            [0.125, 0.9],  # x co-ords
            [0.80, 0.80],  # y co-ords
            transform=fig.transFigure,
            clip_on=False,
            color="k",
            linewidth=1.5,
        )

        # set the x and y labels
        ax.tick_params(axis="both", which="major", labelsize=16)
        plt.xlabel(xlabel, fontsize=20, fontname=self.text_font_family)
        plt.ylabel(ylabel, fontsize=20, fontname=self.text_font_family)

        # grid lines
        # keep only toned down vertical lines
        plt.grid(axis="y", alpha=0.4)
        plt.grid(axis="x", alpha=0.2)

        # turn off spines
        plt.gca().spines[["left", "right", "top"]].set_visible(False)

        # change space on top of chart we are actually adjusting the scale of the plot as well.
        plt.subplots_adjust(top=0.8, wspace=0.3)

        # return everything to the user
        return fig, ax

    def test(self):
        print("This is a test")
        return 1


def test():
    print("This is a test")
    return 1
