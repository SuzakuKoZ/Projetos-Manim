from manim import *

class Taylor(Scene):
    def construct(self):
        # Título
        title = Text("Série de Taylor", font="Courier Prime", font_size=50, color=WHITE)
        manim_logo = ManimBanner().scale(0.2).to_edge(UP)
        author = Text("@pedroh.physics", font="Courier Prime", font_size=20, color=WHITE).to_edge(DOWN)
        Author = Text('Siga @pedroh.physics', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(Write(title))
        self.play(Write(author), Create(manim_logo))
        self.play(FadeOut(title))

        # Definição da série de Taylor para uma função qualquer
        text1 = Text("Seja uma função", font_size=30, font="Courier Prime")
        eq1 = MathTex(r"f(x)").next_to(text1, RIGHT)
        text2 = Text("contínua e", font_size=20, font="Courier Prime", color=YELLOW).next_to(eq1, DOWN)
        text3 = Text("infinitamente diferenciável", font_size=20, font="Courier Prime", color=YELLOW).next_to(text2, DOWN)
        self.play(Write(text1), Write(eq1))
        self.play(Write(VGroup(text2, text3)))
        self.wait()
        self.play(FadeOut(VGroup(text1, text2, text3)))
        eq2 = MathTex("f(x)", "=", "\sum_{n = 0}^\infty", "\\frac{f^{(n)}(a)}{n!}", "(x - a)^n")
        self.play(ReplacementTransform(eq1, eq2), run_time=2)
        self.wait()
        box0 = SurroundingRectangle(eq2[0])
        text0 = Text("função de interesse", font_size=20, font="Courier Prime", color=YELLOW).next_to(box0, UP)
        self.play(Create(box0), Write(text0))
        self.wait()
        box1 = SurroundingRectangle(eq2[3][0:4])
        text4 = Text("n-ésima derivada de f(x)", font_size=20, font="Courier Prime", color=YELLOW).next_to(box1, UP)
        self.play(ReplacementTransform(box0, box1), ReplacementTransform(text0, text4))
        self.wait()
        box2 = SurroundingRectangle(eq2[3][8:10])
        text5 = Text("n fatorial", font_size=20, font="Courier Prime", color=YELLOW).next_to(box2, DOWN)
        self.play(ReplacementTransform(box1, box2), ReplacementTransform(text4, text5))
        self.wait()
        box3 = SurroundingRectangle(eq2[4])
        text6 = Text("polinômio de grau n", font_size=20, font="Courier Prime", color=YELLOW).next_to(box2, DOWN)
        self.play(ReplacementTransform(box2, box3), ReplacementTransform(text5, text6))
        self.wait()
        box4 = SurroundingRectangle(eq2[4][3])
        text7 = Text("ponto em que f(x) é expandida", font_size=20, font="Courier Prime", color=YELLOW).next_to(eq2[4], DOWN)
        self.play(ReplacementTransform(box3, box4), ReplacementTransform(text6, text7))
        self.wait()
        box5 = SurroundingRectangle(eq2[2])
        text8 = Text("somatório", font_size=20, font="Courier Prime", color=YELLOW).next_to(box5, UP)
        self.play(ReplacementTransform(box4, box5), ReplacementTransform(text7, text8))
        self.wait()
        self.play(FadeOut(VGroup(text8, box5, eq2)))

        # Exemplo: Função seno
        ## Escreve f(x)=sin x
        ex_text = Text("Tomemos um exemplo, com a = 0:", font_size=30, font="Courier Prime").next_to(manim_logo, DOWN).to_edge(LEFT)
        ex_eq1 = MathTex(r"f(x) = \sin(x)").next_to(ex_text, DOWN).to_edge(LEFT)
        self.play(Write(ex_text))
        self.play(Write(ex_eq1))
        ## Plot
        # Define os eixos x,y
        axes = Axes(
            x_range=[-6.3, 6.3],
            y_range=[-1.2, 1.2],
            x_length=5,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False},
            y_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False}
        ).to_edge(RIGHT)
        x_label = MathTex(r"x", color=WHITE).next_to(axes.x_axis, buff=0.2)
        y_label = MathTex(r"y", color=WHITE).next_to(axes.y_axis, UP, buff=0.2)
        ## Cria os eixos originais na tela
        self.play(Create(axes))
        self.play(Write(VGroup(x_label, y_label)))
        self.wait()

        # Cria a função seno
        seno = axes.plot(lambda x: np.sin(x), color=YELLOW)
        seno_label = MathTex(r"f(x)").set_color(YELLOW).next_to(axes, UP).to_edge(RIGHT)
        self.play(Create(seno), Write(seno_label))
        self.wait()

        ## Escreve g(x) e vai adicionando termos enquanto muda o gráfico
        ex_eq2 = MathTex(r"g(x) = x").next_to(ex_eq1, DOWN).to_edge(LEFT)
        g_label = MathTex(r"g(x)").set_color(BLUE).next_to(seno_label, DOWN)
        self.play(Write(VGroup(ex_eq2, g_label)))
        g1 = axes.plot(lambda x: x, color=BLUE)
        self.play(Create(g1))
        self.wait()
        g2 = axes.plot(lambda x: x - x**3/6, color=BLUE)
        ex_eq3 = MathTex(r"g(x) = x - \frac{x^3}{3!}").next_to(ex_eq1, DOWN).to_edge(LEFT)
        self.play(ReplacementTransform(ex_eq2, ex_eq3), ReplacementTransform(g1, g2))
        self.wait()
        g3 = axes.plot(lambda x: x - x**3/6 + x**5/120, color=BLUE)
        ex_eq4 = MathTex(r"g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!}").next_to(ex_eq1, DOWN).to_edge(LEFT)
        self.play(ReplacementTransform(ex_eq3, ex_eq4), ReplacementTransform(g2, g3))
        self.wait()
        g4 = axes.plot(lambda x: x - x ** 3 / 6 + x ** 5 / 120 - x**7 / 5040, color=BLUE)
        ex_eq5 = MathTex(r"g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!}").next_to(ex_eq1, DOWN).to_edge(LEFT)
        self.play(ReplacementTransform(ex_eq4, ex_eq5), ReplacementTransform(g3, g4))
        self.wait()
        g5 = axes.plot(lambda x: x - x ** 3 / 6 + x ** 5 / 120 - x ** 7 / 5040 + x**9 / 362880, color=BLUE)
        ex_eq6 = MathTex(r"g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!}").next_to(ex_eq1, DOWN).to_edge(
            LEFT)
        self.play(ReplacementTransform(ex_eq5, ex_eq6), ReplacementTransform(g4, g5))
        self.wait()
        g6 = axes.plot(lambda x: x - x ** 3 / 6 + x ** 5 / 120 - x ** 7 / 5040 + x ** 9 / 362880 - x ** 11 / 39916800, color=BLUE)
        ex_eq7 = MathTex(r"g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \frac{x^{11}}{11!}").next_to(
            ex_eq1, DOWN).to_edge(LEFT)
        self.play(ReplacementTransform(ex_eq6, ex_eq7), ReplacementTransform(g5, g6))
        self.wait()
        gfinal = axes.plot(lambda x: np.sin(x), color=GREEN)
        ex_eq8 = MathTex(r"g(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...").next_to(
            ex_eq1, DOWN).to_edge(LEFT)
        self.play(ReplacementTransform(ex_eq7, ex_eq8))
        eqfinal = MathTex(r"f(x)=g(x)").set_color(GREEN).next_to(y_label, RIGHT)
        self.play(ReplacementTransform(VGroup(g6, seno), gfinal), ReplacementTransform(VGroup(seno_label, g_label), eqfinal), run_time=2)
        self.wait()


        # Encerramento e CTA
        self.play(FadeOut(VGroup(eqfinal, gfinal, ex_eq1, ex_text, axes, ex_eq8, x_label, y_label)))
        self.play(ReplacementTransform(author, Author), manim_logo.expand())
        self.wait()

if __name__ == "__main__":
    scene = Taylor()
    scene.render()
