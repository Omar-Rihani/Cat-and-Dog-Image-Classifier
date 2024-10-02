# Cat and Dog Image Classifier

## Overview
This project implements a Convolutional Neural Network (CNN) using TensorFlow 2.0 and Keras to classify images of cats and dogs. The model aims to achieve at least 63% accuracy, with extra credit for reaching 70% accuracy.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Installation
To run this project, you will need to have access to Google Colaboratory. No local installation is required.

1. Open [Google Colaboratory](https://colab.research.google.com/).
2. Create a new notebook or upload this project as a Jupyter notebook.

## Dataset
The dataset used in this project is the Cats and Dogs dataset, which consists of images of cats and dogs. The dataset is structured as follows:


The images are downloaded and organized automatically in the project.

## Project Structure
The project consists of the following sections:

- **Cell 1**: Importing required libraries such as TensorFlow, Keras, and Matplotlib.
- **Cell 2**: Downloading the Cats and Dogs dataset and setting key variables such as image dimensions and batch size.
- **Cell 3**: Creating image generators for training, validation, and testing datasets using `ImageDataGenerator`.
- **Cell 4**: Defining a function to plot images and visualizing a few random training images.
- **Cell 5**: Implementing data augmentation for the training dataset to reduce overfitting.
- **Cell 6**: Visualizing augmented images to confirm the transformations.
- **Cell 7**: Building the CNN model architecture using Keras.
- **Cell 8**: Training the model on the training dataset and validating on the validation dataset.
- **Cell 9**: Plotting the training accuracy and loss over epochs for analysis.
- **Cell 10**: Making predictions on the test dataset and visualizing the results.
- **Cell 11**: Final check to confirm predictions and verify performance.

## Usage
1. After copying the code into a new Google Colaboratory notebook, run each cell in order.
2. Monitor the training process through the plotted accuracy and loss graphs.
3. After the training, observe the predictions made on the test dataset.

## Results
The model should achieve at least 63% accuracy, with the possibility of reaching 70% accuracy with fine-tuning and additional epochs.

