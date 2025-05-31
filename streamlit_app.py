import streamlit as st
from streamlit_drawable_canvas import st_canvas  # EKLENDİ
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
from keras.models import load_model

# Başlık
st.title("✍️ El Yazısı Rakam Tanıma")
st.write("Lütfen aşağıya bir rakam çizin (0-9).")


model = load_model("digit_model.keras")

# Tuval
canvas = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas"
)
