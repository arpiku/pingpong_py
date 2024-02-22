import numpy as np
from typing import NewType,Callable


SizeT = NewType('SizeT',int)
isPositive = lambda a : a > 0;
createCanvas = lambda f,w,h : f(w,h)

class Canvas():
    def __init__(self,canvasWidth: SizeT,canvasHeight: sizeT, canvasCreator:Callable[[SizeT,SizeT],Any]) -> Any: #True if created False otherwise
        if not (isPositive(canvasHeight) and isPositive(canvasWidth)):
            raise ValueError("The canvas size must be positive")
            return None 
        return createCanvas(canvasCreator,canvasWidth,canvasHeight) 

       

    


