---
layout: post
title: "Climate Bench Reproduction"
categories: [projects, ML]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/CB/Reproduction
related_posts:
    -
sitemap: false
# image: /assets/projects/loan-predictions/webapp image.png
---

# Climate Bench Reproduction

For my quarter 1 for my Senior Project at **UCSD** my project group and I created a reproduction of my mentor's ([Duncan Watson-Parris](https://duncanwp.github.io/)) paper [ClimateBench](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021MS002954).

## What is ClimateBench?
Climate Bench is the first benchmarking framework that leverages data from a set of *Coupled Model Intercomparison Projects (CMIPS)*, *AerChemMip* and *Detection-Attrition Model Intercomparison Projects* which are extremely complex simulations performed by the state of the art **Earth Model Systems (EMS)**. In order to create a lighter and more accessible benchmark which can be used for climate research and understanding our climate better. 

### What does ClimateBench do?
Essentially Climate Bench takes the data from the CMIPS, AerChemMip, and DAMIP and creates a benchmarking framework using the simulations to emulate and model the possible scenarios of our climate. As of the reproduction of the paper, the model currently predicts 4 different scenarios, which are the following:

- **Mean Surface Air Temperature (TAS)** 
- **Diurnal Temperature Range (DTR)**
- **Precipitation (PR)**
- **90th percentile of daily precipitation (PR90)**

Some of the readily available data can be found on the [ESFG LLNL Website](https://esgf-node.llnl.gov/projects/esgf-llnl/)
