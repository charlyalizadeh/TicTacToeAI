
import guiTicTacToe

def actions(state,dim=3):
    return [i for i in range(dim*dim) if state[i]==' ']

def results(state,a,player,dim=3):
    newState = state[:]
    newState[a] = player
    return newState

def isTerminal(state,dim=3):
    #Raws and Columns
    for i in range(dim):
        rawAI = sum(1 for j in range(dim) if state[i*dim+j]=='O')
        rawHuman = sum(1 for j in range(dim) if state[i*dim+j]=='X')
        colAI = sum(1 for j in range(dim) if state[j*dim+i]=='O')
        colHuman = sum(1 for j in range(dim) if state[j*dim+i]=='X')
        if dim in (rawAI,rawHuman,colAI,colHuman):
            return True
    
    #Diag
    diag1AI = sum(1 for i in range(0,dim*dim,dim+1) if state[i]=='O')
    diag1Human = sum(1 for i in range(0,dim*dim,dim+1) if state[i]=='X')
    diag2AI = sum(1 for i in range(dim-1,2*dim+1,dim-1) if state[i]=='O')
    diag2Human = sum(1 for i in range(dim-1,2*dim+1,dim-1) if state[i]=='X')
    if dim in (diag1AI,diag1Human,diag2AI,diag2Human):
        return True

    #Null
    if sum(1 for i in range(dim*dim) if state[i]==' ')==0:
        return True

    return False

def utility(state,dim=3):
    #Raws and Columns
    for i in range(dim):
        rawAI = sum(1 for j in range(dim) if state[i*dim+j]=='O')
        colAI = sum(1 for j in range(dim) if state[j*dim+i]=='O')
        if dim in (rawAI,colAI):
            return 100
        colHuman = sum(1 for j in range(dim) if state[j*dim+i]=='X')
        rawHuman = sum(1 for j in range(dim) if state[i*dim+j]=='X')
        if dim in (rawHuman,colHuman):
            return -100

    
    #Diag
    diag1AI = sum(1 for i in range(0,dim*dim,dim+1) if state[i]=='O')
    diag2AI = sum(1 for i in range(dim-1,2*dim+1,dim-1) if state[i]=='O')
    if dim in (diag1AI,diag2AI):
        return 100

    diag1Human = sum(1 for i in range(0,dim*dim,dim+1) if state[i]=='X')
    diag2Human = sum(1 for i in range(dim-1,2*dim+1,dim-1) if state[i]=='X')
    if dim in (diag1Human,diag2Human):
        return -100

    return 0

def minmax(state,depth,player,alpha,beta,dim=3):
    print('Depth : ',depth)
    if isTerminal(state,dim):
        return utility(state,dim)

    if player == 'O':
        value = -10
        for a in actions(state,dim):
            value = max(value,minmax(results(state,a,'O'),depth + 1,'X',alpha,beta,dim))
            if value>=beta:
                return value
            alpha = max(alpha,value)
        return value
    
    if player == 'X':
        value = 10
        for a in actions(state,dim):
            value = min(value,minmax(results(state,a,'X'),depth + 1,'O',alpha,beta,dim))
            if value<=alpha:
                return value
            beta = min(beta,value)
        return value

def bestMove(state,dim=3):
    depth = 0
    bestMove = -1
    bestValue = -10
    alpha = -100
    beta = 100
    for a in actions(state,dim):
        value = minmax(results(state,a,'O',dim),depth,'X',alpha,beta,dim)
        print('Action : ',a,' Value : ',value)
        if value>bestValue:
            bestValue = value
            bestMove = a
    return bestMove


def modifyState(state,action,gui,dim=3):
    if state[action]==' ':
        state[action]='X'
        gui.display(state,dim)
        if not isTerminal(state):
            state[bestMove(state,dim)] = 'O'
            gui.display(state,dim)
        else:
            gui.quit()


def game(dim = 3,startPlayer = 'X'):
    gui = guiTicTacToe.TicTacToeGUI(dim)
    #state = [' ' for i in range(dim*dim)]
    state = [' ' for i in range(dim*dim)]
    gui.display(state,dim)
    for i in range(dim*dim):
            gui.label[i].bind('<Button-1>',lambda e,a=i:modifyState(state,a,gui,dim))
    gui.mainloop()

game(3)
    
