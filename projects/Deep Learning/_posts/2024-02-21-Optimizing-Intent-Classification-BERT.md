---
layout: post
title: "Intent Classification using Hugging Face and BERT"
categories: [projects, Deep Learning]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/DeepLearning/IntentClassification/BERT/
related_posts:
    -
sitemap: false
# image: \assets\projects\ClimateBench\Plus\home.png
---

# Intent Classification using Hugging Face and BERT
Intent Classification is a classic task in Natural Language Processing (NLP) where the goal is to classify the intent of a user's input. This is useful in many applications such as chatbots, virtual assistants, and search engines. In this project, we will be using the Hugging Face Transformers library to fine-tune a pre-trained BERT model on the Amazon massive Intent Classification dataset.

## Data
The dataset we are using is the Amazon massive Intent Classification dataset which contains 16.5 thousand training points which are already split into training set, validation set and test set. 

> The dataset can be found [here.](https://huggingface.co/datasets/mteb/amazon_massive_intent/viewer/en/train)

## BERT
With the recent boom with transformer due to their parallelization capabilities and their ability to capture long-range dependencies. There have been many nice transformers being develop daily, but for this project we are focused on BERT (Bidirectional Encoder Representations from Transformers) which is a transformer model that was developed by Google. The base model for BERT is trained on the Toronto Book Corpus and Wikipedia, and the specific variant of the model we are using is the `bert-base-uncased` which is a smaller version of the original BERT model that is trained on lower-cased text and is suitable for intents classification.

> More on the BERT model can be found [here.](https://huggingface.co/transformers/model_doc/bert.html)

## Models
We trained 5 total models to gauge the performance of the BERT model on the Amazon massive Intent Classification dataset, the models are:

1. Baseline Model - BERT model with no fine-tuning achiving an accuracy of 0.0148
2. Custom Tuned Model - Included Warmup Scheduler and re-initialized some of the layers of the BERT model, achieving an accuracy of 0.8675
3. SupContrast Model - Used the Supervised Contrastive Loss function to train the model, achieving an accuracy of 0.8141.
4. SLIMCLR Model - Used the SLIMCLR loss function to train the model, achieving an accuracy of 0.8773.

## Deliverables
For a more in-depth look at the project, you can download the project below, and you can also view the code by clicking the image below.


<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/Intent-Classification-with-BERT/tree/main" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Intent-Classification-with-BERT\github.png" alt="Preview of Github"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\Deep-Learning\Character-Level-Music-Generator\report.pdf" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Intent-Classification-with-BERT\report.png" alt="Preview Image of report"><p>Report</p></div>
    </a>
</div>
</div>





























