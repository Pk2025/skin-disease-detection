#  Skin Disease Detection using Deep Learning

##  Project Overview

This project is a **web-based application** that detects skin diseases using deep learning models. Users can upload an image of a skin condition, and the system predicts the possible disease along with relevant information.

The goal of this project is to assist in **early detection of skin diseases** using AI-powered image classification.

---

##  Features

* Upload skin images through a web interface
* Predict skin diseases using trained deep learning models
* Fast and user-friendly interface using Flask
* Modular and clean backend structure

---

##  Tech Stack

* **Programming Language:** Python
* **Framework:** Flask
* **Deep Learning Models:** ResNet50, VGG16
* **Libraries:** TensorFlow / Keras, PyTorch, OpenCV
* **Frontend:** HTML, CSS

---

 ## Model Details
 ResNet50
A deep convolutional neural network with skip connections
Helps in solving vanishing gradient problems
Provides high accuracy for image classification tasks
 VGG16
A simple and powerful CNN architecture
Uses small convolution filters (3x3)
Effective for feature extraction in medical images



## Images 
<img width="714" height="576" alt="image" src="https://github.com/user-attachments/assets/dd2b2673-5d92-4577-a172-9828f464d88a" />
<img width="586" height="455" alt="image" src="https://github.com/user-attachments/assets/42b3316e-e561-42bf-9752-c23c913c2cba" />
<img width="851" height="650" alt="image" src="https://github.com/user-attachments/assets/cd5a9734-7fd6-4f66-9f5b-5e76930fc374" />
<img width="645" height="559" alt="image" src="https://github.com/user-attachments/assets/fd4f94b8-d0b0-4fe1-b9a5-f09c5f4b127f" />
<img width="1042" height="411" alt="image" src="https://github.com/user-attachments/assets/8fb88931-ebf5-4c61-9fa5-0deb731088f7" />
<img width="842" height="643" alt="image" src="https://github.com/user-attachments/assets/a5f8e839-31cc-4718-8e52-207b80f76c24" />
<img width="500" height="534" alt="image" src="https://github.com/user-attachments/assets/1c67dcb5-c5e1-4d51-9b77-a4e64b4f4f77" />
<img width="581" height="529" alt="image" src="https://github.com/user-attachments/assets/cae632df-c13c-45bf-bc3f-c2454abf6d9a" />








###  ResNet50

* A deep convolutional neural network with skip connections
* Helps in solving vanishing gradient problems
* Provides high accuracy for image classification tasks

###  VGG16

* A simple and powerful CNN architecture
* Uses small convolution filters (3x3)
* Effective for feature extraction in medical images

---

##  How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Pk2025/skin-disease-detection.git
cd skin-disease-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
skin-disease-detection/
│── app.py
│── utils.py
│── requirements.txt
│── static/
│   └── styles.css
│── templates/
│   └── index.html
│── models/   (excluded from repository)
```

---

##  Note on Model Files

Model files are not included in this repository due to GitHub file size limitations.




## 🎯 Future Improvements

* Add more skin disease categories
* Improve model accuracy with larger datasets
* Deploy the application online (AWS / Render / Heroku)
* Add user authentication system

---

## 👨‍💻 Author

**Parth Karande**

---

## ⭐ Acknowledgment

This project is developed as part of a deep learning application to solve real-world healthcare problems.
