#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import random
import cluster
from typing import List, Tuple
import easygraphics as eg


class ColorBody(cluster.Body):
    color: eg.Color

    def __init__(self, mass: float = 1, radius: float = 3, location=(0, 0), velocity=(0, 0),
                 color: eg.Color = eg.Color.RED):
        super().__init__(mass=mass, radius=radius, location=location, velocity=velocity)
        self.color = color


def generate_random_bodies_circle_color(n: int, center: Tuple[float, float] = (0, 0), radius: float = 100,
                                        mass_range: Tuple[float, float] = (1, 5),
                                        body_radius_range: Tuple[float, float] = (1, 1),
                                        body_speed_range: Tuple[float, float, float, float] = (0, 0, 0, 0),
                                        color: eg.Color = eg.Color.RED):
    bodies_lst = []

    for i in range(n):
        fi = random.uniform(0, 2 * math.pi)
        rad = random.uniform(0, radius)
        mass = random.uniform(mass_range[0], mass_range[1])
        body_radius = random.uniform(body_radius_range[0], body_radius_range[1])
        vx = random.uniform(body_speed_range[0], body_speed_range[1])
        vy = random.uniform(body_speed_range[2], body_speed_range[3])
        b = ColorBody(mass=mass, radius=body_radius,
                      location=[rad * math.cos(fi) + center[0], rad * math.sin(fi) + center[1]], velocity=(vx, vy),
                      color=color)
        bodies_lst.append(b)
    return bodies_lst


def render_points_from_body_list(lst: List[ColorBody]):
    for body in lst:
        eg.set_fill_color(body.color)
        eg.set_color(body.color)
        eg.draw_circle(body.point.x, body.point.y, body.radius)
