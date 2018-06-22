from scipy import stats
import numpy as np

class Random_Variable:
    def __init__(self, name, values, probability_distribution):
        self.name = name
        self.values = values
        self.probability_distribution = probability_distribution

        self.type = 'numeric'
        print(self.type)
        self.rv = stats.rv_discrete(name=name, values=(values, probability_distribution))

    def sample(self, size):
        if (self.type == 'numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'):
            numeric_samples = self.rv.rvs(size=size)
            mapped_samples = [self.values[x] for x in numeric_samples]
            return mapped_samples

    def probs(self):
        return self.probability_distribution

    def vals(self):
        print(self.type)
        return self.values
