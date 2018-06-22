import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from hmmlearn import hmm
import random

class HiddenMarkov:
    def __init__(self):
        self.states = ['Healthy', 'Injured']
        self.transitionMatrix = [[0.7, 0.3],[0.5, 0.5]]
        self.start()

    def start(self):
        currentState = 'Healthy'
        listOfStates = [currentState]
        for i in range(0, 10):
            if currentState == 'Healthy':
                randomNumber = random.random()
                print(randomNumber)
                transitionStay = self.transitionMatrix[0][0]
                print(transitionStay)
                if randomNumber > transitionStay:
                    currentState = 'Injured'
                    listOfStates.append(currentState)
                else:
                    listOfStates.append(currentState)

            else:
                randomNumber = random.random()
                print(randomNumber)
                transitionStay = self.transitionMatrix[1][0]
                print(transitionStay)
                if randomNumber > transitionStay:
                    currentState = 'Healthy'
                    listOfStates.append(currentState)
                else:
                    listOfStates.append(currentState)
        print(listOfStates)

startMarkov = HiddenMarkov()

