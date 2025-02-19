from sklearn_extra.cluster import KMedoids

class Kmedoids:
    """
    Implements the KMedoids function from the sklearn_extra library (https://scikit-learn-extra.readthedocs.io/en/stable/generated/sklearn_extra.cluster.KMedoids.html).

    This class provides a wrapper around the KMedoids function, allowing for the selection
    of a subset of samples from a dataset based on the k-medoids clustering strategy. The selection
    can be performed using different initialization methods and distance metrics.

    Parameters:
    -----------
    b_samples : int
        The number of samples to select (i.e., the number of clusters).
    init : str, optional (default='k-medoids++')
        The method for initialization. Options are  are 'random', 'heuristic', 'k-medoids++', and 'build'.
    metric : str, optional (default='euclidean')
        The metric to use for computing distances. Options are 'euclidean', 'manhattan', etc.
    random_state : int, optional (default=None)
        The seed used by the random number generator.

    Methods:
    --------
    fit(X):
        Fits the kmedoids function to the data matrix X, with shape (n_samples, n_features), and returns the indices of the selected samples (medoids).
    """
    def __init__(self, b_samples, init='k-medoids++', metric='euclidean', random_state=None,  max_iter=300):
        self.b_samples =b_samples
        self.init = init
        self.metric = metric
        self.random_state = random_state
        self.max_iter = max_iter

    def fit(self, X,):
        self.kmedoids = KMedoids(
                                n_clusters=self.b_samples,
                                init=self.init,
                                metric=self.metric,
                                random_state=self.random_state,
                                max_iter=self.max_iter
                                )
        self.kmedoids.fit(X)
        return self.kmedoids.medoid_indices_