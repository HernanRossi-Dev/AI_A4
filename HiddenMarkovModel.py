from RandomVariable import Random_Variable
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from hmmlearn import hmm

class HiddenMarkovModel:
    def __init__(self):
        print('Starting Hidden Markov Model')
        transitionMatrix = np.array([[0.7, 0.3], [0.5, 0.5]])

        state2color = {}
        state2color['H'] = 'green'
        state2color['I'] = 'red'
        samplesMarkov = self.markov_chain(transitionMatrix, 0, ['H', 'I'], 300)
        print(samplesMarkov)
        self.plot_player_samples(samplesMarkov, state2color)


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
