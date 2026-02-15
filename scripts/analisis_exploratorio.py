import pandas as pd

def realizar_eda(ruta_datos: str):
    df = pd.read_csv(ruta_datos)
    
    print("--- ANÁLISIS EXPLORATORIO DE DATOS (EDA) ---")
    print(f"\n1. Forma del dataset: {df.shape}")
    
    print("\n2. Valores nulos por columna:")
    print(df.isnull().sum())
    
    print("\n3. Estadísticas de duración y coordenadas:")
    # Analizamos solo las columnas que nos interesan para la limpieza
    cols_interes = ['trip_duration', 'pickup_latitude', 'pickup_longitude', 'passenger_count']
    print(df[cols_interes].describe())

    # Retornamos el dataframe por si queremos usarlo de inmediato
    return df

if __name__ == "__main__":
    ruta = "datos/train.csv"
    realizar_eda(ruta)