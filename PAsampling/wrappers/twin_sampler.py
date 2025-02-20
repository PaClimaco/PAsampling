from twinning import twin
import numpy as np

class Twin:
    """
    This class implements the twin function from the Twinning library https://github.com/avkl/twinning.

    Parameters:
    ----------
    r : float
        The ratio parameter for the twin function.
    u1 : int
        The initial point index for the twin function.

    Methods
    -------
    fit(X)
        Fits the twin function to the data X, with shape (n_sample, n_features) and returns the result as a list.
    
 
    Returns:
    --------
    Samples : list
        List of indices representing the selected points using the Twin algorithm.   
    """
    
    def __init__(self, ratio, idx_initial_point):
        self.r = ratio
        self.u1 = idx_initial_point

    def fit(self, X):
        X = np.asarray(X, dtype=np.float64)
        return twin(X, r=self.r, u1=self.u1).tolist()