from typing import Callable,NewType


class GameState():
    _state = None
    def __init__(self,state):
        self._state = state 

    def getCurrentState(self)->Any:
        return self._state

class GameLogic():
    _gameLogic = None
    def __init__(self,gameLogic):
        self._gameLogic = gameLogic

    def getStateUpdator(self,gameState):
        return self._gameLogic(gameState)





