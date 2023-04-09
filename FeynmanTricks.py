from manim import *

class FInt(Scene):
    def construct(self):
        #Título
        title = Text("Integral sob o sinal diferencial", color=WHITE, font="Courier Prime", font_size=50)
        title2 = Text("(Truque de Feynman)", color=WHITE, font="Courier Prime", font_size=40).next_to(title, DOWN)
        self.play(Write(title), Write(title2))

        # cria o texto do @ e remove o título
        arroba = Text('@pedroh.physics', color=YELLOW, font="Courier Prime", font_size=20).to_edge(DOWN)
        self.play(Write(arroba))
        Arroba = Text('Siga @pedroh.physics', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(FadeOut(VGroup(title, title2)))
        self.wait()

        # Escreve a integral desejada
        text_int = Text("Desejamos calcular", color=WHITE, font="Courier Prime", font_size=30).shift(UP)
        self.play(Write(text_int))
        int = MathTex(r"I = \int_0^\infty \frac{\sin x}{x} dx")
        self.play(Write(int))
        self.play(FadeOut(text_int))
        self.play(int.animate.shift(LEFT * 4))

        # Faz o plot do integrando
        axes = Axes(
            x_range=[0.0000001,15],
            y_range=[-0.5,1.2],
            x_length=7,
            y_length=5,
            axis_config={"color":WHITE},
            x_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False},
            y_axis_config={"numbers_to_exclude": [0], "include_ticks": False, "include_tip": False}
        )
        self.play(Create(axes.shift(RIGHT * 2)))
        integrando = axes.plot(lambda x: np.sin(x)/x, color=YELLOW)
        integrando_label = MathTex(r"h(x) = \frac{\sin(x)}{x}", font_size=30, color=YELLOW).next_to(integrando, UP * 0.5)
        self.play(Create(integrando), Write(integrando_label))
        self.wait()
        self.play(FadeOut(VGroup(integrando, integrando_label, axes, int)))

        # Modelagem por parâmetro lambda
        eq1 = MathTex(r"I(\lambda) = \int_a^b \frac{f(x,\lambda)}{g(x)}dx \leftrightarrow \frac{\partial f(x,\lambda)}{\partial\lambda} = g(x)f(x,\lambda)")
        self.play(Write(eq1))
        eq2 = MathTex(r"\frac{\partial I(\lambda)}{\partial \lambda} = \int_a^b \frac{dx}{b(x)}\frac{\partial f(x,\lambda)}{\partial \lambda}")
        eq3 = MathTex(r"\frac{\partial I(\lambda)}{\partial \lambda} = \int_a^b f(x,\lambda) dx")
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(FadeOut(eq3))

        # Escreve as condições


        # Equação de 'autovalor'
        eq4 = MathTex("\\frac{\partial}{\partial\lambda}", "f(x,\lambda)", "=", "g(x)", "f(x,\lambda)")
        self.play(Write(eq4))
        frame1 = SurroundingRectangle(eq4[0], buff=0.1)
        frame1_label = Text("Operador", color=YELLOW, font_size=20, font="Courier Prime").next_to(frame1, UP)
        frame2 = SurroundingRectangle(eq4[3], buff=0.1)
        frame2_label = Text("Autovalor", color=YELLOW, font_size=20, font="Courier Prime").next_to(frame2, UP)
        frame3 = SurroundingRectangle(eq4[1], buff=0.1)
        frame3_label = Text("Autofunção", color=YELLOW, font_size=20, font="Courier Prime").next_to(frame3, UP)
        frame4 = SurroundingRectangle(eq4[4], buff=0.1)
        frame4_label = Text("Autofunção", color=YELLOW, font_size=20, font="Courier Prime").next_to(frame4, UP)
        self.play(Create(frame1), Write(frame1_label))
        self.play(ReplacementTransform(frame1, frame2), ReplacementTransform(frame1_label, frame2_label))
        self.play(ReplacementTransform(frame2, VGroup(frame3, frame4)), ReplacementTransform(frame2_label, VGroup(frame3_label, frame4_label)))
        self.play(FadeOut(VGroup(frame3, frame4, frame3_label, frame4_label)))
        eq5 = MathTex(r"\ln(f(x,\lambda) - c(x) = \lambda g(x)")
        eq6 = MathTex(r"f(x,\lambda) = e^{\lambda g(x) + c(x)}")
        self.play(ReplacementTransform(eq4, eq5))
        self.play(ReplacementTransform(eq5, eq6))
        self.wait()

        # Integral mais geral
        text_general = Text("Seja a integral (mais geral)", font="Courier Prime", font_size=30).shift(UP)
        self.play(ReplacementTransform(eq6, text_general))
        eq7 = MathTex(r"I(\lambda) = \int_0^\infty\frac{e^{ix}e^{\lambda x}}{x}dx")
        self.play(Write(eq7.next_to(text_general, DOWN)))
        brace = Brace(eq7, direction=DOWN, color=YELLOW)
        brace_label = MathTex(r"g(x) = x,").next_to(brace, DOWN)
        brace_label2 = MathTex(r"c(x) = ix").next_to(brace_label, RIGHT)
        self.play(GrowFromCenter(brace))
        self.play(Write(VGroup(brace_label, brace_label2)))
        self.wait()
        self.play(FadeOut(VGroup(brace, brace_label, brace_label2, text_general)))

        # Integração de I'(b)
        eq8 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = \frac{d}{d\lambda}\int_0^\infty\frac{e^{ix}e^{\lambda x}}{x}dx")
        eq9 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = \int_0^\infty\frac{\partial}{\partial\lambda}\left[\frac{e^{ix}e^{\lambda x}}{x}\right]dx")
        eq10 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = \int_0^\infty e^{ix}e^{\lambda x} dx")
        eq11 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = \int_0^\infty e^{(\lambda + i)x} dx")
        eq12 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = \frac{1}{\lambda + i}e^{(\lambda+i)x}\bigg|_0^\infty")
        eq13 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = - \frac{1}{\lambda + i}, \lambda < 0")
        eq14 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = - \frac{(\lambda - i))}{(\lambda + i)(\lambda - i)}")
        eq15 = MathTex(r"\frac{dI(\lambda)}{d\lambda} = - \frac{\lambda}{\lambda^2 + 1} + \frac{i}{\lambda^2 + 1}")
        self.play(ReplacementTransform(eq7, eq8))
        self.play(ReplacementTransform(eq8, eq9))
        self.play(ReplacementTransform(eq9, eq10))
        self.play(ReplacementTransform(eq10, eq11))
        self.play(ReplacementTransform(eq11, eq12))
        self.play(ReplacementTransform(eq12, eq13))
        self.play(ReplacementTransform(eq13, eq14))
        self.play(ReplacementTransform(eq14, eq15))
        self.wait()
        eq16 = MathTex(r"\int \frac{dI(\lambda)}{d\lambda} d\lambda = - \int\frac{\lambda}{\lambda^2 + 1}d\lambda + i\int\frac{1}{\lambda^2 + 1}d\lambda")
        self.play(ReplacementTransform(eq15, eq16))
        eq17 = MathTex(r"I(\lambda) = -\frac{1}{2}\ln(\lambda^2 + 1) + i\arctan(\lambda) + C")
        self.play(ReplacementTransform(eq16, eq17))
        self.wait()

        # Limite b→-inf
        text = Text("Nos interessa apenas a parte imaginária dessa solução:", font_size=30, font="Courier Prime").shift(UP)
        self.play(ReplacementTransform(eq17, text))
        eq18 = MathTex("\Im(I(\lambda)) = \int_0^\infty \\frac{\sin x}{x}e^{\lambda x}dx = \\arctan(\lambda) +", "C")
        frame5 = SurroundingRectangle(eq18[1], buff=0.1)
        text_cte = Text("Podemos determinar via limite", font="Courier Prime", font_size=20).next_to(frame5, DOWN)
        self.play(Write(eq18))
        self.play(Create(frame5), Write(text_cte))
        self.wait()
        self.play(FadeOut(VGroup(frame5, text_cte, text)))
        eq19 = MathTex(
            r"\lim_{\lambda\rightarrow-\infty}\left[\int_0^\infty \frac{\sin x}{x}e^{\lambda x}dx\right] = \lim_{\lambda\rightarrow-\infty}\left[\arctan(\lambda) + C\right]")
        self.play(ReplacementTransform(eq18, eq19))
        eq20 = MathTex(
            r"\left[\int_0^\infty \frac{\sin x}{x}\lim_{\lambda\rightarrow-\infty}e^{\lambda x}dx\right] = \lim_{\lambda\rightarrow-\infty}\arctan(\lambda) + \lim_{\lambda\rightarrow-\infty}C")
        self.play(ReplacementTransform(eq19, eq20))
        eq21 = MathTex(r"0 = \lim_{\lambda\rightarrow-\infty}\arctan(\lambda) + \lim_{\lambda\rightarrow-\infty}C")
        eq22 = MathTex(r"0 = \lim_{\lambda\rightarrow-\infty}\arctan(\lambda) + C")
        eq23 = MathTex(r"0 = -\frac{\pi}{2} + C")
        eq24 = MathTex(r"C = \frac{\pi}{2}")
        self.play(ReplacementTransform(eq20, eq21))
        self.play(ReplacementTransform(eq21, eq22))
        self.play(ReplacementTransform(eq22, eq23))
        self.play(ReplacementTransform(eq23, eq24))
        self.wait()
        final = Text("Assim", font_size=30, font="Courier Prime")
        self.play(ReplacementTransform(eq24, final))
        self.wait()
        eq25 = MathTex(r"\Im(I(\lambda)) = \int_0^\infty \frac{\sin x}{x}e^{\lambda x}dx = \arctan(\lambda) + \frac{"
                       r"\pi}{2}")
        eq26 = MathTex(r"\Im(I(0)) = \int_0^\infty \frac{\sin x}{x}e^{0\cdot x}dx = \arctan(0) + \frac{\pi}{2}")
        eq27 = MathTex(r"\int_0^\infty \frac{\sin x}{x}dx = \frac{\pi}{2}")
        frame_final = SurroundingRectangle(eq27, buff=0.1)
        self.play(ReplacementTransform(final, eq25))
        self.play(ReplacementTransform(eq25, eq26))
        self.play(ReplacementTransform(eq26, eq27))
        self.play(Create(frame_final))
        self.wait()

        # CTA
        self.play(FadeOut(VGroup(frame_final, eq27)))
        self.play(ReplacementTransform(arroba, Arroba))
        self.wait()

if __name__ == "__main__":
    scene = FInt()
    scene.render()
