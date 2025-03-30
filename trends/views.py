from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .google_trends import get_google_trends  # Importa la función
from .youtube_trends import get_youtube_trends

def google_trends(request):
    """Obtiene las tendencias de Google."""

    kw_list = ["Django", "Machine Learning", "Google Trends"]  # Palabras clave a buscar

    trends_data = get_google_trends(kw_list)

    if trends_data is None:
        return JsonResponse({"error": "No se encontraron datos"}, status=404)

    return JsonResponse({"trends": trends_data})


def youtube_trends(request):
    # Obtener las tendencias de YouTube
    trends = get_youtube_trends()
    return render(request, 'trends/youtube_trends.html', {'trends': trends})