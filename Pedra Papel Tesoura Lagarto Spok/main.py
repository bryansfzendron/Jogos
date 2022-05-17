
import random
from re import L
from time import sleep
from tkinter import * 
escolhaUser = "0"

def play(escolhaUser):
    if escolhaUser == '1':
        escolhaM = 'Pedra'
    elif escolhaUser == '2':
        escolhaM = 'Papel'
    elif escolhaUser == '3':
        escolhaM = 'Tesoura'
    elif escolhaUser == '4':
        escolhaM = 'Spok'
    elif escolhaUser == '5':
        escolhaM = 'Lagarto'


    if escolhaUser == '1':
        escolhaP = '👊🏻'
    elif escolhaUser =='2':
        escolhaP = '🧻'
    elif escolhaUser == '3':
        escolhaP = '✂'
    elif escolhaUser == '4':
        escolhaP = '🖖🏻'
    elif escolhaUser =='5':
        escolhaP = '🦎'



    escolhas = ['Pedra','Papel','Tesoura','Spok', 'Lagarto']

    r = random.choice(escolhas)

    if r == 'Pedra':
        escolhaR = '👊🏻'
    elif r == 'Papel':
        escolhaR = '🧻'
    elif r == 'Tesoura':
        escolhaR = '✂'
    elif r == 'Spok':
        escolhaR = '🖖🏻'
    elif r == 'Lagarto':
        escolhaR = '🦎'
    


    if escolhaM == r:

        lbn2 = Label(app,text=f"Empate\nMaquina: {escolhaR}\nPlayer: {escolhaP}",background='#dde',foreground='#009',anchor=CENTER,font='arial 14', justify=CENTER,bd=1,relief='solid')
        lbn2.place(x=0,y=150,width=300,height=100)
    elif escolhaM == 'Papel' and r == 'Pedra' or escolhaM == 'Tesoura' and r == 'Papel' or escolhaM == 'Pedra' and r == 'Tesoura' or escolhaM == "Lagarto" and r == 'Papel'or escolhaM == "Lagarto" and r == 'Spok'or escolhaM == "Pedra" and r == 'Lagarto'or escolhaM == "Tesoura" and r == 'Lagarto'or escolhaM == "Spok" and r == 'Pedra' or escolhaM == "Spok" and r == 'Tesoura' or escolhaM == "Papel" and r == 'Spok':
        lbn2 = Label(app,text=f"Vitoria do Player \nMaquina: {escolhaR}\nPlayer: {escolhaP}",background='#dde',foreground='#009',anchor=CENTER,font='arial 14', justify=CENTER,bd=1,relief='solid')
        lbn2.place(x=0,y=150,width=300,height=100)


    elif r == 'Pedra' and  escolhaM == 'Papel' or r == 'Tesoura' and escolhaM == 'Papel' or r == 'Pedra' and escolhaM == 'Tesoura' or r == "Lagarto" and escolhaM == 'Papel'or r == "Lagarto" and escolhaM == 'Spok'or r == "Pedra" and escolhaM == 'Lagarto'or r == "Tesoura" and escolhaM == 'Lagarto'or r == "Spok" and escolhaM == 'Pedra' or r == "Spok" and escolhaM == 'Tesoura' or r == "Papel" and escolhaM == 'Spok':

        lbn2 = Label(app,text=f"Vitoria da Maquina \nMaquina: {escolhaR}\nPlayer: {escolhaP}",background='#dde',foreground='#009',anchor=CENTER,font='arial 14', justify=CENTER,bd=1,relief='solid')
        lbn2.place(x=0,y=150,width=300,height=100)    
        


app=Tk()
app.title("JOKENPÔ")
app.minsize(width=300, height=300)
app.maxsize(width=300, height=300)
app.geometry("300x300")
app.configure(background="#dde")
lbn2 = Label(app,text='')
def clearTextInput():
    lbn2.delete()
    lbn2.delete(0, 'end')

lbn1 = Label(app,text='JOKENPÔ\nEscolha uma opção',background='#dde',foreground='#009',anchor=CENTER, font='arial 12', justify=CENTER)
lbn1.place(x=0,y=20,width=300,height=100)

btnPedra = Button(app,text="👊🏻",font= 20 , command=lambda: play('1'))
btnPedra.place(x=65,y=100,width=30,height=25)

btnPapel = Button(app,text="🧻",font= 20,command=lambda: play('2'))
btnPapel.place(x=100,y=100,width=30,height=25)

btnTesoura = Button(app,text="✂", font= 20, command=lambda: play('3'))
btnTesoura.place(x=135,y=100,width=30,height=25)

btnTesoura = Button(app,text="🖖🏻", font= 20, command=lambda: play('4'))
btnTesoura.place(x=170,y=100,width=30,height=25)

btnTesoura = Button(app,text="🦎", font= 20, command=lambda: play('5'))
btnTesoura.place(x=205,y=100,width=30,height=25)


app.mainloop()