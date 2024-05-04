import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importing Tensorflow and Tensorflow Datasets
import tensorflow as tf
import tensorflow_datasets as tfds

# Fetching the parameters of the dataset
ds, info = tfds.load('cats_vs_dogs', split='train', shuffle_files=False, with_info=True, as_supervised=True)
assert isinstance(ds, tf.data.Dataset)

# Displaying the parameters of the dataset as tuple
# For this, we had to set as_supervised = True when loading the dataset
# image.shape in the print statement prints the specifications of the image size
# label in the print statement prints either 0 or 1, 0 signifying cats and 1 signifying dogs

# Taking only the first 100 indices of this dataset for simplicity when it comes to printing and handling data
ds = ds.take(100)

# Prints/displays the parameters for the first hundred data pieces in the dataset
for image, label in ds:
    print(image.shape, label)

# Code that was written to check if there were anomalies; no anomalies were found

# for image, label in ds:
#     if (label != 1 and label != 0): // If the label signified neither a cat or a dog, then it was an anomaly
#         print ("Anomaly found.")

# Upon writing this condition, the output statement was never printed, concluding that no anomalies were found.
# If I had found any anomalies, when writing the dataset to the CSV file, I would have ensured that I include
# a condition which only writes in data with a label of 1 or 0 into the CSV file.

# In order to export the dataset to a CSV file, we will first convert the dataset into a dataframe
# We will then export the dataframe as a CSV file

# Converting the dataset to a dataframe
# Prints the dataframe as well to visualize what is contained
# print(df) prints two columns, one for the rgb values of the photos and the second column for the label (0 or 1)
df = tfds.as_dataframe(ds.take(100), info)
print(df)

# Exporting the dataframe to a CSV file format
# We only export the label of the dataframe as that simplifies the CSV file making it more readable and is the crucial data
from google.colab import files
df.label.to_csv('CatsvsDogs.csv')
files.download('CatsvsDogs.csv')

# Drawing a histogram of the data
# The x-axis has two bars, (1) representing the dogs and (0) representing the cats
# The y-axis has the frequency of these values
df['label'].plot(kind='hist')