from manim import *

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