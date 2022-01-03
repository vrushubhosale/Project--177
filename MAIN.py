from tkinter import *
from PIL import ImageTk , Image
from tkinter import ttk

root = Tk()
root.title("V Drinks")
root.geometry("800x600")

class juice:
    def __init__(self, fruit_name, quantity):
       self.fruit = fruit_name
       self.quantity = quantity
       self.__cost = 250
        
    def _calculatecost(self):
        total_cost = self.quantity * self.__cost
        print("You have to pay : ""$"+str(total_cost))
        if(self.fruit == "Apple"):
          calorie = self.quantity * 52
        elif (self.fruit == "Mango"):
          calorie  = self.quantity * 60
        elif(self.fruit == "Orange"):
          calorie = self.quantity * 47
        print("x"+str(self.quantity)+ " = "+str(calorie))
        
    def getCost(self):
        self._calculatecost()
        
def orderJuice():
   fruit = "orange"
   quantity = 200
   obj1 = juice(fruit,quantity)
   obj1.getCost()
    
btn = Button(root, text="TOTAL", command=orderJuice())
btn.place(relx=0.95, rely=0.5, anchor= E)

root.mainloop()