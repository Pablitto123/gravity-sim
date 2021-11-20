#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import random
from typing import List, Dict, Tuple


class DynPoint2D:
    x: float
    y: float
    vx: float
    vy: float

    def __init__(self, loc: Tuple[float], vel: Tuple[float]):
        self.x = loc[0]
        self.y = loc[1]
        self.vx = vel[0]
        self.vy = vel[1]


class Body:
    radius: float
    mass: float
    point: DynPoint2D

    def __init__(self, mass: float = 1, radius: float = 3, location=(0, 0), velocity=(0, 0)):
        self.radius = radius
        self.mass = mass
        self.point = DynPoint2D(location, velocity)

    def act_by_force(self, force: Tuple[float, float]):
        self.point.vx += force[0] / self.mass
        self.point.vy += force[1] / self.mass

    def move(self, time: float = 0.001):
        self.point.x += self.point.vx * time
        self.point.y += self.point.vy * time


def generate_random_bodies_circle(n: int, center: Tuple[float, float] = (0, 0), radius: float = 100,
                                  mass_range: Tuple[float, float] = (1, 5),
                                  body_radius_range: Tuple[float, float] = (1, 1),
                                  body_speed_range: Tuple[float, float, float, float] = (0, 0, 0, 0)):
    bodies_lst = []

    for i in range(n):
        fi = random.uniform(0, 2 * math.pi)
        rad = random.uniform(0, radius)
        mass = random.uniform(mass_range[0], mass_range[1])
        body_radius = random.uniform(body_radius_range[0], body_radius_range[1])
        vx = random.uniform(body_speed_range[0], body_speed_range[1])
        vy = random.uniform(body_speed_range[2], body_speed_range[3])
        b = Body(mass=mass, radius=body_radius,
                 location=[rad * math.cos(fi) + center[0], rad * math.sin(fi) + center[1]], velocity=(vx, vy))
        bodies_lst.append(b)
    return bodies_lst


class Gravity:
    G_const: float = 2
    eps_sq = 0.0000001  # softening factor

    def __init__(self, G_const=0.5, soft_fact=math.sqrt(0.00001)):
        self.G_const = G_const
        self.eps_sq = soft_fact ** 2

    def force_two_bodies(self, body1: Body, body2: Body):
        distance_sq = (body1.point.x - body2.point.x) ** 2 + (body1.point.y - body2.point.y) ** 2
        force = self.G_const * body1.mass * body2.mass / (distance_sq + self.eps_sq)
        c_fi_1 = (body2.point.x - body1.point.x) / math.sqrt(distance_sq + self.eps_sq)
        s_fi_1 = (body2.point.y - body1.point.y) / math.sqrt(distance_sq + self.eps_sq)
        b1_force = (force * c_fi_1, force * s_fi_1)
        b2_force = (-b1_force[0], -b1_force[1])
        return b1_force, b2_force

    def sim_bodies_list(self, bodies: List[Body]):
        for i in range(len(bodies)):
            for j in range(i + 1, len(bodies)):
                f1, f2 = self.force_two_bodies(bodies[i], bodies[j])
                bodies[i].act_by_force(f1)
                bodies[j].act_by_force(f2)
        for body in bodies:
            body.move()


def calculate_total_momentum_of_bodies(bodies: List[Body]):
    momentum = [0, 0]
    for body in bodies:
        momentum[0] += body.point.vx * body.mass
        momentum[1] += body.point.vy * body.mass
    return tuple(momentum)


def calculate_total_energy_of_bodies(bodies: List[Body], G_const: float = 2):
    # FIXME
    energy = 0
    for body in bodies:
        energy += (body.point.vx ** 2 + body.point.vy ** 2) * body.mass / 2

    pot_energy = 0
    for i in range(len(bodies)):
        for j in range(i + 1, len(bodies)):
            distance_sq = (bodies[i].point.x - bodies[j].point.x) ** 2 + (bodies[i].point.y - bodies[j].point.y) ** 2
            d_e = -G_const * bodies[i].mass * bodies[j].mass / math.sqrt(distance_sq)
            pot_energy += d_e

    return energy + pot_energy
