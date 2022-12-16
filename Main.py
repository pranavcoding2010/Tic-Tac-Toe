from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.title('Tic,Tac,Toe')
Label(root,text='Player1:x',font='times 15').grid(row=0,column=1)
Label(root,text='Player2:o',font='times 15').grid(row=0,column=2)
digits = [1,2,3,4,5,6,7,8,9]
mark = ''
count = 0
panels = ['panel']*10
def win(panel,sign):
    return ((panels[1]==panels[2]==panels[3]==sign)
    or (panels[1]==panels[5]==panels[9]==sign)
    or (panels[1]==panels[4]==panels[7]==sign)
    or (panels[2]==panels[5]==panels[8]==sign)
    or (panels[3]==panels[6]==panels[9]==sign)
    or (panels[4]==panels[5]==panels[6]==sign)
    or (panels[7]==panels[8]==panels[9]==sign)
    or (panels[3]==panels[5]==panels[7]==sign))
def checker(digit):
    global count,mark,digits
    if digit == 1 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button1.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 2 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button2.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()
    
    if digit == 3 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button3.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 4 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button4.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 5 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button5.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 6 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button6.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 7 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button7.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 8 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button8.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()

    if digit == 9 and digit in digits:
        digits.remove(digit)
        if count % 2 == 0 :
            mark = 'x'
            panels [digit]=mark
        elif count % 2 !=0:
            mark = 'o'
            panels [digit]=mark 
        Button9.config(text=mark)
        count = count + 1
        sign = mark
        if (win(panels,sign)and sign == 'x'):
            msg.showinfo('result','player 1 wins')
            root.destroy()
        elif (win(panels,sign)and sign == 'o'):
            msg.showinfo('result','player 2 wins')
            root.destroy()


Button1=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(1))
Button1.grid(row=1,column=1)
Button2=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(2))
Button2.grid(row=1,column=2)
Button3=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(3))
Button3.grid(row=1,column=3)
Button4=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(4))
Button4.grid(row=2,column=1)
Button5=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(5))
Button5.grid(row=2,column=2)
Button6=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(6))
Button6.grid(row=2,column=3)
Button7=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(7))
Button7.grid(row=3,column=1)
Button8=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(8))
Button8.grid(row=3,column=2)
Button9=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(9))
Button9.grid(row=3,column=3)

root.mainloop()

