import tkinter as tk
from tkinter import messagebox
from plateau import Plateau as P

def reveal(i,j):
    plateau.tableau[i][j].hidden = False
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if not x == -1 and not y == -1 and not x >= len(plateau.tableau) and not y >= len(plateau.tableau) and plateau.tableau[x][y].hidden and (plateau.tableau[i][j].value == 0 or plateau.tableau[x][y].value==0):
                reveal(x,y)
def perdu():
    draw_plateau(None)
    for i in plateau.tableau:
        for j in i:
            if j.value == 9:
                canvas.create_rectangle(j.coord[0]*case_size,j.coord[1]*case_size,j.coord[0]*case_size+case_size,j.coord[1]*case_size+case_size,fill='red')
    messagebox.showerror(message="vous avez perdu !")
    fen.destroy()



def reveal_case(event):
    if not plateau.fist_click:
        plateau.place_bombe((event.x//case_size,event.y//case_size))
        plateau.set_value()
        plateau.fist_click = True
    x = int(event.x//case_size)
    y = int(event.y//case_size)
    if plateau.tableau[x][y].value == 9:
        perdu()
    else:
        if not plateau.tableau[x][y].marked:
            reveal(x,y)
            plateau.get_affichage()
            draw_plateau(None)


def draw_plateau(event):
    canvas.delete('all')
    for i in plateau.tableau:
        for j in i:
            if j.hidden and not j.marked:
                canvas.create_rectangle(j.coord[0]*case_size,j.coord[1]*case_size,j.coord[0]*case_size+case_size,j.coord[1]*case_size+case_size,fill='green')
            elif j.marked:
                canvas.create_oval(j.coord[0]*case_size,j.coord[1]*case_size,j.coord[0]*case_size+case_size,j.coord[1]*case_size+case_size,fill='red')
            else:
                canvas.create_text(j.coord[0]*case_size+4,j.coord[1]*case_size,anchor="nw", text=j.value,font=(f'Helvetica {int(case_size*0.7)} bold'))

def drapeau(event):
    x = int(event.x//case_size)
    y = int(event.y//case_size)
    case = plateau.tableau[x][y]
    if case.hidden:
        case.marked = not case.marked
    draw_plateau(None)

plateau = P(0)
case_size = 20
fen = tk.Tk()
fen.geometry(f"{len(plateau.tableau)*20}x{len(plateau.tableau)*20+100}")
fen.title('Demineur')
canvas = tk.Canvas(width=len(plateau.tableau)*20, height=len(plateau.tableau)*20)
canvas.pack(side=tk.BOTTOM)
canvas.bind('<Button-1>', reveal_case)
canvas.bind('<Button-3>',drapeau)
draw_plateau(None)
fen.mainloop()