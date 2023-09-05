import tkinter as tk

# Creating a calculator by Muhammad Arslan using Tkinter gui approach and eval function
empty_string =  ''

#Calculator logic functions


#add input to calculator
def add_input(symb):
    global empty_string
    empty_string+= str(symb)
    Screen.delete(1.0,'end')  # Deletes all characters between the provided indexes
    Screen.insert(1.0,empty_string)  # Inserts symbols/characters before the index
    
    pass

#do calculation or evaluate the results

def calculate():
    global empty_string
    try :
        empty_string = str(eval(empty_string))  #Function is a safety risk as code can be injected, caution must be exercised while using this funciton.
        Screen.delete(1.0,'end')
        Screen.insert(1.0,empty_string )
    except:
        clear_screen()
        Screen.insert(1.0,"Error") #Error only occurs if user inputs an invalid calculation expression
        
        return

#Clear the screen when C (clear button) is pressed.
def clear_screen():
    global empty_string #Influence the global variable from within the function
    empty_string=''
    Screen.delete(1.0,'end')
    pass

def delete_char():
    global empty_string
    Screen.delete('end-2c')
    empty_string = empty_string[:-1]
    
#TKinter-gui code

root = tk.Tk()
root.title("Python Calculator")
root.configure(background='grey')
root.geometry('500x500')

Screen = tk.Text(root,inactiveselectbackground='grey',background='black',width =3, height= 3, font = ("Calibri",18), fg='white')
Screen.pack(fill='both')


#button style


#Create buttons and button frame
button = tk.Frame(root)
button.grid_columnconfigure(0, uniform=1, weight = 1)
button.grid_columnconfigure(1, uniform=1, weight = 1)
button.grid_columnconfigure(2, uniform=1, weight = 1)
button.grid_columnconfigure(3, uniform=1, weight = 2)
button.grid_rowconfigure(0, uniform=1, weight= 1)
button.grid_rowconfigure(1, uniform=1, weight= 1)
button.grid_rowconfigure(2, uniform=1, weight= 1)
button.grid_rowconfigure(3, uniform=1, weight= 1)
button.grid_rowconfigure(4, uniform=1, weight= 1)
button.pack(expand='true', fill= 'both')


btn1= tk.Button(button, text='0', command=lambda:add_input(0), width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn1.grid(row=4, column=3,sticky= 'nsew', padx = 0)

btn1= tk.Button(button, text='1', command=lambda:add_input(1), width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn1.grid(row=0, column=0,sticky= 'nsew', padx = 0)

btn2= tk.Button(button, text='2', command=lambda:add_input(2),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn2.grid(row=0, column=1,sticky= 'nsew', padx = 0)

btn3= tk.Button(button, text='3', command=lambda:add_input(3),width=5, height=5 , font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn3.grid(row=0, column=2, sticky= 'nsew', padx = 0)

btn4= tk.Button(button, text='4', command=lambda:add_input(4),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn4.grid(row=1, column=0, sticky= 'nsew', padx = 0)

btn5= tk.Button(button, text='5', command=lambda:add_input(5),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn5.grid(row=1, column=1, sticky= 'nsew', padx = 0)

btn6= tk.Button(button, text='6', command=lambda:add_input(6),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn6.grid(row=1, column=2, sticky= 'nsew', padx = 0)

btn7= tk.Button(button, text='7', command=lambda:add_input(7),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn7.grid(row=2, column=0, sticky= 'nsew', padx = 0)

btn8= tk.Button(button, text='8', command=lambda:add_input(8),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn8.grid(row=2, column=1,sticky= 'nsew', padx = 0 )

btn9= tk.Button(button, text='9', command=lambda:add_input(9),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white') #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btn9.grid(row=2, column=2,sticky= 'nsew' , padx = 0)

btnadd= tk.Button(button, text= "+", command=lambda:add_input('+'),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btnadd.grid(row=3, column=0,sticky= 'nsew' , padx = 0)

btnmult = tk.Button(button, text = 'x', command=lambda:add_input('*'),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btnmult.grid(row= 3, column= 1, sticky= 'nsew', padx = 0)

btnsub = tk.Button(button, text = '-', command=lambda:add_input('-'),width=5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btnsub.grid(row= 3, column= 2, sticky= 'nsew', padx = 0)

btnbrac= tk.Button(button, text='(', command=lambda:add_input('('), width =5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btnbrac.grid(row= 4, column= 0, sticky= 'nsew', padx = 0)

btnbrak= tk.Button(button, text=')', command=lambda:add_input(')'), width =5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btnbrak.grid(row= 4, column= 1,sticky= 'nsew', padx = 0)

btndiv= tk.Button(button, text='/', command=lambda:add_input('/'), width =5, height=5, font=('Arial', 18), bg ='grey', fg='white')
btndiv.grid(row= 4, column= 2,sticky= 'nsew', padx = 0)

# Adding the clear and Equals button

btnclear= tk.Button(button, text='C', command=lambda:clear_screen(), width =5, height=5, bg='orange', fg='black', font=('Arial', 18),)
btnclear.grid(row= 0, column= 3,sticky= 'nsew', columnspan= 2, rowspan= 1)

btnz= tk.Button(button, text='=', command=lambda:calculate(),width=5, height=5, font=('Arial', 18)) #Using a lambda expression allows the function to be called when button is pressed, and does not just immediately call the function.
btnz.grid(row= 2, column= 3,sticky= 'nsew', rowspan=2)

btndel= tk.Button(button, text='⩽', command=lambda:delete_char(), width =5, height=5, bg='red', fg='black', font=('Arial', 18),)
btndel.grid(row= 1, column= 3,sticky= 'nsew', columnspan= 2, rowspan =1)

#Running the main loop

root.mainloop()