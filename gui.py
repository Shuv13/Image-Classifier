import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import sys
import os
from keras.models import load_model

# ---------------- Fix encoding for VS Code terminal on Windows ----------------
if os.name == 'nt':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
# -----------------------------------------------------------------------------

# Load the trained model
model = load_model('model1_cifar_10epoch.h5')

# CIFAR‑10 class names
classes = {
    0: 'aeroplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer',
    5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'
}

# Initialize GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Image Classification – CIFAR‑10')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    image = Image.open(file_path).resize((32, 32))
    image = np.array(image).astype('float32') / 255.0
    image = np.expand_dims(image, axis=0)

    pred = model.predict(image, verbose=0)  # Suppress Keras output
    class_index = int(np.argmax(pred, axis=1)[0])
    sign = classes[class_index]

    # Safe print for VS Code terminal
    print("Predicted class:", sign.encode('utf-8', errors='replace').decode())

    label.configure(foreground='#011638', text=sign)

def show_classify_button(file_path):
    Button(top, text="Classify Image", command=lambda: classify(file_path),
           padx=10, pady=5,
           background='#364156', foreground='white',
           font=('arial', 10, 'bold')
          ).place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail((top.winfo_width() / 2.25,
                            top.winfo_height() / 2.25))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except Exception as e:
        print("Error:", str(e))

# Upload button
Button(top, text="Upload an image", command=upload_image,
       padx=10, pady=5,
       background='#364156', foreground='white',
       font=('arial', 10, 'bold')
      ).pack(side=BOTTOM, pady=50)

sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

heading = Label(top, text="Image Classification – CIFAR‑10",
                pady=20, font=('arial', 20, 'bold'),
                background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
