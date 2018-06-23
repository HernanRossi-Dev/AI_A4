
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


        sumTrans00 = 0
        sumTrans01 = 0
        sumTrans10 = 0
        sumTrans11 = 0
        sumEmit00 = 0
        sumEmit01 = 0
        sumEmit02 = 0
        sumEmit10 = 0
        sumEmit11 = 0
        sumEmit12 = 0
        sumPredict = 0
        for i in range(0,1000):
            currentState = 0
            emitedEvidence = []
            stateList = []
            for j in range(0, 300):
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
            emitedEvidence = np.reshape(emitedEvidence, (-1,1))
            stateList = np.reshape(stateList, (-1,1))

            # print(model.fit(emitedEvidence, [300]))
            model.fit(emitedEvidence, [300])
            sumTrans00 += model.transmat_[0][0]
            sumTrans01 += model.transmat_[0][1]
            sumTrans10 += model.transmat_[1][0]
            sumTrans11 += model.transmat_[1][1]
            # print(model.transmat_)
            # print(model.emissionprob_)
            sumEmit00 +=model.emissionprob_[0][0]
            sumEmit01 +=model.emissionprob_[0][1]
            sumEmit02 +=model.emissionprob_[0][2]
            sumEmit10 +=model.emissionprob_[1][0]
            sumEmit11 +=model.emissionprob_[1][1]
            sumEmit12 +=model.emissionprob_[1][2]
            emissionPredict = model.predict(emitedEvidence)
            correctPredictions = 0
            for k in range(0, 300):
                if emissionPredict[k] == stateList[k]:
                    correctPredictions +=1

            # print(correctPredictions)
            # print(correctPredictions/300)
            sumPredict += correctPredictions
        totalTrans00 = sumTrans00 / 1000
        totalTrans01 = sumTrans01 / 1000
        totalTrans10 = sumTrans10 / 1000
        totalTrans11 = sumTrans11 / 1000
        print(totalTrans00, totalTrans01)
        print(totalTrans10, totalTrans11)

        totalEmit00 = sumEmit00 / 1000
        totalEmit01 = sumEmit01 / 1000
        totalEmit02 = sumEmit02 / 1000
        totalEmit10 = sumEmit10 / 1000
        totalEmit11 = sumEmit11 / 1000
        totalEmit12 = sumEmit12 / 1000
        print(totalEmit00, totalEmit01,totalEmit02)
        print(totalEmit10, totalEmit11,totalEmit12)



        totalPred = sumPredict / 1000
        percentPred = totalPred / 300
        print(totalPred)
        print(percentPred)
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