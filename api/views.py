from django.http import JsonResponse
from sports.models import Sport  # Ensure you have a Sport model in models.py

def sport_list(request):
    sports = Sport.objects.all()
    sports_list = [{"id": sport.id, "name": sport.name, "description": sport.description} for sport in sports]
    return JsonResponse(sports_list, safe=False)

def sport_detail(request, id):
    try:
        sport = Sport.objects.get(id=id)
        sport_detail = {"id": sport.id, "name": sport.name, "description": sport.description}
        return JsonResponse(sport_detail)
    except Sport.DoesNotExist:
        return JsonResponse({"error": "Sport not found"}, status=404)
