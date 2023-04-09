import numpy as np
from manim import *

# CONSTRUÇÃO VETORIAL
class Solution(Scene):
    def construct(self):
        # cria o texto do @
        arroba = Text('@manual.fisica', color=YELLOW, font="Courier Prime", font_size=20)
        Arroba = Text('Siga o @manual.fisica', color=YELLOW, font="Courier Prime", font_size=30)

        # cria o eixo x e y
        axes = Axes(
            x_range=[0, 7, 10],  # O step foi colocado no range máximo para não exibir marcações nos eixos
            y_range=[0, 7, 10],
            x_length=7,
            y_length=7,
            tips=True,  # Tips são as pontas dos eixos
            axis_config={"color": WHITE},
            z_index=2  # Este parâmetro faz com que o objeto esteja acima dos demais na cena. Default = 0
        )

        # Define o estilo do eixo
        axes.x_axis.set_stroke(width=5)
        axes.y_axis.set_stroke(width=5)

        # adiciona os eixos cartesianos na cena
        self.play(Create(axes))

        # cria o vetor a
        a_vector = Vector(direction=[5, 2, 0], color=RED, buff=0, z_index=1).shift([-3.5, -3.5, 0])
        a_label = MathTex(r"\vec{a}").next_to(a_vector, direction=RIGHT, buff=0.1)

        # adiciona o vetor a na cena
        self.play(Create(a_vector))
        self.play(Write(a_label))

        # cria o vetor b
        b_vector = Vector(direction=[2, 5, 0], color=BLUE, buff=0, z_index=1).shift([-3.5, -3.5, 0])
        b_label = MathTex(r"\vec{b}").next_to(b_vector, direction=UP, buff=0.1)

        # adiciona o vetor b na cena
        self.play(Create(b_vector))
        self.play(Write(b_label))
        self.wait(1)

        # cria o ângulo que o vetor a faz com o eixo x e o nomeia de alpha
        alpha = Angle(axes.x_axis, a_vector, radius=1.2, other_angle=False, color=WHITE)
        alpha_label = MathTex(r"\alpha", z_index=0).next_to(alpha, RIGHT, buff=0.1)

        # cria o ângulo que o vetor b faz com o eixo x e o nomeia de beta
        beta = Angle(axes.x_axis, b_vector, radius=2.1, other_angle=False, color=WHITE)
        beta_label = MathTex(r"\beta", z_index=0).next_to(beta, UP, buff=0.1)

        # adiciona os ângulos à cena
        self.play(Create(alpha))
        self.play(Write(alpha_label))
        self.wait()
        self.play(Create(beta))
        self.play(Write(beta_label))

        # agrupar todos os elementos
        grupo = VGroup(axes, alpha, alpha_label, beta, beta_label, a_vector, b_vector)

        # decomposição vetorial
        vec_a = MathTex(r"\vec{a} = a_x \hat{x} + a_y \hat{y} + a_z \hat{z}").shift(np.array([3.5, 3, 0]))
        vec_a2 = MathTex(r"\vec{a} = a\cos\alpha \hat{x} + a\sin\alpha \hat{y} + 0 \hat{z}").shift(UP)
        vec_a3 = MathTex(r"\vec{a} = a(\cos\alpha,\sin\alpha,0)").shift(UP)
        vec_b = MathTex(r"\vec{b} = b_x \hat{x} + b_y \hat{y} + b_z \hat{z}").shift(np.array([3.5, 2, 0]))
        vec_b2 = MathTex(r"\vec{b} = b\cos\beta \hat{x} + b\sin\beta \hat{y} + 0 \hat{z}").shift(DOWN)
        vec_b3 = MathTex(r"\vec{b} = b(\cos\beta,\sin\beta,0)").shift(DOWN)

        # remove o grupo e adiciona a decomposição na cena junto ao arroba
        self.play(ReplacementTransform(a_label, vec_a))
        self.play(ReplacementTransform(b_label, vec_b))
        self.play(FadeOut(grupo))
        self.play(Write(arroba.to_edge(DOWN)))

        # transforma
        self.play(ReplacementTransform(vec_a, vec_a2))
        self.play(ReplacementTransform(vec_b, vec_b2))
        self.wait(1)
        self.play(ReplacementTransform(vec_a2, vec_a3))
        self.play(ReplacementTransform(vec_b2, vec_b3))
        self.wait(1)

        # Remove o conteúdo anterior
        self.play(FadeOut(vec_a3, vec_b3))

        #Define as equações
        eq1 = MathTex(r"\vec{a}\cdot\vec{b} = ab\cos(\beta - \alpha)")
        eq2 = MathTex(r"a_xb_x + a_yb_y = ab\cos(\beta - \alpha)")
        eq3 = MathTex(r"a\cos\alpha b\cos\beta + a\sin\alpha b\sin\beta = ab\cos(\beta - \alpha)")
        eq4 = MathTex(r"ab(\cos\alpha\cos\beta + \sin\alpha\sin\beta) = ab\cos(\beta - \alpha)")
        eq5 = MathTex(r"\cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\beta - \alpha)")
        eq6 = MathTex(r"\cos(\beta - \alpha) = \cos\alpha\cos\beta + \sin\alpha\sin\beta")
        eq7 = MathTex(r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta")
        texto = Text('Cosseno da diferença', color=RED, font="Courier Prime")
        framecos = SurroundingRectangle(eq7, buff=0.1)

        #Animações
        self.play(Write(texto))
        self.wait()
        self.play(ReplacementTransform(texto, eq1))
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(ReplacementTransform(eq3, eq4))
        self.play(ReplacementTransform(eq4, eq5))
        self.play(ReplacementTransform(eq5, eq6))
        self.play(ReplacementTransform(eq6, eq7))
        self.play(Create(framecos))
        self.wait()

        #Outras definições
        Eq1 = MathTex(r"\vec{a}\times\vec{b} = \hat{z}(a_xb_y - a_yb_x)")
        Eq2 = MathTex(r"|\vec{a}\times\vec{b}| = a_xb_y - a_yb_x")
        texto2 = Text('Seno da diferença', color=RED, font="Courier Prime")
        Eq3 = MathTex(r"a_xb_y - a_yb_x = |\vec{a}\times\vec{b}|")
        Eq4 = MathTex(r"a_xb_y - a_yb_x = ab\sin(\beta - \alpha)")
        Eq5 = MathTex(r"a\cos\alpha b\sin\beta - a\sin\alpha b\cos\beta = ab\sin(\beta - \alpha)")
        Eq6 = MathTex(r"ab(\cos\alpha\sin\beta - \sin\alpha\cos\beta) = ab\sin(\beta - \alpha)")
        Eq7 = MathTex(r"\cos\alpha\sin\beta - \sin\alpha\cos\beta = \sin(\beta - \alpha)")
        Eq8 = MathTex(r"\cos\alpha\sin\beta - \sin\alpha\cos\beta = -\sin(\alpha - \beta)")
        Eq9 = MathTex(r"\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta")
        framesin = SurroundingRectangle(Eq9, buff=0.1)

        #Outras Animações
        self.play(FadeOut(eq7, framecos))
        self.play(Write(texto2))
        self.wait()
        self.play(ReplacementTransform(texto2, Eq1))
        self.play(ReplacementTransform(Eq1, Eq2))
        self.play(ReplacementTransform(Eq2, Eq3))
        self.play(ReplacementTransform(Eq3, Eq4))
        self.play(ReplacementTransform(Eq4, Eq5))
        self.play(ReplacementTransform(Eq5, Eq6))
        self.play(ReplacementTransform(Eq6, Eq7))
        self.play(ReplacementTransform(Eq7, Eq8))
        self.play(ReplacementTransform(Eq8, Eq9))
        self.play(Create(framesin))
        self.wait()

        #Finalização

        self.play(FadeOut(framesin, Eq9))
        self.play(ReplacementTransform(arroba, Arroba))

if __name__ == "__main__":
    scene = Solution()
    scene.render()
