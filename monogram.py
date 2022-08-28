from manim import *


def create_letter(points):
    point1 = Dot(points[0], 0)
    point2 = Dot(points[1], 0)
    point3 = Dot(points[2], 0)
    point4 = Dot(points[3], 0)
    point5 = Dot(points[4], 0)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point4)
    line4 = Line(point4, point5)

    return VGroup(line1, line2, line3, line4)


# define the zoom for the scene
config.frame_width = 4


class CreateMonogram(Scene):
    def construct(self):
        grid_points = {
            "up": [1, 1, 0],
            "ul": [0, 1, 0],
            "lt": [-1, 1, 0],
            "ur": [1, 0, 0],
            "cn": [0, 0, 0],
            "dl": [-1, 0, 0],
            "rt": [1, -1, 0],
            "dr": [0, -1, 0],
            "dn": [-1, -1, 0]
        }

        s_points = [
            grid_points["up"],
            grid_points["ul"],
            grid_points["cn"],
            grid_points["dl"],
            grid_points["dn"]
        ]

        s = create_letter(s_points)
        s.set_z_index(2)

        m_points = [
            grid_points["lt"],
            grid_points["ul"],
            grid_points["cn"],
            grid_points["ur"],
            grid_points["rt"]
        ]

        m = create_letter(m_points)
        m.set_z_index(3)

        frame_points = [
            Dot(s_points[0], 0),
            Dot(m_points[4], 0),
            Dot(s_points[4], 0),
            Dot(m_points[0], 0)
        ]

        frame_line1 = Line(frame_points[0], frame_points[1])
        frame_line2 = Line(frame_points[1], frame_points[2])
        frame_line3 = Line(frame_points[2], frame_points[3])
        frame_line4 = Line(frame_points[3], frame_points[0])

        frame_grid = VGroup(frame_line1, frame_line2, frame_line3, frame_line4)
        frame_grid.set_color(DARK_GRAY)

        green_vertices = (grid_points["up"], grid_points["ul"], grid_points["cn"], grid_points["ur"])
        green_square = Polygon(*green_vertices)
        green_square.set_color(DARK_GRAY)
        green_square.set_fill(GREEN_E, 1)
        green_square.set_z_index(1)

        purple_vertices = (grid_points["lt"], grid_points["ul"], grid_points["cn"], grid_points["dl"])
        purple_square = Polygon(*purple_vertices)
        purple_square.set_color(DARK_GRAY)
        purple_square.set_fill(PURPLE_E, 1)
        purple_square.set_z_index(1)

        black_vertices = (grid_points["ur"], grid_points["rt"], grid_points["dn"], grid_points["dl"])
        black_rectangle = Polygon(*black_vertices)
        black_rectangle.set_color(DARK_GRAY)
        black_rectangle.set_fill(BLACK, 1)
        black_rectangle.set_z_index(1)

        monogram = VGroup(green_square, purple_square, black_rectangle, frame_grid, s, m)
        monogram.rotate(PI / 4)

        self.play(Create(frame_grid))
        self.play(FadeIn(black_rectangle))
        self.wait(1)

        self.play(Create(s))
        self.play(FadeIn(green_square))
        self.wait(1)

        self.play(Create(m))
        self.play(FadeIn(purple_square))
        self.wait(1)

        self.pause(5)
