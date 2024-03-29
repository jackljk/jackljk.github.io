---
layout: post
title: "Semantic Segmentation using Fully Convolutional Networks"
categories: [projects, Deep Learning]
sitemap: false
hide_last_modified: true
permalink: /projects/dsc/DeepLearning/VOC2007/FCN/
related_posts:
    -
sitemap: false
image: \assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\home.png
---

# Semantic Segmentation using Fully Convolutional Networks
Semantic Segmentation is the task of classifying each pixel in an image into a category and is an extremely important task in computer vision as it has many real life uses such as in autonomous driving, medical imaging, and satellite imaging. In this project, my group and I implemented a Fully Convolutional Network (FCN) to perform semantic segmentation on the VOC2007 dataset.

## Dataset 
The PASCAL VOC 2007 dataset is a dataset for object detection, segmentation, and classification. It consists of 20 classes (21 including the backgrond class). It is also pre-split into 2 sets, a training set and a validation set. The dataset can be found [here](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/index.html).

**Example Image from the Dataset**
![Full-width](\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\semantic-segmentation-example.png){:.lead width="800" height="50" loading="lazy}

## Fully Convolutional Networks (FCNs)
To understand FCNs, one should first be introduced to what a Convoluted Neural Network (CNN) is. A CNN is a type of neural network that is used for image classification and object detection. It is made up of convolutional layers and pooling layers which are used to extract only the relevant information from images by applying a filter to the image and then pooling the output to reduce the size of the image. Finally the output is passed through a fully connected layer to classify the image, hence giving us a FCN.

**CNN Visual Representation**
![Full-width](\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\CNN-example.png){:.lead width="800" height="50" loading="lazy}

## Implementation
During the implementation of the FCN, we trained 4 different architectures in order to see which would perform the best on the dataset. The architectures were:

1. Baseline FCN
2. Custom FCN a simplified U-Net
3. A Res-Net Transfer Learning FCN
4. A fully connected U-Net

### Baseline
For the baseline we used a simple architecture which uses convolutions to upsample the image to a size of 512x512 to make the features more prominent, and then we down size it down to the number of classes and classifing the pixels individually.

For some improvements that we made to the baseline, we included a *cosine annealing learning rate*, we also included batch normalizations after each convolutions. In addition to that, we performed data augementation on the dataset to increase effictively giving us more training data, without needing more images. Finaly since looking at [the example above](#dataset) we can see that the background class is the majority class by a lot, which can easily cause the model to predict everything as the background class, so we add a class weight to the loss function to help the model learn the other classes better.

More detailed information on this can be found in the [report](temp)

### Custom FCN
The custom FCN, was out implementation of a simplified U-Net which offers a balance between computational efficiency and segmentation accuracy. It uses a encoder and a decoder to extract features and then upsample the image to the original size. The architecture is as follows:


| Layer           | In Channels | Out Channels | Kernel | Stride | Padding | Activation |
|:-----------|:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|
|    enc conv1       | 3           | 64           | 3      | 1      | 1       | ReLU |
|   enc conv2       | 64          | 128          | 3      | 1      | 1       | ReLU |
|    enc conv3       | 128         | 256          | 3      | 1      | 1       | ReLU |
 |   bottleneck conv | 256         | 512          | 3      | 1      | 1       | ReLU |
 |   dec upconv1     | 512         | 256          | 2      | 2      | 0       | ReLU |
 |   dec conv1       | 256         | 256          | 3      | 1      | 1       | ReLU |
 |   dec upconv2     | 256         | 128          | 2      | 2      | 0       | ReLU |
 |   dec conv2       | 128         | 128          | 3      | 1      | 1       | ReLU |
 |   dec upconv3     | 128         | 64           | 2      | 2      | 0       | ReLU |
 |   dec conv3       | 64          | 64           | 3      | 1      | 1       | ReLU |
 |   final conv      | 64          | 21           | 1      | 1      | 0       | - |
{:.scroll-table}
Simplified U-Net Architecture
{:.figcaption}

### Res-Net Transfer Learning FCN
For this architecture we used a pre-trained Res-Net 50. Which is pre-trained on **ImageNet** to develop a semantic segmentation model. Using Res-Net as a backbone, it serves as a feature extractor which we then append a decoder that upsamples the feature which then classifies the pixels. The architecture is as follows:

|Layer      | In Channels | Out Channels | Kernel | Stride | Padding | Activation |
|:-----------|:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|
|    backbone   | -           | -            | -      | -      | -       | - |
|    conv1      | 2048        | 1024         | 1      | -      | -       | ReLU |
|    conv2      | 1024        | 512          | 1      | -      | -       | ReLU |
|    deconv1    | 512         | 256          | 3      | 2      | 1       | ReLU |
|    deconv2    | 256         | 128          | 3      | 2      | 1       | ReLU |
|    deconv3    | 128         | 64           | 3      | 2      | 1       | ReLU |
|    bn1        | -           | -            | -      | -      | -       | BatchNorm2d |
|    deconv4    | 64          | 64           | 3      | 2      | 1       | ReLU |
|    bn2        | -           | -            | -      | -      | -       | BatchNorm2d |
|    classifier | 64          | 21           | 1      | -      | -       | - |
{:.scroll-table}
Res-Net Transfer Learning FCN Architecture
{:.figcaption}

### Fully Connected U-Net
The U-Net is a popular architecture for semantic segmentation. It is made up of an encoder and a decoder, where the encoder extracts features from the image and the decoder upsamples the image to then classify the pixels. It also implements a crop and copy between the encoder and decoder to help the model learn better. The architecture is as follows:

<div style="max-height: 400px; overflow-y: auto;">
    <table>
        <thead>
            <tr>
                <th>Layer</th>
                <th>In Channels</th>
                <th>Out Channels</th>
                <th>Kernel</th>
                <th>Stride</th>
                <th>Padding</th>
                <th>Activation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Conv11</td>
                <td>3</td>
                <td>64</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>Conv1</td>
                <td>64</td>
                <td>64</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>MaxPool1</td>
                <td>-</td>
                <td>-</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Conv21</td>
                <td>64</td>
                <td>128</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>Conv2</td>
                <td>128</td>
                <td>128</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>MaxPool2</td>
                <td>-</td>
                <td>-</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Conv31</td>
                <td>128</td>
                <td>256</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>Conv3</td>
                <td>256</td>
                <td>256</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>MaxPool3</td>
                <td>-</td>
                <td>-</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Conv41</td>
                <td>256</td>
                <td>512</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>Conv4</td>
                <td>512</td>
                <td>512</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>MaxPool4</td>
                <td>-</td>
                <td>-</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>-</td>
            </tr>
            <tr>
                <td>Bottleneck1</td>
                <td>512</td>
                <td>1024</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>Bottleneck2</td>
                <td>1024</td>
                <td>1024</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>ConvTransposed1</td>
                <td>1024</td>
                <td>512</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv11</td>
                <td>1024</td>
                <td>512</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv12</td>
                <td>512</td>
                <td>512</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>ConvTransposed2</td>
                <td>512</td>
                <td>256</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv21</td>
                <td>512</td>
                <td>256</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv22</td>
                <td>256</td>
                <td>256</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>ConvTransposed3</td>
                <td>256</td>
                <td>128</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv31</td>
                <td>256</td>
                <td>128</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv32</td>
                <td>128</td>
                <td>128</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>ConvTransposed4</td>
                <td>128</td>
                <td>64</td>
                <td>2</td>
                <td>2</td>
                <td>0</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv41</td>
                <td>128</td>
                <td>64</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>upConv42</td>
                <td>64</td>
                <td>64</td>
                <td>3</td>
                <td>1</td>
                <td>1</td>
                <td>ReLU</td>
            </tr>
            <tr>
                <td>softmax</td>
                <td>64</td>
                <td>21</td>
                <td>1</td>
                <td>1</td>
                <td>0</td>
                <td>-</td>
            </tr>
        </tbody>
    </table>
</div>

**Here is a visual representation of the U-Net Architecture:**
![Full-width](\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\U-Net-arch.png){:.lead width="800" height="50" loading="lazy}

## Results
Among the 4 architectures, the Res-Net Transfer Learning FCN performed the best as we were able to train it to segment the images correctly while the others still seemed random after approximately 500 epochs. 

**Example of the Res-Net Transfer Learning FCN's output:**
![Full-width](\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\misc-example.png){:.lead width="800" height="50" loading="lazy}
Example of the Res-Net Transfer Learning FCN's output
{:.figcaption}

## Discussion
The Res-Net Transfer Learning FCN performed the best as it was able to segment the images correctly. The other architectures were not able to segment the images correctly as they seemed random after approximately 500 epochs. This could be due to the fact that the Res-Net Transfer Learning FCN was pre-trained on ImageNet which is a large dataset and hence it was able to learn the features of the images better. Compared to the others where we trained the locally from scratch which could imply that some of the other models did not have enough training to learn properly. For example the U-Net was able to segment and get the shape of the objects but it was not able to get the correct colors of the objects, which could imply that more training is required.

**U-Net's output:**
![half-width](\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\U-net-example.png){:.lead width="400" height="50" loading="lazy}
Image of a bird segmented by the U-Net
{:.figcaption}


## Deliverables
For a more in-depth look at the project, you can download the project below, and you can also view the code by clicking the image below.

<div id = "my-project-cards">
<div id = "project-cards">
    <a href = "https://github.com/jackljk/Semantic-Segementation-VOC2007" class = "project-card" download>
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\github.png" alt="Preview of Github"><p>Code</p></div>
    </a>
    <a href = "\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\report.pdf" class = "project-card">
    <div class = "project-card-border"></div>
    <div class = "project-card-content"><img src="\assets\projects\Deep-Learning\FCN-Semantic-Segmentation-VOC\report.png" alt="Preview Image of report"><p>Report</p></div>
    </a>
</div>
</div>