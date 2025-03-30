import tweepy
from django.conf import settings


def get_trends():
    # Autenticación con la API v2 usando Tweepy Client
    client = tweepy.Client(
        bearer_token=settings.X_API_KEY
    )

    # Buscar tweets relacionados con una palabra clave (ejemplo: 'trends')
    query = "trends -is:retweet lang:en"
    response = client.search_recent_tweets(query=query, max_results=10)

    # Verificar si hay resultados antes de procesar
    if response.data:
        trend_names = [tweet.text for tweet in response.data]
    else:
        trend_names = ["No se encontraron tendencias recientes."]

    return trend_names
