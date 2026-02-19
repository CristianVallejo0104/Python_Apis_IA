import pandas as pd
from scripts.analisis_exploratorio import AnalizadorEstadistico
from scripts.Limpieza import LimpiadorData
from scripts.utilidades import corroborar_proceso

@corroborar_proceso
def main():
    # 1. Carga de datos
    ruta = r"C:\Users\cristian\OneDrive\Escritorio\python_apis_ia\datos\train.csv"
    df_raw = pd.read_csv(ruta)

    # 2. EDA (Estadísticas y GRÁFICOS)
    analisis = AnalizadorEstadistico(df_raw)
    print("\n📊 Estadísticas Iniciales:")
    print(analisis.resumen_critico)
    
    analisis.visualizar_datos()

    # 3. Limpieza y Validación
    procesador = LimpiadorData(df_raw)
    procesador.filtrar_con_pandas()
    df_clean = procesador.validar_integridad_pydantic()

    # 4. Guardado
    ruta_salida = r"C:\Users\cristian\OneDrive\Escritorio\python_apis_ia\datos\train_limpio.csv"
    df_clean.to_csv(ruta_salida, index=False)
    print(f"\n💾 Archivo guardado en: {ruta_salida}")

if __name__ == "__main__":
    main()