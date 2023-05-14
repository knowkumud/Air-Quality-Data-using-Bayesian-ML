| Task Name     | Status        | Link        
| ------------- | ------------- | --------    |
| 1-Implemetation of Inverse CDF for Frechet distribution         | Attempted       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1SDq4D2DdW1u6WrG4Da5GmdaT_gErTol_?usp=sharing)

   |
| 2-Implement Entropy & terms         | Attempted       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ocWGpnbGnhPWZejMIs6RJnl3eLr-8hmH?usp=sharing)
   |
| 3-AQI Data of Delhi  | Attempted, partial output |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16Cc2EYT4sYoOC8w-XbjcnpuFfy_IxagV?usp=sharing)    |
| 4-Image Classification of Fox v/s Dog   |  Attempted  |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DnteSNhNQTytM7_vjlQGbvObWrS74Pxx?usp=sharing)      |
| 5-Summary of the Research Paper | Attempted | [Question 5.md](https://github.com/knowkumud/Air-Quality-Data-using-Bayesian-ML/blob/main/Question%205.md)           |
| 6-Two-mode distribution with a Mixture of Gaussian | Attempted |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KVTqbyU-aEKDHhqjz7CQe6R_kkkmlu5x?usp=sharing)      |
| 7-Kumarswamy Distribution | Read, not attempted |    N/A    |

# Air-Quality-Data-using-Bayesian-ML
#1 Implement Inverse CDF sampling for the Fréchet distribution. With sufficient number of samples, plot the kernel density estimation plot and show that you are able to match the PDF. Also, reproduce the following figure and visualize it

#2 Briefly explain and implement from scratch the following functions: i) cross-entropy; ii) entropy; iii) mutual information; iv) conditional entropy; v) KL divergence. Take appropriate example toy data/distributions and explain the insights from calculating these quantities.

#3 Download a week of PM2.5 dataset from the OpenAQ website for Delhi. Fill in the missing data with appropriate methods. Use i) the sklearn Random Forest regressor; ii) sklearn Linear regression and iii) Gaussian process regressor to interpolate the PM2.5 values across the space. Use all the available features that you can get from the OpenAQ website or elsewhere (e.g., meteorological variables). Compare the results and prepare a table showing the metrics in K-Fold cross-validation setting.
The dataset is named as measurement_8118


#4 Prepare your own image dataset for binary classification with two classes: Fox v/s Dog. Use an appropriate neural network library (JAX or any other library) and a small CNN 


#5 Summarize the following paper within 200 words:https://arxiv.org/pdf/1906.08158.pdf

#6 Consider a two-mode distribution with a Mixture of Gaussians (both modes should have different heights and locations). Your task is to fit a single Normal distribution to this distribution. Use KL-divergence to minimize the distance between these two distributions. Create an animation that shows the iteration-wise progress as you fit the normal distribution to the two-mode distribution.





**References**
	
	https://seeing-theory.brown.edu/
	https://www.mdpi.com/2073-8994/13/4/572
	https://towardsdatascience.com/entropy-cross-entropy-and-kl-divergence-explained-b09cdae917a
	https://tungmphung.com/information-theory-concepts-entropy-mutual-information-kl-divergence-and-more/
	https://towardsdatascience.com/10-minutes-to-building-a-cnn-binary-image-classifier-in-tensorflow-4e216b2034aa
