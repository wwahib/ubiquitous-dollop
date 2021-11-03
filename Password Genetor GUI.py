from tkinter  import * 
import random
import string
import pyperclip
			#################    Password Generator     ###################
password_chars=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

def password_genetor():
	password_field.delete(0, END)
	length = int(char_input.get())
	password=''.join([random.choice(password_chars)for _ in range(length) ])
	password_field.insert(0, password)
	pyperclip.copy(password)
									#----->USER INTER FACE<--------#

root=Tk()

root.title('#WELCOME TO THE PASSWOARD GENERATOR#')
root.geometry("500x300")

#Creating the label frame
lf=LabelFrame(root,text='How many Characters:')
lf.pack(pady=20)

#creating the Entry box 
char_input=Entry(lf,text='HELLO',bg="#fb743e",font=("helvetica",20,))
char_input.pack(pady=20,padx=20)
char_input.insert(0, "12")
char_input.focus()

#creating the entery box for retuend password
password_field=Entry(root,text='',font=("helvetica",20))
password_field.pack(pady=20)

#creating the frame of a button AND CLIP BOARD 
my_frame_button_clip=Frame(root)
my_frame_button_clip.pack(pady=20)

#										Creating the button 
my_button=Button(my_frame_button_clip,text='GENERATOR STRONG PASSWOARD',command=password_genetor)
my_button.grid(row=0,column=0,padx=10)

# #creating the clipboard button 
# my_clip=Button(my_frame_button_clip,text='Copy to the clip Board')
# my_clip.grid(row=0,column=1,padx=10)


root.mainloop()
