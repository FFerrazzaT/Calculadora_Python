from tkinter import *

#Ação dos botoes
def btnClick(numbers):
    global operator
    operator= operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnIgual():
    global operator
    igual=str(eval(operator))
    text_Input.set(igual)

#Tela
cal = Tk()
cal.title("Calculadora Python")
operator=""
text_Input=StringVar()

txtDisplay=Entry(cal,fg="black", font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

#Botões numeros
btn9=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="9", bg="powder blue", command=lambda:btnClick(9)).grid(row=1,column=2)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="8", bg="powder blue", command=lambda:btnClick(8)).grid(row=1,column=1)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="7", bg="powder blue", command=lambda:btnClick(7)).grid(row=1,column=0)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="6", bg="powder blue", command=lambda:btnClick(6)).grid(row=2,column=2)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="5", bg="powder blue", command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="4", bg="powder blue", command=lambda:btnClick(4)).grid(row=2,column=0)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="3", bg="powder blue", command=lambda:btnClick(3)).grid(row=3,column=2)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="2", bg="powder blue", command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="1", bg="powder blue", command=lambda:btnClick(1)).grid(row=3,column=0)
btn0=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="0", bg="powder blue", command=lambda:btnClick(0)).grid(row=4,column=0)

#Botões Operação
btn_menos=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="-", bg="powder blue", command=lambda:btnClick("-")).grid(row=1,column=4)
btn_mais=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="+", bg="powder blue", command=lambda:btnClick("+")).grid(row=2,column=4)
btn_vezes=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="*", bg="powder blue", command=lambda:btnClick("*")).grid(row=3,column=4)
btn_dividir=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="/", bg="powder blue", command=lambda:btnClick("/")).grid(row=4,column=4)
btn_limpar=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="C", bg="powder blue", command=lambda:btnClear()).grid(row=4,column=1)
btn_igual=Button(cal,padx=16,bd=8,fg="black",font=('arial', 20, 'bold'), text="=", bg="powder blue", command=lambda:btnIgual()).grid(row=4,column=2)
cal.mainloop()