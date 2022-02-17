from tkinter import *
import time

root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()


def create_grid(canvasName):
    for y in range(1, 11):
        for x in range(1, 11):
            print(x*20, y*20)
            canvasName.create_rectangle(x*20, y*20, x*20+20, y*20+20)   #coin en haut a gauche, coin en bas a gauche        coin en bas a droite


def create_mine(x, y, canvasName):
    x1 = x * 20
    y1 = y * 20
    x2 = x * 20 + 20
    y2 = y * 20 + 20
    canvasName.create_oval(x1, y1, x2, y2, fill='green')
    canvasName.create_oval(x1+4, y1+4, x2-4, y2-4, fill='red')


def add_flag(x, y, canvasName):
    x1 = x * 20
    y1 = y * 20
    x2 = x * 20 + 20
    y2 = y * 20 + 20
    canvasName.create_rectangle(x1, y1, x2, y2, fill="green", outline = 'green')
    canvasName.create_rectangle(x1, y1, x2, y2, fill="black", outline = 'orange')
    canvasName.create_line(x1, x1, x2, y2, fill="red")
    canvasName.create_line(x1, y1, x2, y2, fill="purple")


create_grid(myCanvas)
while True:
    x = input("entrez l'abcisses de la case: ")
    y = input("entrez l'ordonnée de la case: ")
    create_mine(x, y, myCanvas)
    #add_flag(3, 8, myCanvas)
    root.mainloop()