import numpy as np
from manim import *

class Bhaskara(Scene):
    def construct(self):
        # Título e autor
        title = Text("Fórmula de Bhaskara", font="Courier Prime", font_size=50, color=WHITE)
        subtitle = Text("- DEMONSTRAÇÃO -", font="Courier Prime", font_size=30, color=YELLOW).next_to(title, DOWN)
        author = Text("@manual.fisica", font="Courier Prime", font_size=20, color=WHITE).to_edge(DOWN)
        Author = Text('Siga @manual.fisica', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(Write(VGroup(title, subtitle)))
        self.play(Write(author))
        self.play(FadeOut(VGroup(title, subtitle)))

        # Equações iniciais
        eq1 = MathTex(r"ax^2 + bx + c = 0, a \neq 0")
        self.play(Write(eq1))
        eq2 = MathTex(r"ax^2 + bx + c = 0")
        self.play(ReplacementTransform(eq1, eq2))
        eq3 = MathTex(r"x^2 + \frac{b}{a}x + \frac{c}{a} = 0")
        self.play(ReplacementTransform(eq2, eq3))
        eq4 = MathTex(r"x^2 + \frac{b}{a}x = - \frac{c}{a}")
        self.play(ReplacementTransform(eq3, eq4))
        eq5 = MathTex("x^2", "+", "\\frac{b}{a}x", "=", "-\\frac{c}{a}")
        self.play(ReplacementTransform(eq4,eq5.to_edge(UL)))
        self.wait()

        # Geometrização

        ## Cria um quadrado
        A = np.array([-np.sqrt(2),np.sqrt(2),0])
        B = np.array([np.sqrt(2),np.sqrt(2),0])
        C = np.array([np.sqrt(2),-np.sqrt(2),0])
        D = np.array([-np.sqrt(2),-np.sqrt(2),0])
        square = Polygon(A, B, C, D).set_color(WHITE)
        self.play(Create(square), run_time=2)
        square.set_fill(BLUE, opacity=0.3)
        eq5[0].set_color(BLUE)
        Eq1 = MathTex(r"x^2")
        self.play(ReplacementTransform(eq5[0].copy(), Eq1))
        Eq1a = MathTex(r"x").rotate(90 * DEGREES).next_to(Line(A, D), LEFT)
        Eq1b = MathTex(r"x").next_to(Line(A, B), UP)
        self.play(ReplacementTransform(Eq1, VGroup(Eq1a, Eq1b)))
        self.wait()


        ## Cria um retângulo
        E = np.array([-np.sqrt(2),-np.sqrt(2)-1,0])
        F = np.array([np.sqrt(2),-np.sqrt(2)-1,0])
        rectangle = Polygon(D, C, F, E).set_color(WHITE)
        self.play(Create(rectangle), run_time=2)
        eq5[2].set_color(RED)
        rectangle.set_fill(RED, opacity=0.3)
        Eq2 = MathTex(r"\frac{b}{a}x").shift([0,-2*np.sqrt(2)+1,0]).rotate(45 * DEGREES)
        self.play(ReplacementTransform(eq5[2].copy(), Eq2))
        Eq2a = MathTex(r"\frac{b}{a}").rotate(90 * DEGREES).next_to(Line(D, E), LEFT)
        Eq2b = MathTex(r"x").next_to(Line(E, F), DOWN)
        self.play(ReplacementTransform(Eq2, VGroup(Eq2a, Eq2b)))
        self.wait()

        ## Fraciona o retângulo ao meio
        G = np.array([-np.sqrt(2),-np.sqrt(2)-0.5,0])
        H = np.array([np.sqrt(2),-np.sqrt(2)-0.5,0])
        line = Line(G, H)
        self.play(Create(line))
        self.wait()
        rec1 = Polygon(D, C, H, G).set_color(WHITE)
        rec2 = Polygon(G, H, F, E).set_color(WHITE)
        self.add(rec1.set_fill(RED, opacity=0.3), rec2.set_fill(RED, opacity=0.3))
        self.remove(rectangle, line)
        Eq3a = MathTex(r"\frac{b}{2a}").rotate(90 * DEGREES).next_to(Line(D, G), LEFT)
        Eq3b = MathTex(r"\frac{b}{2a}").rotate(270 * DEGREES).next_to(Line(H, F), RIGHT)
        self.play(ReplacementTransform(Eq2a, VGroup(Eq3a, Eq3b)))
        self.wait()

        ## Move uma parte
        line2 = Line(B, C)
        Eq3c = Eq3b.copy().rotate(90 * DEGREES)
        self.play(rec2.animate.rotate(90 * DEGREES, about_point=H).shift([0,2*np.sqrt(2)+0.5,0]))
        self.play(ReplacementTransform(Eq3b, Eq3c.next_to(rec2, UP)), FadeOut(Eq2b))
        #ReplacementTransform(Eq3b, Eq3c.next_to(square, UR)), FadeOut(Eq2b)

        ## Completa o quadrado
        X = np.array([np.sqrt(2)+0.5,-np.sqrt(2),0])
        Y = np.array([np.sqrt(2)+0.5,-np.sqrt(2)-0.5,0])
        small_square = Polygon(C, X, Y, H).set_color(WHITE)
        self.play(Create(small_square), run_time=2)
        small_square.set_fill(YELLOW, opacity=0.3)
        Eq4 = MathTex(r"\frac{b^2}{4a^2}").set_color(YELLOW).next_to(small_square, DR)
        self.play(ReplacementTransform(VGroup(Eq3a.copy(), Eq3b.copy()), Eq4))
        self.wait()
        eq6 = MathTex(r"x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} = - \frac{c}{a} + \frac{b^2}{4a^2}").to_edge(UL)
        self.play(ReplacementTransform(VGroup(eq5, Eq4), eq6))
        self.wait()
        Square = VGroup(square, rec1, rec2, small_square)
        self.play(ReplacementTransform(VGroup(square, rec1, rec2, small_square), Square.set_fill(WHITE, opacity=1)),
                  run_time=2)
        Eq5 = MathTex(r"\left(x + \frac{b}{2a}\right)^2").set_color(BLACK)
        self.play(ReplacementTransform(VGroup(Eq3a, Eq3c, Eq1a, Eq1b), Eq5.next_to(Square, IN)))

        # Volta para as equações
        eq7 = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = - \frac{c}{a} + \frac{b^2}{4a^2}")
        self.play(ReplacementTransform(VGroup(Square, Eq5, eq6), eq7))
        self.wait()
        eq8 = MathTex(r"\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}")
        self.play(ReplacementTransform(eq7, eq8))
        eq9 = MathTex(r"x + \frac{b}{2a} = \pm \sqrt{\frac{b^2 - 4ac}{4a^2}}")
        self.play(ReplacementTransform(eq8, eq9))
        eq10 = MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}")
        self.play(ReplacementTransform(eq9, eq10))
        eq11 = MathTex(r"x = - \frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a}")
        self.play(ReplacementTransform(eq10, eq11))
        eq12 = MathTex(r"x = \frac{- b \pm \sqrt{b^2 - 4ac}}{2a}")
        frame = SurroundingRectangle(eq12)
        self.play(ReplacementTransform(eq11, eq12), Create(frame), run_time=2)
        self.wait()

        # Encerramento/CTA
        self.play(FadeOut(VGroup(frame, eq12)))
        self.play(ReplacementTransform(author, Author))
        self.wait()

if __name__ == "__main__":
    scene = Bhaskara()
    scene.render()
