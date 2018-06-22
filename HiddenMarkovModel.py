from RandomVariable import Random_Variable
import matplotlib.pyplot as plt
from scipy import stats
import random
import numpy as np
from hmmlearn import hmm

class HiddenMarkovModel:
    def __init__(self):
        print('Starting Hidden Markov Model')
        transitionMatrix = np.array([[0.3, 0.7], [0.5, 0.5]])

        state2color = {}
        state2color['H'] = 'green'
        state2color['I'] = 'red'
        samplesMarkov = self.markov_chain(transitionMatrix, 0, [0, 1], 300)
        print(samplesMarkov)
        emitedEvidence =[]
        for state in samplesMarkov:
            if state == 0:
                evidenceRandomNumber = random.random()
                if evidenceRandomNumber < 0.7:
                    emitedEvidence.append( 2)
                elif evidenceRandomNumber < 0.8:
                    emitedEvidence.append( 1)
                else:
                    emitedEvidence.append( 0)
            else:
                evidenceRandomNumber = random.random()
                if evidenceRandomNumber < 0.6:
                    emitedEvidence.append( 1)
                elif evidenceRandomNumber < 0.9:
                    emitedEvidence.append( 0)
                else:
                    emitedEvidence.append( 2)
        model = hmm.MultinomialHMM(n_components=2)
        emitedEvidence = np.reshape(emitedEvidence, (-1, 1))
        # print(emitedEvidence)
        print(model.fit(emitedEvidence, [300]))
        print(model.transmat_)
        print(model.emissionprob_)

    def markov_chain(self, transitionMatrix, state, state_names, samples):
        (rows, cols) = transitionMatrix.shape
        rvs = []
        values = list(np.arange(0, rows))

        # create random variables for each row of transition matrix
        for r in range(rows):
            rv = Random_Variable("row" + str(r), values, transitionMatrix[r])
            rvs.append(rv)
        # start from initial state and then sample the appropriate
        # random variable based on the state following the transitions
        states = []
        for n in range(samples):
            state = rvs[state].sample(1)[0]
            states.append(state_names[state])
        return states


    def plot_player_samples(self, samples, state2color):
        colors = [state2color[x] for x in samples]
        x = np.arange(0, len(colors))
        y = np.ones(len(colors))
        plt.figure(figsize=(10, 1))
        plt.bar(x, y, color=colors, width=1)

startMarkov = HiddenMarkovModel()
