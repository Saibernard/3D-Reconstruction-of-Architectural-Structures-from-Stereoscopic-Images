from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        E_essential_estimate = least_squares_estimation(X1[sample_indices], X2[sample_indices])
        print(E_essential_estimate)

        s3 = np.array([[0,-1,0],[1,0,0],[0,0,0]])
        distance = np.zeros((len(test_indices),1))

        for i in range(len(test_indices)):
            distance[i] = (((X2[test_indices[i]]@E_essential_estimate@X1[test_indices[i]].reshape(-1,1))**2)/(np.linalg.norm(s3@E_essential_estimate@X1[test_indices[i]]))**2) + (((X1[test_indices[i]]@E_essential_estimate.T@X2[test_indices[i]].reshape(-1,1))**2)/(np.linalg.norm(s3@E_essential_estimate.T@X2[test_indices[i]]))**2)

        # print(distance)

        residuals = np.where(distance<eps)
        # print(residuals)
        f = residuals[0]
        if len(f)>0:
            inliers = test_indices[f]
            # print(inliers)

            inliers = np.concatenate((sample_indices, inliers))



        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E_essential_estimate
            best_inliers = inliers


    return best_E, best_inliers