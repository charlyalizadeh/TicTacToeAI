import guiGrid

class TicTacToeGUI(guiGrid.GuiGrid):
    def __init__(self, dim = 3,stateAI = 'O',stateHuman = 'X',stateNull = ' '):
        guiGrid.GuiGrid.__init__(self,dim,dim,'500x500')
        self.imageAI = guiGrid.tk.PhotoImage(file='gameImages/circle.gif')
        self.imagePlayer = guiGrid.tk.PhotoImage(file='gameImages/cross.gif')
        self.stateAI = stateAI
        self.stateHuman = stateHuman
        self.stateNull = stateNull




    def display(self,state,dim):
        self.clear()
        for i in range(dim*dim):
            if(state[i] == self.stateNull):
                self.label[i]['image'] = ''
            elif(state[i] == self.stateAI):
                self.label[i]['image'] = self.imageAI
            elif(state[i] == self.stateHuman):
                self.label[i]['image'] = self.imagePlayer
        self.update()




                
   
       
