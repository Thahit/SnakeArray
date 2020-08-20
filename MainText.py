from func_timeout import FunctionTimedOut, func_timeout  #pip install func_timeout
from random import randint

def finder(list, value): # find index in 2d array
    return next((i, j) for i, l in enumerate(list)
                for j, x in enumerate(l) if x == value)

class ground:
    def __init__(self, dif):
        self._score = 0
        self.dif=dif
        # defining difficulty levels
        if dif == "1":
            self._len = 10
            self._field = [[0] * self._len for i in range(self._len)]
            self._speed=4

        elif dif == "2":
            self._len = 9
            self._field =a = [[0] * self._len for i in range(self._len)]
            self._speed = 3

        else:
            self._len = 8
            self._field = [[0] * self._len for i in range(self._len)]
            self._speed = 2

        self._field[3][3] = "8"  # =player head
        self._loc=(3,3)

    def see(self):# showing the playing field
        print("Score: ", self._score, "\tDifficulty:", self.dif)
        for r in self._field:
            row=""
            for el in r:
                row=row+str(el) +"\t" # if i printed the array, the field would be uggly as different chars have different sizes
            print(row)

    def newPoint(self): # replacing the food, if eaten or  new game
        pointloc = (randint(0, self._len - 1), randint(0, self._len - 1))
        while self._field[pointloc[0]][pointloc[1]] !=0:
            pointloc = (randint(0, self._len - 1), randint(0, self._len - 1))
        self._field[pointloc[0]][pointloc[1]] =1

    def lose(self):
        print("you lost. Your score is: ", self._score)
        self._alive=False

    def move(self, way):
        if way == "w":
            if self._loc[0]-1 <0:  #out of array
                self.lose()
            elif type(self._field[self._loc[0]-1][self._loc[1]])==str: #biting tail
                self.lose()
            elif self._field[self._loc[0]-1][self._loc[1]]==1: #finding food
                self._score+=1
                self._field[self._loc[0] - 1][self._loc[1]]="8"
                self._field[self._loc[0] ][self._loc[1]]=chr(self._score +64)
                self._loc=(self._loc[0]-1, self._loc[1])
                self.newPoint()
            else:
                self._field[self._loc[0] - 1][self._loc[1]] = "8"
                if self._score > 0:
                    self._field[self._loc[0]][self._loc[1]] = chr(self._score + 65)
                    for i in range(self._score + 1):
                        l = finder(self._field, chr(i + 65))
                        if i > 0:
                            self._field[l[0]][l[1]] = chr(i + 64)
                        else:
                            self._field[l[0]][l[1]] = 0
                else:
                    self._field[self._loc[0] ][self._loc[1]] = 0
                self._loc = (self._loc[0] - 1, self._loc[1])

        if way == "a":
            if self._loc[1]-1 <0:  #out of array
                self.lose()
            elif type(self._field[self._loc[0]][self._loc[1]-1])==str: #biting tail
                self.lose()
            elif self._field[self._loc[0]][self._loc[1]-1]==1: #finding food
                self._score+=1
                self._field[self._loc[0] ][self._loc[1]-1]="8"
                self._field[self._loc[0] ][self._loc[1]]=chr(self._score +64)
                self._loc=(self._loc[0], self._loc[1]-1)
                self.newPoint()
            else:
                self._field[self._loc[0] ][self._loc[1]-1] = "8"
                if self._score > 0:
                    self._field[self._loc[0]][self._loc[1]] = chr(self._score + 65)
                    for i in range(self._score + 1):
                        l = finder(self._field, chr(i + 65))
                        if i > 0:
                            self._field[l[0]][l[1]] = chr(i + 64)
                        else:
                            self._field[l[0]][l[1]] = 0
                else:
                    self._field[self._loc[0] ][self._loc[1]] = 0

                self._loc = (self._loc[0] , self._loc[1]-1)

        if way == "d":
            if self._loc[1]+1 <0:  #out of array
                self.lose()
            elif type(self._field[self._loc[0]][self._loc[1]+1])==str: #biting tail
                self.lose()
            elif self._field[self._loc[0]][self._loc[1]+1]==1: #finding food
                self._score+=1
                self._field[self._loc[0] ][self._loc[1]+1]="8"
                self._field[self._loc[0] ][self._loc[1]]=chr(self._score +64)
                self._loc=(self._loc[0], self._loc[1]+1)
                self.newPoint()
            else:
                self._field[self._loc[0]][self._loc[1]+1] = "8"
                if self._score > 0:
                    self._field[self._loc[0]][self._loc[1]] = chr(self._score + 65)
                    for i in range(self._score + 1):
                        l = finder(self._field, chr(i + 65))
                        if i > 0:
                            self._field[l[0]][l[1]] = chr(i + 64)
                        else:
                            self._field[l[0]][l[1]] = 0
                else:
                    self._field[self._loc[0] ][self._loc[1]] = 0

                self._loc = (self._loc[0] , self._loc[1]+1)

        if way == "s":
            if self._loc[0]+1 <0:  #out of array
                self.lose()
            elif type(self._field[self._loc[0]+1][self._loc[1]])==str: #biting tail
                self.lose()
            elif self._field[self._loc[0]+1][self._loc[1]]==1: #finding food
                self._score+=1
                self._field[self._loc[0] + 1][self._loc[1]]="8"
                self._field[self._loc[0]][self._loc[1]]=chr(self._score +64)
                self._loc=(self._loc[0]+1, self._loc[1])
                self.newPoint()
            else:
                self._field[self._loc[0] + 1][self._loc[1]] = "8"
                if self._score > 0:
                    self._field[self._loc[0]][self._loc[1]] = chr(self._score + 65)
                    for i in range(self._score + 1):
                        l = finder(self._field, chr(i + 65))
                        if i > 0:
                            self._field[l[0]][l[1]] = chr(i + 64)
                        else:
                            self._field[l[0]][l[1]] = 0
                else:
                    self._field[self._loc[0]][self._loc[1]] = 0
                self._loc = (self._loc[0] + 1, self._loc[1])


    def play(self):
        self._alive=True
        way="w"
        ways=["w", "a", "s", "d"]
        self.newPoint()

        while self._alive==True:
            self.see()
            try:
                a=way
                a = func_timeout(self._speed, lambda: input('Press enter -> direction -> enter\t'))
            except FunctionTimedOut:
                pass
            if a in ways:
                way = a
            else:
                print("no")
            print("Direction=",way)
            self.move(way)

if __name__=="__main__":
    #beginning of game
    print("Attention, you will need to make the output console bigger.")
    a=input("Chose a difficulty level (1-3): ")
    levels=["1", "2", "3"]
    while a not in levels:
        a = input("Your input is invalid. Chose a difficulty level (1-3): ")
    print("You chose difficulty: ", a)
    print("Your character is  \"8\", you play with w,a,s,d and you need to press enter after each input")
    print("Your Tail is letters, the food on the map is \"1\"")

    s=ground(a)
    s.play()