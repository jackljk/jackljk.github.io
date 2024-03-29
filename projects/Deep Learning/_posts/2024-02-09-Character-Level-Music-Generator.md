---
layout: post
title: "Character Level Music Generator Using RNN and LSTM"
categories: [projects, Deep Learning]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/DeepLearning/MusicGen/RNN&LSTM/
related_posts:
    -
sitemap: false
image: \assets\projects\Deep-Learning/Character-Level-Music-Generator/home.png
---

# Character Level Music Generator Using RNN and LSTM
Recurrent Neural Networks (RNN) are a special kind of Neural Network that maintains a state or memory of the previous inputs allowing them to remember important information over a sequence of inputs. This makes them ideal for tasks that require sequential information where the order of the data matters. Long Short-Term Memory (LSTM) networks are a variation of RNNs that fix the issue of vanishing gradients in traditional RNNs that happen due to the backpropagation of errors over many time steps causing the gradients to vanish. Making both RNN and LSTM networks ideal for tasks like music generation where the order of the notes is important.

## Data
The data that we are using is a `.txt` file containing the tunes in **ABC** format. The ABC format is a notation for music that uses ASCII characters to represent music. The data is preprocessed to remove any unwanted characters and to convert the data into a format that can be fed into the model. Each song in the `.txt` file is delimited with a `<start>` tag and an `<end>` tag. This allows the Deep Learning Model to be able to generate music from scratch.

![full-width image](\assets\projects\Deep-Learning\Character-Level-Music-Generator\abc-notation.png){:.lead width="800" height="50" loading="lazy"}
ABC Notation Example
{: .figcaption}

## Model
For a baseline model we used  1 hidden layer for Music Generation, which depending on the config, can be either an RNN or an LSTM layer. Which is then followed by a dropout layer for regularization and a linear output layer. Then to train the model, we implement this technique called teacher forcing, which uses the *True* previous token is used as the next input to the model during training.

Then to make the model generate music, we first need to *prime* the model. This is done by first manually adding the characters in `<start>` to let the model know that it is the start of a sequence, then we can feed the model a random sequence of characters, and from there use the previous outputs as it input to generate the next character, therefore generating music. 

The following is pseudo code for the generating music process:
```python
generated_song = "<start>" # To store generated song

for c in "<start>" # Priming the model
    model.forward(c)
for _ in range(max_len)
    probs = model.forward(last_outputed_char)
    <temperature scale the probs>
    <get highest prob from tprobs>
    generated_song += highest_prob_char
    break when "<end>" is outputted or max len reached
```

## Results
We trained a total of 6 models with varying hyper-parameters, which are the number of neurons in the hidden layer and the dropout rate. Overall, it is hard to validate what the best model is, as we are generating music and there is no clear metric to evaluate the model. However, we are able to listen to the generated music and see if it sounds good or not. Ater testing all the models, we thought that all the models except the baseline produced relatively good music, which are still a little random but was not complete undiscernable noise. We also think that the music generated could be improved with both more training data which would allow the Model to learn a song structure better.

## Demonstration
> Download the following `.txt` file $$\rightarrow$$ [Generated Music Data](\assets\projects\Deep-Learning\Character-Level-Music-Generator\generated-song.txt). Go to this ABC Notation Player $$\rightarrow$$ [ABC Notation Player](https://notabc.app/abc-converter/) and paste the contents of the `.txt` file to listen to the generated music.
{:.lead}

## Deliverables
For a more in-depth look at the project, you can download the project below, and you can also view the code by clicking the image below.

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/Character-Level-Music-Generator" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Character-Level-Music-Generator\github.png" alt="Preview of Github"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\Deep-Learning\Character-Level-Music-Generator\report.pdf" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\Character-Level-Music-Generator\report.png" alt="Preview Image of report"><p>Report</p></div>
    </a>
</div>
</div>