import torch
from torchvision import transforms
import numpy as np
from PIL import Image
import tensorflow as tf

# Define your class names (based on dataset labels)
class_names = [
    "Acne", "Eczema", "Melanoma", "Psoriasis",
    "Rosacea", "Warts", "Healthy"
]

# TensorFlow preprocessing
def preprocess_image_tf(image: Image.Image):
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.vgg16.preprocess_input(img_array)
    return img_array

# PyTorch preprocessing
def preprocess_image_torch(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    img = transform(image).unsqueeze(0)
    return img
