#Importa a biblioteca Turtle
import turtle
#Instrucoes para o uso
print("Para utilizarmos esse programa, você deve escolher uma combinação entre (-,I,II,III,IIII,IIIII) ")
print("depois deve escolher uma inclinação, que deve ser entre 0 e 360")
print("E por fim escolherá uma cor entre elas: blue, green, red, yellow")

#Tamanho do traço
turtle.pensize(5)

#Pergunta ao usuário o código que ele quer inserir
init=input("Digite aqui sua combinação entre as disponíveis: ").split(" ")
#Pergubta ao usuario a inclinacao inicial
incli=int(input("Qual será a inclinação inicial? "))
#Pergunta ao usuario qual cor ele pretende usar
cor=input("Escolha uma cor dentre as opções: ")

cont=0
maxi=0
code=0

#Laço for
for i in init:
    if i=="-":
        maxi=maxi+1
    if i=="I":
        code=code+10
    if i=="II":
        code=code+20
    if i=="III":
        code=code+30
    if i=="IIII":
        code=code+40
    if i=="IIIII":
        code=code+50

turtle.pencolor(cor)
turtle.left(90)
turtle.up()
turtle.backward(150)
turtle.down()
turtle.forward(code)

#Função
def fig(code, cont):
    tamanho=turtle.pensize()
    turtle.pensize(tamanho*2/3)

    code=code-5
    turtle.left(incli)
    turtle.forward(code)

    if cont<maxi:
        fig(code, cont+1)

    turtle.pencolor(cor)
    turtle.up()
    turtle.backward(code)
    turtle.down()
    turtle.right(incli*2)
    turtle.forward(code)

    if cont<maxi:
        fig(code,cont+1)

    turtle.pencolor(cor)
    turtle.up()
    turtle.backward(code)
    turtle.down()
    turtle.left(incli)
    turtle.pensize(tamanho)

fig(code, cont)
turtle.done()