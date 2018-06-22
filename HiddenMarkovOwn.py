import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from hmmlearn import hmm
import random

class HiddenMarkov:
    def __init__(self):
        # Healthy = 0, Injured = 1
        self.states = ['Healthy', 'Injured']
        # Dribble = 0, Pass = 1, Shoot=2
        self.evidence = ['Dribble', 'Pass', 'Shoot']
        self.transitionMatrix = [[0.7, 0.3],[0.5, 0.5]]
        self.sensorMatrix = [[0.2, 0.1, 0.7],[0.3, 0.6, 0.1]]
        self.start()

    def start(self):
        currentState = 0
        emitedEvidence = []
        stateList = []
        for i in range(0, 300):
            evidenceRandomNumber = random.random()
            transitionRandomNumber = random.random()
            if currentState == 0:
                stateList.append(currentState)
                if evidenceRandomNumber < 0.7:
                    emitedEvidence.append(2)
                elif evidenceRandomNumber < 0.8:
                    emitedEvidence.append(1)
                else:
                    emitedEvidence.append(0)

                if transitionRandomNumber > 0.7:
                    currentState = 1

            else:
                stateList.append(currentState)
                if evidenceRandomNumber < 0.6:
                    emitedEvidence.append(1)
                elif evidenceRandomNumber < 0.9:
                    emitedEvidence.append(0)
                else:
                    emitedEvidence.append(2)

                if transitionRandomNumber < 0.5:
                    currentState = 0



        model = hmm.MultinomialHMM(n_components=2)
        # print(stateList)
        # print(emitedEvidence)
        emitedEvidence = np.reshape(emitedEvidence, (-1,1))
        stateList = np.reshape(stateList, (-1,1))

        print(model.fit(emitedEvidence, [300]))
        print(model.transmat_)
        print(model.emissionprob_)
        emissionPredict = model.predict(emitedEvidence)
        correctPredictions = 0
        for i in range(0, 300):
            if emissionPredict[i] == stateList[i]:
                correctPredictions +=1

        print(correctPredictions)
        print(correctPredictions/300)

        # transmat = np.array([[0.7, 0.3],
        #                      [0.5, 0.5]])
        #
        # start_prob = np.array([1.0, 0.0])
        #
        # # yellow and red have high probs for sunny
        # # blue and grey have high probs for cloudy
        # emission_probs = np.array([[0.2, 0.1, 0.7],
        #                            [0.3, 0.6, 0.1]])
        #
        # model2 = hmm.MultinomialHMM(n_components=2)
        # model2.startprob_ = start_prob
        # model2.transmat_ = transmat
        # model2.emissionprob_ = emission_probs
        #
        # # sample the model - X is the observed values
        # # and Z is the "hidden" states
        #
        # X, Z = model2.sample(3000)
        # fitmodel = hmm.MultinomialHMM(n_components=2)
        # print(fitmodel.fit(X, [3000]))
        # print(fitmodel.transmat_)
        # print(fitmodel.emissionprob_)
        # predictHmm = fitmodel.predict(X)
        # correctPredictions = 0
        # for i in range(0, 300):
        #     if predictHmm[i] == X[i]:
        #         correctPredictions += 1
        #
        # print(correctPredictions)
        # print(correctPredictions / 300)

startMarkov = HiddenMarkov()


