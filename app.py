from flask import Flask, render_template, request, jsonify
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import tensorflow as tf
import numpy as np
import os
from utils import preprocess_image_tf, preprocess_image_torch, class_names
from collections import OrderedDict

app = Flask(__name__)

# -----------------------------
# Load TensorFlow (VGG16) model
# -----------------------------
vgg_model_path = "models/vgg16_best_finetuned.keras"
vgg_model = tf.keras.models.load_model(vgg_model_path)

# -----------------------------
# Load PyTorch (ResNet50) model
# -----------------------------
resnet_model_path = "models/resnet50-0676ba61.pth"
num_classes = len(class_names)

# Step 1: Create ResNet50 architecture without pretrained weights
resnet_model = models.resnet50(weights=None)

# Step 2: Replace the fully connected layer for 7 classes
resnet_model.fc = nn.Linear(resnet_model.fc.in_features, num_classes)

# Step 3: Load checkpoint, ignore fc layer to prevent size mismatch
state_dict = torch.load(resnet_model_path, map_location=torch.device('cpu'))
new_state_dict = OrderedDict()
for k, v in state_dict.items():
    if "fc" not in k:  # skip fc layer
        new_state_dict[k] = v

resnet_model.load_state_dict(new_state_dict, strict=False)
resnet_model.eval()

# -----------------------------
# Flask Routes
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    file = request.files['image']
    model_type = request.form.get('model_type', 'vgg16')  # default VGG16

    image = Image.open(file.stream).convert('RGB')

    if model_type == 'vgg16':
        img = preprocess_image_tf(image)
        preds = vgg_model.predict(img)
        pred_idx = np.argmax(preds[0])
    else:
        img = preprocess_image_torch(image)
        with torch.no_grad():
            preds = resnet_model(img)
            pred_idx = torch.argmax(preds, 1).item()

    predicted_label = class_names[pred_idx]
    return jsonify({'disease': predicted_label})

# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
