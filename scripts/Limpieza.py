import pandas as pd
from pydantic import ValidationError
from scripts.schemas import TaxiRideInput  
from scripts.utilidades import corroborar_proceso

# --- IMPORTANTE: El nombre de la clase debe ser EXACTAMENTE este ---
class LimpiadorData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @corroborar_proceso
    def filtrar_con_pandas(self):
        """Limpieza rápida vectorizada (Nivel 1)"""
        print("🧹 Aplicando filtros masivos...")
        self.df = self.df.dropna()
        self.df = self.df[
            (self.df['trip_duration'].between(60, 7200)) &
            (self.df['passenger_count'] > 0)
        ]
        return self.df

    @corroborar_proceso
    def validar_integridad_pydantic(self):
        """Nivel 2: Validación estricta fila por fila usando el Schema."""
        print("🛡️ Iniciando auditoría Pydantic...")
        
        registros = self.df.to_dict(orient="records")
        registros_validos = []
        errores = 0

        for fila in registros:
            try:
                fila_validada = TaxiRideInput(**fila)
                registros_validos.append(fila_validada.model_dump())
            except ValidationError as e:
                errores += 1
                if errores == 1: 
                    print(f"⚠️ Ejemplo de error detectado: {e.json()}")

        print(f"📊 Reporte Pydantic: {len(registros_validos)} aprobados | {errores} rechazos.")
        
        self.df = pd.DataFrame(registros_validos)
        return self.df