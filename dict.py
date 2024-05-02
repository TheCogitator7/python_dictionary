#import tkinter module
from tkinter import *
import random


#key input func
def answer():
    get_a_question=entry.get()
    output.delete(0.0, END)
    try:
        definition=flash_cards[get_a_question]
    except:
        definition="Choose a question"
    output.insert(END, definition)

def question():
    questions=list(flash_cards.keys())
    entry.delete(0, END)
    i=random.randrange(0, len(flash_cards))
    entry.insert(END, questions[i])

    



#main
window=Tk()
window.title("My Coding Club Flash Cards")

#button
Button(window, text="Question", width=10, command=question).grid(row=0, column=0, sticky=W)
Button(window, text="Answer", width=10, command=answer).grid(row=0, column=0, sticky=E)

#entry
entry=Entry(window, width=20, bg="light gray")
entry.grid(row=1, column=0, sticky=W)


#label
Label(window, text="\ndefinition :").grid(row=2, column=0, sticky=W)


#text box
output=Text(window, width=75, height=6, background="light gray")
output.grid(row=3, column=0, sticky=W)


#dict
flash_cards={
    "school" : "학교",
    "desk" : "책상",
    "chair" : "의자",
    "blackboard" : "칠판",
    }



#run main loop
window.mainloop()
