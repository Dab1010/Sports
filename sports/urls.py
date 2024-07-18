from django.urls import path
from .views import SportList, sport_list, sport_detail

urlpatterns = [
    path('', SportList.as_view(), name='sport-list'),
    path('api/sports/', sport_list, name='sport-list-api'),
    path('api/sports/<int:id>/', sport_detail, name='sport-detail-api'),
]
