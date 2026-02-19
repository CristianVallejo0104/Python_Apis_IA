import time
from functools import wraps

# REVISA QUE EL NOMBRE SEA EXACTAMENTE ESTE:
def corroborar_proceso(func):  
    """Decorador estilo Sierra para auditoría de procesos."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--- 🚀 Iniciando: {func.__name__.upper()} ---")
        inicio = time.time()
        try:
            resultado = func(*args, **kwargs)
            tiempo = time.time() - inicio
            print(f"✅ Éxito: {func.__name__} finalizado en {tiempo:.4f} seg.")
            return resultado
        except Exception as e:
            print(f"❌ Error Crítico en {func.__name__}: {str(e)}")
            raise e
    return wrapper
