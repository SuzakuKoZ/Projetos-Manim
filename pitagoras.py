import numpy as np
from manim import *


class Pitagoras(Scene):
    def construct(self):
        # Título e autor
        title = Text("Teorema de Pitágoras", font="Courier Prime", font_size=50, color=WHITE)
        subtitle = Text("Uma demonstração geométrica", font="Courier Prime", font_size=30, color=YELLOW).next_to(title,
                                                                                                                 DOWN)
        author = Text("@manual.fisica", font="Courier Prime", font_size=20, color=WHITE).to_edge(DOWN)
        Author = Text('Siga @manual.fisica', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(Write(VGroup(title, subtitle)))
        self.play(Write(author))
        self.play(FadeOut(VGroup(title, subtitle)))


        # Cria um triângulo na cena
        ## Vértices
        A = np.array([-2, -1.5, 0])
        B = np.array([2, -1.5, 0])
        C = np.array([2, 1.5, 0])
        ponto_A = Dot(A)
        ponto_B = Dot(B)
        ponto_C = Dot(C)
        a = Line(ponto_A, ponto_B)
        a_inve = Line(ponto_B, ponto_A)
        b = Line(ponto_B, ponto_C)
        b_inve = Line(ponto_C, ponto_B)
        c = Line(ponto_C, ponto_A)
        c_inve = Line(ponto_A, ponto_C)
        a_label = MathTex(r"a", color=WHITE).shift([0, -2, 0])
        b_label = MathTex(r"b", color=WHITE).shift([2.5, 0, 0])
        c_label = MathTex(r"c", color=WHITE).shift([0, 0.4, 0]).rotate(30 * DEGREES)

        ## Triângulo
        triang = Polygon(A, B, C, z_index=1).set_color(WHITE)
        alpha = Angle(a, c_inve, radius=0.5, other_angle=False, color=RED)
        alpha_label = MathTex(r"\alpha", color=RED).shift([-1.3, -1.3, 0])
        beta = Angle(b_inve, c, radius=0.5, other_angle=True, color=YELLOW)
        beta_label = MathTex(r"\beta", color=YELLOW).shift([1.7, 0.7, 0])
        gamma = Angle(a_inve, b, radius=0.5, other_angle=True, color=WHITE, dot=True)

        ## Adiciona o triângulo na cena
        self.play(Create(triang), run_time=2)
        self.play(Create(VGroup(alpha, beta, gamma)), Write(VGroup(alpha_label, beta_label)),
                  Write(VGroup(a_label, b_label, c_label)))
        self.wait()
        self.play(FadeOut(VGroup(alpha_label, beta_label, a_label, b_label, c_label)))

        # Quadruplica o triângulo
        start = np.array([0, 0, 0])
        end = np.array([-3, 2, 0])
        trajetoria = Line(start, end)
        tri1 = VGroup(triang, alpha, beta, gamma)
        self.play(ReplacementTransform(VGroup(triang, alpha, beta, gamma), tri1))
        self.play(tri1.animate.scale(0.5), MoveAlongPath(tri1, trajetoria), run_time=2)
        tri2 = tri1.copy()
        tri3 = tri1.copy()
        tri4 = tri3.copy()
        self.add(tri2, tri3, tri4)
        self.play(tri2.animate.shift(RIGHT * 6), tri3.animate.shift(DOWN * 3.2),
                  tri4.animate.shift(RIGHT * 6).shift(DOWN * 3.2))

        # Rotaciona os triângulos
        self.play(tri1.animate.rotate(90 * DEGREES, about_point=tri1.get_center()), tri2.animate.rotate(90 * DEGREES, about_point=tri2.get_center()), tri3.animate.rotate(270 * DEGREES, about_point=tri3.get_center()))
        self.play(tri1.animate.rotate(90 * DEGREES, about_point=tri1.get_center()))

        # Forma um quadrado com os triângulos
        self.play(tri1.animate.shift([2.2, -0.5, 0]), tri2.animate.shift([-2, -0.75, 0]),
                  tri3.animate.shift([1.95, 1, 0]), tri4.animate.shift([-2.25, 0.75, 0]))

        # Destaca o quadrado no centro
        self.wait()
        tri1.set_fill(BLUE, opacity=0.4)
        tri2.set_fill(BLUE, opacity=0.4)
        tri3.set_fill(BLUE, opacity=0.4)
        tri4.set_fill(BLUE, opacity=0.4)
        plus_label = MathTex(r"a+b")
        self.play(Write(VGroup(a_label.next_to(tri1, UP), b_label.next_to(tri2, UP), c_label.shift([0.8, -0.6, 0]))))
        self.play(ReplacementTransform(VGroup(a_label, b_label), plus_label.shift([0, 2.7, 0])))
        quadrado_grande = VGroup(tri1, tri2, tri3, tri4, plus_label, c_label)
        self.play(ReplacementTransform(VGroup(tri1, tri2, tri3, tri4, plus_label, c_label), quadrado_grande))
        self.play(quadrado_grande.animate.scale(0.8).shift(RIGHT * 2.5).shift(DOWN))
        self.wait()

        # Demonstração
        tex1 = Text("Note que", font_size=30, font="Courier Prime").shift(np.array([-3, 0, 0]))
        eq1 = MathTex(r"A_{Q>} = 4\cdot A_T + A_{Q<}").next_to(tex1, DOWN)
        self.play(Write(tex1), Write(eq1))
        self.play(FadeOut(tex1), FadeOut(quadrado_grande))
        eq2 = MathTex(r"(a + b)^2 = 4\cdot\frac{ab}{2} + c^2")
        self.play(ReplacementTransform(eq1, eq2), run_time=1.5)
        eq3 = MathTex(r"(a + b)^2 = 2ab + c^2")
        self.play(ReplacementTransform(eq2, eq3), run_time=1.5)
        eq4 = MathTex(r"a^2 + 2ab + b^2 = 2ab + c^2")
        self.play(ReplacementTransform(eq3, eq4), run_time=1.5)
        eq5 = MathTex(r"a^2 + b^2 = c^2")
        self.play(ReplacementTransform(eq4, eq5), run_time=1.5)
        frame = SurroundingRectangle(eq5, buff=0.1)
        tex2 = Text("Teorema de Pitágoras", font_size=20, font="Courier Prime").next_to(frame)
        self.play(Create(frame), Write(tex2))
        self.wait()
        self.play(FadeOut(VGroup(eq5, frame, tex2)))

        # Encerramento e CTA
        self.play(ReplacementTransform(author, Author))

if __name__ == "__main__":
    scene = Pitagoras()
    scene.render()
