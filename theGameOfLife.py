import tkinter as tk
from random import randint
t=[[randint(0,1) for i in range(15)]for j in range(10)]
m=t.copy()

root = tk.Tk()
root.title("Game of life")
root.geometry("330x210")

# game of life function with 2 arrays for the n step and n+1 step
def Gof(t,nbEtapes):
    s=0
    for l in range(nbSteps):
        for i in range(len(t)):
            for j in range(len(t[0])):
                for k in range(-1,2,1):
                    for x in range(-1,2,1):
                        if i+k < 0 or j+x < 0 or i+k >= 10 or j+x >= 15 or (k == 0 and x == 0):
                            s+=0
                        else :
                            s+=t[i+k][j+x]
                if s >=4:
                    m[i][j] = 0
                elif s <= 1:
                    m[i][j] = 0
                elif s == 3:
                    m[i][j] = 1
                s=0
        t=m.copy()
#printing the array in tkinter
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == 1:
                    x = "⬛"
                else :
                    x = "⬜"
                l1 = tk.Label(root, text=x)
                l1.grid(row=i, column=j)
        root.after(50, root.update())


nbSteps = 100
Gof(t,nbSteps)
root.mainloop()
