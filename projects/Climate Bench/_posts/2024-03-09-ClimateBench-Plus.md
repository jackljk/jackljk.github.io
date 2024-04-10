---
layout: post
title: "Climate Bench Plus"
categories: [projectsm ClimateBench]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/CB/plus/
related_posts:
    -
sitemap: false
image: \assets\projects\ClimateBench\Plus\dkl.png
---

# Climate Bench Plus
An extension to my professors ([Duncan Watson-Parris](https://duncanwp.github.io/)) paper [ClimateBench](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021MS002954) which is a benchmarking framework that leverages data from a set of *Coupled Model Intercomparison Projects (CMIPS)*, *AerChemMip* and *Detection-Attrition Model Intercomparison Projects* which are extremely complex simulations performed by the state of the art **Earth Model Systems (EMS)**. In order to create a lighter and more accessible benchmark which can be used for climate research and understanding our climate better. 

The extension to the paper is to improve upon the Baseline model by leveraging more advanced Deep Learning models that build on top of the Baseline models, which are the **Gaussian Process**, **Convoluted Neural Network** and **Random Forest**. The purpose of this extension is to see if the more advanced models can improve upon the Baseline model and lead to better predictions and therefore making our benchmarking framework more accurate and reliable.

This is a part of my Senior Project at **UCSD**, where I worked on 3 different models with 2 other group members. The models that I worked on were the **Gaussian Process** and I improved upon it by building a hybrid model that combined a **Gaussian Process** with a **Neural Network**. 

## Improved models 
As part of the extension of the project, we improeved on the 3 baseline models. As mentioned earlier, I worked on a hybrid model that combined a **Gaussian Process** with a **Neural Network** which is called a **Deep Kernel Learning** model. The hybrid model works by using the descriptive capabilities of the **Neural Network** to learn a feature representation of the data which then gets translated into a kernel function that the **Gaussian Process** can use to make predictions.

The the model which acts as the improvement for the **Convoluted Neural Network** is called a **Physics Informed Neural Network** which essentially improves upon the baseline by implementing physical equations to the model, whcih allows it to understand the physical constraints of the climate, allowing the model to make better more informed decisions and therefore improving the predictions.

Finally we improved upon the **Random Forest** by implementing a **Gradient Boosting** model called **XGBoost** which is a more advanced version of the **Random Forest** model. The **XGBoost** model works by building a series of trees with gradient boosting, which allows the model to make better predictions by learning from the mistakes of the previous trees.

## Deliverables for the Extension
For a more in-depth look at the models and the project as a whole, below is the deliverables from the project. 

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://jackljk.github.io/DSC180B-website/" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\Plus\website.png" alt="Image of Website"><p>Website</p></div>
    </a>
    <a href = "https://github.com/jackljk/ClimateBench-Plus" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\Plus\github.png" alt="Image of Github page"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\ClimateBench\Plus/report.pdf" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\Plus\report.png" alt="Report Preview"><p>ClimateBench Plus Report</p></div>
    </a>
    <a href = "\assets\projects\ClimateBench\Plus/poster.pdf" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\Plus\poster.png" alt="Image of Pster"><p>Poster</p></div>
    </a>
</div>
</div>


> Click the links above to view/download the deliverables from the project.
- For a more in-depth technical look at the project, download the [Report](\assets\projects\ClimateBench\Plus/report.pdf).
- For the code of the project, visit the [Github Repository](https://github.com/jackljk/ClimateBench-Plus).
- For a more visual representation and more high-level overview of the project, visit the [Website](https://jackljk.github.io/DSC180B-website/).
- To view the poster that was used for the poster presentation, download the [Poster](\assets\projects\ClimateBench\Plus/poster.pdf).

## Conclusion
A quick overview of the project, overall, our improved models were able to improve upon the Baseline models by a significant margin. Bringing us ne step closer to creating a more accurate and reliable benchmarking framework for climate research, without the need for cumbersome and hard to use EMS simulations. 
