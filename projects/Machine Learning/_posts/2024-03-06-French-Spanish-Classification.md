---
layout: post
title: "French and Spanish Words Classification"
categories: [projects, Machine Learning]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/ML/French-Spanish-Classification/
related_posts:
    -
sitemap: false
image: \assets\projects\Machine-Learning\French-Spanish-Classification\home.png
---

# French and Spanish Words Classification
The task was to classify French and Spanish words using Machine Learning, by building the classifier from scratch. The dataset we were given consisted of 1200 words of 600 French words and 600 Spanish words. 

## Model
Given the task, I decided to use a naive bayes approach to classify the words. This is because for the classification task, the features I used were bigrams and trigrams as I noticed that both languages have a different distribution of bigrams and trigrams that are more common in each of the languages. Hence, giving me a probabilistic mindset when solving this problem.

![Model](\assets\projects\Machine-Learning\French-Spanish-Classification\nb.png)

## Results
The model was able to achieve an accuracy of 87% on the test set made from doing a train test split. The code can be downloaded [here](/coding/UCSD/DSC/DSC140A/Homeworks/Downloadables/classifier.py).