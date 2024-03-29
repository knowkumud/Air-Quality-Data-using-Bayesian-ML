﻿BALD is based on mutual information and assigns points based on how well their label informs us about the genuine model parameter distribution.
BatchBALD beats BALD on repeated MNIST with acquisition size 10, although BALD outperforms random acquisition due to replications in the dataset.
While scoring points jointly with BALD can find batches of useful data points, batch acquisition of numerous points with BALD performs badly.  A greedy method that chooses the optimal batch to acquire in linear time and gives an open-source implementation.


To calculate the mutual information between the model predictions and the model parameters, BALD employs an acquisition function. 
BALD overestimates joint mutual information, whereas BatchBALD considers variable overlap.  We can shorten the computations by factoring and taking a sum that can be converted into a matrix product.  We may speed up the procedure even further by doing batch matrix multiplication to compute the joint entropy for different xn and recursively computing P 1:n using P 1:n1 and P n.
BatchBALD retains high performance even with increased acquisition sizes on MNIST and EMNIST and delivers a significant performance boost in the transfer learning situation.
BatchBALD outperforms BALD with acquisition size 10 and comes close to being ideal, but BALD cannot beat random acquisition. It outperforms both random and BALD acquisition and collects a more diverse set of data points.




CINIC-10 is a huge dataset containing data from two independent sources: a transfer learning model that received a 59% mark at 1170 for BatchBALD and 1330 for BALD.
For function evaluations, Bayesian optimization has the drawback of having only one worker. Limiting the number of MC dropout samples and relying on noisy estimates solves the problem.
