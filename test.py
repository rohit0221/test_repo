# create some random code using tensor flow

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a simple dataset


x = np.linspace(-10, 10, 100)
y = np.sin(x) + 0.1 * np.random.normal(size=x.shape)

# Define a simple linear model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model