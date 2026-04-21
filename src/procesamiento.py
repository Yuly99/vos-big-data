"""
Proyecto Big Data - Procesamiento de datos de smartphones
"""

import pandas as pd

def cargar_datos():
    print("Cargando datos...")
    smartphones = pd.read_csv("data/smartphones.csv")
    ventas = pd.read_csv("data/ventas.csv")
    return smartphones, ventas

def limpiar_datos(smartphones, ventas):
    print("Limpiando datos...")
    smartphones = smartphones.dropna()
    ventas = ventas.dropna()
    return smartphones, ventas

def unir_datos(smartphones, ventas):
    print("Uniendo datos...")
    df = pd.merge(smartphones, ventas, on="modelo", how="inner")
    return df

def analisis_por_marca(df):
    print("Analizando ventas por marca...")
    resultado = df.groupby("marca")["ventas"].sum().reset_index()
    resultado.to_csv("results/brand_sales.csv", index=False)
    return resultado

def analisis_por_ciudad(df):
    print("Analizando ventas por ciudad...")
    resultado = df.groupby("ciudad")["ventas"].sum().reset_index()
    resultado.to_csv("results/city_sales.csv", index=False)
    return resultado

def analisis_por_anio(df):
    print("Analizando ventas por año...")
    resultado = df.groupby("anio")["ventas"].sum().reset_index()
    resultado.to_csv("results/year_sales.csv", index=False)
    return resultado

def promedio_especificaciones(df):
    print("Calculando promedios...")
    columnas = ["ram", "almacenamiento", "bateria"]
    resultado = df[columnas].mean().to_frame(name="promedio")
    resultado.to_csv("results/specs_avg.csv")
    return resultado

def main():
    smartphones, ventas = cargar_datos()
    smartphones, ventas = limpiar_datos(smartphones, ventas)
    df = unir_datos(smartphones, ventas)

    print("\n--- RESULTADOS ---")
    print(analisis_por_marca(df))
    print(analisis_por_ciudad(df))
    print(analisis_por_anio(df))
    print(promedio_especificaciones(df))

if __name__ == "__main__":
    main()
