import easygraphics as eg
import easygraphics.processing as egpr
import cluster
import animation


def mainloop():
    x = 0
    eg.set_color(eg.Color.BLUE)
    eg.set_fill_color(eg.Color.GREEN)
    grav = cluster.Gravity(G_const=2)
    v_r = (-0, 0, -0, 0)
    d1 = 250
    bodies1 = animation.generate_random_bodies_circle_color(n=50, center=(900+d1, 500.0), radius=40.0,
                                                            body_radius_range=(2, 2),
                                                            body_speed_range=(0, 0, -140, -150), mass_range=(0.001, 0.001),
                                                            color=eg.Color.BLUE)
    d2 = 300
    bodies2 = animation.generate_random_bodies_circle_color(n=50, center=(900 - d2, 500.0), radius=35.0,
                                                            body_radius_range=(2, 2),
                                                            body_speed_range=(0, 0, -140, -144), mass_range=(0.001, 0.001),
                                                            color=eg.Color.YELLOW)
    d3 = 360
    bodies3 = animation.generate_random_bodies_circle_color(n=50, center=(900, 500 + d3), radius=50.0,
                                                            body_radius_range=(2, 2),
                                                            body_speed_range=(90, 100, 0, 0), mass_range=(0.001, 0.001),
                                                            color=eg.Color.MAGENTA)

    bd = animation.ColorBody(mass=10000, radius=30, location=(900, 500), velocity=(0, 0), color=eg.Color.RED)
    bd2 = animation.ColorBody(mass=600, radius=10, location=(1030, 500), velocity=(0, 300), color=eg.Color.WHITE)
    bd3 = animation.ColorBody(mass=400, radius=10, location=(730, 500), velocity=(0, 300), color=eg.Color.GREEN)
    bodies = bodies1 + bodies2 + bodies3 + [bd] + [bd2] + [bd3]
    eg.fill_image(color=eg.Color.BLACK)
    time = 0
    while eg.is_run():
        x = (x + 1) % 440
        if eg.delay_jfps(60):
            time += 0.001
            #eg.fill_image(color=eg.Color.BLACK)
            animation.render_points_from_body_list(bodies)
            grav.sim_bodies_list(bodies)
            mom = cluster.calculate_total_momentum_of_bodies(bodies)
            eg.draw_text(1500, 20, "momentum:" + " x: %.3f" % mom[0] + " y: %.3f" % mom[1])
            eg.draw_text(1500, 40, "time: %.3f" % time)


def main():
    eg.init_graph(1800, 1000)
    eg.set_render_mode(eg.RenderMode.RENDER_MANUAL)
    mainloop()
    eg.close_graph()


if __name__ == '__main__':
    eg.easy_run(main)
    pass
