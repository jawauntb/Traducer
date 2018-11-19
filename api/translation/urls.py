from django.urls import path
from .views import ListTranslationsView


urlpatterns = [
    path('translations/', ListTranslationsView.as_view(), name="translations-all")
]