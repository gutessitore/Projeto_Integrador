import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor

class Models(object):

    def __init__(self):
        pass

class MultiLayerPerceptron(Models):

    def __init__(self):
        super().__init__()

        self.search_space = {
            'num_layer': [1, 20],
            'hidden_layer_sizes': [100, 200],
            'alpha': [1e-4, 1],
            'random_state': [42, 10000],
            'learning_rate_init': [1e-4, 1]
        }

        self.pipeline = Pipeline(
            verbose=True,
            steps=[
                ('scale', MinMaxScaler()),
                ('Mlp', MLPRegressor(
                    verbose=False,
                    early_stopping=True,
                    n_iter_no_change=100,
                    learning_rate='constant',
                    max_iter=2000,
                    tol=1e-5
                )
                 ),
            ]
        )