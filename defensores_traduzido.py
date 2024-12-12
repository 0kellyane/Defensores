import random
import time 

giro = 5


def atualizar_pontuacao(nome, pontuacao_final):
    jogador = {"nome": nome, "pontuacao": pontuacao_final}
    ranking.append(jogador)

    for jogador in ranking:
        if jogador["nome"] == nome:
            jogador["pontuacao"] += pontuacao_final
            print(f"Pontuação de {nome} atualizada para {jogador['pontuacao_final']} pontos.")
            return
    print("Jogador não encontrado no ranking.")

def exibir_ranking():
    if not ranking:
        print("Nenhum jogador no ranking ainda.")
        return
    print("Ranking de jogadores:")
    for i, jogador in enumerate(sorted(ranking, key=lambda x: x["pontuacao"], reverse=True), 1):
        print(f"{i}. {jogador['nome']} - {jogador['pontuacao']} pontos")


def menu():
    print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |::::::::::::::::::::::::DEFENSORES DO LIMITE DA TERRA::::::::::::::::::::|                                                                  
             |                                                                         |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                  ➳      INICIAR              [PRESSIONE--1]            |
             |                                                                         |
             |                  ➳      CONTROLES           [PRESSIONE--2]             |
             |                                                                         |
             |                  ➳      SOBRE O JOGO        [PRESSIONE--3]             |
             |                                                                         |
             |                  ➳      EXIBIR RANKING      [PRESSIONE--4]             |
             |                                                                         |
             |                  ➳      SAIR DO JOGO        [PRESSIONE--5]             |
             |                                                                         |
             |_________________________________________________________________________|                                                                        
    """)
    escolha = input('Escolha uma opção acima:- ')
    print('>------------<>------------<')


    if (escolha == '1'):
        jogo()


    elif (escolha == '2'):
        print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |::::::::::::::::::::::::::::::::::CONTROLES::::::::::::::::::::::::::::::|                                                                  
             |                                                                         |
             |        ✵  PARA ACELERAR PARA FRENTE        PRESSIONE [W]               |                                                  
             |                                                                         |
             |        ✵  PARA DESACELERAR PARA FRENTE     PRESSIONE [S]               |                                      
             |                                                                         |
             |        ✵  PARA GIRAR À DIREITA             PRESSIONE [D]               |                                      
             |                                                                         |
             |        ✵  PARA GIRAR À ESQUERDA            PRESSIONE [A]               |                                      
             |                                                                         |
             |        ✵  PARA LANÇAR MÍSSIL              PRESSIONE [BARRA DE ESPAÇO]  |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |::::::::::::::::::::::::::::::::::REGRAS:::::::::::::::::::::::::::::::::|                                                                         
             |                                                                         |
             |        ☛  ATIRAR EM NAVES ALIENÍGENAS {VERMELHAS}  AUMENTA 50 PONTOS    |
             |                                                                         |
             |        ☛  ATIRAR EM ALIADOS {AZUIS}        DIMINUI 20 PONTOS            |
             |                                                                         |             
             |        ☛  COLIDIR COM NAVES ALIENÍGENAS    DIMINUI 10 PONTOS            |
             |                                                                         |             
             |_________________________________________________________________________|""")                                                                      
        escolha = input('                           Pressione qualquer tecla para voltar ao menu:- ')
        print('                            >------------<>------------<')
        if (escolha == 'm'):
             menu()
        else:
             menu()
    elif (escolha == '3'):
        print("""             __________________________________________________________________________
             |                                                                         |
             |                                                                         |
             |:::::::::::::::::::::::::::::SOBRE O JOGO::::::::::::::::::::::::::::::: |                                                                  
             |                                                                         |
             |                                                                         |             
             |                                                                         |
             |                                                                         |
             |  O JOGO {DEFENSORES DO LIMITE DA TERRA} É SOBRE UMA INVASÃO DE NAVES    |
             |  ALIENÍGENAS {VERMELHAS} AO SEU PLANETA. VOCÊ É O GENERAL DO EXÉRCITO   |
             |  ESPACIAL DA TERRA [E.S.A]. VOCÊ PRECISA DEFENDER A TERRA NO SEU ARCA   |   
             |  {BRANCO}, COM A AJUDA DOS SEUS ALIADOS {AZUIS}.                        |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |
             |                                                                         |             
             |_________________________________________________________________________|  """)                                                                     
           
        escolha = input('                          Pressione qualquer tecla para voltar ao menu:- ')
        print('                            >------------<>------------<')
        if (escolha == 'm'):
            menu()
        else:
            menu()
    elif (escolha == '4'):
        exibir_ranking()
        menu()
    elif (escolha == '5'):
        quit()
    else:
        print("Escolha errada. Por favor, selecione novamente.")
        menu()

# O restante do código segue com comentários em português...

ranking = []
pontuacao_final = 0 

def jogo():
    
    global pontuacao_final
    nome = input("Digite o nome do jogador atual: ")
    import turtle
    import time

    # Tempo limite do jogo (em segundos)
    tempo_limit = 20
    inicio_jogo = time.time()

    # Configuração inicial do Turtle
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0) # colocar em tela cheia
    turtle.fd(0)
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.title("::::::::::::::::::::::::::::DEFENSORES DO LIMITE DA TERRA::::::::::::::::::::::::::::")
    turtle.ht()
    turtle.setundobuffer(1)
    turtle.tracer(4)

    # Classe base para os objetos do jogo
    class Sprite(turtle.Turtle):
        def __init__(self, forma, cor, inicio_x, inicio_y):
            turtle.Turtle.__init__(self, shape=forma)
            self.speed(0)
            self.penup()
            self.color(cor)
            self.fd(0)
            self.goto(inicio_x, inicio_y)
            self.velocidade = 1

        def mover(self):
            self.fd(self.velocidade)

            if self.xcor() > 290:
                self.setx(290)
                self.rt(60)
            if self.xcor() < -290:
                self.setx(-290)
                self.rt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.rt(60)
            if self.ycor() < -290:
                self.sety(-290)
                self.rt(60)

        def colisao(self, outro):
            if (self.xcor() >= (outro.xcor() - 20)) and \
               (self.xcor() <= (outro.xcor() + 20)) and \
               (self.ycor() >= (outro.ycor() - 20)) and \
               (self.ycor() <= (outro.ycor() + 20)):
                return True
            else:
                return False

    class Jogador(Sprite):
        def __init__(self, forma, cor, inicio_x, inicio_y):
            Sprite.__init__(self, forma, cor, inicio_x, inicio_y)
            self.shapesize(stretch_wid=1, stretch_len=3)
            self.velocidade = 4
            self.velocidade_rotacao = 0

        def girar_esquerda(self):
            self.velocidade_rotacao = giro

        def girar_direita(self):
            self.velocidade_rotacao = -giro

        def parar_rotacao(self):
            self.velocidade_rotacao = 0

        def acelerar(self):
            self.velocidade += 1

        def desacelerar(self):
            if self.velocidade > 1:
                self.velocidade -= 1

        def mover(self):
            self.setheading(self.heading() + self.velocidade_rotacao)
            self.fd(self.velocidade)

            # Limites do movimento
            limite_x = 290
            limite_y = 290

        # Verifica se o jogador saiu do limite e reposiciona
            if self.xcor() > limite_x:
                self.setx(limite_x)
            elif self.xcor() < -limite_x:
                self.setx(-limite_x)

            if self.ycor() > limite_y:
                self.sety(limite_y)
            elif self.ycor() < -limite_y:
                self.sety(-limite_y)

    class Inimigo(Sprite):
        def __init__(self, forma, cor, inicio_x, inicio_y):
            Sprite.__init__(self, forma, cor, inicio_x, inicio_y)
            self.shapesize(stretch_wid=1, stretch_len=3)
            self.velocidade = 4
            self.setheading(random.randint(0, 360))

    class Aliado(Sprite):
        def __init__(self, forma, cor, inicio_x, inicio_y):
            Sprite.__init__(self, forma, cor, inicio_x, inicio_y)
            self.shapesize(stretch_wid=2, stretch_len=3)
            self.velocidade = 5
            self.setheading(random.randint(0, 360))

    class Missil(Sprite):
        def __init__(self, forma, cor, inicio_x, inicio_y):
            Sprite.__init__(self, forma, cor, inicio_x, inicio_y)
            self.shapesize(stretch_wid=0.2, stretch_len=0.4)
            self.velocidade = 25
            self.status = "pronto"
            self.goto(-1000, 1000)

        def disparar(self):
            if self.status == "pronto":
                self.goto(jogador.xcor(), jogador.ycor())
                self.setheading(jogador.heading())
                self.status = "disparando"

        def mover(self):
            if self.status == "pronto":
                self.goto(-1000, 1000)
            elif self.status == "disparando":
                self.fd(self.velocidade)
                if self.xcor() < -290 or self.xcor() > 290 or \
                   self.ycor() < -290 or self.ycor() > 290:
                    self.goto(-1000, 1000)
                    self.status = "pronto"

    class Jogo:
        def __init__(self):
            self.pontuacao = 0
            self.pen = turtle.Turtle()

        def desenhar_borda(self):
            self.pen.speed(0)
            self.pen.color("white")
            self.pen.pensize(10)
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.pendown()
            for _ in range(4):
                self.pen.fd(600)
                self.pen.rt(90)
            self.pen.penup()
            self.pen.ht()

        def mostrar_status(self):
            self.pen.undo()
            mensagem = f"Pontuação: {self.pontuacao}"
            self.pen.color("white")
            self.pen.penup()
            self.pen.goto(-300, 310)
            self.pen.write(mensagem, font=("Arial", 32, "bold"))

    jogo = Jogo()
    jogo.desenhar_borda()
    jogo.mostrar_status()

    jogador = Jogador("turtle", "orange", 0, 0)
    missil = Missil("triangle", "yellow", 0, 0)

    inimigos = [Inimigo("arrow", "red", -100, 0) for _ in range(6)]
    aliados = [Aliado("classic", "blue", 100, 0) for _ in range(6)]


    # Vinculação de teclas
    turtle.onkeypress(jogador.acelerar, "w")
    turtle.onkeypress(jogador.desacelerar, "s")
    turtle.onkeypress(jogador.girar_esquerda, "a")
    turtle.onkey(jogador.parar_rotacao, "a")
    turtle.onkeypress(jogador.girar_direita, "d")
    turtle.onkey(jogador.parar_rotacao, "d")
    turtle.onkeypress(missil.disparar, "space")
    turtle.listen()

    def atualizar():
        jogador.mover()
        screen.ontimer(atualizar, 20)

    # Loop principal
    while True:
        if time.time() - inicio_jogo > tempo_limit:
            pontuacao_final = jogo.pontuacao 
            print("Tempo esgotado! Fim do jogo!")
            turtle.clearscreen()  # Limpa a tela para voltar ao menu
            menu() 
            break

        turtle.update()
        time.sleep(0.001)
        jogador.mover()
        missil.mover()

        for inimigo in inimigos:
            inimigo.mover()
            if jogador.colisao(inimigo):
                inimigo.goto(random.randint(-250, 250), random.randint(-250, 250))
                jogo.pontuacao -= 10
                jogo.mostrar_status()
            if missil.colisao(inimigo):
                inimigo.goto(random.randint(-250, 250), random.randint(-250, 250))
                missil.status = "pronto"
                jogo.pontuacao += 50
                jogo.mostrar_status()

        for aliado in aliados:
            aliado.mover()
            if missil.colisao(aliado):
                aliado.goto(random.randint(-250, 250), random.randint(-250, 250))
                missil.status = "pronto"
                jogo.pontuacao -= 20
                jogo.mostrar_status()

    atualizar()

    screen.mainloop()
menu()

