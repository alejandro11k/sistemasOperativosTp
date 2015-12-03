
from enum import Enum

class ProcessStates(Enum):
    #processNew = 1
    processReady = 2
    processRunning = 3
    processWaiting = 4
    #processTermanited = 5
    processRunningIO = 6