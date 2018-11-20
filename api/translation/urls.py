from django.urls import path
from .views import ListCreateTranslationsView


urlpatterns = [
    path('translations/', ListCreateTranslationsView.as_view(), name="translations-list-create"),
]

