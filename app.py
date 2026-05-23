import pandas as pd
import streamlit as st
import libreria_funciones as lf

st.title("Proyecto Final UCG")
st.sidebar.title("Parámetros")
st.sidebar.image("python_logo.png")

modulo = st.selectbox ("sleccione un módulo", ["Módulo 1", "Módulo 2", "Módulo 3"])

if modulo == "Modulo 1":
    upload_files= st.file_uploader(
        "Upload data", accep_multiple_fiales, type="csv"
    )
    for aupload_file in uploaded_files:
        df= pd.read_csv(upload_file)
    

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

monto= st.number_input("Ingrese monto:", min_value=0, max_value=1000, value=1000)
interes= st.number_input("Ingrese el interes", min_value=0.0, max_value=1.0, value=0.10)
anios= st.number_input ("Ingrese el número de años del préstamo", value=1)
numero_pagos= st.number_input ("Ingrese el número de pagos anuales", value=12)

cuota = lf.cuota_prestamo (monto, interes, anios,numero_pagos)
st.write(cuota)
