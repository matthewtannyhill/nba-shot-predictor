from api import views
from django.urls import path


urlpatterns = [
    path('campaign/', views.CampaignList.as_view()),
    path('campaign/<int:pk>/', views.CampaignDetail.as_view()),
]
