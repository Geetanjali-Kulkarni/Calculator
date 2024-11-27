from tkinter import *

#Useful variables
font=('Calibri',22)

#IMportant functions
def Del():
     s=textField.get()
     textField.delete(len(s)-1)
       
def all_clr():
     textField.delete(0,END)
     
def click_btn_function(event):
     print("Button clicked")
     b=event.widget
     text=b["text"]
     print(text)

     if text=='=':
          ex=textField.get()
          answer=eval(ex)
          textField.delete(0,END)
          textField.insert(0,answer)
          return
     
     textField.insert(END,text)

#Creating main window
window = Tk()
window.title("Calculator")
x=window.configure(bg="orange")


window.minsize(380,380)
window.maxsize(480,480)

#Heading label
heading=Label(window,text="Calculator")
heading.pack()

#Textfield
textField=Entry(window,justify=CENTER)
textField.pack(fill=X)

#Creating Button Frame
ButtonFrame=Frame(window)
ButtonFrame.pack(side=TOP)

#Adding Buttons from 1 to 9 
temp=1
for i in range(0,3):
     for j in range(0,3):
          btn=Button(ButtonFrame,text=str(temp), font=font, width=5,fg='blue',bg='white',relief=GROOVE)
          btn.grid(row=i,column=j,padx=5,pady=5)
          temp=temp+1
          btn.bind('<Button-1>',click_btn_function)


zerobtn=Button(ButtonFrame,text="0", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
zerobtn.grid(row=3,column=0,padx=5,pady=5)

dotbtn=Button(ButtonFrame,text=".", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
dotbtn.grid(row=3,column=1,padx=5,pady=5)

equalbtn=Button(ButtonFrame,text="=", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
equalbtn.grid(row=3,column=2,padx=5,pady=5)

plusbtn=Button(ButtonFrame,text="+", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
plusbtn.grid(row=0,column=3,padx=5,pady=5)

minusbtn=Button(ButtonFrame,text="-", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
minusbtn.grid(row=1,column=3,padx=5,pady=5)

multbtn=Button(ButtonFrame,text="*", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
multbtn.grid(row=2,column=3,padx=5,pady=5)

divbtn=Button(ButtonFrame,text="/", font=font, width=5,fg='blue',bg='white',relief=GROOVE,)
divbtn.grid(row=3,column=3,padx=5,pady=5)

clrbtn=Button(ButtonFrame,text="clear", font=font, width=11,fg='blue',bg='white',relief=GROOVE,command=all_clr)
clrbtn.grid(row=4,column=0,padx=5,pady=5,columnspan=2)

delbtn=Button(ButtonFrame,text="del", font=font,fg='blue',bg='white',relief=GROOVE, width=11,command=Del)
delbtn.grid(row=4,column=2,padx=5,pady=5,columnspan=2)

#Binding all buttons
zerobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
plusbtn.bind('<Button-1>',click_btn_function)
minusbtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)
multbtn.bind('<Button-1>',click_btn_function)
divbtn.bind('<Button-1>',click_btn_function)

window.mainloop()
