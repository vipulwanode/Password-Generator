from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string , random
root=Tk()
root.geometry('500x500')
root.title(' Password Generator  ')
root.config(bg='beige')
root.resizable(False,False)

def password_generate():
    try:
        length_password=solidboss.get()
        small_letter=string.ascii_lowercase
        capital_letter=string.ascii_uppercase
        digits=string.digits 
        special_character=string.punctuation
        all_list=[]
        all_list.extend(list( small_letter))
        all_list.extend(list(capital_letter))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set(''.join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel('A Problem Has Been Occured','Please Try Again')

# this is for selecting the length of our password........
all_no={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10'}

Title=Label(root,text='Password Generator Using Python ',bg='pink',fg='black',font=('futura',20,'bold'))
Title.pack(anchor='center',pady='20px')

length=Label(root,text='Select The Length of Your Password : ',fg='black',bg='beige',font=('ubuntu',12,'bold'))
length.place(x='5px',y='70px')


def enter(a):
    generated_btn['bg']='grey'
    generated_btn['fg']='white'
def leave(a):
    generated_btn['bg']='orange'
    generated_btn['fg']='black'

solidboss=IntVar()
selector =Combobox(root,textvariable=solidboss,state='readonly')
selector['values']=[l for l in all_no.keys()]
selector.current(7)

selector.place(x='230px',y='72px')
generated_btn=Button(root,text='Generated Password ',bg='orange',fg='black',font=('ubuntu',15 ),cursor='hand2',command=password_generate)
generated_btn.bind('<Enter>',enter)
generated_btn.bind('<Leave>',leave)

generated_btn.pack(anchor='center',pady='50px')

result_lable=Label(root,text='Generated Password Here : ',bg='beige',fg='black',font=('ubuntu',12,'bold'))
result_lable.place(x='15px',y='160px')
password=StringVar()
password_final=Entry(root,textvariable=password,state='readonly',fg='blue',font=('ubuntu',15))
password_final.place(x='180px',y='160px')

root.mainloop()