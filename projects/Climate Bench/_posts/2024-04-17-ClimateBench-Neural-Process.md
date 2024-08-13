---
layout: post
title: "ClimateBench Neural Process"
categories: [projects, ClimateBench]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/CB/NP/
related_posts:
    -
sitemap: false
image: 
---

# ClimateBench Neural Process

The project was done as a further extension upon my [Senior Capstone Project](/projects/dsc/CB/plus/). Which I undertook the challenge due to my interest in the Deep Learning and hybrid models that were used in the project. In my Senior Project I worked on a **Deep Kernel Learning** model which combined the capabilities of a **Gaussian Process** with a **Neural Network** forming a more complex and improved model. However, there are many limitations to the model, such as it's limited ability to incorporate the spatial and temporal dependencies of the climate data. This is where a **Neural Process** comes in, which is a model instead takes and blends ideas from neural networks and Gaussian processes.

## Neural Process still in development

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/ClimateBenchNPs" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\NPs\github.png" alt="Image of Website"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\ClimateBench\NPs/report.pdf" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\ClimateBench\NPs\report.png" alt="Report Preview"><p>ClimateBench Plus Report</p></div>
    </a>
</div>
</div>

## Conclusion
Although as of writing this conclusion the project is still incomplete, and following the incomplete report there is much that still needs to be completed. For example, I am trying to implement 3 variations of the Neural Process, which are the **Base Neural Process** which takes in a sparse representation of the climate data, the **Convolutional Neural Process** which takes in a spatial representation of the climate data using a CNN to extract features from the data and finally a **Spherical Convolutional Neural Process** which takes in a spatial representation of the climate data using a spherical CNN with the hopes to have the model understand the spherical nature of the Earth and the climate data. All of these models are still in development and I hope to have them completed soon.

