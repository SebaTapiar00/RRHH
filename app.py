import streamlit as st
import pandas as pd
from utils.pdf_generator import generar_liquidacion_pdf
from utils.tasas_updater import obtener_tasas_actualizadas

st.set_page_config(page_title="Liquidación de Sueldo", layout="centered")
st.title("🧾 Generador de Liquidaciones de Sueldo")

archivo = st.file_uploader("📤 Cargar nómina de trabajadores (CSV)", type="csv")

if archivo:
    df = pd.read_csv(archivo)
    st.success("Archivo cargado exitosamente.")
    st.dataframe(df)

    tasas = obtener_tasas_actualizadas()

    trabajador = st.selectbox("👤 Seleccionar trabajador", df["Nombre"].unique())
    fila = df[df["Nombre"] == trabajador].iloc[0]

    if st.button("📄 Generar Liquidación PDF"):
        ruta_pdf = generar_liquidacion_pdf(fila, tasas)
        with open(ruta_pdf, "rb") as file:
            st.download_button("📥 Descargar PDF", file, file_name=ruta_pdf)