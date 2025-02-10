class Case:
    def __init__(self, x : int, y : int):
        self.coord : tuple = (x,y)
        self.bombe : bool = False
        self.value : int = 0
        self.hidden : bool = True
        self.marked : bool = False
    def set_bombe(self):
        self.bombe = True
        self.value = 9
    def set_value(self, value):
        self.value = value
    def __str__(self):
        print(self.value)
    