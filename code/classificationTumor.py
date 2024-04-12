from manim import *
import numpy as np

class Classification(Scene):

    def construct(self):
        ax = NumberLine(
            x_range = [0, 21, 2],
            include_numbers= True
        )
        self.add(ax)

        greendot1 = Dot(point=RIGHT*3, radius=0.08, color=DARK_BLUE)
        greendot2 = Dot(point=ORIGIN, radius=0.08, color=DARK_BLUE)
        greendot3 = Dot(point=RIGHT, radius=0.08, color=DARK_BLUE)
        reddot1 = Dot(point=LEFT*2, radius=0.08, color=ORANGE)
        reddot2 = Dot(point=LEFT*3, radius=0.08, color=ORANGE)
        reddot3 = Dot(point=LEFT*5, radius=0.08, color=ORANGE)
        self.add(greendot1,greendot2,greendot3, reddot1, reddot2, reddot3)


class ClassificationNewInstance(Scene):

    def construct(self):
        ax = NumberLine(
            x_range = [0, 21, 2],
            include_numbers= True
        )
        self.add(ax)

        greendot1 = Dot(point=RIGHT*3, radius=0.08, color=DARK_BLUE)
        greendot2 = Dot(point=ORIGIN, radius=0.08, color=DARK_BLUE)
        greendot3 = Dot(point=RIGHT, radius=0.08, color=DARK_BLUE)
        reddot1 = Dot(point=LEFT*2, radius=0.08, color=ORANGE)
        reddot2 = Dot(point=LEFT*3, radius=0.08, color=ORANGE)
        reddot3 = Dot(point=LEFT*5, radius=0.08, color=ORANGE)
        newdot = Dot(point=RIGHT * 0.5, radius=0.08, color=YELLOW)
        self.add(greendot1,greendot2,greendot3, reddot1, reddot2, reddot3, newdot)

class Classification2(Scene):

    def construct(self):
        ax = NumberLine(
            x_range = [0, 21, 2],
            include_numbers= True
        )
        self.add(ax)

        greendot1 = Dot(point=RIGHT*3, radius=0.08, color=DARK_BLUE)
        greendot2 = Dot(point=ORIGIN, radius=0.08, color=DARK_BLUE)
        greendot3 = Dot(point=RIGHT, radius=0.08, color=DARK_BLUE)
        reddot1 = Dot(point=RIGHT, radius=0.08, color=ORANGE)
        reddot2 = Dot(point=LEFT*3, radius=0.08, color=ORANGE)
        reddot3 = Dot(point=LEFT*5, radius=0.08, color=ORANGE)
        self.add(greendot1,greendot2,greendot3, reddot1, reddot2, reddot3)

class Classification2NewInstance(Scene):

    def construct(self):
        ax = NumberLine(
            x_range = [0, 21, 2],
            include_numbers= True
        )
        self.add(ax)

        greendot1 = Dot(point=RIGHT*3, radius=0.08, color=DARK_BLUE)
        greendot2 = Dot(point=ORIGIN, radius=0.08, color=DARK_BLUE)
        greendot3 = Dot(point=RIGHT*1.2, radius=0.08, color=DARK_BLUE)
        reddot1 = Dot(point=RIGHT, radius=0.08, color=ORANGE)
        reddot2 = Dot(point=LEFT*3, radius=0.08, color=ORANGE)
        reddot3 = Dot(point=LEFT*5, radius=0.08, color=ORANGE)
        newdot = Dot(point=RIGHT * 0.6, radius=0.08, color=YELLOW)
        self.add(greendot1,greendot2,greendot3, reddot1, reddot2, reddot3, newdot)


class Classification2D(Scene):

    def construct(self):
        ax = Axes(
            x_range = [0, 21, 2],
            y_range = [0, 200, 20]
        )
        greendot1 = Dot(point=np.array([3, 2, 0]), color=DARK_BLUE)
        self.add(ax, greendot1)