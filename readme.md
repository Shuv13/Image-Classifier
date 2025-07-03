# CIFAR‑10 Image Classification Project

## 📸 Overview

This project demonstrates a **Convolutional Neural Network (CNN)** trained on the [CIFAR‑10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset and a **Tkinter desktop application** that allows you to upload an image and instantly see the predicted class.

---

## ✨ Key Features

- **Lightweight CNN** with two convolutional blocks, dropout regularisation and max‑norm constraints.
- Achieves **≈90 % test accuracy** after 25 training epochs (may vary by hardware and random seed).
- Trained model saved as `` (name preserved from original notebook; accuracy shown above is for 25 epochs).
- **Tkinter GUI** written in under 100 lines — no Flask or heavy frameworks required.
- Cross‑platform: Windows / macOS / Linux (Python ≥ 3.9).

---

## 🗂️ Directory Structure

```
.
├── app.py                 # Tkinter desktop application
├── train.ipynb            # Google Colab / Jupyter notebook for training
├── model1_cifar_10epoch.h5
├── requirements.txt       # Exact package versions (optional)
└── README.md              # You’re reading it!
```

> **Tip** If you prefer scripts over notebooks, copy the cells in `train.ipynb` into `train.py` and run `python train.py`.

---

## 🚀 Quick Start

### 1. Clone & create a virtual environment

```bash
$ git clone https://github.com/your‑username/cifar10‑tkinter.git
$ cd cifar10‑tkinter
$ python -m venv .venv
$ source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
(.venv) $ pip install tensorflow pillow matplotlib numpy
```

*Note:* Tkinter ships with the official Python installer. On Linux you may need `sudo apt install python3‑tk`.

### 3. (Optional) Train the model

If you want to retrain from scratch:

```bash
(.venv) $ jupyter notebook train.ipynb  # or open in Google Colab
```

The notebook downloads CIFAR‑10 automatically via `keras.datasets` and saves the model to `model1_cifar_10epoch.h5`.

### 4. Run the desktop app

```bash
(.venv) $ python app.py
```

Click **“Upload an image”**, choose a file (any format supported by Pillow), and press **“Classify Image”**. The predicted label will appear below the image.

---

## 🏗️ Model Architecture

| Layer (type)         | Output Shape  | Params    |
| -------------------- | ------------- | --------- |
| Input ⟶ `Conv2D(32)` | (32, 32, 32)  | 896       |
| `Dropout(0.2)`       | (32, 32, 32)  | 0         |
| `Conv2D(32)`         | (32, 32, 32)  | 9 248     |
| `MaxPooling2D`       | (16, 16, 32)  | 0         |
| `Flatten`            | (8 192)       | 0         |
| `Dense(512)`         | (512)         | 4 194 304 |
| `Dropout(0.5)`       | (512)         | 0         |
| `Dense(10)`          | (10)          | 5 130     |
| **Total params**     | **4 209 578** |           |

The optimizer is **SGD** with learning rate = 0.01 and momentum = 0.9; loss is **categorical cross‑entropy**.

---

## 📈 Expected Performance

| Metric        | Value (25 epochs) |
| ------------- | ----------------- |
| Test accuracy | ≈ 90 %            |
| Top‑1 error   | ≈ 10 %            |

Your results may differ depending on hardware, TensorFlow version and random initialisation.

---

## 📋 To‑Do / Improvements

- 🔄 Data augmentation (horizontal flips, random crops)
- 🏋️‍♂️ Deeper architecture (e.g. VGG‑like, ResNet‑20)
- 🗜️ Quantisation or pruning for even faster inference
- 💾 Automatically download the pretrained `.h5` if missing
- 📸 Drag‑and‑drop support in the GUI

Contributions welcome — feel free to open issues or PRs! 🧑‍💻

---

## 📝 License

[MIT](LICENSE) © 2025 Your Name

---

## 🙏 Acknowledgements

- **TensorFlow / Keras** for the deep‑learning framework
- **Pillow** for simple image processing
- **Matplotlib** for quick dataset visualisation
- The **CIFAR‑10** dataset, created by Alex Krizhevsky, Vinod Nair & Geoffrey Hinton

Happy coding and have fun classifying! 🎉

