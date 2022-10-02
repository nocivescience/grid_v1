from manim import *
class SinGrid(Scene):
    def construct(self):
        title=Tex('Modificando una maya')
        title.to_edge(UP,buff=.3)
        grid=NumberPlane()
        grid.prepare_for_nonlinear_transform()
        self.play(Write(title),FadeIn(grid))
        self.play(
            grid.animate.apply_function(
                lambda p:p[1]+np.array([
                    np.sin(-p[1]),
                    np.cos(-p[0]),
                    0
                ])
            ),run_time=3, rate_func=there_and_back
        )
        self.wait()
        self.play(
            grid.animate.apply_function(
                lambda p:p[0]+np.array([
                    np.sin(-p[1]),
                    np.cos(-p[0]),
                    0
                ])
            ),run_time=3,rate_func=there_and_back
        )
        self.wait()
        self.play(
            grid.animate.apply_function(
                lambda p:p+np.array([
                    np.sin(-p[1]),
                    np.cos(-p[0]),
                    0
                ])
            ),run_time=3,rate_func=there_and_back
        )
        self.wait()
        self.play(
            grid.animate.apply_function(
                lambda p:p+np.array([
                    np.sin(p[1]),
                    np.cos(p[0]),
                    0
                ])
            ),run_time=3,rate_func=there_and_back
        )
        self.wait()