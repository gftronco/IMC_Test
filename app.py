import streamlit as st
import pandas as pd
import requests

# Función para calcular el IMC
def calcular_imc(peso, altura):
    altura_mts = altura / 100  # Convertimos la altura de cms a metros
    imc = peso / (altura_mts ** 2)
    return imc

# Función para obtener información sobre el IMC promedio en tu país y continente
def obtener_estadisticas(imc, pais, continente):
    # Aquí puedes utilizar una API o base de datos para obtener datos promedio de IMC
    # En este caso, vamos a simular estos datos con valores ficticios.
    # Simulamos un resultado de IMC promedio por continente
    estadisticas = {
        "Asia": {"IMC_promedio": 22.0},
        "Europa": {"IMC_promedio": 25.0},
        "América": {"IMC_promedio": 27.0},
        "África": {"IMC_promedio": 21.5},
        "Oceanía": {"IMC_promedio": 26.0},
    }
    
    imc_promedio_continente = estadisticas.get(continente, {"IMC_promedio": 25.0})["IMC_promedio"]
    
    # Aquí podrías agregar la lógica para obtener el IMC promedio de tu país,
    # pero por ahora lo dejamos con un valor ficticio.
    imc_promedio_pais = 24.0  # Suponemos un valor ficticio

    return imc_promedio_pais, imc_promedio_continente

# Interfaz de usuario en Streamlit
def app():
    st.title("Cálculo de Índice de Masa Corporal (IMC)")
    
    # Campos de entrada
    peso = st.number_input("Ingrese su peso en kilogramos (kg)", min_value=1.0, step=0.1)
    altura = st.number_input("Ingrese su altura en centímetros (cm)", min_value=1, step=1)
    edad = st.number_input("Ingrese su edad", min_value=1, step=1)
    pais = st.text_input("Ingrese su país (por ejemplo, España, México, Argentina)")
    continente = st.text_input("Ingrese su continente (por ejemplo, Europa, América, Asia)")

    if st.button("Calcular IMC"):
        # Cálculo del IMC
        imc = calcular_imc(peso, altura)
        st.write(f"Tu IMC es: {imc:.2f}")
        
        # Evaluación del IMC
        if imc < 18.5:
            evaluacion = "bajo peso"
        elif 18.5 <= imc < 24.9:
            evaluacion = "normal"
        elif 25 <= imc < 29.9:
            evaluacion = "sobrepeso"
        else:
            evaluacion = "obesidad"
        
        st.write(f"Tu evaluación: {evaluacion}")
        
        # Comparación con el IMC promedio
        imc_promedio_pais, imc_promedio_continente = obtener_estadisticas(imc, pais, continente)
        st.write(f"IMC promedio en {pais}: {imc_promedio_pais}")
        st.write(f"IMC promedio en tu continente ({continente}): {imc_promedio_continente}")

        # Evaluar si el IMC está por encima o debajo del promedio
        if imc < imc_promedio_continente:
            st.write("Tu IMC está por debajo del promedio de tu continente.")
        else:
            st.write("Tu IMC está por encima del promedio de tu continente.")

        if imc < imc_promedio_pais:
            st.write("Tu IMC está por debajo del promedio de tu país.")
        else:
            st.write("Tu IMC está por encima del promedio de tu país.")

# Ejecutar la aplicación
if __name__ == "__main__":
    app()
