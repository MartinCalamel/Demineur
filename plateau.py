from case import Case
from random import randint

class Plateau:
    def __init__(self, level):
        self.level_config = [10,20,50,1000]
        self.level : int = level
        self.tableau : list = self.initialise_tableau(self.level)
        self.affichage : list = self.get_affichage()
        self.fist_click = False
    
    def initialise_tableau(self,level):
        nb_case = self.level_config[level]
        tableau = [[Case(i, j) for j in range(nb_case)] for i in range(nb_case)]
        return tableau
    
    def place_bombe(self,coord):
        nb_case = self.level_config[self.level]
        for i in range(2):
            x,y = randint(0,nb_case-1),randint(0,nb_case-1)
            while self.tableau[x][y].bombe or coord==(x,y):
                x,y = randint(0,nb_case-1),randint(0,nb_case-1)
            self.tableau[x][y].set_bombe()
    
    def set_value(self):
        nb_case = self.level_config[self.level]
        for i in range(nb_case):
            for j in range(nb_case):
                if not self.tableau[i][j].bombe:
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                            try:
                                if not x == -1 and not y == -1:
                                    if self.tableau[x][y].bombe:
                                        self.tableau[i][j].value+=1
                            except:
                                pass

    def get_affichage(self):
        self.affichage = []
        for i in self.tableau:
            ligne = []
            for j in i:
                if not j.hidden :
                    ligne.append(str(j.value))
                else :
                    ligne.append('x')
            self.affichage.append(ligne)
    
    def __str__(self):
        self.get_affichage()
        texte = ""
        for i in self.affichage:
            texte += str(i) + '\n'
        return texte

if __name__ == '__main__':
    print(Plateau(0))