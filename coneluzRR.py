from manim import *
import numpy as np

class conedeluz(Scene):
    def construct(self):
        # Título
        title = Text("Efeito geométrico das", color=WHITE, font="Courier Prime", font_size=50)
        title2 = Text("Transformações de Lorentz", color=WHITE, font="Courier Prime", font_size=50).next_to(title, DOWN)
        self.play(Write(title), Write(title2))
        self.wait()

        # cria o texto do @ e remove o título
        arroba = Text('@pedroh.physics', color=YELLOW, font="Courier Prime", font_size=20).to_edge(DOWN)
        self.play(Write(arroba))
        Arroba = Text('Siga @pedroh.physics', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(FadeOut(VGroup(title, title2)))
        self.wait()

        # Define os eixos x,t
        original_axes = Axes(
            x_range=[0,5],
            y_range=[0,5],
            x_length=5,
            y_length=5,
            axis_config={"color":WHITE},
            x_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False},
            y_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False}
        )
        original_x_label = MathTex(r"x", color=WHITE).next_to(original_axes.x_axis, buff=0.2)
        original_y_label = MathTex(r"ct", color=WHITE).next_to(original_axes.y_axis, UP, buff=0.2)
        copy = original_axes.copy()
        axes_transformation = original_axes.copy()
        axes_transformation.axis_config["preserve_aspect_ratio"] = False

        # Cria os eixos originais na tela
        self.play(Create(original_axes))
        self.play(Write(VGroup(original_x_label, original_y_label)))
        self.wait()

        # Traça o cone de luz
        cone = original_axes.plot(lambda x: x, color=GREEN)
        cone_label = Text("Cone de luz", font="Courier Prime", font_size=20).rotate(angle=np.pi/4).shift([2.0,2.5,0.0])
        self.play(Create(cone), Write(cone_label))
        self.wait()

        # Remove o cone de luz

        # Adiciona as TL's na cena
        eq1 = MathTex(r"t' = \gamma t - \gamma\beta x").shift([-5.0,2.5,0.0])
        eq2 = MathTex(r"x' = \gamma x - \gamma\beta t").next_to(eq1, DOWN)
        self.play(Write(VGroup(eq1, eq2)))
        self.wait()


        # Cria os eixos após as TL's
        velocity = 0.4
        gamma_function = lambda v: (np.sqrt(1 - v ** 2)) ** (-1)
        lorentz_transformation = np.array([
            [gamma_function(velocity), velocity * gamma_function(velocity), 0],
            [velocity * gamma_function(velocity), gamma_function(velocity), 0],
            [0, 0, 1]
        ])
        axes_transformation.apply_matrix(lorentz_transformation)
        axes_transformation.shift(original_axes.coords_to_point(0,0) - axes_transformation.coords_to_point(0,0)) #Faz com que os eixos coincidam
        axes_transformation.set_color(YELLOW)
        transformed_x_label = MathTex(r"x'", color=YELLOW).next_to(axes_transformation.x_axis, UR, buff=0.2)
        transformed_y_label = MathTex(r"ct'", color=YELLOW).next_to(axes_transformation.y_axis, UR, buff=0.2)
        self.add(copy)
        self.play(ReplacementTransform(copy, axes_transformation), Write(VGroup(transformed_x_label, transformed_y_label)))
        self.wait()

        # Adiciona o ângulo beta
        beta1 = Angle(original_axes.x_axis, axes_transformation.x_axis, radius=1.2, other_angle=False, color=RED)
        beta2 = Angle(original_axes.y_axis, axes_transformation.y_axis, radius=1.2, other_angle=True, color=RED)
        beta1_label = MathTex(r"\beta", color=RED).next_to(beta1, RIGHT, buff=0.1)
        beta2_label = MathTex(r"\beta", color=RED).next_to(beta2, UP, buff=0.1)
        beta_symbol = beta1_label.copy()
        self.play(Create(VGroup(beta1, beta2)))
        self.play(Write(VGroup(beta1_label, beta2_label)))
        self.add(beta_symbol)
        self.wait()
        beta = MathTex(r"\beta = V/c", color=RED).shift([4.5, -2.0, 0.0])
        self.play(ReplacementTransform(beta_symbol, beta))
        self.wait()


        # Encerramento
        grupo = VGroup(cone, cone_label, beta, original_axes, original_x_label, original_y_label, axes_transformation, transformed_x_label, transformed_y_label, eq1, eq2, beta1_label, beta2_label, beta1, beta2)
        self.play(FadeOut(grupo))
        self.play(ReplacementTransform(arroba, Arroba))
        self.wait()

if __name__ == "__main__":
    scene = conedeluz()
    scene.render()
