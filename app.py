import pandas as pd
import streamlit as st
import libreria_funciones as lf

st.title("Proyecto Final UCG")
st.sidebar.title("Parámetros")
st.sidebar.image("python_logo.png")

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

monto= st.number_input("Ingrese monto:" )
interes= st.number_input("Ingrese el interes")
anios= st.number_input ("Ingrese el número de años del préstamo")
numero_pagos= st.number_input ("Ingrese el número de pagos anuales")

cuota = lf.cuota_prestamo (1000, 0.10, 5,12)
st.write(cuota)
