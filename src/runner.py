
from typing import Callable, NewType, Any
Running = NewType('Running',bool)

bothExist = lambda a,b : True if a and b else False

class GameRunner:
    gameState = None
    gameLogic = None

    def __init__(self,gameState,gameLogic,*args) -> Any:
        self.gameState = gameState
        self.gameLogic = gameLogic

    def startGame(self):
        if bothExist(gameState,gameLogic):
                 while self.gameLogic(self.gameState): #Infinite Loop, can be stopped by the gameLogic
                     ...





