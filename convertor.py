from tkinter import *
# Centimetro para polegada
cor1 = '#6959CD'
principal = Tk()
principal.title('Convertor polegadas')
principal.configure(background = cor1)
principal.geometry('400x400+300+300')
label1= Label(text='Insira o valor em centímetro',background=cor1)
label1.place(x='80',y='70')
entrada=Entry(principal)
entrada.place(x='80',y='100')

def bt_click():
  centimetro = int(entrada.get())
  polegada = centimetro/2.54
  label3['text']=polegada

botao=Button(principal,command=bt_click,text='Calcular')
botao.place(x='80',y='130')
label2=Label(principal,background=cor1,text='O valor em polegadas é:')
label2.place(x='80',y='170')
label3=Label(background=cor1,text='')
label3.place(x='80',y='200')

# Polegadas para Centimetros

label4=Label(text='Insira o valor em polegadas',background=cor1)
label4.place(x='400',y='70')
entrada1=Entry(principal)
entrada1.place(x='400',y='100')

def bt_click():
  polegada1 = int(entrada1.get())
  centimetro1 = polegada1*2.54
  label6['text']=centimetro1

botao1=Button(principal,command=bt_click,text='Calcular')
botao1.place(x='400',y='130')

label5=Label(principal,background=cor1,text='O valor em centimetros é:')
label5.place(x='400',y='170')
label6=Label(background=cor1,text='')
label6.place(x='400',y='200')