# import time
# from pytrends.request import TrendReq
#
#
# def get_google_trends(keywords, timeframe='now 1-H', geo=''):
#     pytrends = TrendReq(hl='en-US', tz=360)
#
#     # Agregar delay para evitar bloqueo
#     time.sleep(5)  # Espera 5 segundos entre solicitudes
#
#     # Configurar parámetros de la consulta
#     pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
#
#     # Obtener datos de tendencias
#     trends_data = pytrends.interest_over_time()
#
#     # Verificar si hay resultados
#     if trends_data.empty:
#         return {"error": "No hay datos disponibles para esta búsqueda."}
#
#     return trends_data

from pytrends.request import TrendReq
import time

def get_google_trends(keywords, timeframe='now 1-d', geo=''):
    """Obtiene las tendencias de Google para un conjunto de palabras clave."""
    try:
        pytrends = TrendReq(hl='es', tz=360)  # Configura en español y zona horaria UTC+6
        pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)  # Configura los parámetros

        # Intentar obtener datos
        trends_data = pytrends.interest_over_time()

        # Si los datos están vacíos, devolver un mensaje de error
        if trends_data.empty:
            return {"error": "No se encontraron datos para las palabras clave solicitadas."}

        # Convertir los datos a diccionario de registros para una mejor estructuración
        return trends_data[keywords].to_dict(orient="records")

    except Exception as e:
        return {"error": f"Ocurrió un error al obtener las tendencias: {str(e)}"}

    # Para evitar sobrecargar la API, añadir un pequeño retraso
    time.sleep(2)
