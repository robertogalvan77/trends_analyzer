# trends/youtube_trends.py
from googleapiclient.discovery import build
import os

# Usar la clave API de YouTube
API_KEY = 'AIzaSyDzAn8hwlQDn7ct0NjkLgqaR73oMVl-WVo'

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_youtube_trends():
    # Obtener los videos más populares de YouTube
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",  # Puedes cambiar el código de la región
        maxResults=10
    )
    response = request.execute()

    # Retornar los datos de los videos más populares
    return response.get('items', [])

if __name__ == "__main__":
    trends = get_youtube_trends()
    for trend in trends:
        print(f"Titulo: {trend['snippet']['title']}")
        print(f"URL: https://www.youtube.com/watch?v={trend['id']}")
        print()
