from django.http import JsonResponse
from django.views.generic import ListView
from .models import Sport

# Class-based view for SportList
class SportList(ListView):
    model = Sport
    template_name = 'sports/sport_list.html'
    context_object_name = 'sports'

# Function-based view for sport list (API)
def sport_list(request):
    sports = Sport.objects.all()
    sports_list = [{"id": sport.id, "name": sport.name, "description": sport.description} for sport in sports]
    return JsonResponse(sports_list, safe=False)

# Function-based view for sport detail (API)
def sport_detail(request, id):
    try:
        sport = Sport.objects.get(id=id)
        sport_detail = {"id": sport.id, "name": sport.name, "description": sport.description}
        return JsonResponse(sport_detail)
    except Sport.DoesNotExist:
        return JsonResponse({"error": "Sport not found"}, status=404)
#root view 
from django.http import HttpResponse

def index(request):
    return HttpResponse("All things Sports...You're Welcome!!")
