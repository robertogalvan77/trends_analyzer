from pytrends.request import TrendReq

def get_google_trends(keywords, timeframe='now 1-d', geo=''):
    """Obtiene las tendencias de Google para un conjunto de palabras clave."""
    pytrends = TrendReq(hl='es', tz=360)  # Configura en español y zona horaria UTC+6
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)  # Configura los parámetros
    trends_data = pytrends.interest_over_time()

    if trends_data.empty:
        return None  # No se encontraron datos

    # Convertir los datos a diccionario de registros para una mejor estructuración
    return trends_data[keywords].to_dict(orient="records")
