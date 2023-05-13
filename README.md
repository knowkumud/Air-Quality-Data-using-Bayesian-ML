# Air-Quality-Data-using-Bayesian-ML
#1 Implement Inverse CDF sampling for the Fréchet distribution. With sufficient number of samples, plot the kernel density estimation plot and show that you are able to match the PDF. Also, reproduce the following figure and visualize it:
https://en.wikipedia.org/wiki/File:Frechet_pdf.svg

#2 Briefly explain and implement from scratch the following functions: i) cross-entropy; ii) entropy; iii) mutual information; iv) conditional entropy; v) KL divergence. Take appropriate example toy data/distributions and explain the insights from calculating these quantities.

#3 Download a week of PM2.5 dataset from the OpenAQ website for Delhi. Fill in the missing data with appropriate methods. Use i) the sklearn Random Forest regressor; ii) sklearn Linear regression and iii) Gaussian process regressor to interpolate the PM2.5 values across the space. Use all the available features that you can get from the OpenAQ website or elsewhere (e.g., meteorological variables). Compare the results and prepare a table showing the metrics in K-Fold cross-validation setting.

#4 Prepare your own image dataset for binary classification with two classes: Fox v/s Dog. Use an appropriate neural network library (JAX or any other library) and a small CNN (not necessary to use big models like ResNet, or VGG if you do not have the compute power). Use an appropriate active learning algorithm from https://modal-python.readthedocs.io/en/latest/ library and show the active learning iterations v/s test accuracy curve. Explain your insights.

#5 Summarize the following paper within 200 words:
https://arxiv.org/pdf/1906.08158.pdf

#6 Consider a two-mode distribution with a Mixture of Gaussians (both modes should have different heights and locations). Your task is to fit a single Normal distribution to this distribution. Use KL-divergence to minimize the distance between these two distributions. Create an animation that shows the iteration-wise progress as you fit the normal distribution to the two-mode distribution. You have to show this for Forward KL and Reverse KL divergence. Explain your insights about the nature of the fit in each of these cases. You can use https://github.com/tensorflow/probability JAX substrate to do this task.
