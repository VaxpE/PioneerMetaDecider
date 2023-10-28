from modules.tournament import tournament
from modules.meta import meta
from modules.Deck import Deck
from tkinter import *
from tkinter import scrolledtext


def printresult():
    with open('data.txt', 'r') as tournament_result:
        with open('results.txt', 'r') as current_meta:
            temp = meta(current_meta, tournament_result)

    current_meta = open('results.txt', 'w')
    for index, deck in enumerate(temp):
        label = Label(window, text = deck, width=20)
        label.grid(row=index, column=1)
        print(deck, file = current_meta)
    current_meta.close()

window = Tk()
window.title('SPb Pioneer Metagame')
window.geometry('960x540')
printresult() 
btn = Button(window, text = 'Добавить турнир', command = printresult)
btn.grid(row=1,column=3)

window.mainloop()