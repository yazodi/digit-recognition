---
license: mit
tags:
  - digit-recognition
  - mnist
  - keras
  - tensorflow
  - deep-learning
  - image-classification
  - handwritten-digit
---

# ✍️ El Yazısı Rakam Tanıma (Digit Recognition)

Bu model, **MNIST el yazısı rakam veri seti** ile eğitilmiş bir derin öğrenme modelidir. Kullanıcının çizdiği veya yüklediği 28x28 boyutundaki görüntülerden **0-9 arasındaki rakamları tanımak** için kullanılır.

---

## 🧠 Model Özeti

- **Model Türü**: CNN (Convolutional Neural Network)
- **Veri Kümesi**: MNIST (60.000 eğitim / 10.000 test)
- **Giriş Boyutu**: `(28, 28, 1)`
- **Çıkış**: 10 sınıf (rakamlar 0-9)
- **Kütüphaneler**: TensorFlow / Keras

---

## 🔍 Kullanım

### Python ile yükleme:
```python
from keras.models import load_model

model = load_model("digit_model.keras")


https://huggingface.co/yazodi/digit-recognition