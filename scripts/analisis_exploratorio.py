import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.utilidades import corroborar_proceso

class AnalizadorEstadistico:
    """
    Clase encargada del Análisis Exploratorio de Datos (EDA).
    Usa POO para encapsular el DataFrame y métodos visuales.
    """
    
    def __init__(self, dataframe: pd.DataFrame):
        self._df = dataframe
        # Configuración estética profesional para las gráficas
        sns.set_theme(style="whitegrid", palette="viridis")

    @property
    def resumen_critico(self):
        """
        Usa @property para devolver el resumen estadístico 
        como si fuera un atributo, sin necesidad de paréntesis ().
        """
        return self._df[['trip_duration', 'passenger_count']].describe()

    @corroborar_proceso
    def visualizar_datos(self):
        """
        Genera un panel gráfico 2x2.
        Se abrirá en el panel 'Plots' de Positron y guardará una imagen PNG.
        """
        print("🎨 Generando tablero de control gráfico...")
        
        # Crear un lienzo (Figure) con 4 sub-gráficos (Axes)
        fig, axes = plt.subplots(2, 2, figsize=(16, 10))
        fig.suptitle('EDA: Análisis de Taxis en NYC', fontsize=16, fontweight='bold')

        # 1. Histograma de Duración (Limitado a 2 horas para ver mejor)
        duracion_visual = self._df[self._df['trip_duration'] < 7200]
        sns.histplot(data=duracion_visual, x='trip_duration', bins=60, kde=True, ax=axes[0, 0], color='teal')
        axes[0, 0].set_title('Distribución de Duración (Segundos)')
        axes[0, 0].set_xlabel('Tiempo (s)')

        # 2. Conteo de Pasajeros (Gráfico de Barras)
        sns.countplot(
        data=self._df, 
        x='passenger_count', 
        hue='passenger_count',  
        legend=False,           
        ax=axes[0, 1], 
        palette="magma")

        # 3. Mapa de Calor Geográfico (Scatterplot de las coordenadas)
        # Tomamos una muestra de 10,000 puntos para optimizar rendimiento
        muestra = self._df.sample(n=min(10000, len(self._df)), random_state=42)
        sns.scatterplot(x='pickup_longitude', y='pickup_latitude', data=muestra, 
                        alpha=0.3, s=15, ax=axes[1, 0], color='purple', edgecolor=None)
        axes[1, 0].set_title('Mapa de Recogidas (Muestra 10k)')
        axes[1, 0].set_xlim(-74.05, -73.9) # Zoom en Manhattan
        axes[1, 0].set_ylim(40.7, 40.85)
        axes[1, 0].set_xlabel('Longitud')
        axes[1, 0].set_ylabel('Latitud')

        # 4. Boxplot para detectar Outliers en Duración
        sns.boxplot(x=self._df['trip_duration'], ax=axes[1, 1], color='orange')
        axes[1, 1].set_title('Detección de Outliers (Boxplot)')
        axes[1, 1].set_xlim(0, 5000) # Zoom a la zona principal

        # Ajustar espacios para que no se solapen los títulos
        plt.tight_layout()
        
        # Guardar evidencia
        nombre_archivo = "eda_reporte_grafico.png"
        plt.savefig(nombre_archivo)
        print(f"💾 Gráfico guardado como '{nombre_archivo}'")

        # Mostrar en pantalla (Esto activa el panel de Positron)
        plt.show()