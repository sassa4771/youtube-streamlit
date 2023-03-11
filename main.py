import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')
st.write('Display Image')

img = Image.open('demo.png')

st.image(img, caption='demo', use_column_width=True)
