from tkinter import  *
import parser

window= Tk()
window.title("Calulator")

#get user input 
i=0
def get_var(num):
    global i
    display.insert(i,num)
    i+=1
    
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
    
def get_operator(operator):
    global i 
    length = len(operator)
    display.insert(i,operator)
    i+=length
    
def fact():
    facto = 1
    number = display.get()
    num = number[-1:]
    for x in range(1,num+1):
        facto = facto * x
    clear_all()
    display.insert(0,facto)
    

def clear_all():
    display.delete(0,END)
    
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
        
#adding input field
display = Entry(window)
display.grid(row=0,columnspan=6,sticky=W+E)

Button(window,text="1",command=lambda:get_var(1)).grid(row=1,column=0)
Button(window,text="2",command=lambda:get_var(2)).grid(row=1,column=1)
Button(window,text="3",command=lambda:get_var(3)).grid(row=1,column=2)

Button(window,text="4",command=lambda:get_var(4)).grid(row=2,column=0)
Button(window,text="5",command=lambda:get_var(5)).grid(row=2,column=1)
Button(window,text="6",command=lambda:get_var(6)).grid(row=2,column=2)

Button(window,text="7",command=lambda:get_var(7)).grid(row=3,column=0)
Button(window,text="8",command=lambda:get_var(8)).grid(row=3,column=1)
Button(window,text="9",command=lambda:get_var(9)).grid(row=3,column=2)

Button(window,text="AC",command=lambda:clear_all()).grid(row=4,column=0)
Button(window,text="0",command=lambda:get_var(0)).grid(row=4,column=1)
Button(window,text="=",command=lambda:calculate()).grid(row=4,column=2)

Button(window,text="+",command=lambda:get_operator("+")).grid(row=1,column=3)
Button(window,text="-",command=lambda:get_operator("-")).grid(row=2,column=3)
Button(window,text="*",command=lambda:get_operator("*")).grid(row=3,column=3)
Button(window,text="/",command=lambda:get_operator("/")).grid(row=4,column=3)

Button(window,text="pi",command=lambda:get_operator("3.142")).grid(row=1,column=4)
Button(window,text="%",command=lambda:get_operator("%")).grid(row=2,column=4)
Button(window,text="(",command=lambda:get_operator("(")).grid(row=3,column=4)
Button(window,text="exp",command=lambda:get_operator("**")).grid(row=4,column=4)

Button(window,text="<-",command=lambda:undo()).grid(row=1,column=5)
Button(window,text="x!",command=lambda:fact()).grid(row=2,column=5)
Button(window,text=")",command=lambda:get_operator(")")).grid(row=3,column=5)
Button(window,text="^2",command=lambda:get_operator("**2")).grid(row=4,column=5)

window.mainloop()
