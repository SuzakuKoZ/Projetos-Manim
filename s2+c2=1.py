from manim import *
import numpy as np

class Equality(Scene):
    def construct(self):
        # Título do vídeo e arroba
        texto = Text('VERIFICAÇÃO GRÁFICA DE', color=YELLOW, font="Courier Prime")
        eq = MathTex(r"\sin^2\theta + \cos^2\theta = 1", font_size=60)
        arroba = Text('@manual.fisica', color=YELLOW, font="Courier Prime", font_size=20)
        Arroba = Text('Siga o @manual.fisica', color=YELLOW, font="Courier Prime", font_size=30)
        self.play(Write(texto))
        self.wait()
        self.play(Write(eq.shift(DOWN)))
        self.wait()
        self.play(Write(arroba.shift([0.0,-3.8,0.0])))
        self.wait()
        self.play(FadeOut(texto, eq))

        # Cria os eixos
        axes = Axes(
            x_range=[-6,6,1],
            y_range=[-1.5,1.5,1],
            tips=True,
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "include_tip": True,
                "tip_style": {"fill_opacity": 1, "fill_color": WHITE, "stroke_width": 0}
            },
            x_axis_config={"numbers_to_include":[-6,-4,-2,2,4,6]},
            y_axis_config={"numbers_to_include":[-1,1]}
        )

        #Desenha os eixos
        self.play(Create(axes))
        self.wait()

        # Cria a função seno
        seno = axes.plot(lambda x: np.sin(x), color=YELLOW)
        seno_label = MathTex(r"\sin\theta").set_color(YELLOW).shift([4.0,2.5,0.0])
        self.play(Create(seno), Write(seno_label))
        self.wait()

        # Transforma em seno ao quadrado
        s2 = axes.plot(lambda x: np.sin(x)**2, color=YELLOW)
        s2_label = MathTex(r"\sin^2\theta").set_color(YELLOW).shift([4.0,2.5,0.0])
        areas2 = axes.get_area(s2)
        self.play(ReplacementTransform(seno, s2), ReplacementTransform(seno_label, s2_label))
        self.add(areas2)
        self.wait()
        self.play(FadeOut(s2))
        self.wait()

        # Cria a função cosseno
        cosseno = axes.plot(lambda x: np.cos(x), color=BLUE)
        cosseno_label = MathTex(r"\cos\theta").set_color(BLUE).shift([-4.0,2.5,0.0])
        self.play(Create(cosseno), Write(cosseno_label))
        self.wait()

        # Transforma em cosseno ao quadrado
        c2 = axes.plot(lambda x: np.cos(x)**2, color=BLUE)
        c2_label = MathTex(r"\cos^2\theta").set_color(BLUE).shift([-4.0,2.5,0.0])
        areac2 = axes.get_area(c2)
        self.play(ReplacementTransform(cosseno, c2), ReplacementTransform(cosseno_label, c2_label))
        self.add(areac2)
        self.wait()

        # Desenha a reta y=1
        reta = axes.plot(lambda x: 1, color=GREEN)
        reta_label = MathTex(r"\sin^2\theta + \cos^2\theta").set_color(GREEN).shift([4.0,2.5,0.0])
        grupo_equations = VGroup(s2_label, c2_label)
        areareta = axes.get_area(reta)
        area_grupo = VGroup(areas2, areac2)
        self.play(ReplacementTransform(c2, reta), ReplacementTransform(area_grupo, areareta), ReplacementTransform(grupo_equations, reta_label))

        #Agrupa tudo e remove da cena
        grupo = VGroup(axes, reta, areareta, reta_label)
        self.play(FadeOut(grupo))

        # Sobe o texto @manual.fisica
        self.play(ReplacementTransform(arroba, Arroba))
        self.wait()

if __name__ == "__main__":
    scene = Equality()
    scene.render()
