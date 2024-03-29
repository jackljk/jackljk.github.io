---
layout: post
title: "MNIST Classification with Softmax Regression"
categories: [projects, Deep Learning]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/DeepLearning/MNIST/SoftmaxNN/
related_posts:
    -
sitemap: false
image: \assets\projects\Deep-Learning\Softmax-NN-MNIST\MNIST.jpg
---

# MNIST Classification with Softmax Regression


## Introduction
For this project, I implemented a Softmax Regression Neural Network from scratch to classify the MNIST dataset. The MNIST dataset is a dataset of handwritten digits from 0-9, which is a popular dataset used for benchmarking and testing new Machine Learning models. The task was to classify the handwritten digits into their respective classes using a Softmax Regression Neural Network.

> The dataset can be found [here](https://paperswithcode.com/dataset/mnist).

## Softmax Regression
Softmax Regression is a type of Logistic Regression that is used for multi-class classification problems. It is used when the output has more than two classes. The Softmax function is used to convert the raw scores of the model into probabilities. The Softmax function is defined as:

$$
y_k^n = \frac{exp(a_k^n)}{\sum_{k'}a_k^n} \hspace{2em}
a_k^n = w^T_kx^n
$$

where for a given example, $$x^n$$ and c possible classes, the softmax regression, outputs a vector $$y^n$$ where each entry represents a probabliity that a given kth class is predicted. And $$a_k^n$$ is the input to the softmax output layer from the neural network.

## Implementation
Implementing the network from scratch, we only used numpy for matrix computations.

The network includes a stochatic gradient descent in order to improve the training speed which is implemented using the following algorithm,

![Index Page](\assets\projects\Deep-Learning/Softmax-NN-MNIST/SGD.png){:.lead width="800" height="100" loading="lazy"}

where $$E^n$$ is defined as the Error across the average over the number of training examples, and normalizes it as well. It is also known as the softmax cost function

$$
E = - \sum_n \sum_{k=1}^c t_k^n \ln y_k^n
$$

Then the gradient of the cost function to be used in the backpropagation through the network layers is defined below:

$$
-\frac{\partial E^n(w)}{\partial w_{jk}} =  (t_k^n - y_k^n)x^n_{j}
$$

## Results
The best model that we achieved was achieved with the following hyper-parameters with RELU activiations on all the layers

| Hyperparameters |Values      |
|-----------------|:-----------|
| Learning Rate   |0.01        |
| Batch Size  | 128 |
| Epochs | 100 |
| early stop | True | 
| early stop epochs |  3 |
| regularization type | L2 |
| L2 penalty | 0.001 |
|L1 penalty | 0.01 |
| momentum | True|
| momentum gamma | 0.9 |

This model achieved a test set accuracy of 97.59%.

> For a more in-depth overview of the code and results look at the report and code linked below in [deliverables](#deliverables)

## Deliverables
For a more in-depth review of the project download the report below. And the link to the github with the code is also linked below.

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/Neural-Network-with-Softmax-Regression-from-Scratch-on-MNIST" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Softmax-NN-MNIST\github.png" alt="Preview of Github"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\Deep-Learning\Softmax-NN-MNIST\report.pdf" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Softmax-NN-MNIST\report.png" alt="Preview Image of report"><p>Report</p></div>
    </a>
</div>
</div>