import pandas as pd
import numpy as np

#datos = pd.read_csv(r"C:\Users\cristian\OneDrive\Escritorio\python_apis_ia\datos\train.csv")
#print(datos.isnull().sum())
#print(datos.describe())

#datos_limpios= datos[datos["trip_duration"].between(120,7200)]
#datos_limpios= datos_limpios[datos_limpios["passenger_count"] > 0]

#datos_limpios = datos_limpios[(datos_limpios['pickup_latitude'].between(40.5, 41.0)) &(datos_limpios['pickup_longitude'].between(-74.1, -73.7))]


def limpiar_datos_taxi(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función pura para la limpieza del dataset NYC Taxi.
    Recibe un DataFrame y devuelve uno nuevo filtrado.
    """
    # Creamos una copia para no afectar los datos originales (esencial para IA)
    df_clean = df.copy()

    # 1. Filtro de duración (Quitamos los errores de segundos y horas infinitas)
    df_clean = df_clean[df_clean["trip_duration"].between(120, 7200)]

    # 2. Filtro de pasajeros (Eliminamos viajes con 0 personas)
    df_clean = df_clean[df_clean["passenger_count"] > 0]

    # 3. Filtro geográfico (Aseguramos que el taxi esté en Nueva York)
    df_clean = df_clean[
        (df_clean['pickup_latitude'].between(40.5, 41.0)) & 
        (df_clean['pickup_longitude'].between(-74.1, -73.7))
    ]

    return df_clean

# Este bloque permite que el script siga funcionando si lo corres solo
if __name__ == "__main__":
    ruta = r"C:\Users\cristian\OneDrive\Escritorio\python_apis_ia\datos\train.csv"
    datos = pd.read_csv(ruta)
    
    # Llamamos a nuestra función modular
    datos_finales = limpiar_datos_taxi(datos)
    
    print(f"✅ Limpieza terminada.")
    print(f"Registros eliminados: {len(datos) - len(datos_finales)}")
    
    # Guardamos el resultado para que la IA lo use luego
    datos_finales.to_csv("datos/train_limpio.csv", index=False)
