from ..native_functions import  fps_np

class FPS:
    """
    Implements the Farthest Point Sampling (FPS) algorithm.

    This class provides a wrapper around the fps_np function, allowing for the selection
    of a subset of samples from a dataset based on the FPS strategy. The selection can be 
    performed using different distance functions and can handle precomputed distance matrices.

    Attributes:
    -----------
    precomputed_distances : bool, optional (default=False)
        If True, the input X is assumed to be a precomputed distance matrix.

    Methods:
    --------
    fit(X, initial_subset, b_samples, distance_func=None, verbose=False):
        Fits the model to the data X and returns the indices of the selected samples.
        
    Parameters:
    -----------
    X : numpy.ndarray
        Input data matrix, representing a set of data points or precomputed distance matrix.
    initial_subset : list
        List of indices (rows of the input points matrix) representing the initial set of selected elements.
    b_samples : int
        The desired number of points to select.
    distance_func : callable, optional (default=None)
        A function to compute pairwise distances. If None, Euclidean distance is used.
    verbose : bool, optional (default=False)
        If True, progress messages are printed.

    Returns:
    --------
    Samples : list
        List of indices representing the selected points using the FPS algorithm.
    """
    
    def __init__(self, precomputed_distances= False):
        self.precomputed_distances = precomputed_distances

    def fit(self, X, initial_subset, b_samples, distance_func=None, verbose=False):
        return fps_np(X, initial_subset, b=b_samples, distance_func=distance_func, precomputed_distances=self.precomputed_distances, verbose=verbose)
        

